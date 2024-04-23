

from django.urls import path, include
from eCommerceApp import urls
urlpatterns = [
    path('', include(urls))
]
