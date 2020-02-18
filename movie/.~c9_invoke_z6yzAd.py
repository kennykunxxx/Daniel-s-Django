from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import requests
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponseRedirect
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.utils.dateparse import parse_date
from dvd.

from .models import movie
# Create your views here.

base_url = 'https://api.themoviedb.org/3/'
api_key = '44546d0b46d2674ccb7766f74d0369f0'

def home(request):
    return render(request, 'movie/home.html')

def search(request):
    search_query = request.GET.get('q')
    url = f'{base_url}search/movie?api_key={api_key}&query={search_query}'
    search = requests.get(url)
    search = search.json()
    results = {'searches': search}
    
    return render(request, 'movie/search.html', context = results)
    
def detail(request, search_id):
    url = f'{base_url}movie/{search_id}?api_key={api_key}'
    search_detail = requests.get(url)
    search_detail = search_detail.json()
    search_result = {'search_detail': search_detail}
    
    return render(request, 'movie/detail.html', context=search_result)
    


def add(request, search_id):
    if request.method == 'POST':
        url = f'{base_url}movie/{search_id}?api_key={api_key}'
        search_detail = requests.get(url)
        search_detail = search_detail.json()
        temp_date = parse_date(search_detail['release_date'])
        if request.user.is_authenticated:
            if movie.objects.filter(title=search_detail['title'], user=request.user).exists():
                return HttpResponse('It is already saved in the list')
            else:    
                save_item = movie(title=search_detail['title'], description=search_detail['overview'], year=temp_date)
                save_item.user = request.user
                save_item.save()
                messages.success(request, 'saved')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse('<h1> user is not authenticated </h1>')
            
    elif request.method == 'GET':
        pass
    
    return render(request, 'movie/add.html')


def user_list(request):
    movie_list = movie.objects.filter(user=request.user)
    return render(request, 'movie/user_list.html', {'movie_list': movie_list})
    
def delete_movie(request, movie_id):
    if request.method == 'GET':
        get_movie = get_object_or_404(movie, id = movie_id)
        get_movie.delete()
        messages.success(request, 'movie deleted')
        
    return redirect('movie:user_list')
        
        
        
        
        
"""
@require_POST  
def add(request, search_id, search_overview, search_date):
    if request.method == 'POST':
        form = request.method['POST']
        add_movie = movie(title=form['search_id'], description=form['search_overview'], year=form['search_date'])
        add_movie.save()
    return HttpResponseRedirect(request.path_info)

@require_POST  
def add(request, search_id, search_overview):
    if request.method == 'POST':
        add_movie = movie(title=search_id, description=search_overview)
        add_movie.save()
    return redirect('home')
    
@require_GET
def add(request, search_id, search_overview):
    pass
    



def add(request, search_id):
    if request.method == 'POST':
        url = f'{base_url}movie/{search_id}?api_key={api_key}'
        search_detail = requests.get(url)
        search_detail = search_detail.json()
        if request.user.is_authenticated:
            if search_detail['title']:
                save_item = movie(title=search_detail['title'])
                save_item.user = request.user
                save_item.save()
                
                
        else:
            return HttpResponse('<h1> user is not authenticated </h1>')
            
    elif request.method == 'GET':
        pass
    return render(request, 'movie/add.html')
    
"""    