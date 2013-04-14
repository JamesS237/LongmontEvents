# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserEvent.going_count'
        db.add_column(u'API_userevent', 'going_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserEvent.going_count'
        db.delete_column(u'API_userevent', 'going_count')


    models = {
        u'API.userevent': {
            'Meta': {'object_name': 'UserEvent'},
            'address': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'None'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '300'}),
            'going_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'org': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '50'}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'None'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '70'})
        }
    }

    complete_apps = ['API']