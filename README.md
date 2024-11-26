
# SafeReg

SafeReg is a Django-based web application designed for secure and efficient data registration and management. It provides a robust, user-friendly interface and adheres to modern security standards.

## Features

- Secure data registration and management.
- User authentication and authorisation.
- Customizable forms and templates for flexibility.
- Supports scalable and modular architecture.
- Easy to set up and deploy.

## Project Structure

```plaintext
SafeReg/
├── db.sqlite3                # SQLite database
├── manage.py                 # Django project management script
├── requirements.txt          # Python dependencies
├── safeReg/                  # Core project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL configuration
│   ├── wsgi.py               # WSGI configuration for deployment
│   ├── asgi.py               # ASGI configuration for async support
│   ├── .env                  # Environment variables (not included)
│   └── ...
└── secureReg/                # Main application directory
    ├── models.py             # Database models
    ├── views.py              # Application views
    ├── forms.py              # Django forms
    ├── templates/            # HTML templates
    ├── templatetags/         # Custom template tags
    ├── migrations/           # Database migrations
    └── ...
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/IpfaniMuleya/SafeReg.git
   cd safereg
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the `safeReg/` directory and set the required variables (e.g., `SECRET_KEY`, `DATABASE_URL`).

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Dependencies

- Python 3.8+
- Django 4.0+
- SQLite (default) or another database of your choice.

Refer to `requirements.txt` for the full list of dependencies.

## Contributing

Contributions are welcome! Please fork this repository, create a new branch for your feature, and submit a pull request. Ensure that your code follows the project's style guidelines and passes all tests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, feel free to reach out to us at muleyaipfani22@gmail.com.
