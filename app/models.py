from django.db import models


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=30, unique=True)
    loc = models.CharField(max_length=20)

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    mgr = models.IntegerField(null=True,blank=True)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=10,decimal_places=2)
    comm = models.DecimalField(null=True, blank=True,max_digits=8,decimal_places=2)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    lowsal=models.DecimalField(null=False,max_digits=8,decimal_places=3)
    hisal=models.DecimalField(null=False,max_digits=6,decimal_places=2)
    
    