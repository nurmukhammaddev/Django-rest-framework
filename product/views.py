from django.shortcuts import render
from django.http import JsonResponse
import json


def api_view(request):
    body = request.body
    print(body)
    json_data = json.loads(body)
    print(json_data)
    json_data["headers"] = dict(request.headers)
    json_data["content_type"] = request.content_type
    json_data["params"] = request.GET

    return JsonResponse(json_data)
