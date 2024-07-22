from django.urls import path, re_path
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)    # Пакет для генерации схемы OpenAPI
from . import views


urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),  # URL detail представления записи поста
    path('', views.PostList.as_view(), name='post_list'),               # URL list представления записей поста
    re_path('^user/(?P<id>.+)/$', views.UserPostList.as_view()),    # URL list представления записей поста пользователя
    path("schema/", SpectacularAPIView.as_view(), name="schema"),   # URL пакета для генерации схемы OpenAPI
    path("schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name="redoc"),   # URL пакета для генерации схемы OpenAPI
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui"),   # URL пакета для генерации схемы OpenAPI
]
