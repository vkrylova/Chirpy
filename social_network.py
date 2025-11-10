from admin_user import AdminUser
from user import User
from verified_user import VerifiedUser


class SocialNetwork:
    def __init__(self):
        self._users = []  # This list will store User objects
        self._posts = []  # This list will store Post objects

    @property
    def posts(self):
        return self._posts

    @property
    def users(self):
        return self._users

    def add_user(self, user, is_verified=False, is_admin=False):
        #account_type = is_verified
        username = user.username
        display_name = user.display_name
        password = user._password

        # Check if user already exists
        if self.search_user_by_username(username):
            print(f"User with username: <{username}> already exists!")
            return

        # Create the appropriate user object
        if is_admin:
            new_user = AdminUser(username, display_name, password)
            role = "Admin🔧"
        elif is_verified:
            new_user = VerifiedUser(username, display_name, password)
            role = "Verified✅"
        else:
            new_user = User(username, display_name, password)
            role = "Regular"

        # Add the new user to the network
        self._users.append(new_user)
        print(f"{display_name} has been added to Chirpy as {role}.")

    def add_post(self, post):
        self.posts.append(post)
        print(f"A new post was created: '{post.content}' by {post.author.display_name}")

    def search_user_by_username(self, username):
        return next((user for user in self._users if user.username == username), None)

    def remove_user(self, username):
        if user_to_remove := self.search_user_by_username(username):
            self._users.remove(user_to_remove)
        else:
            print(f"User with username: <{username}> does not exist!")

    def list_all_posts(self):
        if not self.posts:
            print("No posts to display")
        else:
            for i, post in enumerate(self.posts):
                print(f"\n[{i}]{post.author.username} @{post.author.display_name}:")
                print(f">> {post.content}")
                print(f"{post.get_like_count} ❤️")

                if post.comments:
                    print("  💬 Comments:")
                    for j, comment in enumerate(post.comments):
                        print(f"    [{j}] ", end="")
                        comment.display_comment(indent_level=2)
                else:
                    print("  No comments yet.")

    def list_post_comments(self, post_index):
        if 0 <= post_index < len(self._posts):
            post = self._posts[post_index]
            if not post.comments:
                print("No comments yet on this post.")
            else:
                print(f"Comments on {post.author.display_name}'s post:")
                for i, comment in enumerate(post.comments):
                    print(f"  [{i}] ", end="")
                    comment.display_comment()
        else:
            print("Invalid post index.")

    def search_post_by_keyword(self, keyword):
        return [post for post in self.posts if keyword.lower() in post.content.lower()]
