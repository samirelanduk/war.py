from django.urls import path
from maps.views import MapListView, MapDetailView

urlpatterns = [
    path("maps/", MapListView.as_view()),
    path("maps/<int:pk>/", MapDetailView.as_view()),
]
