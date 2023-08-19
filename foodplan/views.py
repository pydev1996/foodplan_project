from django.shortcuts import render, redirect
from .models import FoodPlan
from .forms import FoodPlanForm

def add_food_plan(request):
    if request.method == 'POST':
        form = FoodPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foodplan_list')
    else:
        form = FoodPlanForm()
    return render(request, 'foodplan/add_food_plan.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodPlan

def update_food_plan(request, pk):
    food_plan = get_object_or_404(FoodPlan, pk=pk)
    if request.method == "POST":
        day = request.POST.get("day")
        breakfast = request.POST.get("breakfast")
        lunch = request.POST.get("lunch")
        evening_snacks = request.POST.get("evening_snacks")
        dinner = request.POST.get("dinner")
        bed_snacks = request.POST.get("bed_snacks")
        
        food_plan.day = day
        food_plan.breakfast = breakfast
        food_plan.lunch = lunch
        food_plan.evening_snacks = evening_snacks
        food_plan.dinner = dinner
        food_plan.bed_snacks = bed_snacks
        
        food_plan.save()
        return redirect("foodplan_list")  # Redirect to the food plan list view
    
    context = {"food_plan": food_plan}
    return render(request, "foodplan/update_food_plan.html", context)

def foodplan_list(request):
    food_plans = FoodPlan.objects.all()
    print(food_plans)
    return render(request, 'foodplan/foodplan_list.html', {'food_plans': food_plans})
