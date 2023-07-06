from django.urls import path
from .views import (
    ArticleListView, 
    ArticleUpdateView, 
    ArticleDetailView, 
    ArticleDeleteView,
    ArticleCreateView,
    AddCommentView,
    CommentDeleteView,
    CommentEditView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('<int:pk>/delete_comment/', CommentDeleteView.as_view(), name='delete_comment'),
    path('<int:pk>/edit_comment/', CommentEditView.as_view(), name='edit_comment'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]
