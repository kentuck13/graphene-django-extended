from django.core.cache import cache
import json

from django.http import HttpResponse


def graphql_cache_middleware(get_response):
    def middleware(request):
        if request.path.startswith('/graphql') and request.body:
            data = json.loads(request.body.decode('utf8'))
            cache_key = data['query'].replace('\n', '').replace(' ', '').replace('\t', '')
            print(cache_key)

            if response := cache.get(cache_key):
                return HttpResponse(response, content_type='application/json')

            response = get_response(request)
            cache.set(cache_key, response.content, 10)

        response = get_response(request)

        return response

    return middleware
