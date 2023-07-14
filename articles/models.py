from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True ,upload_to="post_images")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey( 
        get_user_model(), on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])
    
    # Funcion para borrar archivos media al borrar el post (gracias chat bing)
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
    
class Comment(models.Model):
    # Recordatorio: el parametro related_name permite usar la variable en la template con los articles
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    image_comment = models.ImageField(null=True, blank=True ,upload_to="comment_images")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.article.id)])
    
    def delete(self, *args, **kwargs):
        self.image_comment.delete()
        super().delete(*args, **kwargs)
    