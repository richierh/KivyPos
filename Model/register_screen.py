from Model.base_model import BaseScreenModel
from Model.automap import Person,PersonDetail
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


class RegisterScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.register_screen.RegisterScreen.RegisterScreenView` class.
    """

    def insert_data(self,*args):
        self.args=args[0]
        self.username = self.args[0]
        self.password = self.args[1]
        self.fullname = self.args[2]
        self.address  = self.args[3]

        engine = db.create_engine('sqlite:///Model/poscore.db',echo=True)
        Session= sessionmaker(bind=engine)
        session= Session()
        person = Person()
        person.username=self.username.text
        person.password=self.password.text
        # obj = session.query(Person.id).order_by(Person.id.desc()).first()
        person_detail=PersonDetail()
        person_detail.fullname=self.fullname.text
        person_detail.address=self.address.text
        session.add(person_detail)
        session.add(person)
        session.flush()
        session.commit()
        session.close()
        return True
