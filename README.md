# Library Management System

A simple and modern web application for managing a library's collection, members, and borrowing records. Built with Django and styled with Bootstrap 5.

## 📸 Screenshot

![Library Management System Screenshot](Screenshot%202025-10-16%20204624.png)

## Features

- **Modern User Interface**: A clean, responsive, and modern UI built with Bootstrap 5.
- **Light & Dark Themes**: A theme switcher that allows users to toggle between light and dark modes, with their preference saved locally.
- **User Authentication**: A complete and secure login/logout system. Pages are protected, ensuring only authenticated users can access the system.
- **Book Management**: Full CRUD (Create, Read, Update, Delete) functionality for the library's book collection.
- **Member Management**: Full CRUD functionality for library members.
- **Borrowing Records**: Track which member has borrowed which book, including borrow and return dates.
- **Search Functionality**: Easily search for books, members, and borrowing records.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (default)

## Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the Repository**
```sh
git clone https://github.com/SL-oomiBoy/Library_Management_System
cd Library_Management_System
```

**2. Create and Activate a Virtual Environment**

*   On Windows:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```
*   On macOS/Linux:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

**3. Install Dependencies**

First, make sure you have a `requirements.txt` file. If not, you can create one with the following command:
```sh
pip freeze > requirements.txt
```
Then, install the required packages:
```sh
pip install -r requirements.txt
```

**4. Run Database Migrations**

This will set up the database schema.
```sh
python manage.py migrate
```

**5. Create a Superuser**

This creates the first administrator account, which you will use to log in.
```sh
python manage.py createsuperuser
```
Follow the prompts to create your username and password.

**6. Run the Development Server**
```sh
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

## Usage

1.  Navigate to `http://127.0.0.1:8000/`.
2.  You will be redirected to the login page.
3.  Log in using the superuser credentials you created during the setup.
4.  You can now access all the features of the Library Management System.

---

**Developed by [Omiya](https://github.com/SL-oomiBoy)**

