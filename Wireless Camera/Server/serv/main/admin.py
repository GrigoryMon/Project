from django.contrib import admin
from .models import Camera,Userc,Images

class CameraAdimn(admin.ModelAdmin):
    list_display = ['camera_id']
    list_display_links = ['camera_id']

class UsercAdimn(admin.ModelAdmin):
    list_display = ['telegram_id']
    list_display_links = ['telegram_id']

class ImagesAdimn(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']

admin.site.register(Camera, CameraAdimn)
admin.site.register(Userc, UsercAdimn)
admin.site.register(Images, ImagesAdimn)