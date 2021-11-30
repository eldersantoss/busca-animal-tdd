from django.shortcuts import render

from animais.models import Animal


def index(request):

    animals = Animal.objects.all()
    animal_name = request.GET.get("animal")
    if animal_name is not None:
        animals = animals.filter(name__icontains=animal_name)
    context = {"animals": animals}
    return render(request, "index.html", context)
