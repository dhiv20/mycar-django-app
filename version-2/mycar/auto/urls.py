from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),			#edit as required
    path('index.html/', views.index, name='index'),
    path('cars.html/', views.cars, name='cars'),
    path('contact.html/', views.contact, name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('services.html/', views.services, name='services'),
   # path('admin/', admin.site.urls),
]
