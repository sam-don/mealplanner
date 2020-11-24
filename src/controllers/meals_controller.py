from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended.utils import get_jwt_identity
from schemas.MealSchema import meal_schema, meals_schema
from main import db
from models.Meal import Meal
from models.User import User
from flask_jwt_extended import jwt_required

meals = Blueprint("meals", __name__, url_prefix="/meals")


@meals.route("/", methods=["GET"])
def meal_index():
    # Return all meals
    meals = Meal.query.all()
    return jsonify(meals_schema.dump(meals))


@meals.route("/", methods=["POST"])
@jwt_required
def meal_create():
    # Create a new meal
    meal_fields = meal_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    new_meal = Meal()
    new_meal.title = meal_fields["title"]

    user.meals.append(new_meal)

    db.session.add(new_meal)
    db.session.commit()

    return jsonify(meal_schema.dump(new_meal))


@meals.route("/<int:id>", methods=["GET"])
def meal_show(id):
    # Return a single meal
    meal = Meal.query.get(id)
    return jsonify(meal_schema.dump(meal))


@meals.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def meal_update(id):
    # Update a meal
    meal_fields = meal_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    meals = Meal.query.filter_by(id=id, user_id=user.id)

    if meals.count() != 1:
        return abort(401, description="Unauthorized to update this book")

    meals.update(meal_fields)

    db.session.commit()

    return jsonify(meal_schema.dump(meals[0]))


@meals.route("/<int:id>", methods=["DELETE"])
@jwt_required
def meal_delete(id):
    # Delete a meal
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    meal = Meal.query.filter_by(id=id, user_id=user.id).first()

    if not meal:
        return abort(400)

    db.session.delete(meal)
    db.session.commit()

    return jsonify(meal_schema.dump(meal))
