from django.conf.urls import url

from . import views

app_name = 'update_api'
urlpatterns = [
    url(r'^notifications/$', views.CreateView.as_view(), name="create"),
    url(r'^notifications/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
]
