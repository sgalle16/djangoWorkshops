# Workshop 01 - Products Model for Marketplace

This project is part of a workshop to develop a basic version of a products model for a marketplace using Django. The project showcases the implementation of various CRUD operations and basic data handling in a web application.

## Description

The application provides a simple interface to create, view, list, and delete products. It focuses on handling basic attributes of a product and demonstrates fundamental web development practices.

## Django Project Setup Instructions 

Prerequisites:

- Python 3.8.10
- pip y virtualenv

1. Set Up Virtual Environment:

      - Create: `python3 -m venv myvenv`
      - Activate:
        - Windows: `myvenv\Scripts\activate`
        - macOS/Linux: `source myvenv/bin/activate`

1. Install Dependencies, staying in the project folder::
      - Run: `pip install -r requirements.txt`

2. Prepare Database:
      - Migrations: 
        - `python manage.py makemigrations`
        - `python manage.py migrate`

3. Start Server:
      - Run: `python manage.py runserver`
      - Visit: http://127.0.0.1:8000/ in your browser.