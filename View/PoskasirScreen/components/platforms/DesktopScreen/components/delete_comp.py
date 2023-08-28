import View.UseScreen.components
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.properties import StringProperty,ListProperty
from View.PoskasirScreen.components.platforms.DesktopScreen.desktop_screen import (
     TableCashRegister)


class DeleteScreenView(MDScreen):
    label_text=ListProperty([])
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print(f'tulisannya {self.label_text}')
        # disini tarik data yang diambil dari mdtabledata pos screen
        self.tablecashregister = TableCashRegister()
        self.data1 = self.tablecashregister.datatable[0]
        self.data2 = self.tablecashregister.datatable[1]
        self.source='assets/images/productimages/gambar_minyak_goreng.jpg'
        self.label_text=[self.data1,self.source,self.data2]
        print(f'tulisannya {self.label_text}')


        # self.label_text=['self.data1',self.source]

    def run(self,kuantiti,nama_produk):

        self.nama_produk  = nama_produk
        self.kuantiti = kuantiti 
        self.data = [self.nama_produk.text,self.kuantiti.text]
        print(self.data)
        
        # disini masukkan data dari input ke dalam database untuk instruksi delete item
        
        
        print('konek')
        self.parent.parent.man_screen.current='pos screen'

    
    def go_back(self):
        # import pdb 
        # pdb.set_trace()
        self.parent.parent.man_screen.current='pos screen'
        print('going back')