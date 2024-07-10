from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),                            # URL панели администратора
    path('', include('blog.urls', namespace='blog')),       # URL приложения blog
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},        # URL для карты сайтов
         name='django.contrib.sitemaps.views.sitemap'),
    path('accounts/', include('accounts.urls')),                # URL для приложения регистрации
    path('accounts/', include('django.contrib.auth.urls')),     # URL авторизации
]
