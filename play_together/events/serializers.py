from .models import Event, Category, Court, Team, Result, Game
from auth_.serializers import PlayerSerializer
from rest_framework import serializers


def max_players_count(players_ids):
    if len(players_ids) > 5:
        raise serializers.ValidationError('Maximum players in one team exceeded')
    return players_ids


class CategorySerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check that the max_age greater than min_age
        """
        if data['max_age'] < data['min_age']:
            raise serializers.ValidationError("Max age must be greater than min age")
        return data

    class Meta:
        model = Category
        fields = '__all__'


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'


class EventBaseSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    courts = CourtSerializer(many=True, read_only=True)

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("finish must occur after start")
        return data

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


class EventDetailSerializer(EventBaseSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta(EventBaseSerializer.Meta):
        model = Event
        fields = EventBaseSerializer.Meta.fields


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class GameDetailSerializer(serializers.ModelSerializer):
    result = ResultSerializer(read_only=True)
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)

    class Meta:
        model = Game
        fields = '__all__'


class TeamDetailSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    team_a_games = GameSerializer(many=True, read_only=True)
    team_b_games = GameSerializer(many=True, read_only=True)

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


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
