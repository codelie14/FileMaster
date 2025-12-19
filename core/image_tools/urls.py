from django.urls import path
from . import views

app_name = 'image_tools'

urlpatterns = [
    path('', views.image_home, name='image_home'),
    path('convert/', views.convert_image, name='convert_image'),
    path('resize/', views.resize_image, name='resize_image'),
    path('compress/', views.compress_image, name='compress_image'),
]