# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.plaz'
        db.add_column('uz_entry', 'plaz',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Entry.kupe'
        db.add_column('uz_entry', 'kupe',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Entry.lux'
        db.add_column('uz_entry', 'lux',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Entry.s1'
        db.add_column('uz_entry', 's1',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Entry.s2'
        db.add_column('uz_entry', 's2',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Entry.for_date'
        db.add_column('uz_entry', 'for_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today()),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.plaz'
        db.delete_column('uz_entry', 'plaz')

        # Deleting field 'Entry.kupe'
        db.delete_column('uz_entry', 'kupe')

        # Deleting field 'Entry.lux'
        db.delete_column('uz_entry', 'lux')

        # Deleting field 'Entry.s1'
        db.delete_column('uz_entry', 's1')

        # Deleting field 'Entry.s2'
        db.delete_column('uz_entry', 's2')

        # Deleting field 'Entry.for_date'
        db.delete_column('uz_entry', 'for_date')


    models = {
        'uz.entry': {
            'Meta': {'object_name': 'Entry'},
            'for_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kupe': ('django.db.models.fields.IntegerField', [], {}),
            'lux': ('django.db.models.fields.IntegerField', [], {}),
            'plaz': ('django.db.models.fields.IntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            's1': ('django.db.models.fields.IntegerField', [], {}),
            's2': ('django.db.models.fields.IntegerField', [], {}),
            'train': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['uz']
