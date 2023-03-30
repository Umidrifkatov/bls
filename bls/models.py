from configparser import MAX_INTERPOLATION_DEPTH
from distutils.command.upload import upload
from email.policy import default
from django.db import models



class Course(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название')
    shortname = models.CharField(max_length=255, verbose_name='Краткое название', null=True)
    description = models.TextField(max_length=2000, verbose_name='Описание')
    location = models.CharField(max_length=255, verbose_name='Место проведения', default='Ташкент, ул. Мустакиллик 45/66')
    price = models.IntegerField(default=80, verbose_name='Стоимость в USD $')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО преподавателя')
    title = models.CharField(max_length=50, verbose_name='Короткое описание деятельности', null=True, default='Кардиолог')
    exp = models.IntegerField(verbose_name='Опыт (лет)', default=2)
    img = models.ImageField(verbose_name='Фото', null=True, upload_to='media')
    about = models.TextField(max_length=500, verbose_name='Инфо о преподавателе max-500')
    tgusername = models.CharField(max_length=50, verbose_name='Телеграм username')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'



class CourseTime(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    places = models.IntegerField(default=6, verbose_name='Количество мест')
    time = models.DateTimeField(verbose_name='Время начала')
    discount = models.IntegerField(verbose_name='Скидка', null=True, blank=True)
    active = models.BooleanField(default=True,  verbose_name='Активность')

    def __str__(self):
        return str(self.time)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-time']


payments = [
    ('p', 'Payme'),
    ('c', 'Click'),
]


class Student(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=14, verbose_name="Телефон")
    email = models.CharField(max_length=255, verbose_name="Почта")
    ct = models.ForeignKey(CourseTime, on_delete=models.SET_NULL, null=True, verbose_name='Запись')
    payed = models.BooleanField(default=False, verbose_name='Оплачено')
    payed_sum = models.IntegerField(verbose_name='Стоимость в UZS', null=True)
    payed_by = models.CharField(max_length=1, default='p', verbose_name='Способ оплаты', choices=payments)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'             

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'студенты' 


class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name='Вопрос')
    answer = models.TextField(max_length=2000, verbose_name='Ответ')
