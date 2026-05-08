# Django Sample Product Search

This Django project models products, categories, and tags, then provides a simple search page where users can combine description search with category and tag filters.


## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run database migrations:

```bash
python manage.py migrate
```

4. Create an admin user:

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the app:

- Product search page: `http://127.0.0.1:8000/`
- Django admin: `http://127.0.0.1:8000/admin/`


## Populating the Database

Data can be populated automatically using the management command.
 
```bash
python manage.py populate_data
```
, or manually using the Django admin to create at least:

- 5 categories
- 10 tags
- 20 products

Each product belongs to one category and may have multiple tags. Product descriptions are searched by the search box on the home page.

## API Documentation

See `API_DOCUMENTATION.md` for endpoint details, query parameters, and example requests.

## Notes

- The project uses SQLite by default for simple local setup.

## Technical Decisions
- Used Django REST Framework with class based views for clean, 
  readable API structure
- Used select_related and prefetch_related to avoid N+1 queries
- Chose vanilla JavaScript fetch() for the frontend to keep 
  the separation between frontend and backend clear
- Added a management command for easy database population

## AI Attribution

AI assistance was used to reduce extra database hits by using select_related for categories and prefetch_related for tags. suggested to return product ordered by name.

