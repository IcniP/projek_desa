from django.urls import path
from . import views

urlpatterns = [
    # URL untuk detail, misal: /berita/5/
    path('<int:pk>/', views.berita_detail, name='berita_detail'),
]