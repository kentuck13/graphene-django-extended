from graphene_django_extras import (
    DjangoListObjectType, DjangoObjectType, DjangoSerializerType
)
from apps.problems.models import Problem, Category
from .serializers import ProblemSerializer
import graphene


class CategoryType(DjangoListObjectType):
    class Meta:
        model = Category
        filter_fields = ('name',)


class ProblemModelType(DjangoSerializerType):
    class Meta:
        filter_fields = {
            'name': ['exact'],
            'category': ['exact'],
            'category__name': ['exact']
        }
        serializer_class = ProblemSerializer
