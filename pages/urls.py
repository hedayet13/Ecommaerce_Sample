from django.urls import path
from .views import page_detail, contact
urlpatterns = [
    path("p/<slug:slug>/", page_detail, name="page_detail"),
    path("contact/", contact, name="contact"),
]
