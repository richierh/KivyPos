from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.properties import ListProperty


class DesktopScreenView(MDScreen):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
       
    
    def delete(self):
        print('try')
        self.man_screen.current = "delete screen"
        pass


class TableCashRegister(MDBoxLayout):
    datatable = ListProperty([])
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.orientation='horizontal'
        self.table()
        self.datatable = ['1','2']
    
    def table(self):
        self.font_size=10
        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            use_pagination=True,
            column_data=[
                ("[size={}]No.[/size]".format(self.font_size), dp(10)),
                ("[size={}]Nama Produk[/size]".format(self.font_size), dp(30)),
                ("[size={}]Kuantiti[/size]".format(self.font_size), dp(10)),
                ("[size={}]Harga[/size]".format(self.font_size), dp(20)),
                ("[size={}]Diskon[/size]".format(self.font_size), dp(15)),
                ("[size={}]Total[/size]".format(self.font_size), dp(30)),
            ],
            row_data=[
                (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
            ],
        )
        layout = self.add_widget(self.data_tables)
        
        return layout

