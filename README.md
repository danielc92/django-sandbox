# Project Title
A sandbox project to test functionality of Django Framework.

# Before you get started
Concepts covered in this project:
- Request methods (POST, GET)
- Template Engine (Jinja)
- ORM Models
- Creating forms from ORM Models
- One to Many, Many to Many relationships
- Rendering templates from ORM Models
- File uploading

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/django-sandbox.git
```

**This project uses a python 3.7 virtual environment**
```sh
virtualenv --python=/path/to/python3bin venv
source activate venv
pip install django
```

**To create the database for the first time**
```sh
cd path/to/this/project (where manage.py resides)
python manage.py makemigrations
python manage.py migrate
```

# Tests
- Created Dog and DogOwner models (one to many relationship)
- Created Article and Tag models (many to many relationship)
- Created and tested route to create new Dogs
- Created and tested route to create new Articles (Tags have to be created beforehand)
- Render Dogs/Owners/Articles in list style

# Notes
- When created a model/form class which uses ImageField make sure request.FILES is passed into form model (eg DogForm(request.POST, request.FILES))
- When creating a model/form class which uses ImageField make sure `enctype="multipart/form-data"` is present in the form attributes.
- Adjust timezone in settings.py. Timezone strings can be found in django docs

# Contributors
- Daniel Corcoran

# Sources
- [Django Documentation](https://docs.djangoproject.com/en/2.2/)