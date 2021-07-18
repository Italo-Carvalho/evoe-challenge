from rest_framework.permissions import IsAuthenticated, AllowAny
from app.api import serializes
from app import models
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class NoteBlocksViewsets(generics.ListCreateAPIView):
    queryset = models.NoteBlock.objects.all().order_by('-updated_at')
    permission_classes = (IsAuthenticated,)
    serializer_class = serializes.NoteBlockSerializer


    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer_class):
        serializer_class.save(created_by=self.request.user)


class NoteBlockViewsets(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NoteBlock.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializes.NoteBlockSerializer

    def get_object(self):
        note = get_object_or_404(self.get_queryset()
            ,pk=self.kwargs.get('note_pk'), created_by= self.request.user)
        return note

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializes.UserSerializer