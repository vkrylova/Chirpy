from comment import Comment


class Post:
    total_posts = 0
    MAX_CONTENT_LENGTH = 280

    def __init__(self, content, author):
        self._content = content  # Store the text of the post
        self._author = author  # Store the user who created it
        self._likes = []  # List of users who liked the post
        self._comments = []  # List of comments on the post
        self._like_count = 0  # Number of likes on the post
        Post.total_posts += 1  # Adds total posts to the Post class

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_content):
        if len(new_content) > 280:
            raise ValueError("Chirp content cannot exceed 280 characters.")
        self._content = new_content

    @property
    def author(self):
        return self._author

    @property
    def get_like_count(self):
        return self._like_count

    # Method to handle liking a post
    def like_post(self, user):
        if user not in self._likes:
            self._likes.append(user)
            self._like_count += 1
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    @property
    def comments(self):
        return self._comments.copy()  # returns a copy to maintain encapsulation

    def unlike_post(self, user):
        if user in self._likes:
            self._likes.remove(user)
            print(user.display_name, "unliked this post!")
        else:
            print(user.display_name, "hasn't liked this post!")

    def display_post(self):
        print(self._author.display_name, " posted: ", self._content)

    # New method to add comments on the post
    def add_comment(self, text, commenter):
        comment = Comment(text, commenter)
        self._comments.append(comment)
        print(f"{comment.commenter.display_name} added a comment on {self._author.display_name}'s post.")
        return comment

    def add_reply(self, comment_index, text, user):
        if 0 <= comment_index < len(self._comments):
            parent_comment = self._comments[comment_index]
            reply = parent_comment.add_reply(text, user)
            print(f"{user.display_name} replied to a comment on {self._author.display_name}'s post.")
            return reply
        else:
            print("Invalid comment index.")
            return None

    # Debugging-friendly representation of a Post object
    def __repr__(self):
        snippet = (
            self._content if len(self.content) <= 30 else f"{self.content[:27]}..."
        )
        return f"Post by {self._author.display_name}: {snippet}, Likes: {self._like_count} "

    # Static method to validate content length without needing an instance
    @staticmethod
    def validate_content_length(content):
        # Checks if a post meets the platform's character limit
        return len(content) <= Post.MAX_CONTENT_LENGTH
