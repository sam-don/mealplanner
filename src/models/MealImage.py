from main import db

class MealImage(db.Model):
    __tablename__ = "meal_images"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String())
    meal_id = db.Column(db.Integer, db.ForeignKey("meals.id"), nullable=False)

    def __repr__(self):
        return f"<MealImage {self.id}>"