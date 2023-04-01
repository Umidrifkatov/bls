from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from .models import Course, Teacher, CourseTime, Student, FAQ
from datetime import datetime

tac = """
Terms and Conditions:
                    PLEASE READ BEFORE CONTINUING
                    
                    CANCELLATION POLICY
                    
                    Once registration has been processed, NO REFUND will be given. Credits may be used up to 60 days from the original class date.
                    
                    RESCHEDULING POLICY
                    
                    To reschedule: In order to reschedule, you must contact us at телефон during business hours (9.00 – 17.00 Tashkent time). 24 hours prior to the class, you are scheduled. We will not honor any rescheduling request if we do not have proof that you have attempted to contact us. If you are unable to reach a customer service representative during those hours, please send us an email us at email. We are closed for national Uzbekistan holidays. Rescheduling requests made on the holidays will not be counted until the next business day. Please see below for more details.
                    On the day rescheduling: Student is not allowed to reschedule on the day of the course. Student who does request this will be considered as a NO SHOW. Please see NO SHOW policy below.  
                    RESCHEDULE FEE - BLS AND HEARTSAVER CPR/AED - $50 .
                    Rescheduled more than once: We do not allow rescheduling more than once. We will not refund nor grant credit to student if the student is not able to make it to the rescheduled class unless there are extreme conditions rendering the student unable to come to class.
                    LATENESS POLICY:
                    Student must come to class on time. We recommend that student arrive to class ON TIME. If the student is more than 15 minutes late to class, the student is considered a NO SHOW. If the student is late for a rescheduled class, the student will also be considered as a NO SHOW. Please see below for the NO SHOW policy. If you know in advance that you will be late for your course, please reschedule within the adequate amount of time to prevent penalties. Please see the above rescheduling policy for more rescheduling details.
                    NO SHOW POLICY:
                    Student who does not show up to class and did not notify us before the start of the class is considered a NO SHOW. We do not honor refund or credit for NO SHOW student.  Rescheduling fee - BLS and HEARTSAVER CLASSES - $50
                    
                    NO eBooks can be exchanged/revoked once claimed online
                    
                    Please contact De Factum education (email, telephone) for any technical issues.
                    
                    At De Factum Education, your privacy is very important to us. Any information you provide us when you make purchases and requests (including your name, address, phone number, mailing address, credit card or other bank information) is kept strictly confidential and is never sold to outside vendors. We use this information only to provide you the services needed to transact your purchases. 
                    
                    ON SITE TRAINING
                    
                    De Factum Education will gladly come to your location to perform an On-Site Training. We ask that you have a minimum of six people. Once you have scheduled an On-Site Training date, we request a non-refundable deposit of 100% of the cost of the training. You can reschedule at least 48 hours prior the scheduled of the On-Site Training. Please be advised that you can only reschedule your training one time. If the On-Site Training is cancelled, you will not receive the deposit back. Also be aware that group discounts are given based on the number of students originally accounted for by the client. If fewer students than expected are present for the class, De Factum Education will not issue a refund for those missing students due to the nature of the discount, we can instead issue a credit for training of those students.
                    
                    DISCLAIMER POLICIES
                    
                    Classes may need to be rescheduled by the De Factum Education in case of an emergency - extreme weather or venue conditions, including heating, ventilation and air conditioning not working, or flooding at locations.
                    """

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
    times = CourseTime.objects.filter(course=course, active=True, places__gte=1, time__gt=datetime.now())
    context = {'courses': get_all_courses(),
                'course': course, 
                'times': times}
    return render(request, 'coursepage.html', context)





def register(request, pk):
    times = get_object_or_404(CourseTime, pk=pk)
    context = {'times': times,
                'tac': _(tac)}
    return render(request, 'registerform.html', context)


