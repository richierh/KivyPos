from View.base_screen import BaseScreenView
from kivy.properties import StringProperty
import time
from kivy.clock import Clock
import threading


class MainScreenView(BaseScreenView):
    mistake=StringProperty('')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.theme_cls.primary_palette='Purple'

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if not(self.matches):
            self.manager_screens.current='maintain screen'

        elif self.controller.login()==True:
            self.manager_screens.current = "mainmenu screen"
            self.manager_screens.get_screen('mainmenu screen').nav_drawer.set_state('close')
        else:
            print('kacau')
            threading.Thread(target=self.do_something).start()

    def do_something(self):
        self.update_time()
        self.mistake=''

    def run(self,number):
        self.number=number
        self.mistake='Username atau password salah {}'.format(self.number)

    def update_time(self):
        for timenow in reversed(range(0,11)):
            Clock.schedule_once(lambda dt: self.run(timenow))
            time.sleep(1)

    def login(self,*args):
        self.username=args[0]
        self.password=args[1]
        token = "a"
        self.token = token
        self.matches = self.controller.token()
        self.controller.login()
        self.model_is_changed()

    def signup(self):
        self.manager_screens.current = "register screen"
        print("go to sign up screen")