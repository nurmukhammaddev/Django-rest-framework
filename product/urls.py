from django.urls import path, include
from .views import api_view, ProductListView, ProductCreateView, \
    ProductListApiCreateView,  RetriveApiView,\
    ProductRetriveUpdateApiView,\
    ProductDelete, \
    ProductRetriveDeleted, \
    ProductRetriveUpdateDeleted, \
    ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = [
    # path('', api_view),
    path('create/', ProductCreateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('list-create/', ProductListApiCreateView.as_view()),
    path('detail/<int:pk>/', RetriveApiView.as_view()),
    path('ret-up/<int:pk>/', ProductRetriveUpdateApiView.as_view()),
    path('delete/<int:pk>/', ProductDelete.as_view()),
    path('ret-del/<int:pk>/', ProductRetriveDeleted.as_view()),
    path('r-d-u/<int:pk>/', ProductRetriveUpdateDeleted.as_view()),
    path("", include(router.urls)),
]
