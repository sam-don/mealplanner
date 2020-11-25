from models.MealImage import MealImage
from models.Meal import Meal
from schemas.MealImageSchema import meal_image_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort, current_app, Response
from pathlib import Path
from main import db
import boto3

meal_images = Blueprint('meal_images', __name__, url_prefix="/meals/<int:meal_id>/image")

@meal_images.route("/", methods=["POST"])
@jwt_required
def meal_image_create(meal_id):
    meals = Meal.query.filter_by(id=meal_id, user_id=get_jwt_identity())

    if meals.count() != 1:
        return abort(401, description="Invalid book")

    if "image" not in request.files:
        return abort(400, description="No image")

    image = request.files["image"]

    if Path(image.filename).suffix not in ['.png', '.jpg', '.jpeg']:
        return abort(400, description="Invalid file type")

    filename = f"{meal_id}{Path(image.filename).suffix}"

    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    key = f"meal_images/{filename}"
    bucket.upload_fileobj(image, key)

    if not (meals[0].meal_image):
        new_image = MealImage()
        new_image.filename = filename
        meals[0].meal_image = new_image
        db.session.commit()

    return ("", 200)

@meal_images.route("/<int:id>", methods=["GET"])
def meal_image_show(meal_id, id):
    meal_image = MealImage.query.filter_by(id=id, meal_id=meal_id).first()

    if not meal_image:
        return abort(404, description="No book image")
    
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    filename = meal_image.filename
    file_obj = bucket.Object(f"meal_images/{filename}").get()

    return Response(
        file_obj['Body'].read(),
        mimetype='image/*',
        headers={"Content-Disposition": f"attachement;filename=image"}
    )

@meal_images.route("/<int:id>", methods=["DELETE"])
@jwt_required
def meal_image_delete(meal_id, id):
    meal = Meal.query.filter_by(id=meal_id, user_id=get_jwt_identity()).first()

    if not meal:
        return abort(401, description = "Invalid meal")

    if meal.meal_image:
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        filename = meal.meal_image.filename

        bucket.Object(f"meal_images/{filename}").delete()

        db.session.delete(meal.meal_image)
        db.session.commit()

    return jsonify("Successfully removed")