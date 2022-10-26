from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # Article
    path('', views.index, name='index'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.article_update, name='article_update'),
    path('<int:article_pk>/delete/', views.article_delete, name='article_delete'),
    path('<int:article_pk>/like/', views.article_like, name='article_like'),
    # Comment
    path('<int:article_pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/like/', views.comment_like, name='comment_like'),
]
