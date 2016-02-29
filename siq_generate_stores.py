from location.models import Store
from django.contrib.auth.models import User
from siqauth.models import Role, UserStoreRole
from tests.helpers.factories import StoreFactory, UserFactory, RoleFactory, UserStoreRoleFactory
from random import randint

num_users = 100

num_roles = 100

num_stores = 9000

while (User.objects.count() < num_users):
    user = User(
        username = 'user{}'.format(User.objects.count()),
    )
    user.set_password('password')
    user.save()

while (Role.objects.count() < num_roles):
    Role(
        name = 'Role {}'.format(Role.objects.count())
    ).save()

while (Store.objects.count() < num_stores):
    Store(
        display_name = 'store {}'.format(Store.objects.count()),
    ).save()

for store in Store.objects.all():
    if not store.display_name in ['Local Store', 'Company']:
        #Assign a random number of users with random roles
        users=[]
        for i in range(randint(0, num_users)):
            # user_1 = None
            # while user_1 == None or user_1.username in ['tim', 'perm', 'AnonymousUser'] or user_1 in users:
                # user_1 = User.objects.all()[randint(0, num_users)]
            try:
                UserStoreRole(
                    user=User.objects.all()[randint(0, num_users)],
                    object=store,
                    role=Role.objects.all()[randint(0, 10)]
                ).save()
            except:
                pass

            # users.append(user_1)


# Execute with:  DJANGO_SETTINGS_MODULE=settings.tim vptest/bin/python manage.py shell < generate_stores.py
