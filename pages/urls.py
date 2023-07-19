from django.urls import path
from .views import HomePageView, UserDetailView, UserUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:username>/', UserDetailView.as_view(), name='user_detail'),
    path('<slug:username>/update', UserUpdateView.as_view(), name='user_update'),
]