# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MailerMessage.bcc_address'
        db.add_column('mailqueue_mailermessage', 'bcc_address',
                      self.gf('django.db.models.fields.EmailField')(max_length=250, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MailerMessage.last_attempt'
        db.add_column('mailqueue_mailermessage', 'last_attempt',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MailerMessage.bcc_address'
        db.delete_column('mailqueue_mailermessage', 'bcc_address')

        # Deleting field 'MailerMessage.last_attempt'
        db.delete_column('mailqueue_mailermessage', 'last_attempt')


    models = {
        'mailqueue.mailermessage': {
            'Meta': {'object_name': 'MailerMessage'},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'bcc_address': ('django.db.models.fields.EmailField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            'html_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_attempt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['mailqueue']