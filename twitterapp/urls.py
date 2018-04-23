from django.conf.urls import url
from .views import SimpleView

urlpatterns = [
    url('^twitter/$', SimpleView.as_view(), name='twitter'),
]
