from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import PDFFile
import os

def pdf_home(request):
    return render(request, 'pdf_tools/home.html')

def merge_pdfs(request):
    if request.method == 'POST' and request.FILES.getlist('pdf_files'):
        pdf_files = request.FILES.getlist('pdf_files')
        # Process PDF merging here
        # This is a placeholder for actual PDF processing logic
        return HttpResponse("PDFs merged successfully!")
    return render(request, 'pdf_tools/merge.html')

def split_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        # Process PDF splitting here
        # This is a placeholder for actual PDF processing logic
        return HttpResponse("PDF split successfully!")
    return render(request, 'pdf_tools/split.html')

def compress_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        # Process PDF compression here
        # This is a placeholder for actual PDF processing logic
        return HttpResponse("PDF compressed successfully!")
    return render(request, 'pdf_tools/compress.html')