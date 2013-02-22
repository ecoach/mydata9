from django.db import models
from django.contrib.auth.models import User

# table format source data
from djangotailoring.models import SubjectData

# Create your models here.

# python ../manage.py makemtsmodel > MODEL.OUT (results go below here)

_SAT_MATH_CHOICES = (
    ('0', 'I did not take the SAT'),
    ('-99', 'I do not remember my SAT math score'),
    ('400', '400 or below'),
    ('410', '410'),
    ('420', '420'),
    ('430', '430'),
    ('440', '440'),
    ('450', '450'),
    ('460', '460'),
    ('470', '470'),
    ('480', '480'),
    ('490', '490'),
    ('500', '500'),
    ('510', '510'),
    ('520', '520'),
    ('530', '530'),
    ('540', '540'),
    ('550', '550'),
    ('560', '560'),
    ('570', '570'),
    ('580', '580'),
    ('590', '590'),
    ('600', '600'),
    ('610', '610'),
    ('620', '620'),
    ('630', '630'),
    ('640', '640'),
    ('650', '650'),
    ('660', '660'),
    ('670', '670'),
    ('680', '680'),
    ('690', '690'),
    ('700', '700'),
    ('710', '710'),
    ('720', '720'),
    ('730', '730'),
    ('740', '740'),
    ('750', '750'),
    ('760', '760'),
    ('770', '770'),
    ('780', '780'),
    ('790', '790'),
    ('800', '800'),
)

_HS_MATH_CHOICES = (
    ('Algebra', 'Algebra'),
    ('Geometry', 'Geometry'),
    ('Precalc_Analysis', 'Precalc/Analysis'),
    ('Non_AP_Calc', 'Non-AP Calclus'),
    ('AP_Calc_AB', 'AP Calculus AB'),
    ('AP_Calc_BC', 'AP Calculus BC'),
    ('equiv_115', 'The equivalent of Math 115 (Calc 1) at a College/University'),
    ('equiv_116', 'The equivalent of Math 116 (Calc 2) at a College/University'),
    ('equiv_215', 'The equivalent of Math 215 (Calc 3: Multivariable Calculus) at a College/University'),
    ('equiv_216', 'The equivalent of Math 216 (Calc 4: Differential Equations) at a College/University'),
    ('Other', 'Other'),
)

_ACT_MATH_CHOICES = (
    ('0', 'I did not take the ACT'),
    ('-99', 'I do not remember my ACT math score'),
    ('15', '15 or below'),
)

_TESTIMONIAL_NAME_2_CHOICES = (
    ('Elaine_Otchere', 'Elaine_Otchere'),
    ('Fabien_Meta', 'Fabien_Meta'),
    ('Blythe_Moreland', 'Blythe_Moreland'),
    ('Christopher_McMullen', 'Christopher_McMullen'),
    ('Katelyn_Videto', 'Katelyn_Videto'),
    ('Timothy_Curran', 'Timothy_Curran'),
    ('Gabrielle_Strzalkowski', 'Gabrielle_Strzalkowski'),
    ('Jordan_Gavin', 'Jordan_Gavin'),
)

_VALUES_AFF_SELECT_CHOICES = (
    ('Art', 'Being good at art'),
    ('Creativity', 'Creativity'),
    ('Relationships', 'Relationships with family and friends'),
    ('Government', 'Government or politics'),
    ('Independence', 'Independence'),
    ('Learning', 'Learning and gaining knowledge'),
    ('Athletic', 'Athletic ability'),
    ('Social', 'Belong to a social group (such as your community, religious group, or school club)'),
    ('Music', 'Music'),
    ('Career', 'Career'),
    ('Spiritual', 'Spiritual or religious values'),
    ('Humor', 'Sense of humor'),
)

_SLC__CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

_COLLEGE_CHEM_CHOICES = (
    ('AP_Test_Out', 'Received AP Credit/Tested Out'),
    ('125_126_130', 'Chemistry 125/126 and 130'),
    ('210_211', 'Chemistry 210 and 211'),
    ('215_216', 'Chemistry 215 and 216'),
    ('230', 'Chemistry 230'),
    ('241_242', 'Chemistry 241/242'),
    ('245_246_247', 'Chemistry 245 and 246/247'),
    ('260_261', 'Chemistry 260/261'),
    ('Higher', 'Higher Level'),
    ('Current', "I'm currently enrolled in one (or more) of the above options"),
    ('Other', 'Other'),
    ('None', "I haven't taken Chemistry (yet)"),
)

_HELPROOM_CHOICES = (
    ('Never', 'Never'),
    ('3_semester', 'Less than 3 times a semester'),
    ('2_week', 'Once every two weeks'),
    ('1_week', 'Once a week'),
    ('More_1_week', 'More than once a week'),
    ('IDK', "What's the physics help room?"),
)

