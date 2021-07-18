from rest_framework import serializers
from app.models import NoteBlock
from django.contrib.auth.models import User


class NoteBlockSerializer(serializers.ModelSerializer):

    class Meta:

        model = NoteBlock
        fields = ('pk' ,'title', 'body', 'created_at', 'updated_at')



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ( 'username', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user