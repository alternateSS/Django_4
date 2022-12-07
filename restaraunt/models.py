from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = 'hashed_password'
        super().save(*args, **kwargs)
        print(f'Пользователь под почтой {self.email}  сохранен')

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    card_number = models.IntegerField()

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField()
    orders = models.ManyToManyField(Ingredient, related_name='food', through='Order')


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.food.name} - {self.ingredient.name} - {self.client.name} - {self.worker.name}'



