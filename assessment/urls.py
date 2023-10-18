from django.urls import path
from .views import SuperHeroListView, SuperHeroDetailView

app_name = "legal"
urlpatterns = [
    path("", SuperHeroListView.as_view(), name="list"),
    path("<int:pk>/detail/", SuperHeroDetailView.as_view(), name="detail"),
]
