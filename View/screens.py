# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.register_screen import RegisterScreenModel
from Controller.register_screen import RegisterScreenController
from Model.mainmenu_screen import MainmenuScreenModel
from Controller.mainmenu_screen import MainmenuScreenController
from Model.poskasir_screen import PoskasirScreenModel
from Controller.poskasir_screen import PoskasirScreenController
from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.inventory_screen import InventoryScreenModel
from Controller.inventory_screen import InventoryScreenController
from Model.productlist_screen import ProductlistScreenModel
from Controller.productlist_screen import ProductlistScreenController
from Model.maintain_screen import MaintainScreenModel
from Controller.maintain_screen import MaintainScreenController
from Model.addproduct_screen import AddproductScreenModel
from Controller.addproduct_screen import AddproductScreenController
from Model.deleteproduct_screen import DeleteproductScreenModel
from Controller.deleteproduct_screen import DeleteproductScreenController

screens = {
    'inventory screen': {
        'model': InventoryScreenModel,
        'controller': InventoryScreenController,
    },
    'register screen': {
        'model': RegisterScreenModel,
        'controller': RegisterScreenController,
    },
    'poskasir screen': {
        'model': PoskasirScreenModel,
        'controller': PoskasirScreenController,
    },
    'deleteproduct screen': {
        'model': DeleteproductScreenModel,
        'controller': DeleteproductScreenController,
    },
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
    'maintain screen': {
        'model': MaintainScreenModel,
        'controller': MaintainScreenController,
    },
    'mainmenu screen': {
        'model': MainmenuScreenModel,
        'controller': MainmenuScreenController,
    },
    'addproduct screen': {
        'model': AddproductScreenModel,
        'controller': AddproductScreenController,
    },
    'productlist screen': {
        'model': ProductlistScreenModel,
        'controller': ProductlistScreenController,
    },
}