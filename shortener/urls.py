from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShortLinkCreateListView.as_view(), name='link-create-list')
]
