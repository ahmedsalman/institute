# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Institute'
        db.create_table(u'institute_institute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_deleted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
        ))
        db.send_create_signal('institute', ['Institute'])

        # Adding model 'Discipline'
        db.create_table(u'institute_discipline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_deleted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'institute', ['Discipline'])

        # Adding M2M table for field institute on 'Discipline'
        db.create_table(u'institute_discipline_institute', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('discipline', models.ForeignKey(orm[u'institute.discipline'], null=False)),
            ('institute', models.ForeignKey(orm['institute.institute'], null=False))
        ))
        db.create_unique(u'institute_discipline_institute', ['discipline_id', 'institute_id'])

        # Adding model 'SubDiscipline'
        db.create_table(u'institute_subdiscipline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_deleted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institute.Institute'])),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['institute.Discipline'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'institute', ['SubDiscipline'])

        # Adding unique constraint on 'SubDiscipline', fields ['institute', 'discipline']
        db.create_unique(u'institute_subdiscipline', ['institute_id', 'discipline_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SubDiscipline', fields ['institute', 'discipline']
        db.delete_unique(u'institute_subdiscipline', ['institute_id', 'discipline_id'])

        # Deleting model 'Institute'
        db.delete_table(u'institute_institute')

        # Deleting model 'Discipline'
        db.delete_table(u'institute_discipline')

        # Removing M2M table for field institute on 'Discipline'
        db.delete_table('institute_discipline_institute')

        # Deleting model 'SubDiscipline'
        db.delete_table(u'institute_subdiscipline')


    models = {
        u'institute.discipline': {
            'Meta': {'object_name': 'Discipline'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_deleted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['institute.Institute']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'institute.institute': {
            'Meta': {'object_name': 'Institute'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_deleted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'institute.subdiscipline': {
            'Meta': {'unique_together': "(('institute', 'discipline'),)", 'object_name': 'SubDiscipline'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_deleted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['institute.Discipline']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['institute.Institute']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['institute']