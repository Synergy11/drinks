from django.db import models

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    drink_description = models.CharField(max_length=500)

    # renaming data in admin page so as to display data as its save note as object one
    def __str__(self):
        return self.drink_name + ' ' + self.drink_description