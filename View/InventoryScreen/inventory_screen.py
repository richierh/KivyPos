from View.base_screen import BaseScreenView
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivymd.uix.button import MDIconButton

class InventoryScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    
    def main_menu(self):
        self.manager_screens.current="mainmenu screen"
    
    def add_product_page(self):
        self.manager_screens.current='addproduct screen'
    
    def del_product_page(self):
        self.manager_screens.current='deleteproduct screen'


class CustomButtonIcon(RectangularRippleBehavior,ButtonBehavior,MDBoxLayout):
    pass