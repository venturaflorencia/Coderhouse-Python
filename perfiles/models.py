from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from ckeditor.fields import RichTextField
import uuid
from django.apps import apps
# Create your models here.

class Avatar(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Avatar de: {self.user}"

class ModelBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True,editable=False)
    tiempo = models.DateTimeField(auto_now_add=True)
    actualizar = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    




