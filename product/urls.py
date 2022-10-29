from django.urls import path, include
from .views import api_view, ProductListView, ProductCreateView, ProductListApiCreateView, ProductUpdateView, RetriveApiView

urlpatterns = [
    path('', api_view),
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('list-create/', ProductListApiCreateView.as_view()),
    path('detail/<int:pk>/', RetriveApiView.as_view()),
    path('update/<int:pk>/', ProductUpdateView.as_view()),
]
