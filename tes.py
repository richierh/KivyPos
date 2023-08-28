import gspread as gs
from google.oauth2 import service_account
from pathlib import Path



SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

class BaseKonek():

    name_file = Path.cwd() / 'Model' / 'token.json'
    SERVICE_ACCOUNT_FILE = name_file

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    client = gs.authorize(credentials)


    sheet = client.open('login')
    edutech_data = sheet.get_worksheet(0)
    get_sheet = sheet.worksheet("login")
    # edutech_data = edutech_data.get_all_records()
    # print (edutech_data)
    selectcell_col1 = get_sheet.col_values(1)
    selectcell_col2 = get_sheet.col_values(2)
    selectcell_col3 = get_sheet.col_values(3)

class Spreadkonek(BaseKonek):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def get_token(self):
        self.result_data = self.get_sheet.get_values('A:C')
        return self.result_data

    def get_data(self):
        self.result_data = self.get_sheet.get_values('A:B')
        return self.result_data

    def get_column(self,*args):
        self.username = args[0]
        print(self.username)
        self.cell = self.get_sheet.find(self.username)  
        try:
            self.cell_pass_col = self.cell.col+1
            self.cell_pass_row = self.cell.row
            self.col = self.cell.col 
            self.row = self.cell.row
        except:
            self.cell_pass_col=25
            self.cell_pass_row = 40
            self.col = 25
            self.row = 30

        self.list = [self.col,self.row,self.cell_pass_col,self.cell_pass_row]

        return self.list
    
    def get_password_from_username(self,*args):
        self.data = args[0]
        self.data_col_user = self.data[0]
        self.data_row_user = self.data[1]
        self.data_col_pass = self.data[2]
        self.data_row_pass = self.data[3]
        self.cell_pass = self.get_sheet.cell(self.data_row_pass,self.data_col_pass).value
        self.cell_user = self.get_sheet.cell(self.data_row_user,self.data_col_user).value
        return [self.cell_user,self.cell_pass]



