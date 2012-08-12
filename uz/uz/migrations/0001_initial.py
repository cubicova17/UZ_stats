# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table('uz_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('train', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('uz', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table('uz_entry')


    models = {
        'uz.entry': {
            'Meta': {'object_name': 'Entry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'train': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['uz']