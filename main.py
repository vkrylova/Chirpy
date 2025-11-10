from social_network import SocialNetwork
from user import User


# Initialize the Chirpy Social Network
_chirpy_network = SocialNetwork()


def display_menu():
    print("\nChirpy Social Media Platform")
    print("========================================")
    print("1. Create New Account")
    print("2. Post a Chirp")
    print("3. View All Chirps")
    print("4. Like a Chirp")
    print("5. Comment on a Chirp")
    print("6. Reply to a Comment")
    print("7. View Profile")
    print("8. List All Users")
    print("9. Exit")


def create_account():
    username = input("Enter username: ")
    display_name = input("Enter display name: ")
    password = input("Enter password: ")
    verified = input("Do you want a verified account? (yes/no): ").strip().lower() == 'yes'
    admin = input("Is this an admin account? (yes/no): ").strip().lower() == 'yes'
    _chirpy_network.add_user(User(username, display_name, password), verified, admin)
    print(f"Account created successfully for {display_name}!")


def post_chirp():
    username = input("Enter username: ")
    if user := _chirpy_network.search_user_by_username(username):
        content = input("Enter chirp content: ")
        post = user.create_post(content)
        _chirpy_network.add_post(post)
    else:
        print("User not found.")


def view_all_chirps():
    _chirpy_network.list_all_posts()


def like_chirp():
    if not _chirpy_network.posts:
        print("No posts to like.")
        return
    username = input("Enter your username: ")
    if user := _chirpy_network.search_user_by_username(username):
        _chirpy_network.list_all_posts()
        try:
            post_index = int(input("Enter post index to like: "))
            if 0 <= post_index < len(_chirpy_network.posts):
                user.like_post(_chirpy_network.posts[post_index])
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a valid post index.")
    else:
        print("User not found.")


def comment_on_chirp():
    if not _chirpy_network.posts:
        print("No posts to comment on.")
        return
    username = input("Enter your username: ")
    if user := _chirpy_network.search_user_by_username(username):
        _chirpy_network.list_all_posts()
        try:
            post_index = int(input("Enter post index to comment on: "))
            if 0 <= post_index < len(_chirpy_network.posts):
                comment = input("Enter your comment: ")
                _chirpy_network.posts[post_index].add_comment(comment, user)
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a valid post index.")
    else:
        print("User not found.")


def reply_to_comment():
    if not _chirpy_network.posts:
        print("No posts to comment on.")
        return
    username = input("Enter your username: ")
    if user := _chirpy_network.search_user_by_username(username):
        _chirpy_network.list_all_posts()
        try:
            post_index = int(input("Enter post index to comment on: "))
            if 0 <= post_index < len(_chirpy_network.posts):
                comment_index = int(input("Enter comment index to reply to: "))
                if not (0 <= comment_index < len(_chirpy_network.posts[post_index].comments)):
                    print("Invalid comment index.")
                    return
                reply_text = input("Enter your reply: ")
                _chirpy_network.posts[post_index].add_reply(comment_index, reply_text, user)
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a valid post index.")
    else:
        print("User not found.")


def view_profile():
    username = input("Enter username: ")
    if user := _chirpy_network.search_user_by_username(username):
        user.show_profile()
    else:
        print("User not found.")


def list_users():
    if _chirpy_network.users:
        print("Registered users:")
        for user in _chirpy_network.users:
            user.show_profile()
    else:
        print("No users registered yet.")


while True:
    display_menu()
    choice = input("Choose an option (1-8): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        post_chirp()
    elif choice == "3":
        view_all_chirps()
    elif choice == "4":
        like_chirp()
    elif choice == "5":
        comment_on_chirp()
    elif choice == "6":
        reply_to_comment()
    elif choice == "7":
        view_profile()
    elif choice == "8":
        list_users()
    elif choice == "9":
        print("Exiting Chirpy. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
