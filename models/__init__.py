#!/usr/bin/python3

from .user import User
from .data import Data
from .device import Device
from .session import Session
from .settings import Settings
from .insight import Insight
from .prediction import Prediction
from .activity import Activity
from .goal import Goal
from .notification import Notification

# Create your models here.
# Exception classes


class ModelException(Exception):
    pass


class InvalidModelData(ModelException):
    pass


class ModelNotFound(ModelException):
    pass
# Model manager class


class ModelManager:
    def __init__(self):
        self.users = []
        self.devices = []
        self.data_points = []
        self.sessions = []
        self.settings = []
        self.insights = []
        self.predictions = []
        self.activities = []
        self.goals = []
        self.notifications = []

    def add_user(self, user: User):
        self.users.append(user)

    def add_device(self, device: Device):
        self.devices.append(device)

    def add_data_point(self, data_point: Data):
        self.data_points.append(data_point)

    def add_session(self, session: Session):
        self.sessions.append(session)

    def add_setting(self, setting: Settings):
        self.settings.append(setting)

    def add_insight(self, insight: Insight):
        self.insights.append(insight)

    def add_prediction(self, prediction: Prediction):
        self.predictions.append(prediction)

    def add_activity(self, activity: Activity):
        self.activities.append(activity)

    def add_goal(self, goal: Goal):
        self.goals.append(goal)

    def add_notification(self, notification: Notification):
        self.notifications.append(notification)

    def get_user(self, user_id: str):
        for user in self.users:
            if user.id == user_id:
                return user
        raise ModelNotFound(f'User with id {user_id} not found')

    def get_device(self, device_id: str):
        for device in self.devices:
            if device.id == device_id:
                return device
        raise ModelNotFound(f'Device with id {device_id} not found')
