from ..app import db

class Restaurant(db.model):
    __tablename__='restaurants'
    id = db.column(db.integer,primary_key=True)
    name = db.column(db.string,nullable=False)
    address = db.column(db.string,nullable=False)

    restaurant_pizzas = db.realationship('RestaurantPizzas', back_populates='restaurant', cascade='all,delete-orphan')
    def __repr__(self):
     return f'<Restaurant {self.name}>'