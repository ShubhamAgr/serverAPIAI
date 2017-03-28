from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserQuerries
from .serializers import UserQuerriesSerializer
import apiai
import json


# This token is of API.ai
CLIENT_ACCESS_TOKEN = 'eef6ff59999d40388dca0ffc361e5b41'

# This class will take request and save Post.data
class UserQuerriesResponse(APIView):
    # Will handle this type of url : http://127.0.0.1:8000/givequery?user_query=question
    def get(self, request):
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        requestAPIAI = ai.text_request()
        requestAPIAI.lang = 'de'  # optional, default value equal 'en'
        # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        requestAPIAI.query = request.GET['user_query']
        # print(request.data['user_query'])
        response = requestAPIAI.getresponse().read().decode('UTF-8')
        res = json.loads(response)
        # print(type(response))
        return Response(res, status=status.HTTP_201_CREATED)
        return Response("Got ur request !!  But i accept only post request")


    # Will handle post request with key 'user_query'
    def post(self, request):
        serializer = UserQuerriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
            requestAPIAI = ai.text_request()
            requestAPIAI.lang = 'de'  # optional, default value equal 'en'
            # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
            requestAPIAI.query = request.data['user_query']
            print(request.data['user_query'])
            response = requestAPIAI.getresponse().read().decode('UTF-8')
            res = json.loads(response)
            # print(type(response))
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
