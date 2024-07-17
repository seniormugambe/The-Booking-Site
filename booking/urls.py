from django.urls import path
from . import views

app_name = "booking"


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'), 
    path('', views.item_list, name='product'),
    path("book/", views.book_item, name='book'),
    path('confirmation/', views.booking_confirmation, name='confirmation'),
    
]
