import sqlite3
from typing import Tuple


class Database:
    def __init__(self, db="data/fpl.db"):
        """
        Initialize the `Database` class by creating a connection to
        the specified SQLite database and creating the tables if
        they do not already exist.
        """
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """
        Create the `users` table in the SQLite database if it
        does not already exist.
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                discord_id TEXT,
                fpl_id TEXT
            )
            """
        )
        self.conn.commit()

    def insert_user(self, discord_id: str, fpl_id: str):
        """
        Insert a new user into the `users` table.

        Args:
            discord_id (str): The Discord user ID of the user to insert.
            fpl_id (str): The FPL user ID of the user to insert.
        """
        self.cursor.execute(
            """
            INSERT INTO users (discord_id, fpl_id)
            VALUES (?, ?)
            """,
            (discord_id, fpl_id),
        )
        self.conn.commit()

    def update_user(self, discord_id: str, fpl_id: str):
        """
        Update the FPL ID of an existing user in the `users` table.

        Args:
            discord_id (str): The Discord user ID of the user to update.
            fpl_id (str): The new FPL user ID to set for the user.
        """
        self.cursor.execute(
            """
            UPDATE users
            SET fpl_id = ?
            WHERE discord_id = ?
            """,
            (fpl_id, discord_id),
        )
        self.conn.commit()

    def get_user(self, discord_id: str) -> Tuple:
        """
        Get the user with the specified Discord ID from the `users` table.

        Args:
            discord_id (str): The Discord user ID of the user to get.

        Returns:
            A tuple containing the user's data, or `None` if no user
            with the specified Discord ID exists in the `users` table.
        """
        self.cursor.execute(
            """
            SELECT *
            FROM users
            WHERE discord_id = ?
            """,
            (discord_id,),
        )
        return self.cursor.fetchone()
