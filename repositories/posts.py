from django.db import connection
from .query_helpers import QueryHelpers as query


class PostsRepository:
    """
    Data access layer for posts data.
    """

    @staticmethod
    def get_posts():
        """
        Gets the posts available to view for a user.
        """
        sql = """
            select 
                p.id,
                p.content,
                strftime(p.created_at) as created_at,
                u.username as author
            from posts p
            inner join auth_user u on p.user_id = u.id
            order by created_at desc
        """
        return query.many(sql)


    @staticmethod
    def create_post(content, user_id):
        """
        Create a post record in the database.
        """

        sql = """
            insert into posts
                (content, user_id)
            values
                (%s, %s)
        """

        return query.insert(sql, [content, user_id])