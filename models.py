from django.db import models
from django.contrib.auth.models import User

# table format source data
from djangotailoring.models import SubjectData

# Create your models here.

# python ../manage.py makemtsmodel > MODEL.OUT (results go below here)

INT_GRADE_NUMBER_CHOICES = (
    ('8', 'A (4.0)'),
    ('7', 'A- (3.7)'),
    ('6', 'B+ (3.3)'),
    ('5', 'B (3.0)'),
    ('4', 'B- (2.7)'),
    ('3', 'C+ (2.3)'),
    ('2', 'C (2.0)'),
    ('1', 'C - or lower (< 2.7)'),
)

INT_AGREE_DISAGREE_CHOICES = (
    ('0', 'Agree'),
    ('1', 'Disagree'),
)

TEXT_OPT_OUT_CHOICES = (
    ('In', 'Yes, take me to the survey now!'),
    ('Out', "No thanks, I'll opt out and understand that if I use ecaoch it will only offer generic advice."),
)

INT_TRUE_FALSE_CHOICES = (
    ('1', 'True'),
    ('0', 'False'),
)

INT_HOURS_STUDY_CHOICES = (
    ('0', 'Less than 1 hour'),
    ('1', '1 hour'),
    ('2', '2 hours'),
    ('3', '3 hours'),
    ('4', '4 hours'),
    ('5', '5 hours'),
    ('6', '6 hours'),
    ('7', '7 hours'),
    ('8', '8 hours'),
    ('9', '9 hours'),
    ('10', '10 hours'),
    ('11', '11 hours or more'),
)

TEXT_REASON_CLASS_CHOICES = (
    ('Physics_req', 'I am considering physics as my concentration'),
    ('Concentration_req', 'This is the physics course required by my concentration'),
    ('Grad_req', 'I need to take physics to prepare for my graduate/professional program'),
    ('NS_Credit', 'For Natural Science credit'),
    ('Interest', "I'm taking this class because of my interest in physics"),
)

TEXT_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

TEXT_COURSE_CHOICES = (
    ('135', 'Physics 135'),
    ('235', 'Physics 235'),
    ('140', 'Physics 140'),
    ('240', 'Physics 240'),
)


class Source1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'source1'
    Name_First = models.CharField(max_length=10, null=True, blank=True)
    Opt_Out = models.CharField(max_length=3, choices=TEXT_OPT_OUT_CHOICES, null=True, blank=True)
    Enrolled = models.IntegerField(null=True, blank=True)
    GB_Participation_1 = models.FloatField(null=True, blank=True)
    GB_Participation_3 = models.FloatField(null=True, blank=True)
    GB_Participation_F = models.FloatField(null=True, blank=True)
    GB_Homework_1 = models.FloatField(null=True, blank=True)
    GB_Homework_F = models.FloatField(null=True, blank=True)
    GB_Homework_3 = models.FloatField(null=True, blank=True)
    MP_Name = models.CharField(max_length=20, null=True, blank=True)
    MP_Name_correct = models.CharField(max_length=1, choices=INT_TRUE_FALSE_CHOICES, null=True, blank=True)
    Name_Last = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=TEXT_GENDER_CHOICES, null=True, blank=True)
    Reg_Gender = models.CharField(max_length=20, null=True, blank=True)
    Reg_Semesters_Completed = models.IntegerField(null=True, blank=True)
    Course = models.IntegerField(null=True, blank=True)
    Reg_Course = models.IntegerField(null=True, blank=True)
    GB_Homework_2 = models.FloatField(null=True, blank=True)
    Reason_Logic__Physics_req = models.NullBooleanField()
    Reason_Logic__Concentration_req = models.NullBooleanField()
    Reason_Logic__Grad_req = models.NullBooleanField()
    Reason_Logic__NS_Credit = models.NullBooleanField()
    Reason_Logic__Interest = models.NullBooleanField()
    Reason_Motivation = models.CharField(max_length=20, null=True, blank=True)
    GB_Exam_Score_1 = models.FloatField(null=True, blank=True)
    GB_Exam_Score_3 = models.FloatField(null=True, blank=True)
    GB_Exam_Score_F = models.FloatField(null=True, blank=True)
    GB_Exam_Score_2 = models.FloatField(null=True, blank=True)
    Final_Grade = models.CharField(max_length=5, null=True, blank=True)
    GB_Participation_2 = models.FloatField(null=True, blank=True)
    Usage_Weeks_Visited = models.IntegerField(null=True, blank=True)
    Usage_Messages_Viewed = models.IntegerField(null=True, blank=True)
    Usage_Sum_Clicks = models.IntegerField(null=True, blank=True)
    Reg_GPA = models.FloatField(null=True, blank=True)

class EmptySource(SubjectData):
    pass


