from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'userinfo'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    template_name = "user_update.html"
    fields = (
            'email' ,'age', 'profile_image',
            'description', 'title', 'waifu', 'website',
            'github', 'linkedin',
        )
    slug_field = 'username'
    slug_url_kwarg = 'username'
    
    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'username': self.object.username})
    
    def test_func(self):
        user = self.get_object()
        return self.request.user == user
    
    
    