from Model.base_model import BaseScreenModel
from Model.automap import Inventory
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


class AddproductScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.addproduct_screen.AddproductScreen.AddproductScreenView` class.
    """

    def add_product(self,*args):
        self.args=args[0]
        self.produk_name = self.args[0]
        self.quantity = self.args[1]
        self.sale_price = self.args[2]
        engine = self.engine()
        # connection = engine.connect()
        Session= sessionmaker(bind=engine)
        session= Session()
        self.inventory = Inventory()
        self.inventory.produk_name = self.produk_name.text
        self.inventory.quantity = self.quantity.text
        self.inventory.sale_price = self.sale_price.text
        session.add(self.inventory)
        session.flush()
        session.commit()
        session.close()
        engine.dispose()
        return True

    def delete_product(self,*args):
        self.args=args[0]
        self.produk_name = self.args[0]
        self.quantity = self.args[1]
        self.sale_price = self.args[2]
        engine = self.engine()
        # connection = engine.connect()
        Session= sessionmaker(bind=engine)
        session= Session()
        self.inventory = Inventory()
        self.inventory.produk_name = self.produk_name.text
        self.inventory.quantity = self.quantity.text
        self.inventory.sale_price = self.sale_price.text
        session.add(self.inventory)
        session.flush()
        session.commit()
        session.close()
        engine.dispose()
        return True
 


