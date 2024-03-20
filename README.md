username: testuser1
passowrd: testpass1

username: testuser2
password: testpass2

username: testuser3
password: testpass3

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