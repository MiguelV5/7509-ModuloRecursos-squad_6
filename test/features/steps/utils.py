from datetime import date, timedelta
import random

def random_date():
    start_date = date.min
    limit_date = date.today()
    delta_days = limit_date - start_date
    random_days = random.randint(0, delta_days.days)
    return str(start_date + timedelta(days=random_days))