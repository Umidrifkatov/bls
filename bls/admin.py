from django.contrib import admin
from .models import Course, CourseTime, Teacher, Student, FAQ
from modeltranslation.admin import TranslationAdmin


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ('name', 'price','location', 'shortname',)


@admin.register(Teacher)
class T(TranslationAdmin):
    list_display = ('name', 'about', 'tgusername',)

@admin.register(Student)
class S(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'email', 'ct', 'payed_sum', 'payed', 'payed_by')


@admin.register(CourseTime)
class CT(admin.ModelAdmin):
    list_display = ('time', 'course', 'teacher', 'places', 'active' )

    def get_time(self):
        return self.time.str


@admin.register(FAQ)
class FAQT(TranslationAdmin):
    list_display = ('question',)



