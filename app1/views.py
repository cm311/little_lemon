from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *

# Create your views here.
def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment',
    }

    choice_of_drink = drink[drink_name]

    return HttpResponse(f"<h2> {choice_of_drink} </h2>")

def home(request):
    my_name = "Colin"
    return HttpResponse(f"<h1>Welcome to Little Lemon!</h1>")

def about(request):
    return HttpResponse(f"<h1>About page</h1>")

def menu(request):
    return HttpResponse(f"<h1>Menu page</h1>")

def book(request):
    return HttpResponse(f"<h1>Book page</h1>")

def form_view(request):
    form = ShiftLoggerForm()

    if request.method == 'POST':
        form = ShiftLoggerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form" : form}
    print(context)
    return render(request, 'app1/home.html', context)

def booking_form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "app1/booking.html", context)
