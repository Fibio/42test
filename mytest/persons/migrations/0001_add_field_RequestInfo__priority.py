# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding field 'RequestInfo._priority'
        db.add_column('request_info', '_priority', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1), keep_default=False)

    def backwards(self, orm):

        # Deleting field 'RequestInfo._priority'
        db.delete_column('request_info', '_priority')

    models = {
        'persons.requestinfo': {
            'Meta': {'object_name': 'RequestInfo', 'db_table': "'request_info'"},
            '_priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'http_accept_charset': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'http_connection': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'http_cookie': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'http_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['persons']
