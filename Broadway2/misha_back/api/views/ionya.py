
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import Event, Club, News, Ticket
from api.serializers import ClubSerializer, NewsSerializer, EventSerializer, TicketSerializer



@api_view(['GET', 'PUT', 'DELETE'])
def top_five_events(request):
    permission_classes = (AllowAny, )
    if request.method == 'GET':
        best_events = Event.objects.filter().order_by('likes')
        events = [] * 5
        for i in range(len(Event.objects.all()) - 1, len(Event.objects.all()) - 6, -1 ):
            events.append(best_events[i])

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['GET', 'PUT', 'DELETE'])
def main_news_list(request):
    permission_classes = (AllowAny, )
    if request.method == 'GET':
        news = []
        for i in range(4):
            news.append(News.objects.all()[i])
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def main_events_list(request):
    permission_classes = (AllowAny, )
    if request.method == 'GET':

        events = []
        last_events = Event.objects.filter().order_by('date_time')
        for i in range(len(Event.objects.all()) - 1, len(Event.objects.all()) - 22, -1):
            events.append(last_events[i])
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
def main_clubs(request):
    if request.method == 'GET':
        top_clubs = []
        clubs = Club.objects.filter().order_by('likes')

        for i in range(len(Club.objects.all()) - 1, len(Club.objects.all()) - 6, -1):
            top_clubs.append(clubs[i])


        serializer = ClubSerializer(top_clubs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# # @permission_classes([AllowAny])
# def getAllTickets(request):
#     try:
#         tickets = Ticket.objects.all()
#     except Ticket.DoesNotExist as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#
#     if request.method == 'GET':
#         serializer = TicketSerializer(tickets, many=True)
#         return Response(serializer.data)