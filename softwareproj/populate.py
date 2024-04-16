import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','softwareproj.settings')
import django
django.setup()

from faker import Faker
from random import *
from testapp.models import Hydjobs
fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project manager','team lead','HR','SE','ASE'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        Hydjobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber

        )
n=int(input('enter number of records:'))
populate(n)
print(f'{n} records inserted successfully')
