from rest_framework import serializers

from example.agent.models import Agent, TopUp


class AgentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Agent
        exclude = ['parent', 'last_login', 'date_joined', 'avatar']


class TopUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = TopUp
        exclude = ['date_created', 'last_updated']
