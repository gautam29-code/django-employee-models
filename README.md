🚀 Learning Django – Model Relationships & Admin Panel

Today I practiced Django ORM by creating a small employee management schema and connecting it with the Django admin panel.

Models implemented:

• Dept – department details
• Emp – employee details
• Salgrade – salary grade structure

Key Concepts Used:

✔ Django Models
✔ Primary Keys
✔ ForeignKey Relationships
✔ Admin Panel Integration
✔ Django ORM

Example relationship:

class Emp(models.Model):
empno = models.IntegerField(primary_key=True)
ename = models.CharField(max_length=20)
dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

After registering the models in admin.py, I was able to manage all records directly from the Django Admin dashboard.

This is one of the powerful features of Django that allows rapid backend development.

Currently improving my skills in Python, Django, and Full Stack Development.

#Python #Django #BackendDevelopment #WebDevelopment #LearningInPublic #FullStackDeveloper
