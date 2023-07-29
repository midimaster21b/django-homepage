# from django.urls import patterns, include, url
from django.urls import include, path
from home import views

# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index'),
# )

urlpatterns = [
    path('', views.index, name='index'),
]
