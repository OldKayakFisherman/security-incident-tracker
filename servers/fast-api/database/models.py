from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Incident(models.Model):
    id = fields.IntField(pk=True)
    external_case_number = fields.CharField(max_length=20, unique=True)
    ip = fields.CharField(max_length=30)
    pen_tester = fields.BooleanField()
    region = fields.CharField(max_length=50)
    country = fields.CharField(max_length=50)
    script_injection = fields.BooleanField()
    command_injection = fields.BooleanField()
    sql_injection = fields.BooleanField()
    cross_frame_scripting = fields.BooleanField()
    path_discovery = fields.BooleanField()
    other = fields.BooleanField()
