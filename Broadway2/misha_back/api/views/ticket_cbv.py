from api.models import Ticket
from api.serializers import TicketSerializer
from requests import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class TicketListAPIView(APIView):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        events = Ticket.objects.all()
        serializer = TicketSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailAPIView(APIView):
    # permission_classes = (AllowAny,)

    def get_object(self, ticket_id):
        try:
            return Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, ticket_id):
        ticket = self.get_object(ticket_id)
        if isinstance(ticket, Response):
            return ticket
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def put(self, request, ticket_id):
        ticket = self.get_object(ticket_id)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ticket_id):
        ticket = self.get_object(ticket_id)
        ticket.delete()
        return Response({'deleted': 'true'})