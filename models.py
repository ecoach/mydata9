from django.db import models
from django.contrib.auth.models import User

# table format source data
from djangotailoring.models import SubjectData

# Create your models here.

# python ../manage.py makemtsmodel > MODEL.OUT (results go below here)

CTEXT_EMPLOYMENT_STATUS_CHOICES = (
    ('No_Job', 'I do not have a job'),
    ('Part_Time', 'I work a part-time job (20 hours or less a week)'),
    ('Full_Time', 'I work a full-time job (more than 20 hours a week)'),
)

INT_TO_LETTER_EXPECTED_GRADE_CHOICES = (
    ('5', 'C- or lower'),
    ('6', 'C'),
    ('7', 'C+'),
    ('8', 'B-'),
    ('9', 'B'),
    ('10', 'B+'),
    ('11', 'A-'),
    ('12', 'A'),
    ('13', 'A+'),
)

CTEXT_COLLEGE_CHOICES = (
    ('LSA', 'LSA'),
    ('Engineering', 'Engineering'),
    ('Kinesiology', 'Kinesiology'),
    ('Other', 'Other'),
)

CTEXT_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

INT_MLECTUREBOOK_CHOICES = (
    ('0', 'none'),
    ('1', 'hw'),
    ('2', 'both'),
)

CINT_SEMSESTERS_COMPLETED_CHOICES = (
    ('9', 'More than 8 semesters'),
)

CTEXT_COLLEGE_CONCENTRATE_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Physics', 'Physics/Astrophysics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Biology_MCDB', 'Biology MCDB'),
    ('Biology_EEB', 'Biology EEB'),
    ('Health', 'Health-related Field (Physical Therapy, Pharmacology, Nursing, etc.)'),
    ('Humanities', 'Humanities'),
    ('Math', 'Mathematics'),
    ('Neurosci', 'Neuroscience'),
    ('Social_Science_not_Psych', 'Social Science (excluding Psychology)'),
    ('Psych_BBCS', 'Psychology or BBCS'),
    ('Education', 'Education'),
    ('IDK', 'I do not know'),
    ('Other', 'Other'),
)

CTEXT_POST_COLLEGE_CHOICES = (
    ('Employment', 'Employment'),
    ('Med_School', 'Medical School or other Health-related Professional School'),
    ('Dent_School', 'Dental School'),
    ('Education', 'Education (teaching, policy, or a certification program)'),
    ('Grad_Life_Sci', 'Graduate School in a Life Science discipline'),
    ('Grad_Other', 'Graduate School in another discipline'),
    ('IDK', "Unsure/I don't know"),
    ('Other', 'Other'),
)

INT_YES_NO_CHOICES = (
    ('0', 'no'),
    ('1', 'yes'),
)

TEXT_OPT_OUT_CHOICES = (
    ('In', 'Yes, take me to the survey now!'),
    ('Out', "No thanks, I'll opt out and understand that if I use ecaoch it will only offer generic advice."),
)

INT_TRUE_FALSE_CHOICES = (
    ('1', 'True'),
    ('0', 'False'),
)

INT_CONFIDENCE_CHOICES = (
    ('1', 'very doubtful'),
    ('2', 'somewhat doubtful'),
    ('3', 'somewhat confident'),
    ('4', 'confident'),
    ('5', 'very confident'),
)

CINT_GPA_CHOICES = (
    ('20', '2.0 or lower'),
    ('21', '2.1'),
    ('22', '2.2'),
    ('23', '2.3'),
    ('24', '2.4'),
    ('25', '2.5'),
    ('26', '2.6'),
    ('27', '2.7'),
    ('28', '2.8'),
    ('29', '2.9'),
    ('30', '3.0'),
    ('31', '3.1'),
    ('32', '3.2'),
    ('33', '3.3'),
    ('34', '3.4'),
    ('35', '3.5'),
    ('36', '3.6'),
    ('37', '3.7'),
    ('38', '3.8'),
    ('39', '3.9'),
    ('40', '4.0'),
)

INT_MTEXTBOOK_CHOICES = (
    ('0', 'none'),
    ('1', 'book'),
    ('2', 'pack'),
)

