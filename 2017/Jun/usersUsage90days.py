from datetime import datetime, timedelta
from apps.taxbot.models import User

count = 0
ninety_days = datetime.now() - timedelta(days=90)
users = User.objects.filter(thirdparty_id=120)

for user in users:
    should_count = False
    trans = user.transaction_set.filter(created__gt=ninety_days)
    trips = user.trip_set.filter(created__gt=ninety_days)
    tripsu = user.tripunclassified_set.filter(created__gt=ninety_days)
    expense = user.expense_set.filter(created__gt=ninety_days)
    if trans or trips or tripsu or expense:
        count += 1
