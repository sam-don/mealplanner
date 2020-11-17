from models.Meal import Meal
from main import db
from schemas.MealSchema import meal_schema, meals_schema
from flask import Blueprint, request, jsonify

meals = Blueprint("meals", __name__, url_prefix="/meals")

@meals.route("/", methods=["GET"])
def meal_index():
    # Return all meals
    meals = Meal.query.all()
    return jsonify(meals_schema.dump(meals))


@meals.route("/", methods=["POST"])
def meal_create():
    # Create a new meal
    meal_fields = meal_schema.load(request.json)

    new_meal = Meal()
    new_meal.title = meal_fields["title"]

    db.session.add(new_meal)
    db.session.commit()

    return jsonify(meal_schema.dump(new_meal))

@meals.route("/<int:id>", methods=["GET"])
def meal_show(id):
    # Return a single meal
    meal = Meal.query.get(id)
    return jsonify(meal_schema.dump(meal))


@meals.route("/<int:id>", methods=["PUT", "PATCH"])
def meal_update(id):
    # Update a meal
    meals = Meal.query.filter_by(id=id)
    meal_fields = meal_schema.load(request.json)
    meals.update(meal_fields)

    db.session.commit()

    return jsonify(meal_schema.dump(meals[0]))


@meals.route("/<int:id>", methods=["DELETE"])
def meal_delete(id):
    # Delete a meal
    meal = Meal.query.get(id)

    db.session.delete(meal)
    db.session.commit()

    return jsonify(meal_schema.dump(meal))
