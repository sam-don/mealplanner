from main import ma
from models.Meal import Meal
from marshmallow.validate import Length

from schemas.UserSchema import UserSchema


class MealSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meal

    title = ma.String(required=True, validate=Length(min=3))
    user = ma.Nested(UserSchema)


meal_schema = MealSchema()
meals_schema = MealSchema(many=True)
