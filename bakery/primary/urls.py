from django.urls import path
from primary import views
from django.conf import settings
from django.conf.urls.static import static



# Template Tagging
app_name = 'primary'

urlpatterns = [
    path('index/',views.RestaurantContactView.as_view(),name='restaurant'),
    path('',views.RestaurantContactView.as_view(),name='restaurant'),
    path('restaurant/',views.RestaurantContactView.as_view(),name='restaurant'),
    path('restaurant-base/',views.RestaurantBaseView.as_view(),name='restaurant-base'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
