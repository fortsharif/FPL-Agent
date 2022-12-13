import unittest

from unittest import mock

import os

import tempfile


from config import Config

from database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Create a new instance of the `Database` class before each test.
        """
        # Create a temporary directory for the test database
        self.temp_dir = tempfile.TemporaryDirectory()

        # Create the full path to the database file
        db_path = os.path.join(self.temp_dir.name, "test.db")

        # Create a new instance of the `Database` class, using the full path to the database file
        self.db = Database(db_path)

    def tearDown(self) -> None:
        """
        Close the test database and delete the temporary directory after each test.
        """
        # Close the database connection
        self.db.conn.close()

        # Delete the temporary directory
        self.temp_dir.cleanup()

    def test_insert_user(self) -> None:
        """
        Test the `insert_user()` method.
        """
        self.db.insert_user("123", "456")
        user = self.db.get_user("123")
        self.assertEqual(user[1], "123")
        self.assertEqual(user[2], "456")

    def test_update_user(self) -> None:
        """
        Test the `update_user()` method.
        """
        self.db.insert_user("123", "456")
        self.db.update_user("123", "789")
        user = self.db.get_user("123")
        self.assertEqual(user[1], "123")
        self.assertEqual(user[2], "789")

    def test_get_user(self) -> None:
        """
        Test the `get_user()` method.
        """
        self.db.insert_user("123", "456")
        user = self.db.get_user("123")
        self.assertEqual(user[1], "123")
        self.assertEqual(user[2], "456")
        self.assertIsNone(self.db.get_user("456"))


@mock.patch.object(Config, "TOKEN", "test_token")
class TestConfig(unittest.TestCase):
    """A unit test class for the Config class."""

    def setUp(self) -> None:
        """Set up the test case by creating mock objects and a Config instance."""
        self.mock_os_environ = mock.Mock()
        self.mock_os_environ.get.return_value = "test_token"

        self.config = Config()

    def test_token(self) -> None:
        """Test that the TOKEN attribute is set to the expected value."""
        self.assertEqual(self.config.TOKEN, self.mock_os_environ.get())

    def test_default_response(self) -> None:
        """Test that the DEFAULT_RESPONSE attribute is set to the expected value."""
        self.assertEqual(
            self.config.DEFAULT_RESPONSE,
            "Sorry, I didn't understand your command. Type `+help` for a list of commands.",
        )


if __name__ == "__main__":
    unittest.main()
