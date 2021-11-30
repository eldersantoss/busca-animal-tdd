from django.db import models


class Animal(models.Model):

    name = models.CharField("nome", max_length=50)
    predator = models.BooleanField("predador")
    poisonous = models.BooleanField("venenoso")
    domestic = models.BooleanField("domestico")

    def __str__(self) -> str:
        return self.name
