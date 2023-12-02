from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    population = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(null=True)

    # Add other fields as needed

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='attraction_images/')
    # Add other fields as needed

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']




class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class UserGeneratedContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_generated_images/')
    # Add other fields as needed

    def __str__(self):
        return self.name





