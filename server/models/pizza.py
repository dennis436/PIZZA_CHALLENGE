from ..app import db

class Pizza(db.model):
    __tablename__='pizzas'

    id =db.Column(db.integer,primary_key=True)
    name = db.Column(db.string ,nullable=False)
    ingredients = db.Column(db.string, nullable=False)

    restaurant_pizzas = db.realtionship('RestaurantPizzas' , back_populates='pizza')

    def __repr__(self):
        return f'<Pizza {self.name}'