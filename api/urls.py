from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register('city', views.CityViewSet)
router.register('attraction', views.AttractionViewSet)
#router.urls

urlpatterns = router.urls


#urlpatterns = [
#    path('city/<int:id>/', views.home, name='home'),
#    path('city_list/', views.city_list, name='city_list'),
#    path('cityes/<int:pk>/', views.city_detail, name='city_detail')
#]