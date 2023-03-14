from modeltranslation.translator import register, TranslationOptions
from .models import Course, Teacher


@register(Course)
class CourseTO(TranslationOptions):
    fields = ('name', 'location', 'description', 'shortname' )


@register(Teacher)
class TeacherTO(TranslationOptions):
    fields = ('name', 'about', )