# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Deleting field 'ModelEntry.model_cls'
        db.delete_column('model_entry', 'model_cls')

    def backwards(self, orm):

        # Adding field 'ModelEntry.model_cls'
        db.add_column('model_entry', 'model_cls', self.gf('django.db.models.fields.CharField')(default='k', max_length=255), keep_default=False)

    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'persons.modelentry': {
            'Meta': {'object_name': 'ModelEntry', 'db_table': "'model_entry'"},
            'action_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'persons.person': {
            'Meta': {'object_name': 'Person', 'db_table': "'person'"},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'persons.requestinfo': {
            'Meta': {'object_name': 'RequestInfo', 'db_table': "'request_info'"},
            'http_accept_charset': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'http_connection': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'http_cookie': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'http_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['persons']
