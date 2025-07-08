# E-commerce Backend API

A RESTful API for an e-commerce platform built with Django, Django REST Framework, and JWT authentication. The API is documented with Swagger and deployed on Render.

## Features

- User registration and authentication using JWT
- Seller profile creation and management
- Product CRUD operations
- Shopping cart and order processing endpoints
- API documentation via Swagger UI

## Tech Stack

- **Framework:** Django
- **API:** Django REST Framework (DRF)
- **Authentication:** JSON Web Tokens (JWT) with `djangorestframework-simplejwt`
- **Documentation:** Swagger UI via `drf-yasg`
- **Database:** PostgreSQL (configured via environment variables)
- **Deployment:** Render

## Live API Documentation

Download de Swagger doc.json:

[https://commerce-backend-cm1y.onrender.com/docs/swagger.json](https://commerce-backend-cm1y.onrender.com/docs/swagger.json)

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/HollowDude/commerce_backend.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables (create a `.env` file in the project root):
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DATABASE_URL=postgres://user:password@host:port/dbname
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the API at `http://localhost:8000/`.



## Contributing

Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
