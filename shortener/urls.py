from django.urls import path
from shortener import views


urlpatterns = [
    path('', views.ShortLinkCreateListView.as_view(), name='link-create-list'),
    path('<int:pk>/', views.ShortlinkRetrieveUpdateDestroyView.as_view(), name='link-detail-update-delete'),
    path('<int:pk>/generate-surl/', views.GenerateSurlView.as_view(), name='generate-surl'),
    path('r/<str:shorted_link>', views.RedirectLink.as_view(), name='redirect-link')
]
