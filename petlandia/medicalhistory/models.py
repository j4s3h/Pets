from django.db import models
from pet.models import Pet
from datetime import datetime, timedelta, date
from parent.models import Parent
class MedicalHistory(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name = 'medical_histories')
    chief_complaint = models.TextField(blank = True,null = True)
    medication_given_prior_to_check_up = models.TextField(null= True, blank = True)
    last_vaccination_given = models.CharField(max_length=100, null = True ,blank = True)
    last_vaccination_date = models.DateField(null =True ,blank = True)
    last_vaccination_brand = models.CharField(max_length=100, null = True, blank = True)
    last_deworming_given = models.CharField(max_length=100, null = True, blank = True)
    last_deworming_date = models.DateField(null =True,blank = True)
    last_deworming_brand = models.CharField(max_length=100, null = True ,blank = True)
    is_transferred_from_other_clinic = models.BooleanField(default= False, null = True,blank = True)
    name_of_clinic = models.CharField(max_length=100, blank=True, null=True)
    case = models.TextField(null=True ,blank = True)
    date_hospitalized = models.DateField(null=True ,blank = True)
    diet = models.TextField(null=True ,blank = True)
    weight = models.FloatField(null=True ,blank = True)
    initial_temp = models.FloatField(null=True,blank = True)
    heart_rate = models.CharField(max_length = 100, null=True ,blank = True)
    respiratory_rate = models.CharField(max_length = 100, null=True ,blank = True) 
    abnormal_findings = models.TextField(null=True ,blank = True) 
    is_cbc = models.BooleanField(null=True ,blank = True)
    is_skin_scrape = models.BooleanField(null=True ,blank = True)
    is_xray = models.BooleanField(null=True ,blank = True)
    is_dfs = models.BooleanField(null=True ,blank = True)
    is_urinalysis = models.BooleanField(null=True ,blank = True)
    is_vaginal_smear = models.BooleanField(null=True ,blank = True)
    tentative_diagnosis = models.TextField(null=True ,blank = True)
    prognosis = models.TextField(null=True ,blank = True)
    treatment_given = models.TextField(null=True ,blank = True)
    take_home_meds = models.TextField(null=True ,blank = True)
    recommendations = models.TextField(null=True ,blank = True)
    followup_checkup_date = models.DateField(null=True,blank = True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    
    @property
    def total_medical_history(self):
        queryset = MedicalHistory.objects.count()
        return queryset
    @property
    def medical_records_for_the_month(self):
        current_month = datetime.now().month
        queryset = MedicalHistory.objects.filter(followup_checkup_date__month=current_month).count()
        return queryset
    
    @property
    def medical_records_for_the_year(self):
        current_month = datetime.now().month
        queryset = MedicalHistory.objects.filter(followup_checkup_date__month=current_month).count()
        return queryset
    
    @property
    def today_or_upcoming_checkups(self):
        today = datetime.now().date()
        queryset= MedicalHistory.objects.filter(followup_checkup_date__gte=today).count()
        
        return queryset
    @property
    def yesterday_checkups(self): 
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        queryset = MedicalHistory.objects.filter(followup_checkup_date=yesterday).count()
        return queryset
    @property
    def today_checkups(self): 
        today = datetime.now().date()
        
        queryset= MedicalHistory.objects.filter(followup_checkup_date=today).count()
        return queryset
    @property
    def parents_with_pets_followup_today(self):
        today_date = date.today()
        queryset= Parent.objects.filter(
        pets__medicalhistory__followup_checkup_date=today_date).distinct().count()
        return queryset
        
        
        