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

screens = {
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
    'mainmenu screen': {
        'model': MainmenuScreenModel,
        'controller': MainmenuScreenController,
    },
    'register screen': {
        'model': RegisterScreenModel,
        'controller': RegisterScreenController,
    },
    'poskasir screen': {
        'model': PoskasirScreenModel,
        'controller': PoskasirScreenController,
    },

}