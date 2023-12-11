from django.db import models

# Create your models here.

class Movies(models.Model):
    title=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    image = models.ImageField(upload_to="mymovies/cover", null=True, blank=True)



    def __str__(self):
        return self.title
