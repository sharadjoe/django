from django.http import Http404
from django.shortcuts import render
from .models import album

def index(request):
    all_albums = album.objects.all()


    return render(request, 'music/index.html', {'all_albums' : all_albums,})

def detail(request, album_id):
    try:
        album = album.objects.get(pk=album_id)
    except album.DoesNotExist:
        raise Http404("Album Doesnot Exist")
    return render(request, 'music/detail.html', {'album' : album})
