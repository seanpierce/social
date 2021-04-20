from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from repositories.posts import PostsRepository


@method_decorator(csrf_exempt, name='dispatch')
class Create(View):
    """
    Creates a new post for a user.
    """
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        content = body['content']
        user = self.request.user
        id = PostsRepository.create_post(content, user.id)
        return HttpResponse(json.dumps(id), content_type='application/json')