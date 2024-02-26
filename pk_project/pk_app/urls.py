from django.urls import path, include
from pk_app import views

urlpatterns = [
    # path('currencies', views.currencies.as_view(), name='currencies'),
    # path('currency/<int:id>', views.currency.as_view(), name='currency'),
    path('ping', views.ping, name='ping'),
    path('jsonrpc', views.jsonrpc, name='jsonrpc'),
]
