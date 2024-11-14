from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    marks=serializers.FloatField()

    def create(self, validated_data):
        roll=validated_data['roll']
        name=validated_data['name']
        marks=validated_data['marks']

        obj=Student(roll=roll,name=name,marks=marks)
        obj.save()
        return obj
    
    def update(self, instance, validated_data):
        instance.roll=validated_data.get['roll']
        instance.name=validated_data.get['name']
        instance.marks=validated_data.get['marks']
        instance.save()
        return instance