_INVOLVED_I_CHOICES = (
    ('Greek', 'Greek Life (Sororities/Fraternities)'),
    ('Sports', 'Sports/Club Sports'),
    ('Religious', 'Religious Organizations'),
    ('Research', 'Research (Thesis, UROP, Lab work)'),
    ('Volunteering', 'Volunteering'),
    ('Music_Art', 'Music/Art'),
    ('Other', 'Other Student Clubs/Organzations'),
)

_PARTNER_EXAM_1_RESPONSE_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

_GPA_NUMBER_CHOICES = (
    ('8', '8'),
    ('7', '7'),
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
    ('0', '0'),
)

_SHE_HE_CHOICES = (
    ('she', 'she'),
    ('he', 'he'),
)

_SEMESTERS_COMPLETED_CHOICES = (
    ('7', 'More than 6 semesters'),
)

_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

_VOTE_PLOT_SELEC_CHOICES = (
    ('Plot_1', 'The histograms (light and dark bars)'),
    ('Plot_2', 'The colored charts (blue and red boxes)'),
)

_ENGINEERING_FIELD_CHOICES = (
    ('AERO', 'Aerospace Engineering (AERO)'),
    ('BME', 'Biomedical Engineering (BME)'),
    ('ChE', 'Chemical Engineering (ChE)'),
    ('CEE', 'Civil and Environmental Engineering (CEE)'),
    ('EECS', 'Electric Engineering and Computer Science (EECS)'),
    ('AOSS', 'Atmospheric, Oceanic, and Space Sciences (AOSS)'),
    ('NERS', 'Nuclear Engineering and Radiology Sciences (NERS)'),
    ('IOE', 'Industrial and Operations Engineering (IOE)'),
    ('MSE', 'Material Science and Engineering (MSE)'),
    ('ME', 'Mechanical Engineering (ME)'),
    ('NAME', 'Naval Architecture and Marine Engineering (NAME)'),
)

