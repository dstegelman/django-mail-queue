# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MailerMessage.reply_to'
        db.add_column(u'mailqueue_mailermessage', 'reply_to',
                      self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MailerMessage.reply_to'
        db.delete_column(u'mailqueue_mailermessage', 'reply_to')


    models = {
        u'mailqueue.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailqueue.MailerMessage']", 'null': 'True', 'blank': 'True'}),
            'file_attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mailqueue.mailermessage': {
            'Meta': {'object_name': 'MailerMessage'},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'bcc_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            'html_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_attempt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reply_to': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['mailqueue']