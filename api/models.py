from django.db import models


RACE_CHOICES = (
    ('Ork', 'Ork'),
    ('Wizard', 'Wizard'),
    ('Elf', 'Elf')
)

class Hero(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50, choices=RACE_CHOICES)

    def __str__(self):
        return self.name
    