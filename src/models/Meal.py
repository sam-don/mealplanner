from main import db
from models.MealImage import MealImage

class Meal(db.Model):
    __tablename__ = "meals"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    meal_image = db.relationship("MealImage", backref="meal", uselist=False)

    def __repr__(self):
        return f"<Book {self.title}>"
