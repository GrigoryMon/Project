from django.urls import path
from .views import MainRequest,Register,AddCamera,Test

urlpatterns = [
    path('', MainRequest.as_view()),
    path('Register/', Register.as_view()),
    path('AddCamera/', AddCamera.as_view()),
    path('Test/', Test.as_view())
]