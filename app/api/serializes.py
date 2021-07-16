from rest_framework import serializers
from app.models import NoteBlock

class NoteBlockSerializer(serializers.ModelSerializer):

    class Meta:

        model = NoteBlock
        fields = ('pk' ,'title', 'body', 'created_at', 'updated_at')
