import unittest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.create_session import create_session  # replace `your_module` with the actual module name


class TestCreateSession(unittest.TestCase):
    def test_create_session_existing_file(self):
        filename = "example_filename"
        with open(f"finaldata/{filename}.rsp", "w") as f:
            # Create an empty file to simulate the database file
            pass

        session = create_session(filename)
        self.assertIsNotNone(session)
        self.assertIsInstance(session, sessionmaker)

    def test_create_session_non_existing_file(self):
        filename = "example_non_existing_filename"
        with self.assertRaises(FileNotFoundError):
            create_session(filename)

    def test_create_session_with_proper_engine(self):
        filename = "example_filename"
        database_name = f"finaldata/{filename}.rsp"
        engine = create_engine(f'sqlite:///{database_name}')
        Session = sessionmaker(bind=engine)
        session = create_session(filename)
        self.assertEqual(type(session.bind.url), type(engine.url))
        self.assertEqual(session.bind.url, engine.url)


if __name__ == '__main__':
    unittest.main()