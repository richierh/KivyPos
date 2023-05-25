import importlib
import numpy as np
import pandas as pd
import View.MainScreen.main_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.MainScreen.main_screen)




class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = View.MainScreen.main_screen.MainScreenView(controller=self, model=self.model)

    def get_view(self) -> View.MainScreen.main_screen:
        return self.view
    
    def token(self):
        self.get_token = self.model.get_token()
        self.get_token_list=[]
        for token in self.get_token:
            token_col = token[1:]
            self.get_token_list.append(token_col)

        self.get_token_dict = dict(self.get_token_list)

        if self.view.token in self.get_token_dict.values() :
            return True
        else:
            return False
    
    def login(self):
        self.get_data_user_password = self.model.get_username_password()
        self.get_user_pass_data = dict(self.get_data_user_password)

        self.get_usr_pswd = self.model.get_username_password_sqlalchemy()
        self.new_list_usr_pswd = []

        for delete in self.get_usr_pswd:
            delete_list=list(delete)
            del delete_list[0]
            self.new_list_usr_pswd.append(delete_list)

        self.usr_pswd_dict = dict(self.new_list_usr_pswd)
        
        if self.view.username.text in self.usr_pswd_dict and self.view.password.text in self.usr_pswd_dict.values():
            print ('cocok')
            print(self.view.username.text,self.view.password.text)
            return True
        elif self.view.username.text in self.get_user_pass_data and self.view.password.text in self.get_user_pass_data.values():
            # superuser online is needed
            print ('cocok')
            return True
        else:
            return False
