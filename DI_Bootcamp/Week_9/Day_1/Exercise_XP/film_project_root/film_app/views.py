from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def homepage(request):
    films = Film.objects.all()
    context = {
        'films':films,
    }
    return render(request, 'homepage.html', context)

def addFilm(request):
    if request.method == "GET":
        return render(request, 'add_film.html', {'add_film':AddFilmForm()})

    if request.method == 'POST':

        add_film = AddFilmForm(request.POST)

        if add_film.is_valid():
            add_film.save()
            return redirect('homepage')

        else:
            return render(request, 'add_film.html', {'add_film':add_film})


class AddDirector(generic.CreateView):
    form_class = AddDirectorForm
    template_name = 'add_director.html'
    success_url = reverse_lazy('homepage.html')
