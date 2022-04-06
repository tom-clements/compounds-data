import click

from pipeline.create_table import create_table
from pipeline.json_to_dynamodb import insert_data


@click.command()
@click.option("--table-name", help="Name of the table in Dynamodb.")
def run(table_name: str):
    create_table(table_name)
    insert_data(table_name)


if __name__ == "__main__":
    run()
