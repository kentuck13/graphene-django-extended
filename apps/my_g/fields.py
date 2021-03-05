import inspect
import graphene
from django.db.models import QuerySet
import graphene_django_optimizer as gql_optimizer


class _Items(graphene.ObjectType):
    total_count = graphene.Int()

    def resolve_total_count(parent, info):
        print(parent)
        if isinstance(parent, QuerySet):
            return parent.count()
        return len(parent)


class DjangoObjectField(graphene.Field):
    def __init__(self, _type, resolver=None, lookup_field='id', *args,
                 **kwargs):
        model = _type._meta.model

        if resolver is None:
            resolver = lambda root, info, **kwargs: model.objects.get(
                **{lookup_field: kwargs[lookup_field]}
            )

        kwargs[lookup_field] = graphene.String()
        super().__init__(
            _type,
            resolver=resolver,
            *args,
            **kwargs
        )


from graphene_django import DjangoListField
from graphene_django.filter import DjangoFilterConnectionField


class ListField(graphene.Field):
    def __init__(self, _type, *args, **kwargs):
        model = _type._meta.model
        self.model = model
        self.get_queryset = getattr(_type, 'get_queryset', None)

        def resolve_results(root, info, limit, offset):
            return gql_optimizer.query(root[offset:offset + limit], info)

        instance = type(model.__name__ + 'List', (_Items,), {
            'results': graphene.List(
                _type,
                limit=graphene.Int(default_value=1000),
                offset=graphene.Int(default_value=0),
            ),
            'resolve_results': resolve_results
        })

        super().__init__(instance, *args, **kwargs)

    def get_resolver(self, parent_resolver):
        if inspect.isfunction(parent_resolver) or \
                inspect.ismethod(parent_resolver):
            return parent_resolver

        model = self.model
        get_queryset = self.get_queryset

        def _resolver(root, info, **kwargs):
            queryset = model.objects.all()
            if get_queryset:
                queryset = get_queryset(queryset, info)

            return queryset

        return _resolver
