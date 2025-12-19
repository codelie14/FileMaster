from django.shortcuts import render
from django.http import HttpResponse

def image_home(request):
    return render(request, 'image_tools/home.html')

def convert_image(request):
    if request.method == 'POST' and request.FILES.get('image_file'):
        image_file = request.FILES['image_file']
        # Process image conversion here
        # This is a placeholder for actual image processing logic
        return HttpResponse("Image converted successfully!")
    return render(request, 'image_tools/convert.html')

def resize_image(request):
    if request.method == 'POST' and request.FILES.get('image_file'):
        image_file = request.FILES['image_file']
        # Process image resizing here
        # This is a placeholder for actual image processing logic
        return HttpResponse("Image resized successfully!")
    return render(request, 'image_tools/resize.html')

def compress_image(request):
    if request.method == 'POST' and request.FILES.get('image_file'):
        image_file = request.FILES['image_file']
        # Process image compression here
        # This is a placeholder for actual image processing logic
        return HttpResponse("Image compressed successfully!")
    return render(request, 'image_tools/compress.html')