from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie


class MovieListView(ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
