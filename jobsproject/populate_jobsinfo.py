import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

def phoneno():
    num = randint(6,9)
    num1 = str(num)
    for i in range(9):
        num1 += str(randint(0,9))
    return int(num1)
fake = Faker()
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftittle = fake.random_element(elements=('Software Engineer','Team Lead','Project lead','Project Manager'))
        feligbility = fake.random_element(elements=('B.E/B.TECH','BSC/MSC','BCA/MCA','M.E/M.TECH'))
        faddress = fake.address()
        femail = fake.email()
        fphoneno = phoneno()
        HydJobs_rec = HydJobs.objects.get_or_create(date=fdate,company=fcompany,tittle=ftittle,eligbility=feligbility,address=faddress,email=femail,phoneno=fphoneno)
populate(30)       

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftittle = fake.random_element(elements=('Software Engineer','Team Lead','Project lead','Project Manager'))
        feligbility = fake.random_element(elements=('B.E/B.TECH','BSC/MSC','BCA/MCA','M.E/M.TECH'))
        faddress = fake.address()
        femail = fake.email()
        fphoneno = phoneno()
        CheJobs_rec = CheJobs.objects.get_or_create(date=fdate,company=fcompany,tittle=ftittle,eligbility=feligbility,address=faddress,email=femail,phoneno=fphoneno)
populate(30)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftittle = fake.random_element(elements=('Software Engineer','Team Lead','Project lead','Project Manager'))
        feligbility = fake.random_element(elements=('B.E/B.TECH','BSC/MSC','BCA/MCA','M.E/M.TECH'))
        faddress = fake.address()
        femail = fake.email()
        fphoneno = phoneno()
        BanJobs_rec = BanJobs.objects.get_or_create(date=fdate,company=fcompany,tittle=ftittle,eligbility=feligbility,address=faddress,email=femail,phoneno=fphoneno)
populate(30)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftittle = fake.random_element(elements=('Software Engineer','Team Lead','Project lead','Project Manager'))
        feligbility = fake.random_element(elements=('B.E/B.TECH','BSC/MSC','BCA/MCA','M.E/M.TECH'))
        faddress = fake.address()
        femail = fake.email()
        fphoneno = phoneno()
        PuneJobs_rec = PuneJobs.objects.get_or_create(date=fdate,company=fcompany,tittle=ftittle,eligbility=feligbility,address=faddress,email=femail,phoneno=fphoneno)
populate(30)
