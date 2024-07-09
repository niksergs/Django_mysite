from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """Определение конкретно-прикладной карты сайта"""
    changefreq = 'weekly'   # Указывает частоту изменения страниц постов
    priority = 0.9          # Указывает релевантность страниц постов (макс. 1)

    def items(self):
        """Возвращает набор запросов QurrySet объектов,
        подлежащих включению в карту сайта"""
        return Post.published.all()

    def lastmod(self, obj):
        """Получает каждый возвращаемый методом items() объект
        и возвращает время последнего изменения объекта"""
        return obj.updated
