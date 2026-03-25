from django.db import models


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=30, unique=True)
    loc = models.CharField(max_length=20)
    
    

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=10, decimal_places=2)
    comm = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ename
    

   

class Salgrade(models.Model):
    grade = models.IntegerField(primary_key=True)
    lowsal = models.DecimalField(max_digits=8, decimal_places=2)
    hisal = models.DecimalField(max_digits=8, decimal_places=2)

 