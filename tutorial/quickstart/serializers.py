from django.contrib.auth.models import *
from rest_framework import serializers
from tutorial.quickstart.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class FootballTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FootballTeam
        fields = ('url', 'team_name', 'team_ranking', 'roster', 'coach', 'location')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')