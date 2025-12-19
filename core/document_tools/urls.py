from django.urls import path
from . import views

app_name = 'document_tools'

urlpatterns = [
    path('', views.document_home, name='document_home'),
    path('convert/', views.convert_document, name='convert_document'),
    path('merge/', views.merge_documents, name='merge_documents'),
    path('extract-text/', views.extract_text, name='extract_text'),
]