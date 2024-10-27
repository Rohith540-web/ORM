

from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
 Bln=models.CharField(max_length=20,primary_key="Bln")
 name=models.CharField(max_length=100)
 Loanamount=models.IntegerField()
 address=models.CharField(max_length=100)
 age=models.IntegerField()
 phoneno=models.IntegerField()

class BankLoanAdmin(admin.ModelAdmin):
 list_display=('Bln','name','Loanamount','address','age','phoneno')


