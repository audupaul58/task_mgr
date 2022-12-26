from django.shortcuts import  redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView,  DetailView, UpdateView, DeleteView
from .forms import ContactForm, AirdropForm
from .models import AirdropModel, Contact
from django.urls import reverse_lazy


# Create your views here.

class AboutUs(TemplateView):
    template_name = 'about.html'

class ListDisplay(ListView):
    model = Contact
    template_name = 'home.html'
    context_object_name = 'post'
    



class CreateItem(LoginRequiredMixin, CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
   
    
  

# ----------------------------------------------------------------  #

# AirdropModel Viewsets

class AirdropView(LoginRequiredMixin, ListView):
    template_name = 'managers/home.html'
    model = AirdropModel
    context_object_name = 'posts'

class MyDetailView(DetailView):
    template_name = 'managers/details.html'
    model = AirdropModel
    context_object_name = 'post'
    
class CreateAirdrop(LoginRequiredMixin, CreateView):
    template_name = 'managers/create.html'
    form_class = AirdropForm
    success_url = reverse_lazy('airdrop')
    
    
class UpdateViewAirDrop(UpdateView):
    template_name = 'managers/update.html'
    model = AirdropModel
    fields = ('url', 'title',  'frequency', 'network', 'wallet', 'completed', 'endDate', 'walletCode')
    success_url = reverse_lazy('airdrop')
    
class DeleteAirDrop(DeleteView):
    template_name = 'managers/delete.html'
    model = AirdropModel
    success_url = reverse_lazy('airdrop')
    
    