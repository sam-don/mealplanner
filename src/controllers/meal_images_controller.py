from models.MealImage import MealImage
from models.Meal import Meal
from schemas.MealImageSchema import meal_image_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

meal_images = Blueprint('meal_images', __name__, url_prefix="/meals/<int:meal_id>/image")

@meal_images.route("/", methods=["POST"])
def meal_image_create(meal_id):
    if "image" in request.files:
        image = request.files["image"]
        image.save("uploaded_images/file_1")
        return ("", 200)
    return abort(400, description="No image")

@meal_images.route("/<int:id>", methods=["GET"])
def meal_image_show(meal_id, id):
    pass

@meal_images.route("/<int:id>", methods=["DELETE"])
@jwt_required
def meal_image_delete(meal_id, id):
    pass