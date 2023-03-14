from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from .models import Course, Teacher, CourseTime, Student


def get_all_courses():
    all_c = Course.objects.all()
    return all_c



# Create your views here.
def main(request):
    context = {'courses': get_all_courses()}
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
