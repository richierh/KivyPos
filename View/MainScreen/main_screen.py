from View.base_screen import BaseScreenView


class MainScreenView(BaseScreenView):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.theme_cls.primary_palette='Purple'

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def login(self):
        self.manager_screens.current = "mainmenu screen"
        self.manager_screens.get_screen('mainmenu screen').nav_drawer.set_state('close')

    def signup(self):
        self.manager_screens.current = "register screen"
        print("go to sign up screen")