from django.urls import path, re_path
from apps.service.views import ServiceCategory, ServiceList, ServiceDetail


urlpatterns = [
    path('', ServiceList.as_view(), name='service_list'),
    path('category/<slug:category_slug>/', ServiceCategory.as_view(), name="service_category"),
    path('<slug:service_slug>/', ServiceDetail.as_view(), name="service_detail"),
]
