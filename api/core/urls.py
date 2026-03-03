from django.urls import include, path

urlpatterns = [
    path("", include("maps.urls")),
]
