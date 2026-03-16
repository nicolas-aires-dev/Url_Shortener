from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShortLinkCreateListView.as_view(), name='link-create-list'),
    path('<int:pk>/', views.ShortlinkRetrieveUpdateDestroyView.as_view(), name='link-detail-update-delete'),
    path('<int:pk>/generate-surl/', views.GenerateSurlView.as_view(), name='generate-surl')
]
