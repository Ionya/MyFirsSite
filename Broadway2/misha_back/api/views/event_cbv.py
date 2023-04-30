from django.shortcuts import Http404
from django.utils.encoding import smart_str

from django.utils.decorators import method_decorator
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Event
from api.serializers import EventSerializer


class EventListAPIView(APIView):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailAPIView(APIView):
    # permission_classes = (AllowAny,)

    def get_object(self, event_id):
        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, event_id):
        event = self.get_object(event_id)
        if isinstance(event, Response):
            return event
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, event_id):
        event = self.get_object(event_id)
        serializer = EventSerializer(instance=event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, event_id):
        event = self.get_object(event_id)
        event.delete()
        return Response({'deleted': 'true'})

