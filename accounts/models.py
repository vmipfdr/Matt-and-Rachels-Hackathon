from django.db import models

# Create your models here.


class User(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.TextField(max_length=50)

    def __str__(self):
        return self.author


# class Comment(models.Model):
#     author = models.CharField(max_length=100)
#     body = models.CharField(max_length=200)
#     post = models.ForeignKey(
#         Post, on_delete=models.CASCADE, related_name='comment')

#     def __str__(self):
#         return self.body

# this gives us the ability to delete the artist and their songs
# with related_name gives us the ability to find songs by artist.songs
# now we need to create a migration for our model
# this is where you run a few commands
# python manage.py makemigrations
# python manage.py migrate
