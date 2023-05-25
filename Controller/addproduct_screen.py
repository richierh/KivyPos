import importlib

import View.AddproductScreen.addproduct_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.AddproductScreen.addproduct_screen)




class AddproductScreenController:
    """
    The `AddproductScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.addproduct_screen.AddproductScreenModel
        self.view = View.AddproductScreen.addproduct_screen.AddproductScreenView(controller=self, model=self.model)

    def get_view(self) -> View.AddproductScreen.addproduct_screen:
        return self.view

    def add_product(self,*args):
        self.args = args[0]
        self.model.add_product(self.args)
        return True