from post import Post
from user import User


class VerifiedUser(User):
    def __init__(self, username, display_name, password):
        # Inherit all attributes from User
        super().__init__(username, display_name, password)
        # Add a new attribute specific to verified users
        self.verification_badge = True

    def get_verification_status(self):
        return "Verified✅" if self.verification_badge else "Regular"

    # Overriding create_post() to add a "✅ " prefix to the content
    def create_post(self, content):
        # Add a special flair to posts created by verified users
        verified_content = f"✅  {content}"
        return Post(verified_content, self)

    def like_post(self, post):
        super().like_post(post)
        print(f"Verified user {self.display_name} liked this post ✅")
