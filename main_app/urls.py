from django.urls import path
from . import views # dot(.) here mean root
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Routes in Express , URLs in Django
    # DONT add / here this mean root
    path('', views.home, name='home') ,

    # signup rout
    path('accounts/signup/',views.signup , name='signup'),

    # profile URL's
    path('accounts/profile/<int:user_id>',views.profile , name='profile'),

    path('accounts/<int:pk>/edit', views.PasswordChangeView.as_view(), name="change_password"),
    # path("password_reset", views.password_reset_request, name="password_reset"),

    # password reset 
    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('accounts/edit/<int:user_id>', views.edit_patient_profile, name='edit_patient_profile'),
    path('edit_admin_profile/<int:user_id>', views.edit_admin_profile, name='edit_admin_profile'),
    path('edit_doctor_profile/<int:user_id>', views.edit_doctor_profile, name='edit_doctor_profile'),



    # path('accounts/<int:pk>/edit',views.editProfile,name='edit_Profile'),



    # departments URL's
    path('departments/', views.DepartmentsList.as_view(), name='departments_index'),
    path('departments/<int:pk>',views.DepartmentsDetail.as_view(),name='departments_detail'),
    path('departments/create', views.DepartmentsCreate.as_view(),name='departments_create'),
    path('departments/<int:pk>/update', views.DepartmentsUpdate.as_view(),name='departments_update'),
    path('departments/<int:pk>/delete/', views.DepartmentsDelete.as_view(), name='departments_delete'),

    # doctors URL's
    path('doctors/', views.DoctorsList.as_view(), name='doctors_index'),
    path('doctors/<int:pk>',views.DoctorsDetail.as_view(),name='doctors_detail'),
    path('doctors/create', views.DoctorsCreate.as_view(),name='doctors_create'),
    path('doctors/<int:pk>/update', views.DoctorsUpdate.as_view(),name='doctors_update'),
    path('doctors/<int:pk>/delete/', views.DoctorsDelete.as_view(), name='doctors_delete'),

    # appointment URL's
    path('appointments/', views.AppointmentsList.as_view(), name='appointments_index'),
    path('appointments/<int:pk>',views.AppointmentsDetail.as_view(),name='appointments_detail'),
    path('appointments/create', views.AppointmentsCreate.as_view(),name='appointments_create'),
    path('appointments/<int:pk>/update', views.AppointmentsUpdate.as_view(),name='appointments_update'),
    path('appointments/<int:pk>/delete/', views.AppointmentsDelete.as_view(), name='appointments_delete'),

    # path('doctor_profile/edit/', views.edit_doctor_profile, name='edit_doctor_profile'),




    # display all doctors in a specific department 
    path('department/<int:department_id>/doctors',views.DepartmentDoctor,name='department_doctor'),

]
