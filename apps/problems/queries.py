import graphene
from graphene import relay
from graphene_django.debug import DjangoDebug
from graphene_django import DjangoListField, DjangoObjectType
from .models import Problem

from .serializers import ProblemSerializer, CategorySerializer
from .models import Category, Problem
from apps.my_g.fields import ListField, DjangoObjectField

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'problems')


class ProblemType(DjangoObjectType):
    class Meta:
        model = Problem
        fields = ('id', 'name', 'category')

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.exclude(id=1)


class Query(graphene.ObjectType):
    problems = ListField(ProblemType)
    category = DjangoObjectField(CategoryType)
    category1 = DjangoObjectField(CategoryType)

    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_problems(root, info):
        return Problem.objects.all()
