import datetime
from django.db import models


def current_year():
    return datetime.datetime.today().year


class Movie(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    year_released = models.PositiveIntegerField(default=current_year())

    def __str__(self):
        return self.name
