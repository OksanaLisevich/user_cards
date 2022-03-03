from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    card_number = models.BigIntegerField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.card_number)


class CardSum(models.Model):
    sum = models.FloatField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
