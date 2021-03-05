import graphene
from .queries import Query
# from apps.mutation import Mutation


schema = graphene.Schema(query=Query)
