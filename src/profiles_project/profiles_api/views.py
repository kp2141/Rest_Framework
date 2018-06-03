from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):

        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'It is similar to a traditional Django view'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):

        return Response({'method':'put'})

    def patch(self,request,pk=None):

        return Response({'method':'patch'})

    def delete(self,request,pk=None):

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    def list(self,request):
        """Return a hello mesage."""

        a_viewset = [
            'Uses actions (list,create,retrieve,update.partial_)',
            'Automatically maps functionality with less code.'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})