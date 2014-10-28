# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MailerMessage.to_address'
        db.alter_column(u'mailqueue_mailermessage', 'to_address', self.gf('django.db.models.fields.TextField')())

        # Changing field 'MailerMessage.bcc_address'
        db.alter_column(u'mailqueue_mailermessage', 'bcc_address', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'MailerMessage.to_address'
        db.alter_column(u'mailqueue_mailermessage', 'to_address', self.gf('django.db.models.fields.EmailField')(max_length=250))

        # Changing field 'MailerMessage.bcc_address'
        db.alter_column(u'mailqueue_mailermessage', 'bcc_address', self.gf('django.db.models.fields.EmailField')(max_length=250))

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
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['mailqueue']