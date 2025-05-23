Bookstore Application
This project is a web-based e-commerce application designed to emulate a manga store. It was developed as the final project for the Web Systems Development course at NJIT. The application allows users to view, add, update, and delete manga records, providing a foundational example of a full-stack web application.

Table of Contents
About

Features

Technologies Used

Getting Started

Prerequisites

Installation

Usage

Project Structure

Contributing

License

About
bookStore is the final project for the Web Systems Development course at NJIT. The project emulates an e-commerce website, specifically taking the form of a manga store. It showcases functionalities typical of an online retail platform, allowing for the management and display of popular manga titles like Naruto and Dragon Ball. This project was implemented using the Django web framework.

Features
Manga Management:

View a list of all available manga titles.

Add new manga records (e.g., title, author, ISBN, publication year, genre).

Update existing manga details.

Delete manga records from the system.

E-commerce Emulation:

(Assumed, based on "e-commerce website emulation"): Functionalities like displaying product details, potentially a shopping cart (if implemented), and order processing.

User Interface:

A simple, intuitive web interface for interacting with the manga data.

Data Persistence:

Stores manga information persistently using a database.

Technologies Used
Python: The core programming language.

Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

HTML/CSS/JavaScript: For the frontend presentation and interactivity.

Database: Typically SQLite for development, and can be configured for PostgreSQL, MySQL, or other relational databases for production.

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Before you begin, ensure you have the following installed:

Python: Version 3.8 or higher.

pip: Python's package installer (usually comes with Python).

Git: For cloning the repository.

An IDE (Optional but Recommended): VS Code, PyCharm, or similar.

Installation
Clone the repository:

git clone https://github.com/Alexs2256/bookStore.git
cd bookStore/bookstore

Create and activate a virtual environment (recommended):

python -m venv venv
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

Install project dependencies:
With your virtual environment activated, install the required Python packages:

pip install -r requirements.txt # Assuming a requirements.txt file exists
# If no requirements.txt, you might need:
# pip install Django

Apply database migrations:
Navigate to the inner bookstore directory (where manage.py is located) and run:

python manage.py migrate

This command sets up the necessary database tables.

Create a superuser (optional, for admin access):

python manage.py createsuperuser

Follow the prompts to create an administrator account.

Usage
Once the application is running, open your web browser and navigate to the appropriate URL.

Default URL (if running locally):

Typically http://127.0.0.1:8000/

You should then be able to:

View the list of manga titles.

Interact with the application's features (e.g., add new manga, edit details, delete entries).

Access the Django admin panel at http://127.0.0.1:8000/admin/ (if you created a superuser).

Project Structure
The project follows a typical Django project structure:

bookstore/
├── bookstore/              # Outer project directory (repository root)
│   ├── bookstore/          # Inner project directory (contains settings.py, urls.py)
│   │   ├── __init__.py
│   │   ├── settings.py     # Project settings
│   │   ├── urls.py         # Main URL configurations
│   │   └── wsgi.py         # WSGI configuration for deployment
│   ├── manage.py           # Django's command-line utility
│   ├── <app_name>/         # Django application directory (e.g., 'manga', 'catalog')
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py        # Admin site configurations
│   │   ├── apps.py
│   │   ├── models.py       # Database models
│   │   ├── tests.py
│   │   ├── urls.py         # App-specific URL configurations
│   │   └── views.py        # View functions/classes
│   ├── templates/          # HTML templates (if not in app directories)
│   ├── static/             # Static files (CSS, JS, images)
│   └── README.md           # This file
└── .gitignore

Contributing
Contributions are welcome! If you have suggestions for improvements or find issues, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/AmazingFeature).

Make your changes.

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details (if one exists in the original repository). If no LICENSE file is present, you may want to add one.


![image](https://github.com/user-attachments/assets/61ba320f-1709-4fe5-8c9f-cfd15b0b6cc6)
![image](https://github.com/user-attachments/assets/b1783c6d-426d-4260-af94-51a7c8238383)
![image](https://github.com/user-attachments/assets/3bb799dc-774d-4982-be86-8265cf883aed)
![image](https://github.com/user-attachments/assets/f5eedd1e-6ae6-4cac-a2ac-2d7a7e5971bd)
-----------------------------------------------------------------------------------------
When Product is clicked
![image](https://github.com/user-attachments/assets/7019db51-8794-4cfc-b488-b30ff782bd3e)

-----------------------------------------------------------------------------------------
When in checkout
![image](https://github.com/user-attachments/assets/e4ac704b-08c3-4734-bd4f-30dec0736535)

IS601 Final Assignment: Bookstore
Eric Varghese
Alexander Stavrou
Paarth Patel

Python 3.10.11
pip 24.0
django-5.0.2
certifi-2024.2.2 
charset-normalizer-3.3.2 
requests-2.31.0 
urllib3-2.2.1

run django server by 'python manage.py runserver' in terminal

Django admin:
Username: Eric
Password: password
