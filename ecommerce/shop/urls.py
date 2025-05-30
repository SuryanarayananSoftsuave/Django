from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/',views.category,name='category'),
    ]