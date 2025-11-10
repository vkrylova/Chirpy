class Comment:
    def __init__(self, text, commenter):
        self._text = text  # The text content of the comment
        self._commenter = commenter  # The User who made the comment
        self._replies = []

    def display_comment(self, indent_level=0, is_reply=False):
        indent = "  " * indent_level
        action = "replied" if is_reply else "commented"  # Change wording for replies
        print(f"{indent}{self._commenter.display_name} {action}: {self._text}")
        for reply in self._replies:
            reply.display_comment(indent_level + 1, is_reply=True)

    def add_reply(self, text, commenter):
        reply = Comment(text, commenter)
        self._replies.append(reply)
        return reply

    @property
    def commenter(self):
        return self._commenter
