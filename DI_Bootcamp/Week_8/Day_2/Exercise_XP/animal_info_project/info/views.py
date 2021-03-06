from django.shortcuts import render
from .models import Family, Animal

def family(request, family_id):
    fam = Family.objects.get(id=family_id)
    context = {'family': fam,}
    return render(request, 'family.html', context)

def animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    context = {'animal': animal}
    return render(request, 'animal.html', context)

def animals(request):
    animals_all = Family.objects.all()
    context = {'animals_all': animals_all}
    return render(request, 'animals.html', context)