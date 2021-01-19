from rest_framework import serializers
from .models import Polls, Questions, Answers, Users


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = 'text', 'question'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = '__all__'


class PollsDetailSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True)

    class Meta:
        model = Polls
        fields = '__all__'


class PollsChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = 'name', 'end_date', 'description'


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'