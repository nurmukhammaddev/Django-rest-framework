from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from .serializer import ProductSerializer
from .models import Product


@csrf_exempt
def api_view(request):
    # body = request.body
    # print(body)
    # json_data = json.loads(body)
    # print(json_data)
    # json_data["headers"] = dict(request.headers)
    # json_data["content_type"] = request.content_type
    # json_data["params"] = request.GET
    body = request.body
    json_data = json.loads(body)
    obj=Product.objects.create(
        title = json_data['title'],
        description = json_data['description'],
        price = json_data['price'],
    )
    result = {
        "id": obj.id,
        "title": obj.title,
        "description": obj.description,
        "price": obj.price,

    }

    return JsonResponse(result)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        price = self.request.GET.get('price')
        if price:
            qs = qs.filter(price__gte = price)
        return qs


class ProductListApiCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super(ProductListApiCreateView, self).get_queryset()
        price = self.request.GET.get('price')
        if price:
            qs = qs.filter(price__gte = price)
        return qs


class RetriveApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'



class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

