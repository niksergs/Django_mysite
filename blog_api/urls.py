from django.urls import path, re_path
from . import views


urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),
    re_path('^user/(?P<id>.+)/$', views.UserPostList.as_view()),
]
