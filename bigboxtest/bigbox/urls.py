from django.contrib import admin
from django.urls import path, include
from .views import BoxListView, box_detail_view, activities_view, detail_activity_view

urlpatterns = [
    path('box/', BoxListView.as_view(), name="box-list"),
    path('box/<str:id>/', box_detail_view, name="box-detail"),
    path('box/<int:id>/activity/', activities_view, name="activities"),
    path('box/<int:box_id>/activity/<int:id>', detail_activity_view, name="activity"),
]
#    path('download/loss/get_info/<int:id>', csrf_exempt(GetDownloadLink.as_view())),
