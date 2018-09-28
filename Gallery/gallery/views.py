from django.shortcuts import render
from django.http  import HttpResponse
from .models import *

# Create your views here.

def gallery(request):
    images = Image.gallery_image()
    return render(request, 'Gallery.html', {"images":images})


def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})