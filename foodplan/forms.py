from django import forms
from .models import FoodPlan

class FoodPlanForm(forms.ModelForm):
    class Meta:
        model = FoodPlan
        fields = '__all__'
