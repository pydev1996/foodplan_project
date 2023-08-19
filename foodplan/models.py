from django.db import models

class FoodPlan(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    breakfast = models.TextField()
    lunch = models.TextField()
    evening_snacks = models.TextField()
    dinner = models.TextField()
    bed_snacks = models.TextField()

    def __str__(self):
        return self.day
