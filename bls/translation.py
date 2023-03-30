from modeltranslation.translator import register, TranslationOptions
from .models import Course, Teacher, FAQ


@register(Course)
class CourseTO(TranslationOptions):
    fields = ('name', 'location', 'description', 'shortname' )


@register(Teacher)
class TeacherTO(TranslationOptions):
    fields = ('name', 'about', 'title',)


@register(FAQ)
class FAQTO(TranslationOptions):
    fields = ('question', 'answer')