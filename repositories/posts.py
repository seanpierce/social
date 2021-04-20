from django.db import connection
from .query_helpers import QueryHelpers as query


class PostsRepository:
    """
    Data access layer for posts data.
    """

    @staticmethod
    def get_posts():
        return []


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