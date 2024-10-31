from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('menu/',MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>',MenuDetailView.as_view(), name='menu-item'),
    # path('booking',BookingView.as_view(), name='booking')
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]