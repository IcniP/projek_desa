# profil/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Selamat Datang di Halaman Profil</h1>")