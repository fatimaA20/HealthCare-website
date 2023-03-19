from django.urls import path
from . import views # dot(.) here mean root

urlpatterns = [
    # Routes in Express , URLs in Django
    # DONT add / here this mean root
    path('', views.home, name='home') ,

    # signup rout
    path('accounts/signup/',views.signup , name='signup'),

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
]