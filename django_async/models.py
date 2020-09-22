from django.db import models


# Create your models here.
class file_and_pic(models.Model):
    upload_file = models.FileField(upload_to="django_async/files")
    picture = models.ImageField(upload_to="django_async/images")