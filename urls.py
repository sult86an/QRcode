from django.urls import path

from QRcode import views

app_name = "QRcode"
urlpatterns = [
    path('', views.start, name='start'),
    path('new/', views.new, name='new'),
]
