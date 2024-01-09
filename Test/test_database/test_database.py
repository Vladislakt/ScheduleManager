import unittest
from sqlalchemy import create_engine
from database.database import create_db

class TestCreateDatabase(unittest.TestCase):
    def test_create_Db(self):
        filename = "test"
        databasename = f'finaldata/{filename}.rsp'
        engine = create_engine(f'sqlite:///{databasename}')

        create_db(filename)
        self.assertTrue(engine.dialect.hastable(engine, f"finaldata/{filename}.rsp"))

if __name__ == '__main__':
    unittest.main()