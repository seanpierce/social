import json
from . import APIView
from repositories.posts import PostsRepository


class Create(APIView):
    """
    Creates a new post for a user.
    """
    def post(self, request, *args, **kwargs):
        payload = self.GetPayload(request, ['content'])
        user = self.request.user
        data = PostsRepository.create_post(payload['content'], user.id)
        return self.Response(data)


class GetFeed(APIView):
    """
    Gets the posts available to view for a user.
    """
    def get(self, request, *args, **kwargs):
        data = PostsRepository.get_posts()
        return self.Response(data)


class DeletePost(APIView):
    """
    Allows a user to delete one of their own posts.
    """
    def post(self, request, *args, **kwargs):
        payload = self.GetPayload(request, ['post_id'])
        user = self.request.user
        success = PostsRepository.delete_post(payload['post_id'], user.id)
        return self.Response(success, 200 if success is True else 401)