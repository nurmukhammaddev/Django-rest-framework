from django.urls import path, include
from .views import api_view, ProductListView, ProductCreateView, ProductListApiCreateView,  RetriveApiView, ProductRetriveUpdateApiView, ProductDelete

urlpatterns = [
    path('', api_view),
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('list-create/', ProductListApiCreateView.as_view()),
    path('detail/<int:pk>/', RetriveApiView.as_view()),
    path('ret-up/<int:pk>/', ProductRetriveUpdateApiView.as_view()),
    path('delete/<int:pk>/', ProductDelete.as_view()),
]
