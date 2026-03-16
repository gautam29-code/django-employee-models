# Django Employee Management Models

This project demonstrates Django model design and admin panel integration.

## Models

Dept
- deptno (Primary Key)
- dname (Unique)
- loc

Emp
- empno (Primary Key)
- ename
- job
- mgr
- hiredate
- sal
- comm
- dept (ForeignKey)

Salgrade
- grade (Primary Key)
- lowsal
- hisal

## Features
- Django ORM models
- ForeignKey relationship
- Admin panel integration
- CRUD operations via Django Admin

## Tech Stack
Python
Django
SQLite