GRADE_PREDICTED_CHOICES = (
    ('8', '8'),
    ('7', '7'),
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

_COLLEGE_MATH_CHOICES = (
    ('Math_115', 'Math 115'),
    ('115_AP', 'AP Credit for Math 115'),
    ('115_Else', 'The equivalent of Math 115 at another College/University'),
    ('116', 'Math 116'),
    ('116_AP', 'AP Credit for Math 116'),
    ('116_Else', 'The equivalent of Math 116 at another College/University'),
    ('156', 'Math 156'),
    ('185', 'Math 185'),
    ('186', 'Math 186'),
    ('214', 'Math 214'),
    ('215', 'Math 215'),
    ('216', 'Math 216'),
    ('217', 'Math 217'),
    ('Stats_250', 'Statistics 250'),
    ('255', 'Math 255'),
    ('285', 'Math 285'),
    ('286', 'Math 286'),
    ('289', 'Math 289'),
    ('295', 'Math 295'),
    ('296', 'Math 296'),
    ('Higher', 'Higher Level'),
    ('Current', "I'm currently enrolled in one (or more) of the above options"),
    ('Other', 'Other'),
    ('None', "I haven't taken Math (yet)"),
)

_COURSE_CHOICES = (
    ('135', 'Physics 135'),
    ('235', 'Physics 235'),
    ('140', 'Physics 140'),
    ('240', 'Physics 240'),
)

_CONCENTRATE_CHOICES = (
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

_TESTIMONIAL_NAME_3_CHOICES = (
    ('Valeri_Zeer', 'Valeri_Zeer'),
    ('Emily_French', 'Emily_French'),
    ('Sheri_VanOmen', 'Sheri_VanOmen'),
    ('Fabien_Meta', 'Fabien_Meta'),
    ('David_Noble', 'David_Noble'),
    ('Christopher_McMullen', 'Christopher_McMullen'),
    ('Angie_Zhang', 'Angie_Zhang'),
    ('Timothy_Audiss', 'Timothy_Audiss'),
    ('Timothy_Curran', 'Timothy_Curran'),
    ('Gabrielle_Strzalkowski', 'Gabrielle_Strzalkowski'),
    ('Jordan_Gavin', 'Jordan_Gavin'),
    ('Bryan_Fiema', 'Bryan_Fiema'),
    ('Blythe_Moreland', 'Blythe_Moreland'),
    ('Katelyn_Videto', 'Katelyn_Videto'),
)

_POST_COLLEGE_CHOICES = (
    ('Employment', 'Employment'),
    ('Med_School', 'Medical School or other Health-related Professional School'),
    ('Dent_School', 'Dental School'),
    ('Education', 'Education (teaching, policy, or a certiciation program)'),
    ('Grad_Life_Sci', 'Graduate School in a Life Science discipline'),
    ('Grad_Other', 'Graduate School in another discipline'),
    ('IDK', "Unsure/I don't know"),
    ('Other', 'Other'),
)

_GRADE_WANT_NUMBER_CHOICES = (
    ('7', '7'),
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

_GRADE_EXPECTED_STUDENT_NUMBER_CHOICES = (
    ('7', '7'),
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

_FIRST_GEN_CHOICES = (
    ('Y', 'Y'),
    ('N', 'N'),
)

_CHANGE_EXAM_1_RESPONSE_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

AGREE_DISAGREE_CHOICES = (
    ('Strongly_Disagree', 'Strongly Disagree'),
    ('Disagree', 'Disagree'),
    ('Neither', 'Neither Agree nor Disagree'),
    ('Agree', 'Agree'),
    ('Strongly_Agree', 'Strongly Agree'),
)

_COENROLL_CHOICES = (
    ('Math_116', 'Math 116'),
    ('Math_215', 'Math 215'),
    ('Math_216', 'Math 216'),
    ('Stats_250', 'Statistics 250'),
    ('Chem_210', 'Chemistry 210'),
    ('Chem_211', 'Chemistry 211'),
    ('Chem_215', 'Chemistry 215'),
    ('Chem_216', 'Chemistry 216'),
    ('Chem_230', 'Chemistry 230'),
    ('Psych_111', 'Psychology 111'),
    ('Bio_172', 'Biology 172'),
    ('Bio_173', 'Biology 173'),
    ('Bio_225', 'Biology 225'),
    ('Bio_305', 'Biology 305'),
    ('Eng_100', 'Engineering 100'),
    ('Eng_101', 'Engineering 101'),
    ('Eng_110', 'Engineering 110'),
    ('MechEng_211', 'Mechanical Engineering 211'),
    ('AeroEng_201', 'Aerospace Engineering 201'),
    ('EECS_215', 'EECS 215'),
    ('EECS_280', 'EECS 280'),
    ('None', 'I am not currently enrolled in any of these courses'),
)

_HS_PHYSICS_CHOICES = (
    ('AP', 'AP Physics'),
    ('non_AP', 'non-AP Physics'),
    ('No', "I didn't take a physics class in high school"),
)

_CONTINUATION_CHOICES = (
    ('235', 'Physics 235 at U of M'),
    ('240', 'Physics 240 at U of M'),
    ('260', 'Physics 260 at U of M'),
    ('cc', 'Second semester physics at a community college'),
    ('four_year_other', 'Second semester physics at another four-year college'),
    ('not_taking', 'Not taking second semester physics'),
    ('other', 'Other'),
)

BTE_AE_WTE_CHOICES = (
    ('BTE', 'BTE'),
    ('AE', 'AE'),
    ('WTE', 'WTE'),
)

_CUM_GPA_CHOICES = (
    ('2', '2.0 or lower'),
)

_CUM_GPA_SURVEY_CHOICES = (
    ('2_0', '2.0 or lower'),
    ('2_1', '2.1'),
    ('2_2', '2.2'),
    ('2_3', '2.3'),
    ('2_4', '2.4'),
    ('2_5', '2.5'),
    ('2_6', '2.6'),
    ('2_7', '2.7'),
    ('2_8', '2.8'),
    ('2_9', '2.9'),
    ('3_0', '3.0'),
    ('3_1', '3.1'),
    ('3_2', '3.2'),
    ('3_3', '3.3'),
    ('3_4', '3.4'),
    ('3_5', '3.5'),
    ('3_6', '3.6'),
    ('3_7', '3.7'),
    ('3_8', '3.8'),
    ('3_9', '3.9'),
    ('4_0', '4.0'),
)

AP_SCORE_CHOICES = (
    ('-99', "I don't remember"),
)

FREQ_MEETING_CHOICES = (
    ('Several', 'Several times per meeting'),
    ('One', 'Once per meeting'),
    ('Few', 'Once every few meetings'),
    ('Rarely', 'Rarely'),
    ('Never', 'Never'),
)

HOURS_CHOICES = (
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
    ('11', '11 hours'),
    ('12', '12 hours'),
    ('13', '13 hours'),
    ('14', '14 hours'),
    ('15', '15 hours'),
    ('16', '16 hours or more'),
)

_EMPLOYMENT_CHOICES = (
    ('No_Job', 'I do not have a job'),
    ('Part_Time', 'I work a part-time job (20 hours or less a week)'),
    ('Full_Time', 'I work a full-time job (more than 20 hours a week)'),
)

_PARENT_ED_CHOICES = (
    ('Less_HS', 'Less than High School'),
    ('HS', 'High School/GED'),
    ('Some_College', 'Some College'),
    ('2_Year_College', '2-Year College Degree (Associates)'),
    ('4_Year_College', '4-Year College Degree (BA, BS)'),
    ('Masters', "Master's Degree"),
    ('Doctoral', 'Doctoral Degree'),
    ('Professional', 'Professional Degree (MD, JD)'),
)

_AP_EXAM_CHOICES = (
    ('AP_B', 'Yes, I took the AP Physics B exam'),
    ('AP_C_Mech', 'Yes, I took the AP Physics C (Mechanics) exam'),
    ('AP_C_EM', 'Yes, I took the AP Physics C (E&M) exam'),
    ('IDK', "Yes, but I'm not sure which exam I took"),
    ('No', 'No, I did not take an AP Physics exam'),
)

FREQUENCY_CHOICES = (
    ('Never', 'Never'),
    ('3_semester', 'Less than 3 times a semester'),
    ('2_week', 'Once every two weeks'),
    ('1_week', 'Once a week'),
    ('More_1_week', 'More than once a week'),
)

_MINOR_OR_MAJOR_CHOICES = (
    ('minor', "Yes, I'm interested in pursuing a physics minor"),
    ('major', "Yes, I'm interested in pursuing a physics major"),
    ('not_interested', "No, I'm not interested in either a physics minor or major"),
)

_CONFIDENCE_CHOICES = (
    ('Not_confident_at_all', 'Not confident<br>at all'),
    ('Not_confident', 'Not confident'),
    ('Somewhat_confident', 'Somewhat<br>confident'),
    ('Confident', 'Confident'),
    ('Very_confident', 'Very confident'),
)

_REASON_CHOICES = (
    ('Physics_req', 'I am considering Physics as my concentration'),
    ('Concentration_req', 'This is the physics course required by my concentration'),
    ('Grad_req', 'I need to take physics to prepare for my graduate/professional program'),
    ('NS_Credit', 'For Natural Science credit'),
    ('Interest', "I'm taking this class because of my interest in Physics"),
)

NUMBER_GRADES_CHOICES = (
    ('8', '8'),
    ('7', '7'),
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

_ECOACH_CHANGE_BEHAVIOR_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_SLC_INTEREST_CHOICES = (
    ('Signed_Up', "Yes, I'm already signed up!"),
    ('Yes_Not_Signed_Up', 'Yes, but I have not signed up yet'),
    ('Not_Interested', "No, I'm not interested"),
    ('IDK', "What's the Science Learning Center?"),
)

_FINAL_GRADE_HAPPY_CHOICES = (
    ('Yes', 'Yes'),
    ('Kind_of', 'Kind of'),
    ('No', 'No'),
)

_GRADE_WANT_CHOICES = (
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C_or_below', 'C or below'),
)

_ECOACH_ARCHIVE_HELPFUL_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_PARTNER_EXAM_1_RESPONSE_DERIVE_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

_CSP_CHOICES = (
    ('Signed_Up', "Yes, I'm already signed up!"),
    ('Interested', 'Yes, tell me how to join'),
    ('Not_Interested', 'No, I am not interested'),
    ('IDK', 'What is CSP?'),
)

_GRADE_EXPECTED_STUDENT_CHOICES = (
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C_or_below', 'C or below'),
)

_HER_HIS_CHOICES = (
    ('her', 'her'),
    ('his', 'his'),
)

SUMMARY_RESPONSES_CHOICES = (
    ('Full_Response', 'Full_Response'),
    ('Partial_Response', 'Partial_Response'),
    ('No_Response', 'No_Response'),
)

GRADES_CHOICES = (
    ('A_plus', 'A+'),
    ('A', 'A'),
    ('A_minus', 'A-'),
    ('B_plus', 'B+'),
    ('B', 'B'),
    ('B_minus', 'B-'),
    ('C_plus', 'C+'),
    ('C_or_below', 'C or below'),
)

_COLLEGE_BIO_CHOICES = (
    ('AP_Test_Out', 'Received AP Credit/Tested Out'),
    ('171', 'Biology 171'),
    ('172', 'Biology 172'),
    ('173', 'Biology 173'),
    ('205', 'Biology 205'),
    ('222', 'Biology 222'),
    ('225_226', 'Biology 225 and 226'),
    ('305', 'Biology 305'),
    ('Higher', 'Higher Level'),
    ('Current', "I'm currently enrolled in one (or more) of the above options"),
    ('Other', 'Other'),
    ('None', "I haven't taken Biology (yet)"),
)

_CONFIDENCE_AFTER_CHOICES = (
    ('not_at_all', 'Not confident at all'),
    ('not', 'Not confident'),
    ('somewhat', 'Somewhat confident'),
    ('confident', 'Confident'),
    ('very_confident', 'Very confident'),
    ('not_taking', 'Not planning on taking second semester physics'),
)

_TESTIMONIAL_NAME_1_CHOICES = (
    ('Tiara_Forsyth', 'Tiara_Forsyth'),
    ('David_Noble', 'David_Noble'),
    ('Blythe_Moreland', 'Blythe_Moreland'),
    ('Christopher_McMullen', 'Christopher_McMullen'),
    ('Angie_Zhang', 'Angie_Zhang'),
    ('Timothy_Curran', 'Timothy_Curran'),
    ('Gabrielle_Strzalkowski', 'Gabrielle_Strzalkowski'),
    ('Bryan_Fiema', 'Bryan_Fiema'),
)

HOURS_EXAM_STUDY_CHOICES = (
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

_CHANGE_EXAM_2_RESPONSE_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_SUGGEST_SLC_CHOICES = (
    ('Suggest', 'Suggest'),
    ('No_Suggest', 'No_Suggest'),
)

_PARTNER_CHOICES = (
    ('Perfect_Partner', 'Yes, I have a perfect study partner'),
    ('Know_Like_To', "I know someone and I'd like to study with them"),
    ('Know_Alone', "I know someone, but I'd like to study alone"),
    ('No', "No, I don't know anyone in this course"),
)

IMPROVE_SAME_DECLINE_CHOICES = (
    ('Improve', 'Improve'),
    ('Same', 'Same'),
    ('Decline', 'Decline'),
)

YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_ECOACH_ARCHIVE_HELPFUL_STUDENTS_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

_COLLEGE_CHOICES = (
    ('LSA', 'LSA'),
    ('Engineering', 'Engineering'),
    ('Kinesiology', 'Kinesiology'),
    ('Other', 'Other'),
)


class EmptySourceData(SubjectData):
    pass

class S_12Data(SubjectData):
    #uid = models.ForeignKey(User, to_field='username', db_column='user_id', blank=True, null=True)  
    First_Name = models.CharField(max_length=20, null=True, blank=True)
    UMID = models.IntegerField(null=True, blank=True)
    uniq_name = models.CharField(max_length=20, null=True, blank=True)
    Participation_Exam_1_Response = models.FloatField(null=True, blank=True)
    Exam_4_Score = models.FloatField(null=True, blank=True)
    Exam_5_Score = models.FloatField(null=True, blank=True)
    Exam_6_Score = models.FloatField(null=True, blank=True)
    Participation_Exam_3_Response = models.FloatField(null=True, blank=True)
    Participation_Exam_Final_Response = models.FloatField(null=True, blank=True)
    MP_Exam_1_Response = models.FloatField(null=True, blank=True)
    MP_Exam_Final_Response = models.FloatField(null=True, blank=True)
    MP_Exam_3_Response = models.FloatField(null=True, blank=True)
    SLC = models.CharField(max_length=1, choices=_SLC__CHOICES, null=True, blank=True)
    Change_Exam_1_Response = models.CharField(max_length=3, choices=_CHANGE_EXAM_1_RESPONSE_CHOICES, null=True, blank=True)
    #Change_Explain_Exam_1_Response = models.TextField()
    Change_Explain_Exam_1_Response = models.TextField()
    #Work_Exam_1_Response = models.TextField()
    Work_Exam_1_Response = models.TextField()
    #Didnt_Work_Exam_1_Response = models.TextField()
    Didnt_Work_Exam_1_Response = models.TextField()
    #Future_Exam_1_Response = models.TextField()
    Future_Exam_1_Response = models.TextField()
    SLC_Discuss_Exam_1_Response = models.CharField(max_length=7, choices=FREQ_MEETING_CHOICES, null=True, blank=True)
    SLC_Question_Exam_1_Response = models.CharField(max_length=7, choices=FREQ_MEETING_CHOICES, null=True, blank=True)
    #Values_Aff_Response_Exam_1_Prep = models.TextField()
    Values_Aff_Response_Exam_1_Prep = models.TextField()
    Hours_exam_study_Exam_1_Response = models.IntegerField(null=True, blank=True)
    Hours_exam_study_Exam_2_Response = models.IntegerField(null=True, blank=True)
    Change_Exam_2_Response = models.CharField(max_length=3, choices=_CHANGE_EXAM_2_RESPONSE_CHOICES, null=True, blank=True)
    #Change_Explain_Exam_2_Response = models.TextField()
    Change_Explain_Exam_2_Response = models.TextField()
    Partner_Exam_1_Response = models.CharField(max_length=1, choices=_PARTNER_EXAM_1_RESPONSE_CHOICES, null=True, blank=True)
    Last_Name = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=_GENDER_CHOICES, null=True, blank=True)
    College = models.CharField(max_length=11, choices=_COLLEGE_CHOICES, null=True, blank=True)
    College_Other = models.CharField(max_length=200, null=True, blank=True)
    Semesters_Completed = models.IntegerField(null=True, blank=True)
    Course = models.IntegerField(null=True, blank=True)
    Cum_GPA_Survey = models.CharField(max_length=3, choices=_CUM_GPA_SURVEY_CHOICES, null=True, blank=True)
    Parent_Ed = models.CharField(max_length=14, choices=_PARENT_ED_CHOICES, null=True, blank=True)
    Employment = models.CharField(max_length=9, choices=_EMPLOYMENT_CHOICES, null=True, blank=True)
    Involved_In__Greek = models.NullBooleanField()
    Involved_In__Sports = models.NullBooleanField()
    Involved_In__Religious = models.NullBooleanField()
    Involved_In__Research = models.NullBooleanField()
    Involved_In__Volunteering = models.NullBooleanField()
    Involved_In__Music_Art = models.NullBooleanField()
    Involved_In__Other = models.NullBooleanField()
    Other_Commitment = models.CharField(max_length=500, null=True, blank=True)
    Concentrate_Other = models.CharField(max_length=200, null=True, blank=True)
    Post_College_GradSchool = models.CharField(max_length=200, null=True, blank=True)
    Post_College_Other = models.CharField(max_length=200, null=True, blank=True)
    CSP = models.CharField(max_length=14, choices=_CSP_CHOICES, null=True, blank=True)
    MP_Exam_2_Response = models.FloatField(null=True, blank=True)
    MP_Exam_1_Prep = models.FloatField(null=True, blank=True)
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
    Participation_Exam_1_Prep = models.FloatField(null=True, blank=True)
    Engineering_Field = models.CharField(max_length=4, choices=_ENGINEERING_FIELD_CHOICES, null=True, blank=True)
    Post_College = models.CharField(max_length=13, choices=_POST_COLLEGE_CHOICES, null=True, blank=True)
    HS_Physics = models.CharField(max_length=6, choices=_HS_PHYSICS_CHOICES, null=True, blank=True)
    HS_Math_Other = models.CharField(max_length=200, null=True, blank=True)
    College_Math_Other = models.CharField(max_length=200, null=True, blank=True)
    College_Chem_Other = models.CharField(max_length=200, null=True, blank=True)
    College_Bio_Other = models.CharField(max_length=200, null=True, blank=True)
    Coenroll__Math_116 = models.NullBooleanField()
    Coenroll__Math_215 = models.NullBooleanField()
    Coenroll__Math_216 = models.NullBooleanField()
    Coenroll__Stats_250 = models.NullBooleanField()
    Coenroll__Chem_210 = models.NullBooleanField()
    Coenroll__Chem_211 = models.NullBooleanField()
    Coenroll__Chem_215 = models.NullBooleanField()
    Coenroll__Chem_216 = models.NullBooleanField()
    Coenroll__Chem_230 = models.NullBooleanField()
    Coenroll__Psych_111 = models.NullBooleanField()
    Coenroll__Bio_172 = models.NullBooleanField()
    Coenroll__Bio_173 = models.NullBooleanField()
    Coenroll__Bio_225 = models.NullBooleanField()
    Coenroll__Bio_305 = models.NullBooleanField()
    Coenroll__Eng_100 = models.NullBooleanField()
    Coenroll__Eng_101 = models.NullBooleanField()
    Coenroll__Eng_110 = models.NullBooleanField()
    Coenroll__MechEng_211 = models.NullBooleanField()
    Coenroll__AeroEng_201 = models.NullBooleanField()
    Coenroll__EECS_215 = models.NullBooleanField()
    Coenroll__EECS_280 = models.NullBooleanField()
    Coenroll__None = models.NullBooleanField()
    Reason__Physics_req = models.NullBooleanField()
    Reason__Concentration_req = models.NullBooleanField()
    Reason__Grad_req = models.NullBooleanField()
    Reason__NS_Credit = models.NullBooleanField()
    Reason__Interest = models.NullBooleanField()
    Grade_Want = models.CharField(max_length=10, choices=_GRADE_WANT_CHOICES, null=True, blank=True)
    Confidence = models.CharField(max_length=20, choices=_CONFIDENCE_CHOICES, null=True, blank=True)
    Grade_Expected_Student = models.CharField(max_length=10, choices=_GRADE_EXPECTED_STUDENT_CHOICES, null=True, blank=True)
    Hours_outside_study = models.CharField(max_length=2, choices=HOURS_CHOICES, null=True, blank=True)
    Exam_1_Score = models.FloatField(null=True, blank=True)
    Exam_3_Score = models.FloatField(null=True, blank=True)
    Exam_Final_Score = models.FloatField(null=True, blank=True)
    Exam_2_Score = models.FloatField(null=True, blank=True)
    Exam_2_Sigma = models.FloatField(null=True, blank=True)
    Final_Grade = models.CharField(max_length=10, choices=GRADES_CHOICES, null=True, blank=True)
    #ECoach_Most_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    ECoach_Most_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    ECoach_Accordion_Helpful = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True, blank=True)
    Helpful_in_Future_Classes = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Helpful_in_Future_Career = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    ECoach_Archive_Helpful = models.CharField(max_length=3, choices=_ECOACH_ARCHIVE_HELPFUL_CHOICES, null=True, blank=True)
    #ECoach_Least_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    ECoach_Least_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    #ECoach_else = models.CharField(max_length=1000, null=True, blank=True)
    ECoach_else = models.CharField(max_length=1000, null=True, blank=True)
    #ECoach_Change_Behavior_Explain = models.CharField(max_length=1000, null=True, blank=True)
    ECoach_Change_Behavior_Explain = models.CharField(max_length=1000, null=True, blank=True)
    #Study_Tech_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    Study_Tech_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    #Study_Tech_Not_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    Study_Tech_Not_Helpful = models.CharField(max_length=1000, null=True, blank=True)
    #Advice_Exam_Prep = models.CharField(max_length=1000, null=True, blank=True)
    Advice_Exam_Prep = models.CharField(max_length=1000, null=True, blank=True)
    ECoach_Change_Behavior = models.CharField(max_length=3, choices=_ECOACH_CHANGE_BEHAVIOR_CHOICES, null=True, blank=True)
    #Advice_Beginning_Semester = models.CharField(max_length=1000, null=True, blank=True)
    Advice_Beginning_Semester = models.CharField(max_length=1000, null=True, blank=True)
    Final_Grade_Happy = models.CharField(max_length=7, choices=_FINAL_GRADE_HAPPY_CHOICES, null=True, blank=True)
    Minor_or_Major = models.CharField(max_length=14, choices=_MINOR_OR_MAJOR_CHOICES, null=True, blank=True)
    Continuation = models.CharField(max_length=15, choices=_CONTINUATION_CHOICES, null=True, blank=True)
    Confidence_After = models.CharField(max_length=14, choices=_CONFIDENCE_AFTER_CHOICES, null=True, blank=True)
    Continuation_Other = models.CharField(max_length=200, null=True, blank=True)
    Vote_Plot_Select = models.CharField(max_length=6, choices=_VOTE_PLOT_SELEC_CHOICES, null=True, blank=True)
    #Vote_Plot_Response = models.CharField(max_length=1000, null=True, blank=True)
    Vote_Plot_Response = models.CharField(max_length=1000, null=True, blank=True)
    Participation_Exam_2_Response = models.FloatField(null=True, blank=True)
    Suggest_SLC = models.CharField(max_length=10, choices=_SUGGEST_SLC_CHOICES, null=True, blank=True)
    Hours_exam_study = models.IntegerField(null=True, blank=True)
    Values_Aff_Select__Art = models.NullBooleanField()
    Values_Aff_Select__Creativity = models.NullBooleanField()
    Values_Aff_Select__Relationships = models.NullBooleanField()
    Values_Aff_Select__Government = models.NullBooleanField()
    Values_Aff_Select__Independence = models.NullBooleanField()
    Values_Aff_Select__Learning = models.NullBooleanField()
    Values_Aff_Select__Athletic = models.NullBooleanField()
    Values_Aff_Select__Social = models.NullBooleanField()
    Values_Aff_Select__Music = models.NullBooleanField()
    Values_Aff_Select__Career = models.NullBooleanField()
    Values_Aff_Select__Spiritual = models.NullBooleanField()
    Values_Aff_Select__Humor = models.NullBooleanField()
    #Values_Aff_Response = models.TextField()
    Values_Aff_Response = models.TextField()
    Hours_MP_study = models.IntegerField(null=True, blank=True)
    Helproom = models.CharField(max_length=11, choices=_HELPROOM_CHOICES, null=True, blank=True)
    Office_Hours = models.CharField(max_length=11, choices=FREQUENCY_CHOICES, null=True, blank=True)
    Partner = models.CharField(max_length=15, choices=_PARTNER_CHOICES, null=True, blank=True)
    SLC_Interest = models.CharField(max_length=17, choices=_SLC_INTEREST_CHOICES, null=True, blank=True)
    Memorize_personal = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Math_Confidence = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Trust_Calculation = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Hard_work_personal_cant_solve = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Innate = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Memorize_general = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Recall_Formula = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Apply_Principles = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    Hard_work_personal_understand = models.CharField(max_length=17, choices=AGREE_DISAGREE_CHOICES, null=True, blank=True)
    AP_Exam__AP_B = models.NullBooleanField()
    AP_Exam__AP_C_Mech = models.NullBooleanField()
    AP_Exam__AP_C_EM = models.NullBooleanField()
    AP_Exam__IDK = models.NullBooleanField()
    AP_Exam__No = models.NullBooleanField()
    AP_B_Score = models.IntegerField(null=True, blank=True)
    AP_C_Mech_Score = models.IntegerField(null=True, blank=True)
    AP_C_EM_Score = models.IntegerField(null=True, blank=True)
    HS_Math = models.CharField(max_length=16, choices=_HS_MATH_CHOICES, null=True, blank=True)
    SAT_Math = models.IntegerField(null=True, blank=True)
    ACT_Math = models.IntegerField(null=True, blank=True)
    College_Math__Math_115 = models.NullBooleanField()
    College_Math__115_AP = models.NullBooleanField()
    College_Math__115_Else = models.NullBooleanField()
    College_Math__116 = models.NullBooleanField()
    College_Math__116_AP = models.NullBooleanField()
    College_Math__116_Else = models.NullBooleanField()
    College_Math__156 = models.NullBooleanField()
    College_Math__185 = models.NullBooleanField()
    College_Math__186 = models.NullBooleanField()
    College_Math__214 = models.NullBooleanField()
    College_Math__215 = models.NullBooleanField()
    College_Math__216 = models.NullBooleanField()
    College_Math__217 = models.NullBooleanField()
    College_Math__Stats_250 = models.NullBooleanField()
    College_Math__255 = models.NullBooleanField()
    College_Math__285 = models.NullBooleanField()
    College_Math__286 = models.NullBooleanField()
    College_Math__289 = models.NullBooleanField()
    College_Math__295 = models.NullBooleanField()
    College_Math__296 = models.NullBooleanField()
    College_Math__Higher = models.NullBooleanField()
    College_Math__Current = models.NullBooleanField()
    College_Math__Other = models.NullBooleanField()
    College_Math__None = models.NullBooleanField()
    College_Chem__AP_Test_Out = models.NullBooleanField()
    College_Chem__125_126_130 = models.NullBooleanField()
    College_Chem__210_211 = models.NullBooleanField()
    College_Chem__215_216 = models.NullBooleanField()
    College_Chem__230 = models.NullBooleanField()
    College_Chem__241_242 = models.NullBooleanField()
    College_Chem__245_246_247 = models.NullBooleanField()
    College_Chem__260_261 = models.NullBooleanField()
    College_Chem__Higher = models.NullBooleanField()
    College_Chem__Current = models.NullBooleanField()
    College_Chem__Other = models.NullBooleanField()
    College_Chem__None = models.NullBooleanField()
    College_Bio__AP_Test_Out = models.NullBooleanField()
    College_Bio__171 = models.NullBooleanField()
    College_Bio__172 = models.NullBooleanField()
    College_Bio__173 = models.NullBooleanField()
    College_Bio__205 = models.NullBooleanField()
    College_Bio__222 = models.NullBooleanField()
    College_Bio__225_226 = models.NullBooleanField()
    College_Bio__305 = models.NullBooleanField()
    College_Bio__Higher = models.NullBooleanField()
    College_Bio__Current = models.NullBooleanField()
    College_Bio__Other = models.NullBooleanField()
    College_Bio__None = models.NullBooleanField()
    Exam_1_Grade_Predicted = models.FloatField(null=True, blank=True)
    Exam_3_Grade_Predicted = models.FloatField(null=True, blank=True)
    Exam_3_Grade_Predicted_Number = models.IntegerField(null=True, blank=True)
    Exam_Final_Grade_Predicted = models.FloatField(null=True, blank=True)
    Exam_Final_Grade_Predicted_Number = models.IntegerField(null=True, blank=True)
    Exam_2_Grade_Predicted = models.FloatField(null=True, blank=True)
    Exam_2_Grade_Predicted_Number = models.IntegerField(null=True, blank=True)
    Exam_1_Grade_Predicted_Number = models.IntegerField(null=True, blank=True)
    Exam_1_Rank = models.IntegerField(null=True, blank=True)
    Exam_2_rank = models.IntegerField(null=True, blank=True)
    Exam_3_Rank = models.IntegerField(null=True, blank=True)
    Exam_Final_Rank = models.IntegerField(null=True, blank=True)


