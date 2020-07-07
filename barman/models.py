from django.db import models
from django.core.validators import validate_ipv4_address, RegexValidator

# Create your models here.

class PostgreSQL(models.Model):
    
    backup_method = (
        ('postgres', 'postgres'),
        ('rsync', 'rsync'),
    )
    retention_policy = (
        ('DAYS', 'DAYS'),
        ('WEEKS', 'WEEKS'),
        ('MONTHS', 'MONTHS'),
    )
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=20, unique=True, validators=[validate_ipv4_address])
    backup_method = models.CharField(choices=backup_method, max_length=20)
    retention = models.PositiveIntegerField(blank=True, null=True)
    retention_policy = models.CharField(choices=retention_policy, max_length=20, help_text='days, weeks or months')
    key_pub = models.TextField(max_length=1000, null=True)
    class Meta:
        verbose_name_plural = 'PostgreSQL'
            
    def __unicode__(self):
        return self.name
