# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'RecipeUpstream', fields ['status']
        db.create_index('rrs_recipeupstream', ['status'])

        # Adding index on 'RecipeUpstream', fields ['date']
        db.create_index('rrs_recipeupstream', ['date'])

        # Adding index on 'RecipeUpstream', fields ['no_update_reason']
        db.create_index('rrs_recipeupstream', ['no_update_reason'])

        # Adding index on 'RecipeUpstream', fields ['type']
        db.create_index('rrs_recipeupstream', ['type'])

        # Adding index on 'RecipeUpgrade', fields ['commit_date']
        db.create_index('rrs_recipeupgrade', ['commit_date'])

        # Adding index on 'RecipeUpgrade', fields ['author_date']
        db.create_index('rrs_recipeupgrade', ['author_date'])

        # Adding index on 'Release', fields ['start_date']
        db.create_index('rrs_release', ['start_date'])

        # Adding index on 'Release', fields ['end_date']
        db.create_index('rrs_release', ['end_date'])

        # Adding index on 'RecipeMaintainerHistory', fields ['date']
        db.create_index('rrs_recipemaintainerhistory', ['date'])

        # Adding index on 'Milestone', fields ['start_date']
        db.create_index('rrs_milestone', ['start_date'])

        # Adding index on 'Milestone', fields ['end_date']
        db.create_index('rrs_milestone', ['end_date'])


    def backwards(self, orm):
        # Removing index on 'Milestone', fields ['end_date']
        db.delete_index('rrs_milestone', ['end_date'])

        # Removing index on 'Milestone', fields ['start_date']
        db.delete_index('rrs_milestone', ['start_date'])

        # Removing index on 'RecipeMaintainerHistory', fields ['date']
        db.delete_index('rrs_recipemaintainerhistory', ['date'])

        # Removing index on 'Release', fields ['end_date']
        db.delete_index('rrs_release', ['end_date'])

        # Removing index on 'Release', fields ['start_date']
        db.delete_index('rrs_release', ['start_date'])

        # Removing index on 'RecipeUpgrade', fields ['author_date']
        db.delete_index('rrs_recipeupgrade', ['author_date'])

        # Removing index on 'RecipeUpgrade', fields ['commit_date']
        db.delete_index('rrs_recipeupgrade', ['commit_date'])

        # Removing index on 'RecipeUpstream', fields ['type']
        db.delete_index('rrs_recipeupstream', ['type'])

        # Removing index on 'RecipeUpstream', fields ['no_update_reason']
        db.delete_index('rrs_recipeupstream', ['no_update_reason'])

        # Removing index on 'RecipeUpstream', fields ['date']
        db.delete_index('rrs_recipeupstream', ['date'])

        # Removing index on 'RecipeUpstream', fields ['status']
        db.delete_index('rrs_recipeupstream', ['status'])


    models = {
        'layerindex.branch': {
            'Meta': {'object_name': 'Branch'},
            'bitbake_branch': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sort_priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'layerindex.layerbranch': {
            'Meta': {'object_name': 'LayerBranch'},
            'actual_branch': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['layerindex.Branch']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['layerindex.LayerItem']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vcs_last_commit': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'vcs_last_fetch': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'vcs_last_rev': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'vcs_subdir': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        'layerindex.layeritem': {
            'Meta': {'object_name': 'LayerItem'},
            'classic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_preference': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'layer_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'mailing_list_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'usage_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vcs_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vcs_web_file_base_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vcs_web_tree_base_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vcs_web_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'layerindex.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'bbclassextend': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'bugtracker': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'depends': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'filepath': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layerbranch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['layerindex.LayerBranch']"}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pn': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'provides': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'pv': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'src_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'rrs.maintainer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Maintainer'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'rrs.milestone': {
            'Meta': {'unique_together': "(('release', 'name'),)", 'object_name': 'Milestone'},
            'end_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rrs.Release']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'})
        },
        'rrs.recipedistro': {
            'Meta': {'object_name': 'RecipeDistro'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'distro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['layerindex.Recipe']"})
        },
        'rrs.recipemaintainer': {
            'Meta': {'object_name': 'RecipeMaintainer'},
            'history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rrs.RecipeMaintainerHistory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maintainer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rrs.Maintainer']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['layerindex.Recipe']"})
        },
        'rrs.recipemaintainerhistory': {
            'Meta': {'object_name': 'RecipeMaintainerHistory'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rrs.Maintainer']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sha1': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'rrs.recipeupgrade': {
            'Meta': {'object_name': 'RecipeUpgrade'},
            'author_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'commit_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maintainer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rrs.Maintainer']", 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['layerindex.Recipe']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'rrs.recipeupstream': {
            'Meta': {'object_name': 'RecipeUpstream'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rrs.RecipeUpstreamHistory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_update_reason': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['layerindex.Recipe']"}),
            'status': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'rrs.recipeupstreamhistory': {
            'Meta': {'object_name': 'RecipeUpstreamHistory'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'rrs.release': {
            'Meta': {'object_name': 'Release'},
            'end_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['rrs']