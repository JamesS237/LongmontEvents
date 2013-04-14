# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserEvent'
        db.create_table(u'API_userevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=70)),
            ('description', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=300)),
            ('time', self.gf('django.db.models.fields.TimeField')(default=None)),
            ('date', self.gf('django.db.models.fields.DateField')(default=None)),
            ('address', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=100)),
            ('org', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=50)),
        ))
        db.send_create_signal(u'API', ['UserEvent'])


    def backwards(self, orm):
        # Deleting model 'UserEvent'
        db.delete_table(u'API_userevent')


    models = {
        u'API.userevent': {
            'Meta': {'object_name': 'UserEvent'},
            'address': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'None'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'org': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '50'}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'None'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '70'})
        }
    }

    complete_apps = ['API']