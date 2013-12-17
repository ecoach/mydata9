# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Source1.ECoach_helpful_study'
        db.add_column('mydata_source1', 'ECoach_helpful_study',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ECoach_helpful_exam'
        db.add_column('mydata_source1', 'ECoach_helpful_exam',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ECoach_helpful_most'
        db.add_column('mydata_source1', 'ECoach_helpful_most',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ECoach_would_change'
        db.add_column('mydata_source1', 'ECoach_would_change',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.ECoach_favorite_message'
        db.add_column('mydata_source1', 'ECoach_favorite_message',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.interest_after_STATS250'
        db.add_column('mydata_source1', 'interest_after_STATS250',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Final_Course_Letter_Grade'
        db.add_column('mydata_source1', 'Final_Course_Letter_Grade',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Method_1_Grade'
        db.add_column('mydata_source1', 'Method_1_Grade',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Method_2_Grade'
        db.add_column('mydata_source1', 'Method_2_Grade',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Source1.ECoach_helpful_study'
        db.delete_column('mydata_source1', 'ECoach_helpful_study')

        # Deleting field 'Source1.ECoach_helpful_exam'
        db.delete_column('mydata_source1', 'ECoach_helpful_exam')

        # Deleting field 'Source1.ECoach_helpful_most'
        db.delete_column('mydata_source1', 'ECoach_helpful_most')

        # Deleting field 'Source1.ECoach_would_change'
        db.delete_column('mydata_source1', 'ECoach_would_change')

        # Deleting field 'Source1.ECoach_favorite_message'
        db.delete_column('mydata_source1', 'ECoach_favorite_message')

        # Deleting field 'Source1.interest_after_STATS250'
        db.delete_column('mydata_source1', 'interest_after_STATS250')

        # Deleting field 'Source1.Final_Course_Letter_Grade'
        db.delete_column('mydata_source1', 'Final_Course_Letter_Grade')

        # Deleting field 'Source1.Method_1_Grade'
        db.delete_column('mydata_source1', 'Method_1_Grade')

        # Deleting field 'Source1.Method_2_Grade'
        db.delete_column('mydata_source1', 'Method_2_Grade')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mydata9.common1': {
            'BirthDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'BirthMo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'BirthYr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Class_Standing': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'College': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'College_Other': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Concentrate_Other': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology_EEB': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology_MCDB': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Chemistry': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Education': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Engineering': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Health': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Humanities': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__IDK': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Math': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Neurosci': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Other': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Physics': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Psych_BBCS': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Social_Science_not_Psych': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Stats': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Cum_GPA_Survey': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Declared': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'Employment': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'First_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'High_School_CumGPA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Greek': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Music_Art': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Other': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Religious': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Research': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Sports': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Volunteering': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Common1', 'db_table': "'mydata_common1'"},
            'Other_Commitment': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Parent_Ed': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'Post_College': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'Semesters_Completed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uniqname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'mydata9.emptysource': {
            'Meta': {'object_name': 'EmptySource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'mydata9.source1': {
            'ACT_REF_01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ACT_REF_11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Confidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ECoach_favorite_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ECoach_helpful_exam': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ECoach_helpful_most': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ECoach_helpful_study': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ECoach_would_change': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Exam1_Self_Advice': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Exam2_Self_Advice': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__0': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__1': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__10': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__2': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__3': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__4': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__5': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__6': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__7': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__8': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Resources__9': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Prep_Simulation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Expected_Grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Final_Course_Letter_Grade': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'GSI_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'GTD_01__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_02__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_03__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_04__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_05__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_06__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_07__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_08__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_09__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_10__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_11__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_12__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_13__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_14__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'GTD_15__done': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_Grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Lecture_Section': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Source1', 'db_table': "'mydata_source1'"},
            'Method_1_Grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Method_2_Grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Permission_To_Use_Exam1_Self_Advice': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Permission_To_Use_Exam_2_Self_Advice': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Reg_Acad_Level': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Reg_Enrolled': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Reg_GPA': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Reg_Gender': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SEQ_GLO_11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SNS_INT_11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Signup_Opt_Out': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Subject_Interest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VIS_VRB_11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'confidence_grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dist_values': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dist_values_after_Exam_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email_request_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email_request_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email_request_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email_request_4': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_exam1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_exam2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_final': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw01': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw02': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw03': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw04': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw05': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw06': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw07': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw08': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw09': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw10': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw11': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw_extra': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_hw_practice': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab00_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab01_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab02_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab03_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab04_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab05_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab06_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab07_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab08_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab09_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab10_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab11_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab12_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_lab13_attend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gb_prelab12': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hw_hours': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_after_STATS250': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'like_about_ecoach': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'make_ecoach_better': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mamazonlab': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mamazonlecture': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mcalculator': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mlecturebook': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mopenmi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mopenmilab': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mtextbook': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'myellow': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'oh_expected': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rested_12': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_01': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_02': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_03': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_04': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_05': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_06': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_07': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_08': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_09': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_10': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_11': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_12': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'study_partner': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_expectation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['mydata9']