from rest_framework import serializers
from api.models import News, Event, Club, Location, Ticket
from django.contrib.auth import get_user_model


class  ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class LocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=1500)
    url = serializers.CharField(max_length=300)

    def create(self, validated_data):
        location = Location.objects.create(**validated_data)
        return location
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get("city", instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.image = validated_data.get('image', instance.image)
        instance.url = validated_data.get('url', instance.url)

        instance.save()
        return instance


class NewsSerializer(serializers.ModelSerializer):
    club = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all())

    class Meta:
        model = News
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['club'] = ClubSerializer(instance.club).data
        return ret


class EventSerializer(serializers.ModelSerializer):
    club = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'image', 'date_time','club', 'location', 'likes', 'dislikes')
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['club'] = ClubSerializer(instance.club).data
        ret['location'] = LocationSerializer(instance.location).data
        return ret



    def create(self, validated_data):
        # Modify the validated_data dictionary here
        validated_data['name'] = validated_data['name'].upper()

        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        return ret

    def create(self, validated_data):
        # Modify the validated_data dictionary here
        validated_data['name'] = validated_data['name'].upper()

        return super().create(validated_data)



class TicketSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Ticket
        fields = ('event', 'user', 'ticket_type', 'standard_cost')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['event'] = EventSerializer(instance.event).data
        ret['user'] = UserSerializer(instance.user).data
        return ret

    def create(self, validated_data):
        # Modify the validated_data dictionary here
        validated_data['name'] = validated_data['name'].upper()

        return super().create(validated_data)