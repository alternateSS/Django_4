from restaraunt.models import *


# Users
user_1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
user_2 = User.objects.create(email='altywa1998@gmail.com', password='nono34')


# Clients
client = Client.objects.create(user=user_1, name='Азат Соколов', card_number=4147_5657_9878_9009)


# Workers
worker = Worker.objects.create(user=user_2, name='Алтынай Алиева', position='Оператор кассы')


# Food
food_1 = Food.objects.create(name='Шаурма', start_price=50)
food_2 = Food.objects.create(name='Гамбургер', start_price=25)

# Ingredients
ingredients_1 = Ingredient.objects.create(name='Сыр', extra_price=10)
ingredients_2 = Ingredient.objects.create(name='Курица', extra_price=70)
ingredients_3 = Ingredient.objects.create(name='Говядина', extra_price=80)
ingredients_4 = Ingredient.objects.create(name='Салат', extra_price=15)
ingredients_5 = Ingredient.objects.create(name='Фри', extra_price=15)

food_1.orders.set([ingredients_3, ingredients_4, ingredients_5], through_defaults={'client':client, 'worker':worker})
order_1 = food_1.start_price + ingredients_3.extra_price + ingredients_4.extra_price + ingredients_5.extra_price
print(order_1)

food_2.orders.set([ingredients_2, ingredients_4], through_defaults={'client':client, 'worker':worker})
order_2 = food_2.start_price + ingredients_2.extra_price + ingredients_4.extra_price
print(order_2)
