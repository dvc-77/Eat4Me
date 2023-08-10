from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from api.forms import UserForm, RestaurantForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='/login/')
def restaurant_dashboard(request):
    return render(request, 'dashboard.html', {})

def restaurant_sign_up(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)
        
        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            )) 

            return redirect(restaurant_dashboard)

 
    return render(request, 'sign_up.html', {
        "uf": user_form,
        "rf": restaurant_form
    }) 

