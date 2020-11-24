from controllers.meals_controller import meals
from controllers.auth_controller import auth
from controllers.meal_images_controller import meal_images

registerable_controllers = [
    meals,
    meal_images,
    auth
]
