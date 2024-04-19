from django.urls import path, re_path
from pages.views import index,PageListCreateAPIView, PageRetrieveUpdateDestroyAPIView

urlpatterns = [
    # path('index/', index),
    re_path(r'^index(?:1)?$' ,index),
    path('page/', PageListCreateAPIView.as_view()),
    path('page/<int:pk>/', PageRetrieveUpdateDestroyAPIView.as_view()),
]