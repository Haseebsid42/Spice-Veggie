# Spice-Veggie
Spice&Veggie is a full-stack e-commerce platform built with Django and Tailwind CSS that allows users to browse, add, and manage fruits, vegetables, and spices in a cart. It features a custom-designed frontend with a responsive layout and seamless user experience.

## 🔧 Tech Stack

- *Backend:* Django (Python)
- *Frontend:* Tailwind CSS, HTML5
- *Database:* SQLite (default for development)
- *Session-based Cart:* Supports adding, removing, and updating item quantities
- *Authentication:* Django's built-in user system with custom login/signup UI
- *Pagination:* Custom item listings with pagination support
- *Admin Panel:* Full access to manage inventory (Products, Vegetables, Fruits)

## ✨ Features

- View product listings (fruits, vegetables, spices) with image, description & price
- Add items to cart (session-based) with quantity controls
- View subtotal, tax, delivery, and total in cart summary
- User registration & login/logout with styled UI
- Tailwind-powered responsive design

## Login Credentials
Username: Haseeb
Password: Alan@12321#

## 📦 Setup Instructions

```bash
git clone https://github.com/your-username/spicerack.git
cd project name
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
