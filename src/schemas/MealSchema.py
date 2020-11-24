from main import ma
from models.Meal import Meal
from marshmallow.validate import Length


class MealSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meal

    title = ma.String(required=True, validate=Length(min=3))


meal_schema = MealSchema()
meals_schema = MealSchema(many=True)
