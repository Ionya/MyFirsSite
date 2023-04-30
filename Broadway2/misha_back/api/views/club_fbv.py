from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import Club, News, Event
from api.serializers import ClubSerializer, NewsSerializer, EventSerializer

@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
def club_list(request):
    if request.method == 'GET':
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([AllowAny])
def club_detail(request, club_id):
    try:
        club = Club.objects.get(id=club_id)
    except Club.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = ClubSerializer(club)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClubSerializer(instance=club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        club.delete()
        return Response({'deleted': 'true'})

@api_view(['GET'])
def club_news(request, club_id):
    try:
        club = Club.objects.get(id=club_id)
    except Club.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        news = News.objects.filter(club=club)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def club_events(request, club_id):
    try:
        club = Club.objects.get(id=club_id)
    except Club.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        events = Event.objects.filter(club=club)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)




    

