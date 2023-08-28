from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from View.MainmenuScreen.mainmenu_screen import MainmenuScreenView


class MobileScreenView(MDScreen):
    
    pass

class MainScreen(MDScreen):

    def go_back(self):
        self.mainmenu_screen = self.parent.parent.parent
        self.mainmenu_screen.manager_screens.current='mainmenu screen'
    
    def go_product_image(self,produk):
        self.produk = produk
        self.manager.current='product screen'
        # import pdb 
        # pdb.set_trace()
    
    def delete(self):
        print('try')
        pass
        

class SecondScreen(MDScreen):

    def go_back(self):
        self.manager.current='pos screen'
