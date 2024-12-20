"""anime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404, url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from animes.sitemaps import StaticSiteMaps, AnimeSiteMaps, EpisodesSiteMaps
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticSiteMaps,
    'animes': AnimeSiteMaps,
}

sitemaps2 = {
    'episodes': EpisodesSiteMaps
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('second-sitemap.xml', sitemap, {'sitemaps': sitemaps2}),
    path('', include('pages.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('anime/', include('urlanime.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'urlanime.views.error404'
handler403 = 'urlanime.views.error403'
handler500 = 'urlanime.views.error500'