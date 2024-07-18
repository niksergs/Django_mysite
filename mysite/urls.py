from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static


"""Карта сайтов"""
sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),                            # URL панели администратора
    path('', include('blog.urls', namespace='blog')),       # URL приложения blog
    path('api/', include('blog_api.urls')),                     # URL приложения blog_api
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},        # URL для карты сайтов
         name='django.contrib.sitemaps.views.sitemap'),
    path('accounts/', include('accounts.urls')),                # URL для приложения регистрации
    path('accounts/', include('django.contrib.auth.urls')),     # URL авторизации
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),     # URL авторизации
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # Настройка urls.py проекта для обслуживания загруженных пользователем медиафайлов во время разработки (когда debug=True)
