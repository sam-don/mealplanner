from flask_sqlalchemy import SQLAlchemy
from main import ma
from models.MealImage import MealImage
from marshmallow.validate import Length

class MealImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MealImage

    filename = ma.String(required=True, validate=Length(min=1))

meal_image_schema = MealImageSchema() 