INT_SUBJECT_INTEREST_CHOICES = (
    ('0', '0<br>Not at all interested'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10<br>Extremely interested'),
)

CTEXT_YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

CTEXT_INVOLVED_IN_CHOICES = (
    ('Greek', 'Greek Life (Sororities/Fraternities)'),
    ('Sports', 'Sports/Club Sports'),
    ('Religious', 'Religious Organizations'),
    ('Research', 'Research (Thesis, UROP, Lab work)'),
    ('Volunteering', 'Volunteering'),
    ('Music_Art', 'Music/Art'),
    ('Other', 'Other Student Clubs/Organzations'),
)

INT_MYELLOW_CHOICES = (
    ('0', 'none'),
    ('1', 'printed'),
    ('2', 'card'),
)

CTEXT_CLASS_STANDING_CHOICES = (
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
)

INT_CONFIDENCE_IN_ABLILITY_CHOICES = (
    ('0', '0<br>Not at all confident'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10<br>Extremely confident'),
)

TEXT_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

INT_SEMESTER_FREQ_CHOICES = (
    ('0', 'never'),
    ('1', 'once or twice during the semester'),
    ('2', 'monthly'),
    ('3', 'weekly'),
    ('4', 'multiple times per week'),
)

INT_TO_LETTER_GOAL_GRADE_CHOICES = (
    ('5', 'C- or lower'),
    ('6', 'C'),
    ('7', 'C+'),
    ('8', 'B-'),
    ('9', 'B'),
    ('10', 'B+'),
    ('11', 'A-'),
    ('12', 'A'),
    ('13', 'A+'),
)

CINT_BDAY_MONTH_CHOICES = (
    ('-1', 'Month'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

CTEXT_PARENT_ED_CHOICES = (
    ('Less_HS', 'Less than High School'),
    ('HS', 'High School/GED'),
    ('Some_College', 'Some College'),
    ('2_Year_College', '2-Year College Degree (Associates)'),
    ('4_Year_College', '4-Year College Degree (BA, BS)'),
    ('Masters', "Master's Degree"),
    ('Doctoral', 'Doctoral Degree'),
    ('Professional', 'Professional Degree (MD, JD)'),
)


class Source1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_source1'
    hw_hours = models.FloatField(null=True, blank=True)
    oh_expected = models.IntegerField(null=True, blank=True)
    study_partner = models.IntegerField(null=True, blank=True)
    Subject_Interest = models.IntegerField(null=True, blank=True)
    time_expectation = models.IntegerField(null=True, blank=True)
    Confidence = models.IntegerField(null=True, blank=True)
    confidence_grade = models.IntegerField(null=True, blank=True)
    GTD_01 = models.IntegerField(null=True, blank=True)
    GTD_02 = models.IntegerField(null=True, blank=True)
    GTD_03 = models.IntegerField(null=True, blank=True)
    GTD_04 = models.IntegerField(null=True, blank=True)
    GTD_05 = models.IntegerField(null=True, blank=True)
    GTD_06 = models.IntegerField(null=True, blank=True)
    GTD_07 = models.IntegerField(null=True, blank=True)
    GTD_08 = models.IntegerField(null=True, blank=True)
    GTD_09 = models.IntegerField(null=True, blank=True)
    GTD_11 = models.IntegerField(null=True, blank=True)
    GTD_10 = models.IntegerField(null=True, blank=True)
    GTD_12 = models.IntegerField(null=True, blank=True)
    GTD_13 = models.IntegerField(null=True, blank=True)
    GTD_14 = models.IntegerField(null=True, blank=True)
    GTD_15 = models.IntegerField(null=True, blank=True)
    gb_hw_practice = models.FloatField(null=True, blank=True)
    gb_hw01 = models.FloatField(null=True, blank=True)
    gb_hw02 = models.FloatField(null=True, blank=True)
    gb_hw03 = models.FloatField(null=True, blank=True)
    gb_hw04 = models.FloatField(null=True, blank=True)
    gb_hw05 = models.FloatField(null=True, blank=True)
    gb_hw06 = models.FloatField(null=True, blank=True)
    gb_hw07 = models.FloatField(null=True, blank=True)
    gb_hw08 = models.FloatField(null=True, blank=True)
    gb_hw09 = models.FloatField(null=True, blank=True)
    gb_hw10 = models.FloatField(null=True, blank=True)
    gb_hw11 = models.FloatField(null=True, blank=True)
    gb_hw_extra = models.FloatField(null=True, blank=True)
    gb_exam1 = models.FloatField(null=True, blank=True)
    gb_exam2 = models.FloatField(null=True, blank=True)
    gb_final = models.FloatField(null=True, blank=True)
    gb_lab00_attend = models.IntegerField(null=True, blank=True)
    gb_lab01_attend = models.IntegerField(null=True, blank=True)
    gb_lab02_attend = models.IntegerField(null=True, blank=True)
    gb_lab03_attend = models.IntegerField(null=True, blank=True)
    gb_lab04_attend = models.IntegerField(null=True, blank=True)
    gb_lab05_attend = models.IntegerField(null=True, blank=True)
    gb_lab06_attend = models.IntegerField(null=True, blank=True)
    gb_lab07_attend = models.IntegerField(null=True, blank=True)
    gb_lab08_attend = models.IntegerField(null=True, blank=True)
    gb_lab09_attend = models.IntegerField(null=True, blank=True)
    gb_lab10_attend = models.IntegerField(null=True, blank=True)
    gb_lab11_attend = models.IntegerField(null=True, blank=True)
    gb_lab12_attend = models.IntegerField(null=True, blank=True)
    gb_lab13_attend = models.IntegerField(null=True, blank=True)
    gb_prelab01 = models.IntegerField(null=True, blank=True)
    gb_prelab02 = models.IntegerField(null=True, blank=True)
    gb_prelab03 = models.IntegerField(null=True, blank=True)
    gb_prelab04 = models.IntegerField(null=True, blank=True)
    gb_prelab05 = models.IntegerField(null=True, blank=True)
    gb_prelab06 = models.IntegerField(null=True, blank=True)
    gb_prelab07 = models.IntegerField(null=True, blank=True)
    gb_prelab08 = models.IntegerField(null=True, blank=True)
    gb_prelab09 = models.IntegerField(null=True, blank=True)
    gb_prelab10 = models.IntegerField(null=True, blank=True)
    gb_prelab11 = models.IntegerField(null=True, blank=True)
    gb_prelab12 = models.IntegerField(null=True, blank=True)
    GSI_Name = models.CharField(max_length=20, null=True, blank=True)
    dist_values = models.CharField(max_length=20, null=True, blank=True)
    Goal_Grade = models.IntegerField(null=True, blank=True)
    Expected_Grade = models.IntegerField(null=True, blank=True)
    mcalculator = models.IntegerField(null=True, blank=True)
    mamazonlecture = models.IntegerField(null=True, blank=True)
    mlecturebook = models.IntegerField(null=True, blank=True)
    mamazonlab = models.IntegerField(null=True, blank=True)
    mopenmi = models.IntegerField(null=True, blank=True)
    mopenmilab = models.IntegerField(null=True, blank=True)
    mtextbook = models.IntegerField(null=True, blank=True)
    myellow = models.IntegerField(null=True, blank=True)

class EmptySource(SubjectData):
    pass

class Common1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_common1'
    First_Name = models.CharField(max_length=20, null=True, blank=True)
    Last_Name = models.CharField(max_length=20, null=True, blank=True)
    uniqname = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=CTEXT_GENDER_CHOICES, null=True, blank=True)
    BirthDay = models.IntegerField(null=True, blank=True)
    BirthMo = models.IntegerField(null=True, blank=True)
    BirthYr = models.IntegerField(null=True, blank=True)
    Semesters_Completed = models.IntegerField(null=True, blank=True)
    College = models.CharField(max_length=11, choices=CTEXT_COLLEGE_CHOICES, null=True, blank=True)
    College_Other = models.CharField(max_length=30, null=True, blank=True)
    Concentrate__Engineering = models.NullBooleanField()
    Concentrate__Physics = models.NullBooleanField()
    Concentrate__Chemistry = models.NullBooleanField()
    Concentrate__Biology = models.NullBooleanField()
    Concentrate__Biology_MCDB = models.NullBooleanField()
    Concentrate__Biology_EEB = models.NullBooleanField()
    Concentrate__Health = models.NullBooleanField()
    Concentrate__Humanities = models.NullBooleanField()
    Concentrate__Math = models.NullBooleanField()
    Concentrate__Neurosci = models.NullBooleanField()
    Concentrate__Social_Science_not_Psych = models.NullBooleanField()
    Concentrate__Psych_BBCS = models.NullBooleanField()
    Concentrate__Education = models.NullBooleanField()
    Concentrate__IDK = models.NullBooleanField()
    Concentrate__Other = models.NullBooleanField()
    Concentrate_Other = models.CharField(max_length=30, null=True, blank=True)
    Declared = models.CharField(max_length=3, choices=CTEXT_YES_NO_CHOICES, null=True, blank=True)
    Class_Standing = models.CharField(max_length=9, choices=CTEXT_CLASS_STANDING_CHOICES, null=True, blank=True)
    Cum_GPA_Survey = models.IntegerField(null=True, blank=True)
    Employment = models.CharField(max_length=9, choices=CTEXT_EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    Involved_In__Greek = models.NullBooleanField()
    Involved_In__Sports = models.NullBooleanField()
    Involved_In__Religious = models.NullBooleanField()
    Involved_In__Research = models.NullBooleanField()
    Involved_In__Volunteering = models.NullBooleanField()
    Involved_In__Music_Art = models.NullBooleanField()
    Involved_In__Other = models.NullBooleanField()
    Other_Commitment = models.CharField(max_length=30, null=True, blank=True)
    Post_College = models.CharField(max_length=13, choices=CTEXT_POST_COLLEGE_CHOICES, null=True, blank=True)
    Parent_Ed = models.CharField(max_length=14, choices=CTEXT_PARENT_ED_CHOICES, null=True, blank=True)
    High_School_CumGPA = models.IntegerField(null=True, blank=True)


