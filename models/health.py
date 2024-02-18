#!/usr/bin/python3

from models import HealthData
from authentication import get_current_user

# Save health data for current user
def save_health_data(data):
    user = get_current_user()
    health_data = HealthData(user=user, **data)
    health_data.save()

# Get health data for current user
def get_health_data():
    user = get_current_user()
    health_data = HealthData.objects(user=user)
    return health_data
