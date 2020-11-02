
from django.urls import path, include
from . import views
from .views import HomePage, ArticleDetailView, AddPostView

urlpatterns = [
    path('', HomePage.as_view(), name='Home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
]

