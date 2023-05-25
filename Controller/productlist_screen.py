import importlib

import View.ProductlistScreen.productlist_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.ProductlistScreen.productlist_screen)




class ProductlistScreenController:
    """
    The `ProductlistScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.productlist_screen.ProductlistScreenModel
        self.view = View.ProductlistScreen.productlist_screen.ProductlistScreenView(controller=self, model=self.model)

    def get_view(self) -> View.ProductlistScreen.productlist_screen:
        return self.view
