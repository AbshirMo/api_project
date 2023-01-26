from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Branch(models.Model):
    branch_name = models.CharField(
        max_length=50, unique=True, help_text='Enter a branch location (e.g Nairobi)')
    address = models.CharField(max_length=50)
    no_of_emps = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.branch_name}'


class Client(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    branch_name = models.ForeignKey(Branch, on_delete=models.RESTRICT)
    join_date = models.DateTimeField('date launched', null=True)
    balance = models.IntegerField(default=0)

    KE_SHILLINGS = 'Kshs'
    DOLLAR = 'Dollar'
    EURO = 'Euro'
    BR_POUND = 'Pound'

    CURRENCY_CHOICES = [
        (KE_SHILLINGS, 'Kenya Shillings'),
        (DOLLAR, 'US Dollars'),
        (EURO, 'Euros'),
        (BR_POUND, 'Pounds')
    ]

    currency = models.CharField(
        max_length=10, choices=CURRENCY_CHOICES, default=KE_SHILLINGS)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Manager(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    branch_name = models.ForeignKey(Branch, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.fname} {self.lname}'
