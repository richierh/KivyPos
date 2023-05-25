from Model.base_model import BaseScreenModel
from Model.konekspreadsheet import Spreadkonek
from Model.automap import Person
import sqlalchemy as db


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def konekspread(self):
        pass

    def get_token(self):
        self.Spreadsheet=Spreadkonek()
        self.result = self.Spreadsheet.get_token()
        return self.result
    
    def get_username_password(self):
        self.Spreadsheet=Spreadkonek()
        self.result = self.Spreadsheet.get_data()
        return self.result
    
    def find_username_password(self,*args):
        self.username_find = args[0]
    
        self.Spreadsheet = Spreadkonek()
        print(self.username_find)

        self.loc_cell = self.Spreadsheet.get_column(self.username_find)
        # location cell = [1,2,3,4]
        # 1. username col
        # 2. username row
        # 3. password col
        # 4. password row
        # print(self.loc_cell)
        self.result = self.Spreadsheet.get_password_from_username(self.loc_cell)
        return self.result 

    def get_username_password_sqlalchemy(self):
        self.personal = Person()
        engine = self.engine()
        connection=engine.connect()
        metadata = db.MetaData()
        person = db.Table('Person', metadata, autoload=True, autoload_with=engine)
        query = db.select([person]) 
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        connection.close()
        engine.dispose()
        # ResultSet[:3]
        return ResultSet
