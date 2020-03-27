from django.db import models

# Create your models here.


class Customer(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    # setting up the @ and . restrictions

    def __str__(self):
        return self.email


# this gives us the ability to delete the artist and their songs
# with related_name gives us the ability to find songs by artist.songs
# now we need to create a migration for our model
# this is where you run a few commands
# python manage.py makemigrations
# python manage.py migrate
