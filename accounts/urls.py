from django.urls import path
from .views import SignUpView, ConfirmLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('confirmlogout/', ConfirmLogoutView.as_view(), name='confirmlogout'),
    
]