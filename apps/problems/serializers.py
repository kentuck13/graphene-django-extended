from apps.problems.models import Problem, Category

from rest_framework import serializers


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'test', 'name', 'category')

    def validate_name(self, name):
        if name == 'Hello':
            raise serializers.ValidationError("SHIT")
        return name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
