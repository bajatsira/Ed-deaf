from rest_framework import serializers

from .models import Course, Unit, Levels

class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    author_id = serializers.IntegerField()
    
    def create(self, validated_data):
         return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance

class UnitSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    level = serializers.IntegerField()
    unit_id = serializers.IntegerField()

class TitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class LevelsSerializer(serializers.Serializer):
    level = serializers.IntegerField()