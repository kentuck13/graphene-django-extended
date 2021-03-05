import graphene
from apps.query import Queries
from apps.mutation import Mutation


schema = graphene.Schema(query=Queries)
