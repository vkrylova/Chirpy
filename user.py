from post import Post
import random


class User:
    total_users = 0  # Class attribute
    max_posts = 5  # Class attribute

    def __init__(self, username, display_name, password, bio=None, ):
        self._username = username
        self._display_name = display_name
        self._password = password
        self._bio = bio
        self._posts_count = 0
        User.total_users += 1  # Adds total users to the User class

    @property
    def username(self):
        return self._username

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        if not value:
            raise ValueError("Display name cannot be empty.")
        if len(value) > 20:
            raise ValueError("Display name cannot be longer than 20 characters.")
        self._display_name = value

    def show_profile(self):
        print(f"<User: {self.display_name} @{self._username}>")

        if self._bio:
            print("Bio: ", self._bio)
            print("------------------")

    def create_post(self, content):
        if self._posts_count < User.max_posts:
            self._posts_count += 1
            return Post(content, self)
        else:
            print(
                f"{self.display_name} has reached the maximum post limit of {str(User.max_posts)} posts."
            )
        return None

    def like_post(self, post):
        post.like_post(self)

    def unlike_post(self, post):
        post.unlike_post(self)

    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print("Password changed successfully.")
        else:
            print("Password must be at least 6 characters long.")

    def check_password(self, input_password):
        return input_password == self._password

    def __str__(self):
        return f"<User: {self.display_name} @{self._username}>"

    @classmethod
    def create_guest_user(cls):
        return cls(username=f'guest{random.randint(1, 9999)}', display_name="Guest", password="1111")
