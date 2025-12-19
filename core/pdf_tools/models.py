from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class PDFFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_file = models.FileField(upload_to='pdfs/original/')
    processed_file = models.FileField(upload_to='pdfs/processed/', null=True, blank=True)
    tool_used = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    processed_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='uploaded')
    
    def __str__(self):
        return f"{self.original_file.name} - {self.tool_used}"