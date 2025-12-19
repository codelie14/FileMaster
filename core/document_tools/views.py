from django.shortcuts import render
from django.http import HttpResponse

def document_home(request):
    return render(request, 'document_tools/home.html')

def convert_document(request):
    if request.method == 'POST' and request.FILES.get('document_file'):
        document_file = request.FILES['document_file']
        # Process document conversion here
        # This is a placeholder for actual document processing logic
        return HttpResponse("Document converted successfully!")
    return render(request, 'document_tools/convert.html')

def merge_documents(request):
    if request.method == 'POST' and request.FILES.getlist('document_files'):
        document_files = request.FILES.getlist('document_files')
        # Process document merging here
        # This is a placeholder for actual document processing logic
        return HttpResponse("Documents merged successfully!")
    return render(request, 'document_tools/merge.html')

def extract_text(request):
    if request.method == 'POST' and request.FILES.get('document_file'):
        document_file = request.FILES['document_file']
        # Process text extraction here
        # This is a placeholder for actual document processing logic
        return HttpResponse("Text extracted successfully!")
    return render(request, 'document_tools/extract_text.html')