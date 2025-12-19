from django.urls import path
from . import views

app_name = 'pdf_tools'

urlpatterns = [
    path('', views.pdf_home, name='pdf_home'),
    path('merge/', views.merge_pdfs, name='merge_pdfs'),
    path('split/', views.split_pdf, name='split_pdf'),
    path('compress/', views.compress_pdf, name='compress_pdf'),
]