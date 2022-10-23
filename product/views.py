from django.shortcuts import render
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

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
