# Hierarchical-Data-and-You
The goal of this assignment is to learn about this type of database and different ways of working with it. Build a simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure. We won't actually be uploading anything, just making model instances and using them to represent real data. See the rubric for more detailed information. Submit as link to your repo on Github.

How To Start Application Locally: 

1. git clone git@github.com:pbuzzo/Hierarchical-Data-and-You.git
2. cd Hierarchical-Data-and-You
3. poetry install
4. poetry shell
5. python manage.py runserver
6. python manage.py createsuperuser
6. Open server in browser at: http://127.0.0.1:8000/
7. View Admin Panel at: http://127.0.0.1:8000/admin/



*Resources:*
- https://django-mptt.readthedocs.io/en/latest/tutorial.html
- https://django-mptt.readthedocs.io/en/latest/templates.html
- https://stackoverflow.com/questions/11508088/django-how-to-do-crud-with-django-mptt
- https://stackabuse.com/modified-preorder-tree-traversal-in-django/