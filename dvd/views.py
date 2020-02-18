from django.shortcuts import render, get_object_or_404, redirect
from dvd.forms import dvd_forms, buy_form
from dvd.models import Dvd
from dvd.cart  import Cart
from movie.models import movie
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

    
def cart_detail(request):
    cart=Cart(request)
    form = buy_form()
    if request.method == 'POST':
        form = buy_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['buy'] == "True":
                order = form.save(commit=False)
                order.save()
                cart.create(order)
                messages.success(request, 'Item has been bought')
                cart.clear()
                return redirect('dvd:cart_detail')
                    
    return render(request, 'dvd/cart_detail.html', {'cart': cart, 'form': form})

def add_movie_cart(request, movie_id):
    cart = Cart(request)
    dvd_object = get_object_or_404(movie, id=movie_id)
    if request.method == 'POST':
        forms = dvd_forms(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            cart.add(dvd=dvd_object, quantity=cd['quantity'], update_quantity=cd['update_quantity'])
    return redirect('dvd:cart_detail')
    
def remove_movie_cart(request, movie_id):
    cart=Cart(request)
    dvd_object=get_object_or_404(movie, id=movie_id)
    if request.method == 'POST':
        cart.remove(dvd_object)
        cart.save()
    return redirect('dvd:cart_detail')