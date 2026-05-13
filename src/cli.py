import argparse
import logging
import os

from src.dbcreate.dbcreate import sqliteCreate
from src.doccreate.pdf_create import docCreate, sqlite2pdf
from src.extraction.check import CheckSpreadsheet
from src.extraction.create_metadata import GenerateMeta
from src.extraction.retrieve_data import GetSpreadsheetData
from src.utils.utils import move_metadata_json, output_exist, save_spreadsheet


logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("logs"), logging.StreamHandler()],
)


def main_cli():
    args = getArgs()
    input_path = os.path.normpath(args.input)

    if os.path.isfile(input_path) is False:
        logging.error(f"{FileNotFoundError}: {input_path} not found")
        raise FileNotFoundError(f"{input_path} not found")

    if args.create_metadata:
        if args.overwrite is False and args.filename is None:
            raise fileExistsHandler(input_path)
        else:
            ss_with_meta, created_metatable = create_missing_metatable(input_path)
            file_format = os.path.splitext(input_path)[1]
            if args.filename:
                filename = os.path.join(
                    os.path.dirname(input_path), args.filename + file_format
                )
            else:
                filename = input_path

            save_spreadsheet(
                sheets_dict=ss_with_meta.sheets_dict, filepath=filename, format=file_format
            )

    else:
        output_path = os.path.normpath(os.path.abspath(args.output_path))

        if args.from_sqlite is True:
            doc = sqlite2pdf(input_path, output_path)
            doc.createPDF()
        else:
            spreadsheet_name = os.path.splitext(os.path.basename(input_path))[0]

            checker = CheckSpreadsheet(input_path, os.path.splitext(input_path)[0])
            checker.validate_spreadsheet()
            checker.validate_meta_terms()

            data = GetSpreadsheetData(
                filepath=input_path,
                checked_data=checker.sheets_dict,
            )

            if args.overwrite is False and args.filename is None:
                fileExistsHandler(output_path, spreadsheet_name)
                move_metadata_json(
                    input_path=os.path.splitext(input_path)[0],
                    output_path=output_path,
                    output_name=spreadsheet_name,
                )
            elif args.overwrite is True and args.filename:
                rm_if_exists(os.path.join(output_path, args.filename + ".sqlite"))
                move_metadata_json(
                    input_path=os.path.splitext(input_path)[0],
                    output_path=output_path,
                    output_name=args.filename,
                )
                data.db_name = args.filename
            elif args.overwrite is True and args.filename is None:
                rm_if_exists(os.path.join(output_path, spreadsheet_name + ".sqlite"))

                move_metadata_json(
                    input_path=os.path.splitext(input_path)[0],
                    output_path=output_path,
                    output_name=spreadsheet_name,
                )
            elif args.overwrite is False and args.filename:
                fileExistsHandler(output_path, args.filename)
                move_metadata_json(
                    input_path=os.path.splitext(input_path)[0],
                    output_path=output_path,
                    output_name=args.filename,
                )
                data.db_name = args.filename

            sqlite_db = sqliteCreate(data, output_dir=output_path)
            sqlite_db.create_db()
            sqlite_db.insert_data()
            sqlite_db.ddict_schema_create()
            sqlite_db.meta_tables_create()

            doc = docCreate(sqlite_db)
            doc.createPDF()

            print(f"Process successful for {input_path}")


def rm_if_exists(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        pass


def fileExistsHandler(output_path, output_basename):
    if output_exist(output_path, output_basename):
        logging.error(
            f"{FileExistsError}: Output(s) already exist in output directory for this spreadsheet\n"
            "Overwrite it with -ow --overwritte flag OR specify anothe name using --filename"
        )
        raise FileExistsError(
            "Output(s) already exist in output directory for this spreadsheet\n"
            "Overwrite it with -ow --overwritte flag OR specify another filename using --filename"
        )


def getArgs():
    parser = argparse.ArgumentParser(
        description="Convert spreadsheets into documented sqlite databases with rich and standardized metadata."
    )

    group = parser.add_argument_group(
        "Processing",
        "Choose between pre-processing of spreadsheet, ie: generate metadata table or conversion of files already compliant with the template",
    )

    exclusive_group = group.add_mutually_exclusive_group(required=True)

    parser.add_argument("input", help="Absolute path to the spreadsheet or sqlite file to process")

    exclusive_group.add_argument(
        "-o", "--output-path", help="Absolute path to the output directory of your choice"
    )
    exclusive_group.add_argument(
        "--create-metadata",
        action="store_true",
        help="Generate metadata tables that should then be filled before running",
    )

    parser.add_argument(
        "--filename",
        type=str,
        help="basename of outputs, default behavior will be using input name",
    )

    parser.add_argument(
        "-ow", "--overwrite", action="store_true", help="overwritte previously generated output"
    )

    parser.add_argument(
        "--from-sqlite", action="store_true", help="Generate PDF from sqlite file"
    )

    return parser.parse_args()


def create_missing_metatable(spreadsheet):
    meta_generator = GenerateMeta(spreadsheet)
    missing_tables = meta_generator.create_metatable()
    return meta_generator, missing_tables
