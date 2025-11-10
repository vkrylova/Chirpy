from user import User


class AdminUser(User):
    def __init__(self, username, display_name, password):
        super().__init__(username, display_name, password)

    @staticmethod
    def delete_post(post_to_delete, posts_list):
        try:
            posts_list.remove(post_to_delete)
            print("The post was deleted by admin🔧.")
        except ValueError:
            print("Post not found.")
