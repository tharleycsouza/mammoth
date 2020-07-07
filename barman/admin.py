from django.contrib import admin
from barman.models import PostgreSQL
# Register your models here.


class PostgreSQLAdmin(admin.ModelAdmin):

    model = PostgreSQL
    search_fields = ('name', 'address',)
    list_display = ('name', 'address', 'retention', 'retention_policy',)
    fieldsets = (
        (None, {
            'fields': ('name', 'address', 'retention', 'retention_policy', 'backup_method', 'key_pub',)
        }),
    )


admin.site.register(PostgreSQL, PostgreSQLAdmin)
