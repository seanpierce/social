import json
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
        data = PostsRepository.create_post(content, user.id)
        return self.Response(data, 200)


class GetFeed(CSRFExemptView):
    """
    Gets the posts available to view for a user.
    """
    def get(self, request, *args, **kwargs):
        data = PostsRepository.get_posts()
        return self.Response(data, 200)