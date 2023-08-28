from kivymd.uix.responsivelayout import MDResponsiveLayout

from View.PoskasirScreen.components import (
    MobileScreenView,
    TabletScreenView,
    DesktopScreenView,
)
from View.base_screen import BaseScreenView
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp



class PoskasirScreenView(MDResponsiveLayout,BaseScreenView):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileScreenView()
        self.tablet_view = TabletScreenView()
        self.desktop_view = DesktopScreenView()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def go_back(self):
        self.manager_screens.current='mainmenu screen'

# class TableCashRegister(MDBoxLayout):

#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.orientation='horizontal'

#         self.table()
    
#     def table(self):
#         self.font_size=10
#         self.data_tables = MDDataTable(
#             size_hint=(1, 1),
#             pos_hint={"center_y": 0.5, "center_x": 0.5},
#             use_pagination=True,
#             column_data=[
#                 ("[size={}]No.[/size]".format(self.font_size), dp(10)),
#                 ("[size={}]Nama Produk[/size]".format(self.font_size), dp(30)),
#                 ("[size={}]Kuantiti[/size]".format(self.font_size), dp(10)),
#                 ("[size={}]Harga[/size]".format(self.font_size), dp(20)),
#                 ("[size={}]Diskon[/size]".format(self.font_size), dp(15)),
#                 ("[size={}]Total[/size]".format(self.font_size), dp(30)),
#             ],
#             row_data=[
#                 (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
#             ],
#         )
#         layout = self.add_widget(self.data_tables)
#         return layout
