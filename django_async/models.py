from django.db import models


# Create your models here.
class file_and_pic(models.Model):
    upload_file = models.FileField(upload_to="file/")
    picture = models.ImageField(width_field=20,upload_to="images/")
