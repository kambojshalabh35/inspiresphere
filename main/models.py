from django.db import models

# Create your models here.
class StartUps(models.Model):
    photo = models.ImageField(upload_to = 'photos/startups/%Y/%m/%d/', blank = True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=512)
    link = models.URLField()

    def __str__(self):
        return self.title
    
class Resources(models.Model):
    photo = models.ImageField(upload_to = 'photos/resources/%Y/%m/%d/', blank = True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=512)
    modules = models.IntegerField()
    link = models.URLField()

    def __str__(self):
        return self.title