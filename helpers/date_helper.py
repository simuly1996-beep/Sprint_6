from datetime import datetime, timedelta   

def get_tomorrow_date(self, days=1):
    today = datetime.now().date()
    return (today + timedelta(days=days)).strftime("%d.%m.%Y")