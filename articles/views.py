from typing import Optional
from django.shortcuts import render
from .models import Article, Comment
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body', 'image')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView): 
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'image')

    # Funcion para hacer author = al request user, se elimina author de fields
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "add_comment.html"
    fields = ('comment', 'image_comment')

    # Get contex data del post actual para mostrarlo al crear el comentario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = get_object_or_404(Article, id=self.kwargs['pk'])

        return super(AddCommentView, self).form_valid(form)
        
# Clases agregadas por mi para editar y eliminar comentarios

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.article.pk})
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    fields = ('comment', 'image_comment')

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.article.pk})
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user