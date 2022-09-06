from django.urls import path, re_path
from apps.photogallery.views import AlbumList, AlbumDetail

urlpatterns = [
    path('', AlbumList.as_view(), name='album_list'),
    path('<slug:album_slug>/', AlbumDetail.as_view(), name="album_detail"),
]