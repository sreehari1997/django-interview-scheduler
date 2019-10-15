from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Slot, Interview, SlotOption
from .serializers import SlotSerializer, InterviewSerializer, SlotOptionSerializer
from django.db.models import Q


class SlotView(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class InterviewView(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

class SlotOptionView(viewsets.ModelViewSet):
    queryset = SlotOption.objects.all()
    serializer_class = SlotOptionSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class AvailableList(generics.ListAPIView):
    serializer_class = SlotSerializer

    def get_queryset(self):
        """
        filtering against candidate and interviewer
        """
        queryset = Slot.objects.all()
        candidate = self.request.query_params.get('candidate', None)
        interviewer = self.request.query_params.get('interviewer', None)
        if candidate is not None and interviewer is not None:
            try:
                queryset=queryset.filter( Q(user_id=candidate) | Q(user_id=interviewer))
            except:
                queryset=None
        return queryset
