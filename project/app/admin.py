from django.contrib import admin
from app.models import Marker, CourseLead, Course, FeedbackSpec, Assignment, AssignmentMarker, Submission, SubmissionMarking

admin.site.register(Marker)
admin.site.register(CourseLead)
admin.site.register(Course)
admin.site.register(FeedbackSpec)
admin.site.register(Assignment)
admin.site.register(AssignmentMarker)
admin.site.register(Submission)
admin.site.register(SubmissionMarking)