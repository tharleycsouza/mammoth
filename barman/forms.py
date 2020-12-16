from django import forms
from django.core.validators import validate_ipv4_address, RegexValidator


class pg_register(forms.Form):
    backup_method = (
        ('postgres', 'postgres'),
        ('rsync', 'rsync'),
    )
    retention_policy = (
        ('DAYS', 'DAYS'),
        ('WEEKS', 'WEEKS'),
        ('MONTHS', 'MONTHS'),
    )
    name = forms.CharField(label='pg_name', max_length=100)
    address = forms.CharField(label='pg_address', max_length=100, validators=[
                              validate_ipv4_address])
    backup_method = forms.ChoiceField(choices=backup_method)
    retention = form.PositiveIntegerField()
    retention_policy = = forms.ChoiceField(choices=retention_policy)
    key_pub = form.TextField(max_length=1000, null=True)
    