from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='product-home'),
    path('<int:product_id>', views.viewmore, name = 'ViewProduct')
]
