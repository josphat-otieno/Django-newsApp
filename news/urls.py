from django.conf.urls import url, include
from django.conf import settings
from django.urls import path
from django.contrib.auth import views 
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView

from . import views

urlpatterns= [
    
    url(r'^$', views.news_of_day, name = 'newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name='pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name ='article'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^new/article$', views.new_article, name='new-article')
]
    
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
