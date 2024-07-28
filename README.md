# Blog Application

This is a simple blog application built with Python, Django, HTML, CSS, and Bootstrap.

## Features
- Create, read, update, delete blog posts (only for admin)
- Responsive design

## Installation

1. Clone the repository:
    git clone https://github.com/azizprodev/blog-website.git

2. Create and activate a virtual environment:
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Apply migrations:
    python manage.py migrate

5. Run the development server:
    python manage.py runserver

## Usage
- Visit `http://127.0.0.1:8000` in your browser.
- Create, edit, and delete blog posts (only for admin).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
