# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MailerMessage.html_content'
        db.alter_column(u'mailqueue_mailermessage', 'html_content', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'MailerMessage.app'
        db.alter_column(u'mailqueue_mailermessage', 'app', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'MailerMessage.bcc_address'
        db.alter_column(u'mailqueue_mailermessage', 'bcc_address', self.gf('django.db.models.fields.EmailField')(default='', max_length=250))

        # Changing field 'MailerMessage.content'
        db.alter_column(u'mailqueue_mailermessage', 'content', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'MailerMessage.subject'
        db.alter_column(u'mailqueue_mailermessage', 'subject', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

    def backwards(self, orm):

        # Changing field 'MailerMessage.html_content'
        db.alter_column(u'mailqueue_mailermessage', 'html_content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'MailerMessage.app'
        db.alter_column(u'mailqueue_mailermessage', 'app', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'MailerMessage.bcc_address'
        db.alter_column(u'mailqueue_mailermessage', 'bcc_address', self.gf('django.db.models.fields.EmailField')(max_length=250, null=True))

        # Changing field 'MailerMessage.content'
        db.alter_column(u'mailqueue_mailermessage', 'content', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'MailerMessage.subject'
        db.alter_column(u'mailqueue_mailermessage', 'subject', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

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
            'bcc_address': ('django.db.models.fields.EmailField', [], {'max_length': '250', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            'html_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_attempt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['mailqueue']