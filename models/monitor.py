#!/usr/bin/python3

from datetime import datetime, timedelta


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    areas_of_expertise = models.ManyToManyField(AreaOfExpertise)
    availability = models.CharField(max_length=200)
    ratings = models.IntegerField(default=0)
    feedback = models.TextField()

    def __init__(self, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)

    def get_available_time_slots(self):
        current_time = datetime.now()
        available_time_slots = []


return available_time_slots


def is_available(self, time_slot):
    current_time = datetime.now()


return True or False


def book_session(self, time_slot, user):
    if self.is_available(time_slot):
        new_session = Session(user=user, start_time=time_slot,
                              end_time=time_slot
                              + timedelta(minutes=30)) new_session.save()
        return True
        else:
            return False


def cancel_session(self, time_slot):
    sessions_to_cancel = Session.objects.filter(
        start_time=time_slot, mentor=self.user)
    for session in sessions_to_cancel:
        session.delete()
    return True


def get_matching_mentees(self):
    matching_mentees = Mentee.objects.filter(
        areas_of_interest__in=self.areas_of_expertise,
        goals__in=self.get_matching_goals())
    return matching_mentees


def get_sessions_count(self):
    sessions = Session.objects.filter(mentor=self.user)
    return sessions.count()


def get_total_sessions_time(self):
    total_time = 0


sessions = Session.objects.filter(mentor=self.user)
for session in sessions:
    total_time += (session.end_time - session.start_time).total_seconds()
return total_time


def get_mentorship_duration(self, mentee):
    mentor_sessions = Session.objects.filter(mentor=self.user, mentee=mentee)
    if mentor_sessions.exists():
        first_session = mentor_sessions.order_by('start_time').first()
        last_session = mentor_sessions.order_by('-start_time').first()
        return (
            last_session.end_time -
            first_session.start_time).total_seconds()
    else:
        return 0


def update_ratings(self, user, rating):
    if user.is_authenticated and user == self.user:
        self.ratings += rating
        self.save()
    else:
        pass


def update_feedback(self, user, feedback):
    if user.is_authenticated:
        feedback_comment = FeedbackComment(
            user=user, feedback=feedback, mentor=self.user)
        feedback_comment.save()
    else:
        pass


def get_average_rating(self):
    if self.ratings_count > 0:
        return self.ratings / self.ratings_count
    else:
        return 0


def get_most_common_feedback(self):
    feedback_comments = FeedbackComment.objects.filter(mentor=self.user)
    feedback_counts = {}
    for comment in feedback_comments:
        feedback = comment.feedback
        if feedback in feedback_counts:
            feedback_counts[feedback] += 1


else:
    feedback_counts[feedback] = 1
most_common_feedback = max(feedback_counts, key=feedback_counts.get)
return most_common_feedback


def get_most_recent_feedback(self):
    feedback_comments = FeedbackComment.objects.filter(
        mentor=self.user).order_by('-created_at')
    if feedback_comments.exists():
        return feedback_comments.first().feedback
    else:
        return None


def __str__(self):
    return f'Mentor - {self.user.username}'
