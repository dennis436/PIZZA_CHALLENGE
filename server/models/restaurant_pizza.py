from ..app import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.model):
    __tablename__= 'restaurant_pizzas'

    id = db.Column(db.integer, primary_key=True)
    price = db.Column(db.integer, nullable=False)
     
    restaurant_id = db.Column(db.Integer, db.ForiegnKey('restaurant.id'),nullable=False)
    pizza_id = db.Column(db.Integer, db.ForiegnKey('pizzas_id'), nullable=False)

    restaurant = db.realtionship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    @validates('prices')
    def validate_price(self, key, value):
        if not (1 <=value <= 30):
            raise ValueError("Price m,ust be between 1 and 30")
        return value         
    def __repr__(self) :
      return f'<RestaurantPizza ${self.price}'