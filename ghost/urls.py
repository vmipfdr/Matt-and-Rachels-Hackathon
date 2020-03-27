from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>', views.customer_detail, name='customer_detail'),
    path('customers/create', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit', views.customer_edit, name='customer_edit'),
    path('customers/<int:pk>/delete', views.customer_delete, name='customer_delete')
]
