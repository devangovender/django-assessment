from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import SuperHero


class SuperHeroListView(ListView):
    model = SuperHero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SuperHeroDetailView(DetailView):
    model = SuperHero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
