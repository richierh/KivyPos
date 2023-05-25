from View.base_screen import BaseScreenView
from kivy.metrics import dp

from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen


class ProductlistScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # import pdb
        # pdb.set_trace()
        self.table_create()
        pass 

    def table_create(self):
        self.column_datas=[
            ("Product Number", dp(30)),
            ("Product Name", dp(100),self.sort_on_name),
            ("Product Variant", dp(30)),
            ("Barcode", dp(30)),
            ("Quantity", dp(60), self.sort_on_signal),
            ("Schedule", dp(30), self.sort_on_schedule),
            ("Team Lead", dp(30), self.sort_on_team),
        ]
        self.row_datas=[
            (
                "1",
                ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                "Astrid: NE shared managed",
                "Medium",
                "Triaged",
                "00:33",
                "Chase Nguyen",
            ),
            (
                "2",
                ("alert-circle", [1, 0, 0, 1], "Offline"),
                "Cosmo: prod shared ares",
                "Huge",
                "Triaged",
                "00:39",
                "Brie Furman",
            ),
            (
                "3",
                (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online",
                ),
                "Phoenix: prod shared lyra-lists",
                "Minor",
                "Not Triaged",
                "3:12",
                "Jeremy lake",
            ),
            (
                "4",
                (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online",
                ),
                "Sirius: NW prod shared locations",
                "Negligible",
                "Triaged",
                "13:18",
                "Angelica Howards",
            ),
            (
                "5",
                (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online",
                ),
                "Sirius: prod independent account",
                "Negligible",
                "Triaged",
                "22:06",
                "Diane Okuma",
            ),
        ]



        self.data_tables = MDDataTable(
        use_pagination=True,
        # check=True,
        column_data=self.column_datas,
        row_data=self.row_datas,
        sorted_on="No",
        sorted_order="ASC",
        elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.boxlayout.add_widget(self.data_tables)
        return self.boxlayout

    def sort_on_name(self,data):
        return zip(*sorted(enumerate(data),key=lambda l:l[1][1]))

    def sort_on_signal(self, data):
        print('hhh')
        print(data)
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        from datetime import datetime
        # c =zip(
        #     *sorted(
        #         enumerate(data),
        #         key=lambda l: sum(
        #             [
        #                 int(l[1][-2].split(":")[0]) * 60,
        #                 int(l[1][-2].split(":")[1]),
        #             ]
        #         ),
        #     )
        # )
        print(data)

        c =zip(
            *sorted(
                enumerate(data),
                key=lambda l: datetime.strptime(l[1][-2],"%H:%M")
                )
        )
        
        return c

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))


    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)