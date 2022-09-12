from django.urls import path, re_path
from apps.tour.views import TourList, TourDetail


urlpatterns = [
    path('', TourList.as_view(), name='tour_list'),
    path('<slug:tour_slug>/', TourDetail.as_view(), name="tour_detail"),
]
