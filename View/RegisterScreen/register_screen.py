from View.base_screen import BaseScreenView


class RegisterScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def kembali(self):
        self.manager_screens.current='main screen'
    
    def registration_proceed(self,*args):
        self.args=args
        self.controller.insert_data(self.args)