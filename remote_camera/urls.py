"""remote_camera URL Configuration

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
from django.contrib import admin
from django.urls import path

# from base.views import (
#     index
# )
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     path('', index, name='main'),
# ]

from django.contrib import admin
from django.urls import path

from base.views import (
    index,
    start_stream,
    stop_stream,
    authorize_key
)


def fake_view(*args, **kwargs):
    """ This view should never be called because the URL paths
        that map here will be served by nginx directly.
    """
    raise Exception("This should never be called!")


urlpatterns = [
    path('', index, name='index'),
    path("admin/", admin.site.urls),
    path("start_stream", start_stream, name="start-stream"),
    path("stop_stream", stop_stream, name="stop-stream"),
    path("authorize_key", authorize_key, name="authorize-key"),
    path("live/<username>/index.m3u8", fake_view, name="hls-url")
]