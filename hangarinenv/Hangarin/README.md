# Hangarin

Hangarin is a Django-based student organization management system.

## Features
- Manage Colleges, Programs, and Organizations.
- Track Student memberships in various organizations.
- Custom Admin interface with search and filters.
- Data generation command for easy testing.

## Setup
1. Create a virtual environment: `python -m venv hangarinenv`
2. Activate the environment: `.\hangarinenv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Navigate to the projectsite folder: `cd projectsite`
5. Run migrations: `python manage.py migrate`
6. Run the data generation command: `python manage.py create_initial_data`
7. Start the server: `python manage.py runserver`

## Authors
- Janry (Developer)
- Peter Joshua (Developer)
