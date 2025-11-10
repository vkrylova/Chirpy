# 🐦 Chirpy

**Chirpy** is a lightweight social network prototype written in Python.  
It focuses on clean class design and core social features such as users, posts, and comments, all implemented without external frameworks.

---

## ✨ Features

- Create and view posts  
- Add comments to posts  
- Display user profiles  
- Role system: regular user, verified user, admin  
- View all users  
- Simple, extensible OOP architecture

---

## 🧩 Project Structure

<details>
<summary>Click to expand</summary>
  
```bash
project_root/
├── admin_user.py
├── comment.py
├── main.py
├── post.py
├── social_network.py
├── user.py
├── verified_user.py
└── README.md
```
</details>

---

## ⚙️ Run the Project
```bash
git clone https://github.com/vkrylova/Chirpy.git
python main.py
```

---

## 🧠 Design Notes
The project follows a class-based structure:
- User — base class for all users
- VerifiedUser — subclass with verified status
- AdminUser — subclass with administrative permissions
- Post and Comment — handle content creation and interactions
- SocialNetwork — manages all data and relationships between users and posts
- No external libraries or databases are required — all logic is handled in memory.

---
