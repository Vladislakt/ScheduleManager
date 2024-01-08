import unittest
from sqlalchemy import create_engine
from database.database import create_db  # Replace 'yourmodule' with the actual module name

class TestCreateDatabase(unittest.TestCase):
    def testcreatedb(self):
        filename = "examplefilename"
        databasename = f'finaldata/{filename}.rsp'
        engine = create_engine(f'sqlite:///{databasename}')

        create_db(filename)
        self.assertTrue(engine.dialect.hastable(engine, "yourtable"))  # Replace 'yourtable' with the actual table name

if __name__ == '__main__':
    unittest.main()