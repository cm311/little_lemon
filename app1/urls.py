from . import views
from django.urls import path



urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    path('home_form/', views.form_view, name="form_view"),
    path('booking_form/', views.booking_form_view, name='booking_form_view')
]