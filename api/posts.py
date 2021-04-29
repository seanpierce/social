import json
from django.http import HttpResponse
from . import CSRFExemptView
from repositories.posts import PostsRepository


class Create(CSRFExemptView):
    """
    Creates a new post for a user.
    """
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        content = body['content']
        user = self.request.user
        id = PostsRepository.create_post(content, user.id)
        return HttpResponse(json.dumps(id), content_type='application/json')


class GetFeed(CSRFExemptView):
    """
    Gets the posts available to view for a user.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(PostsRepository.get_posts()), content_type='application/json')