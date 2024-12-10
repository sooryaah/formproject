from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course',views.course,name='course'),
    path('student',views.student,name='student'),
    path('show_student',views.show_student,name='show_student'),
    path('add_coursedb', views.add_coursedb, name='add_coursedb'),
    path('add_student',views.add_student,name='add_student'),
    path('add_studentdb',views.add_studentdb,name='add_studentdb'),
    path('show_details',views.show_details,name='show_details'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),

                # The home view
]
