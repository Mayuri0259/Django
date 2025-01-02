"""from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


# View that returns True
class ReturnTrue(APIView):
    def get(self, request):
        return Response({'result': True})
        

# View that returns False
class ReturnFalse(APIView):
    def get(self, request):
        return Response({'result': False})
        """

"""from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

# GET API: Simply return a success message
class GetExampleView(View):
    def get(self, request):
        return JsonResponse({"message": "GET function implemented successfully"}, status=200)

# POST API: Simply return a success message
class PostExampleView(View):
    def post(self, request):
        return JsonResponse({"message": "POST function implemented successfully"}, status=201)

# PUT API: Simply return a success message
class PutExampleView(View):
    def put(self, request):
        return JsonResponse({"message": "PUT function implemented successfully"}, status=200)

# DELETE API: Simply return a success message
class DeleteExampleView(View):
    def delete(self, request):
        return JsonResponse({"message": "DELETE function implemented successfully"}, status=204)
        """



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

"""class GetExample(APIView):
    def get(self, request):
        return Response({"message": "GET function implemented successfully"})


class PostExample(APIView):
    def post(self, request):
        return Response({"message": "POST function implemented successfully"})


class PutExample(APIView):
    def put(self, request):
        return Response({"message": "PUT function implemented successfully"})


class DeleteExample(APIView):
    def delete(self, request):
        return Response({"message": "DELETE function implemented successfully"})"""


class Example(APIView):
    def get(self, request):
        return Response({"message": "GET function implemented successfully"})
    def post(self, request):
        return Response({"message": "POST function implemented successfully"})
    def put(self, request):
        return Response({"message": "PUT function implemented successfully"})
    def delete(self, request):
        return Response({"message": "DELETE function implemented successfully"})
