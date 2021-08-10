from . import APIView
from repositories.users import UsersRepository


class GetUserProfile(APIView):
    """
    Gets user data and the user's posts to display on their profile pafe.
    """
    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        data = UsersRepository.get_user_profile(username)
        return self.Response(data, 200)
