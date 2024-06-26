from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/following/', views.following, name='following'),
    path('<int:user_pk>/follower/', views.follower, name='follower'),
]
