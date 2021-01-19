from .models import Polls, Questions, Answers, Users
from rest_framework import generics
from .serializers import (
    PollsSerializer,
    PollsChangeSerializer,
    QuestionsSerializer,
    AnswerSerializer,
    PollsDetailSerializer, UserAnswerSerializer,
)
from rest_framework.permissions import IsAuthenticated


class PollsCreateView(generics.CreateAPIView):
    serializer_class = PollsSerializer
    queryset = Polls.objects.all()
    permission_classes = (IsAuthenticated,)


class PollsDetailView(generics.RetrieveAPIView):
    serializer_class = PollsDetailSerializer
    queryset = Polls.objects.all()
    permission_classes = (IsAuthenticated,)


class PollsDeleteView(generics.DestroyAPIView):
    serializer_class = PollsSerializer
    queryset = Polls.objects.all()
    permission_classes = (IsAuthenticated,)


class PollsUpdateView(generics.UpdateAPIView):
    serializer_class = PollsChangeSerializer
    queryset = Polls.objects.all()
    permission_classes = (IsAuthenticated,)


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = (IsAuthenticated,)


class QuestionDeleteUpdateListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    permission_classes = (IsAuthenticated,)


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answers.objects.all()
    permission_classes = (IsAuthenticated,)


class PollListView(generics.ListAPIView):
    serializer_class = PollsSerializer
    queryset = Polls.objects.all()


class UserAnswerView(generics.CreateAPIView):
    serializer_class = UserAnswerSerializer
    queryset = Users.objects.all()


class UserAnswerListView(generics.RetrieveAPIView):
    serializer_class = UserAnswerSerializer
    queryset = Users.objects.all()


