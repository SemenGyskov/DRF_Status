from django.urls import path
from .views  import *

urlpatterns = [
    path('get-status/', get_status),
    path('order/', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
    path('status/', StatusListCreateView.as_view(), name='status-list-create'),
    path('status/<int:pk>/', StatusRetrieveUpdateDestroyView.as_view(), name='status-retrieve-update-destroy'),
    path('worker/', WorkerListCreateView.as_view(), name='worker-list-create'),
    path('worker/<int:pk>/', WorkerRetrieveUpdateDestroyView.as_view(), name='worker-retrieve-update-destroy'),
    path('work/', WorkListCreateView.as_view(), name='work-list-create'),
    path('work/<int:pk>/', WorkRetrieveUpdateDestroyView.as_view(), name='work-retrieve-update-destroy'),
]
