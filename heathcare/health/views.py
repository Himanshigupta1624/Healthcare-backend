from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics ,status, permissions
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    RegisterSerializer, 
    PatientSerializer, 
    PatientDetailSerializer,
    DoctorSerializer, 
    PatientDoctorMappingSerializer
)

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class=RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":RegisterSerializer(user,context=self.get_serializer_context()).data,
            "message":"User created successfully"
        },status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView) :
    def post(self,request,*args,**kwargs):
        response=super().post(request,*args,**kwargs)
        if response.status_code==200:
            response.data['message']='Login successful'
        
        return response

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class=PatientSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PatientDetailSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)     
    def get_object(self):
        patient=get_object_or_404(Patient,id=self.kwargs['pk'],user=self.request.user)
        return patient

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    serializer_class=PatientDoctorMappingSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        patient = serializer.validated_data['patient']
        doctor = serializer.validated_data['doctor']    
        
        if PatientDoctorMapping.objects.filter(patient=patient,doctor=doctor).exists():
            return Response({
                "error":"Doctor is already assigned to the patient"
            },status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)    

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def patient_doctors_view(request,patient_id) :
    try:
        patient=Patient.objects.get(id=patient_id,user=request.user) 
    except Patient.DoesNotExist:
        return Response({
            "error": "Patient not found or you don't have permission to access this patient"
        }, status=status.HTTP_404_NOT_FOUND)
    
    mappings=PatientDoctorMapping.objects.filter(patient=patient)
    serializer=PatientDoctorMappingSerializer(mappings,many=True)
    return Response(serializer.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_doctor_from_patient(request,mapping_id):
    try:
        mapping=PatientDoctorMapping.objects.get(
            id=mapping_id,
            patient__user=request.user
        )  
        mapping.delete()
        return Response({
            "message": "Doctor removed from patient successfully"
        },status=status.HTTP_204_NO_CONTENT)  
    
    except PatientDoctorMapping.DoesNotExist:
        return Response({
            "error": "Mapping not found or you don't have permission to access this mapping"
        }, status=status.HTTP_404_NOT_FOUND)
        
            
            
                              
        