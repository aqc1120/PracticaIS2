from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import Opinion
from .forms import OpinionForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', { 'destinations': all_destinations})

def opinion(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            # Guardar la opinión en la base de datos
            Opinion.objects.create(
                name=form.cleaned_data['name'],
                cruise=form.cleaned_data['cruise'],
                opinion=form.cleaned_data['opinion']
            )
            # Redirigir a la misma página después de enviar la opinión
            return redirect('opinion')
    else:
        form = OpinionForm()

    opinions = Opinion.objects.all()

    return render(request, 'opinion.html', {'form': form, 'opinions': opinions})


class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'

