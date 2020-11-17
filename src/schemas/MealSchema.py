from main import ma
from models.Meal import Meal

class MealSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meal

meal_schema = MealSchema()
meals_schema = MealSchema(many=True)
