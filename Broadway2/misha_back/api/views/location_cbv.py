from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Location, Event
from api.serializers import LocationSerializer, EventSerializer


class LocationListAPIView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDetailAPIView(APIView):
    def get_object(self, location_id):
        try:
            return Location.objects.get(id=location_id)
        except Location.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, location_id):
        location = self.get_object(location_id)
        if isinstance(location, Response):
            return location
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    
    def put(self, request, location_id):
        location = self.get_object(location_id)
        serializer = LocationSerializer(instance=location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, location_id):
        location = self.get_object(location_id)
        location.delete()
        return Response({'deleted': 'true'})


class LocationEventsAPIView(APIView):
    def get_object(self, location_id):
        try:
            return Location.objects.get(id=location_id)
        except Location.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, location_id):
        location = self.get_object(location_id)
        if isinstance(location, Response):
            return location
        events = Event.objects.filter(location=location)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)