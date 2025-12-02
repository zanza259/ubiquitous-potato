import argparse
import sqlite3
import sys
import logging
from pathlib import Path

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
root_logger.addHandler(console_handler)

logger = logging.getLogger(__name__)


def execute_sql_script(
    connection: sqlite3.Connection, sql_script: str, script_name: str
) -> None:
    """Execute SQL script with error handling."""
    cursor = connection.cursor()
    statements = sql_script.split(";")

    for statement in statements:
        statement = statement.strip()
        if statement:
            try:
                cursor.execute(statement)
            except sqlite3.Error as e:
                logger.error(f"Error executing statement in {script_name}: {e}")
                connection.rollback()
                sys.exit(1)

    connection.commit()
    logger.info(f"\t + Successfully executed {script_name}")


def initialize_database(db_path: Path, sql_path: Path) -> None:
    if not db_path.parent.exists():
        raise ValueError(f"Directory does not exist: {db_path.parent}")

    if not sql_path.exists() or not sql_path.is_dir():
        raise ValueError(f"SQL path is not a valid directory: {sql_path}")

    # Connect to database (creates it)
    logger.info(f"Creating database at {db_path}")
    try:
        connection = sqlite3.connect(str(db_path))
    except sqlite3.Error as e:
        logger.error(f"Error creating database: {e}")
        sys.exit(1)

    # hardcode sql files to execute in order for now
    sql_files = [
        ("00_initialize.sql", sql_path / "00_initialize.sql"),
        ("01_demo_user.sql", sql_path / "01_demo_user.sql"),
        ("02_demo_recipes.sql", sql_path / "02_demo_recipes.sql"),
    ]

    # validate we have all expected files
    for name, file_path in sql_files:
        if not file_path.exists():
            logger.error(f"Expected SQL file not found: {file_path}")
            sys.exit(1)

    try:
        for name, file_path in sql_files:
            logger.info(f"Executing SQL file: {file_path}...")

            with open(file_path, "r") as f:
                sql_script = f.read()

            execute_sql_script(connection, sql_script, name)

        logger.info("Database initialization complete!")

    finally:
        connection.close()


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Initialize SQLite database for potato application"
    )

    parser.add_argument(
        "--db",
        type=Path,
        default=Path.home() / "recipes.db",
        help="Path where SQLite database file should be created",
    )

    parser.add_argument(
        "--sql",
        type=Path,
        help="Path to directory containing SQL files",
    )

    return parser


def main():
    args = build_arg_parser().parse_args()

    initialize_database(
        db_path=args.db,
        sql_path=args.sql,
    )


if __name__ == "__main__":
    main()
