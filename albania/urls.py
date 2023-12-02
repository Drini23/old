from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='albania'),
    path('city/', views.city, name='city'),
    path('attraction/', views.attraction, name='attraction'),
    path('<int:id>', views.detail, name='detail'),
    path('attraction/<int:id>', views.attraction_detail, name='attraction'),


    path('login/', views.loginPage, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.registerPage, name='register'),

]

