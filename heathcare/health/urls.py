from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
urlpatterns = [
    path('auth/register/',views.RegisterView.as_view(),name="register"),
    path('auth/login/',views.CustomTokenObtainPairView.as_view(),name="login"),
    path('auth/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    
    path('patients/',views.PatientListCreateView.as_view(),name='patient'),
    path('patients/<int:pk>/',views.PatientDetailView.as_view(),name='patient-detail'),
    
    path('doctors/',views.DoctorListCreateView.as_view(),name='doctor-list-create'),
    path('doctors/<int:pk>/',views.DoctorDetailView.as_view(),name='doctor-detail'),
    
    path('mappings/',views.PatientDoctorMappingListCreateView.as_view(),name='mapping-list-create'),
    path('mappings/<int:patient_id>/',views.patient_doctors_view,name='patient-doctors'),
    path('mappings/remove/<int:mapping_id>/',views.remove_doctor_from_patient,name="remove-doctor"),
    
]