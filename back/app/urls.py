from django.urls import path
from .api.viewsets import NoteBlocksViewsets, NoteBlockViewsets, UserCreateAPIView


urlpatterns = [
    path('notes/', NoteBlocksViewsets.as_view(),  name='note_blocks'),
    path('notes/<int:note_pk>', NoteBlockViewsets.as_view(),  name='note_block'),
    path('user/', UserCreateAPIView.as_view(), name='user'),
]
