from django.urls import path
from .views import vendor_detail
urlpatterns = [ path("<int:pk>/", vendor_detail, name="vendor_detail") ]
