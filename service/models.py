from django.db import models
from email.message import Message


class contact(models.Model):
      Name=models.CharField
      Email=models.EmailField
      Messages=models.CharField
# Create your models here.
