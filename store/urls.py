from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    # path('product/<int:pk>/',product_details, name='product-details')
    path('product/<slug:slug>/',ProductDetailView.as_view(), name='product-details')
]