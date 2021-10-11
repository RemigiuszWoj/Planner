from itertools import chain

from django.contrib import admin
from django.urls import include, path

from .user.urls import urlpatterns as user_urls

# from rest_framework import routers

# from backend.user import views


api_urlpatterns = list(chain.from_iterable([user_urls]))


urlpatterns = [
    path("", include("backend.vue_api.urls")),
    path("api/", include(api_urlpatterns)),
    path("admin/", admin.site.urls),
]
