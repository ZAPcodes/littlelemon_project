from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/',MenuItemView.as_view(),name='menuitem-list'),
    path('menu/<int:pk>',SingleMenuItemView.as_view(),name='menuitem-detail'),
    path('api-token-auth/', obtain_auth_token),
    path('',index,name='index'),
]