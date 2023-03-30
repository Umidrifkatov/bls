from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from .models import Course, Teacher, CourseTime, Student, FAQ


def get_all_courses(): # for taking from db all coursess !! recommended to use in every func
    all_c = Course.objects.all()
    return all_c



# Only for mainpage usage
# Improve for Teachers and schedule
def main(request):
    teachers = Teacher.objects.all()
    faqs = FAQ.objects.all()
    context = {'courses': get_all_courses(),
                'teachers': teachers,
                'faqs': faqs}
    return render(request, 'index.html', context)



def coursedetail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'courses': get_all_courses(),
                'course': course}
    return render(request, 'coursepage.html', context)





def register(request):
    return render(request, 'bls.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
