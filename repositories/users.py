from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from .query_helpers import QueryHelpers as query


class UsersRepository():

    @staticmethod
    def get_user_from_session_key(session_key):
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        return user

    @staticmethod
    def get_user_profile(username):

        profile_sql = """
            select 
                username,
                cast(date_joined as varchar)
            from auth_user
            where username = %s
        """

        profile = query.single(profile_sql, [username])

        posts_sql = """
            select 
                p.id,
                p.content,
                cast(p.created_at as varchar),
                u.username as author,
                u.id as author_id
            from posts p
            inner join auth_user u on p.user_id = u.id
            where username = %s
            order by created_at desc
        """

        posts = query.many(posts_sql, [username])

        return {
            'profile': profile,
            'posts': posts
        }
        