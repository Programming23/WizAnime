from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from pages.models import Episodes, Anime

class StaticSiteMaps(Sitemap):

    def items(self):
        return ['index', 'list_anime', 'days_anime', 'reset_password','login', 'register', 'list_anime', 'episode']

    def location(self, item):
        return reverse(item)

class AnimeSiteMaps(Sitemap):

    def items(self):
        return Anime.objects.all()


class EpisodesSiteMaps(Sitemap):

    def items(self):
        return Episodes.objects.all()