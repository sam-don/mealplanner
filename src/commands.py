from flask.cli import routes_command
from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Meal import Meal
    from faker import Faker
    faker = Faker()

    for i in range(20):
        meal = Meal()
        meal.title = faker.sentence(nb_words=3)
        db.session.add(meal)

    db.session.commit()
    print("Tables seeded")
