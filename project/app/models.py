from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinLengthValidator

numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')

class Marker(models.Model):
    cid = models.CharField(max_length=8, validators=[numeric, MinLengthValidator(8)], unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cid} [Marker]"

class CourseLead(models.Model):
    cid = models.CharField(max_length=8, validators=[numeric, MinLengthValidator(8)], unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cid} [CourseLead]"
    
class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    course_lead = models.ForeignKey(CourseLead, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
class FeedbackSpec(models.Model):
    TONES = (
        ('formal', 'Formal'),
        ('friendly', 'Friendly'),
    )

    tone = models.CharField(max_length=10, choices=TONES)
    length_min = models.PositiveIntegerField()
    lentgh_max = models.PositiveIntegerField()
    num_actionable_points = models.PositiveIntegerField()

    def __str__(self):
        return f"Feedback for {self.assignment}"
    
class Assignment(models.Model):
    MODERATION_ALGORITHMS = (
        ('linear', 'Linear'),
        ('z-score', 'Z-Score'),
    )
    
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    spec = models.TextField()
    rubric = models.TextField()
    feedback_spec = models.OneToOneField(FeedbackSpec, on_delete=models.CASCADE)
    moderation_algorithm = models.CharField(max_length=10, choices=MODERATION_ALGORITHMS)
    prompt = models.TextField()

    def __str__(self):
        return self.name

class AssignmentMarker(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('assignment', 'marker')

    def __str__(self):
        return f"{self.marker} assigned to mark {self.assignment}"
    
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student_cid = models.CharField(max_length=8, validators=[numeric, MinLengthValidator(8)])
    grade = models.FloatField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    moderated_grade = models.FloatField(null=True, blank=True)
    moderated_feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Submission by {self.student_id} for {self.assignment}"
    
class SubmissionMarking(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete=models.SET_NULL, null=True)
    marker_grade = models.FloatField(null=True, blank=True)
    marker_feedback = models.TextField(null=True, blank=True)
    llm_feedback = models.TextField(null=True, blank=True)
    approved_feedback = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('submission', 'marker')

    def __str__(self):
        return f"Marking by {self.marker} for {self.submission}"