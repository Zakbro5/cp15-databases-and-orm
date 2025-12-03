from helper_functions import clear_screen
clear_screen()

# =========================
# CRUD PRACTICE WITH PEEWEE
# =========================

# 1. Create a dog database
'''
Create a database for dogs using peewee

The dog table should include:
    id
    name
    age
    favorite food (make it so this field is optional by adding null=True)

Using peewee
    1. create a few dogs
    2. print out some of their info,
    2. update a specific dog's favorite food
    3. delete a dog
'''

from peewee import *

db = SqliteDatabase('dogs.db')

class Dog(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age = IntegerField()
    favorite_food = CharField(null=True)

    class Meta:
        database = db

db.connect()
db.create_tables([Dog])

dog1 = Dog.create(name="Joe", age=4, favorite_food="Beef")
dog2 = Dog.create(name="Richard", age=3, favorite_food ="Eggs")
dog3 = Dog.create(name="Hank", age=7)

print("\nDogs in database:")
for dog in Dog.select():
    print(f"{dog.id}. {dog.name} - {dog.age} years old - Favorite food: {dog.favorite_food}")

dog_to_update = Dog.get(Dog.name == "Hank")
dog_to_update.favorite_food = "Chicken"
dog_to_update.save()

print("\nUpdated Hanks's favorite food:")
for dog in Dog.select():
    print(f"{dog.id}. {dog.name} - {dog.age} years old - Favorite food: {dog.favorite_food}")

dog_to_delete = Dog.get(Dog.name == "Joe")
dog_to_delete.delete_instance()

print("\nAfter deleting Joe:")
for dog in Dog.select():
    print(f"{dog.id}. {dog.name} - {dog.age} years old - Favorite food: {dog.favorite_food}")

db.close()