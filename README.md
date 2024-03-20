This is a practice repository

permissions.py
---
cusom created file to ensure authenticaiton across users. The `IsOwnerOrReadOnly` class is imported to views.py `ProfileDetail`.
`permission_classes = [IsOwnerOrReadOnly]` and `self.check_object_permissions(self.request, profile)` checks if the user is authenticated.

posts views.py
---
permissions in `from rest_framework import permissions` and `permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]` ensure that the create post form is only present when the user is authenticated.

django-filter
---
- In terminal:
`pip3 install django-filter`
- Add to settings.py:
`django_filters`
- Inside the views that will use the filtering, import:
`from django_filters.rest_framework import DjangoFilterBackend`
This enable more filtering options

JWT tokens
---
This repository use JWT tokens. To setup:
- In terminal:
`pip3 install rest-auth==2.1.9`
- Add the following to installed apps inside settings.py
rest_framework.authtoken
dj_rest_auth
- Inside the main urls.py, add the following:
`path('dj-rest-auth/', include('dj_rest_auth.urls')),`
- Migrate and freeze
- Run in terminal:
`pip3 install djangorestframework-simplejwt`
- If you have access to the development codespace, add this to the env.py:
`os.environ['DEV'] = '1'`
- Create the REST_FRAMEWORK in settings.py.
![screenshot of REST_FRAMEWORK]()
- Add the following:
![screenshot of the four JWT rows from settings.py]()

All-auth
---
This repository use All-auth to let the user register for an account
- In terminal:
`pip3 install 'dj-rest-auth[with_social]'`
- Add the following to the installed apps:
django.contrib.sites
allauth
allauth.account
allauth.socialaccount
dj_rest_auth.registration
- Create SITE_ID anywhere in the settings.py file:
`SITE_ID = 1`
- Add to the main urls.py file:
`path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),`

Serializers in drf_api?
---
The serializers.py file was created inside drf_api to assign profile id and profile image to each authenticated user

Rest serializer
---
Inside settings.py add:
`REST_AUTH_SERIALIZERS = {'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'}`

JSON for enduser
---
the end user will only need json data, as it would cost unneccessary traffic to load html
- In settings.py
![screenshot of "if 'DEV' not in os.environ:"]()

Database
---
This repository use ElephantSQL to store data. Note that the service is shutting down, so only use this service for practice.
- Run in terminal:
`pip3 install dj_database_url==0.5.0 psycopg2`
- import the following in settings.py underneath `import.os`:
`import dj_database_url`
- Update the DATABASES:
![screenshot of new DATABASES]()
This will connect the end user to the data service, and the developer to the db.sqlite3 file
- in env.py add:
`os.environ['DATABASE_URL'] = "<PostgreSQL> as string"`

Deployment
---
- in terminal:
`pip3 install gunicorn django-cors-headers`
- Don't forger to freeze requirements
- Create the Procfile with the following content:
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi
- Add to installed apps:
corsheaders
- Add to MIDDLEWARE list:
`'corsheaders.middleware.CorsMiddleware'`
- Create this block of code:
![screenshot of if 'CLIENT_ORIGIN' in os.environ:]()
- Set debug to:
`'DEV' in os.environ`
- Set this as the SECRET_KEY:
`SECRET_KEY = os.getenv('SECRET_KEY')`
- freeze requirements