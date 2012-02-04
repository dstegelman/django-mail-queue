# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MailerMessage'
        db.create_table('mailer_mailermessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('to_address', self.gf('django.db.models.fields.EmailField')(max_length=250)),
            ('from_address', self.gf('django.db.models.fields.EmailField')(max_length=250)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('app', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mailer', ['MailerMessage'])


    def backwards(self, orm):
        
        # Deleting model 'MailerMessage'
        db.delete_table('mailer_mailermessage')


    models = {
        'mailer.mailermessage': {
            'Meta': {'object_name': 'MailerMessage'},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['mailer']
