# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-19 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20170119_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_fuck_him_to_death', '弄死小虎逼'), ('can_access_my_course', '可以访问我的课程'), ('can_access_customer_list', '可以访问客户列表'), ('can_access_customer_detail', '可以访问客户详细'), ('can_access_studyrecords', '可以访问学习记录页面'), ('can_access_homework_detail', '可以访问作业详情页面'), ('can_upload_homework', '可以交作业'), ('access_kingadmin_table_obj_detail', '可以访问kingadmin每个表的对象'), ('change_kingadmin_table_obj_detail', '可以修改kingadmin每个表的对象'))},
        ),
    ]
