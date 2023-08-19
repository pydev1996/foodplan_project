from django_cron import CronJobBase, Schedule
from datetime import datetime
from plyer import notification
from .models import FoodPlan

class SendNotificationsCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # Run every 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.send_notifications_cron_job'  # A unique code

    def do(self):
        today = datetime.today().strftime('%A')
        print(today)
        try:
            food_plan = FoodPlan.objects.get(day=today)
            notification_title = f"Food Plan for {today}"
            notification_message = f"Breakfast: {food_plan.breakfast}\nLunch: {food_plan.lunch}\nEvening Snacks: {food_plan.evening_snacks}\nDinner: {food_plan.dinner}\nBed Snacks: {food_plan.bed_snacks}"
            notification.notify(title=notification_title, message=notification_message)
        except FoodPlan.DoesNotExist:
            pass
