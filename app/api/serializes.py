from rest_framework import serializers
from app.models import NoteBlock
from rest_framework.fields import CurrentUserDefault

class NoteBlockSerializer(serializers.ModelSerializer):

    class Meta:

        model = NoteBlock
        fields = ('pk' ,'title', 'body', 'created_at', 'updated_at')
