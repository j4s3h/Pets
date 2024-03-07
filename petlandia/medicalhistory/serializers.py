from rest_framework import serializers
from .models import MedicalHistory


class MedicalHistorySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = MedicalHistory
        exclude = ['created', 'modified']
        
class DetailMedicalHistorySerializer(serializers.ModelSerializer):
    total_medical_history = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = MedicalHistory
        fields = ['id','pet','total_medical_history', 'chief_complaint', 'medication_given_prior_to_check_up', 'last_vaccination_given', 'last_vaccination_date', 'last_vaccination_brand', 'last_deworming_given', 'last_deworming_date', 'last_deworming_brand', 'is_transferred_from_other_clinic', 'name_of_clinic', 'case', 'date_hospitalized', 'diet', 'weight', 'initial_temp', 'heart_rate', 'respiratory_rate', 'abnormal_findings', 'is_cbc', 'is_skin_scrape', 'is_xray', 'is_dfs', 'is_urinalysis', 'is_vaginal_smear', 'tentative_diagnosis', 'prognosis', 'treatment_given', 'take_home_meds', 'recommendations', 'followup_checkup_date', 'created', 'modified', ]
class LandingPageSerializer(serializers.ModelSerializer):
    total_medical_history = serializers.StringRelatedField(read_only = True)
    medical_records_for_the_month = serializers.StringRelatedField(read_only = True)
    medical_records_for_the_year = serializers.StringRelatedField(read_only = True)
    today_or_upcoming_checkups = serializers.StringRelatedField(read_only = True)
    yesterday_checkups = serializers.StringRelatedField(read_only = True)
    today_checkups = serializers.StringRelatedField(read_only = True)
    parents_with_pets_followup_today = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = MedicalHistory
        fields = ['total_medical_history', 'medical_records_for_the_month', 'medical_records_for_the_year', 'today_or_upcoming_checkups' , 'yesterday_checkups', 'today_checkups', 'parents_with_pets_followup_today']
        
        