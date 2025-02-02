from pickle import NONE
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import models
from . import permissions


from . import serializers


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    serializer_class=serializers.helloserializer


    def get(self,request, format=None):
        """Returns a list of API features"""
        an_apiview =[
            'Uses HTTP methods as function (get, post , patch, put, delete)',
            'it is similar to a tarditional Django view',
            'Gives you the most control over your logic',
            'İs mapped manually to Urls',
        ]
        return Response({'message':'Hello me!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer=serializers.helloserializer(data=request.data)
        if serializer.is_valid():
            name =serializer.data.get('name')
            message='Hello my friend {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def put(self,request,pk=None):
        """Handles Updating our object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Patch request, only updates fields provided in the request """
        return Response({'method':'patch'})


    def delete(self,request,pk=None):
        """Deletes an objects"""
        return Response ({'method':'delete'})


####################################################################################################

class helloviewset(viewsets.ViewSet):
    """Test API VİEWSET"""

    serializer_class=serializers.helloserializer

    def list(self,request):
        """Return a hello message"""
        a_viewset=[
            'Uses actions (list, create, retrieve, update, partical_update)',
            'Automaticly  maps to Urls using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello my friend','a_viewset':a_viewset}) 


    def create(self,request):
        """Create a new hello message"""
        serializer=serializers.helloserializer(data=request.data)
        
        if serializer.is_valid():
            name =serializer.data.get('name')
            message='Hello{0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def retrieve(self,request,pk=None):
        """Handles getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an oblject."""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Hnadles updating part of an object """

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Hnadles removing an object"""   

        return Response({'http_method':'DELETE'}) 
########################################################################################
class UserProfileViewset(viewsets.ModelViewSet):
    """Hnadles creating, creating and updating profiles."""
    serializer_class=serializers.UserProfileSerializer

    queryset=models.UserProfile.objects.all()

    authentication_classes=(TokenAuthentication,)

    permission_classes=(permissions.UpdateOwnProfile,)

    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email,',)



##############################################################################################

class LoginViewSet(viewsets.ViewSet):
    """checks email and password and returns an auth  token"""
    serializer_class=AuthTokenSerializer

    def create(self,request):
        """Use obtainauthtoken APIVİEW TO validate and create token. """

        return ObtainAuthToken().as_view()(request=request._request)

######################################################################################################

class UserProfileFeedViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""

    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)







        

               






    

