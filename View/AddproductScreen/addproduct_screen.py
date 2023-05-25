from View.base_screen import BaseScreenView


class AddproductScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def masukan_barang(self,*args):
        self.args=args
        # self.args1=args[1]
        # self.args2=args[2]

        # print(self.args.text)
        # print(self.args1.text)
        # print(self.args2.text)
        self.controller.add_product(self.args)

        self.model_is_changed()


    
    def batalkan_input(self):
        self.manager_screens.current='inventory screen'
        pass