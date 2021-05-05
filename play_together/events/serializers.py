from .models import Event, Category, Court, Team, Result, Game
from auth_.serializers import PlayerSerializer
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('event',)


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        exclude = ('event',)


class EventBaseSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    courts = CourtSerializer(many=True)

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'start_date', 'end_date', 'location', 'address', 'is_active', 'categories',
            'courts')


class EventListSerializer(EventBaseSerializer):
    organization_id = serializers.IntegerField()

    class Meta(EventBaseSerializer.Meta):
        model = Event
        fields = EventBaseSerializer.Meta.fields + ('organization_id',)

    def create(self, validated_data):
        categories_validated_data = validated_data.pop('categories')
        courts_validated_date = validated_data.pop('courts')
        event = Event.objects.create(**validated_data)
        categories_serializer = self.fields['categories']
        courts_serializer = self.fields['courts']
        for each in categories_validated_data:
            each['event'] = event
        categories = categories_serializer.create(categories_validated_data)
        for each in courts_validated_date:
            each['event'] = event
        courts = courts_serializer.create(courts_validated_date)
        return event


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    players_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        players_validated_data = validated_data.pop('players_ids')
        # validated_data['players'] = players_validated_data
        team = Team.objects.create(**validated_data)
        for player in players_validated_data:
            team.players.add(player)
        return team
