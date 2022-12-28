from View.base_screen import BaseScreenView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty,StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem,MDList
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior


class CustomIconButton(RectangularRippleBehavior,ButtonBehavior,MDBoxLayout):
    source = StringProperty()
    def push(self,*args):
        print('hh')
        pass

class PosKasir(MDScreen):
    pass

class MainmenuScreenView(BaseScreenView):
    drawerlist=ObjectProperty()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.posscreen = PosKasir()
        # self.model.add_observer(self.posscreen)
        pass

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """





class ContentNavigationDrawer(MDBoxLayout):
    navigationmain=ObjectProperty()
    screenmanager = ObjectProperty()
    nav_drawer = ObjectProperty()
    screen1 = ObjectProperty()
    navigationtoolbar = ObjectProperty()

    def toggle_nav_drawer(self):
        pass



class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    pass


class DrawerList( MDList):
    md_list = ObjectProperty()
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

    def exit(self):
        self.navigationmain.app.stop()

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
#         # import pdb
#         # pdb.set_trace()

        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )
    def penjualan(self):
        print ('hhh')
        # import pdb
        # pdb.set_trace()
        self.nav_drawer.set_state('close')
        self.screenmanager.current='screen2'
        self.navigationtoolbar.title="Cash Register"
        # self.parent.parent.parent.parent.parent.manager.current='screen2'    
        # /self.ids.manager.current
    
    def product(self):
        self.nav_drawer.set_state('close')
        self.screenmanager.current='product'
        self.navigationtoolbar.title="Produk"
    def logout(self):
        print("logout")
        # import pdb
        # pdb.set_trace()
        self.navigationmain.manager_screens.current='main screen'
        # self.manager_screens.current="login_screen"