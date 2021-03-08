from django.conf.urls import include, url
import HelloDjangoApp.views

# Django processes URL patters in the order they appear in the array
urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^$', HelloDjangoApp.views.index, name='home'),
]