from django.urls import path
from . import views

urlpatterns = [
    path('terbaru/', views.berita_terbaru, name='berita_terbaru'),
    path('<int:pk>/', views.berita_detail, name='berita_detail'),
]