from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.PostListCategory.as_view()),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
