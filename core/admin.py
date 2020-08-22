from django.contrib import admin
from .models import Service, Role, Employee, Feature, OtherImage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'description', 'active', 'updated')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'description', 'active', 'updated')


@admin.register(OtherImage)
class OtherImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'active', 'updated')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio', 'active', 'updated')
