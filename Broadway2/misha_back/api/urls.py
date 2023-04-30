from django.contrib import admin
from django.urls import path, include
from api.views import news_fbv, event_cbv, location_cbv, club_fbv, ionya, ticket_cbv
from rest_framework_jwt.views import obtain_jwt_token


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("login/", obtain_jwt_token),
    path("news/", news_fbv.news_list),
    path("news/<int:news_id>/", news_fbv.news_detail),

    path("clubs/", club_fbv.club_list),
    path("clubs/<int:club_id>/", club_fbv.club_detail),
    path("clubs/<int:club_id>/news/", club_fbv.club_news),
    path("clubs/<int:club_id>/events/", club_fbv.club_events), 

    path("events/", event_cbv.EventListAPIView.as_view()),
    path("events/<int:event_id>/", event_cbv.EventDetailAPIView.as_view()),

    path("locations/", location_cbv.LocationListAPIView.as_view()),
    path("locations/<int:location_id>/", location_cbv.LocationDetailAPIView.as_view()),
    path("locations/<int:location_id/events/", location_cbv.LocationEventsAPIView.as_view()),

    path("main/news/", ionya.main_news_list),
    path("main/events/", ionya.main_events_list),
    path("events/topFive/", ionya.top_five_events),
    path("main/clubs/", ionya.main_clubs),
    # path("tickets/", ionya.getAllTickets),
    path("tickets/", ticket_cbv.TicketListAPIView.as_view()),
    path("tickets/<int:ticket_id>/", ticket_cbv.TicketDetailAPIView.as_view()),


]
