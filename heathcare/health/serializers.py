from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Patient, Doctor, PatientDoctorMapping
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2=serializers.CharField(write_only=True,required=True)
    first_name=serializers.CharField(required=True,max_length=30)
    last_name=serializers.CharField(required=True,max_length=30)
    
    class Meta:
        model=User
        fields=('username', 'password', 'password2', 'email', 'first_name', 'last_name')
    
    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self,validated_data):
        validated_data.pop('password2')
        user=User.objects.create_user(**validated_data)
        return user    

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient 
        fields=['id', 'name', 'age', 'gender', 'phone', 'address', 'medical_history', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_age(self,value):
        if value < 0 or value > 150:
            raise serializers.ValidationError("Age must be between 0 and 150.") 
        return value

class DoctorSerializer(serializers.ModelSerializer):
    patient_count=serializers.SerializerMethodField()
    
    class Meta:
        model=Doctor
        fields = ['id', 'name', 'specialization', 'phone', 'email', 'patient_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_patient_count(self, obj):
        return obj.patient_mappings.count()

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name=serializers.CharField(source='patient.name',read_only=True)
    doctor_name=serializers.CharField(source='doctor.name',read_only=True)
    doctor_specialization=serializers.CharField(source='doctor.specialization',read_only=True)
    
    class Meta:
        model=PatientDoctorMapping
        fields=['id', 'patient', 'doctor', 'patient_name', 'doctor_name', 'doctor_specialization', 'assigned_date', 'notes']  
        read_only_fields=['id', 'assigned_date']    
    def validate(self, attrs):
        patient=attrs['patient']
        doctor=attrs['doctor']
        request=self.context.get('request')
        if request and patient.user!=request.user:
            raise serializers.ValidationError("You can only assign doctors to your own patients.")
        return attrs  

class PatientDetailSerializer(PatientSerializer)   :
    assigned_doctors=serializers.SerializerMethodField()
    
    class Meta(PatientSerializer.Meta):
        fields=PatientSerializer.Meta.fields + ['assigned_doctors']
    
    def get_assigned_doctors(self,obj):
        mappings=obj.doctor_mappings.all()
        return [{
            'id': mapping.doctor.id,
            'name': mapping.doctor.name,
            'specialization': mapping.doctor.specialization,
            'assigned_date': mapping.assigned_date,
            'notes': mapping.notes
        } for mapping in mappings]
                    