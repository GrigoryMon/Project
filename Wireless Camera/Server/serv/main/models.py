from django.db import models
from matplotlib import image

class Userc(models.Model):
    telegram_id = models.IntegerField('Telegram Id')

class Camera(models.Model):
    camera_id = models.IntegerField('Camera')
    user = models.ManyToManyField(Userc, verbose_name='Users')

class Images(models.Model):
    image=models.TextField('Image')
    user = models.ForeignKey(Userc, models.CASCADE, null=True, verbose_name='User')
    camera = models.ForeignKey(Camera, models.SET_NULL, null=True, verbose_name='Camera')
