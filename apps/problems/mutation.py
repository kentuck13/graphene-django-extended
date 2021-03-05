import graphene
from .serializers import ProblemSerializer


class Mutations(graphene.ObjectType):
    pass
    # problem_create = ProblemSerializerMutation.CreateField()

    # def resolve_problem_create(self):
    #     print('asdasd')
