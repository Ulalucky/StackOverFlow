from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Problem, Reply

from .serializers import ProblemSerializer, ReplySerializer


class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
