from django.shortcuts import render,redirect
from django.views.generic import UpdateView,DeleteView,CreateView,ListView
from .models import Laptop

# Create your views here.
class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/laptop/list'

class LaptopListView(ListView):
    model = Laptop

class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/laptop/list'

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url = '/laptop/list'

