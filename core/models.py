import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    file_extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{file_extension}'
    return filename


class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    updated = models.DateField('Updated', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Cog'),
        ('lni-stats-up', 'Stats-Up'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Layers'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    icon = models.CharField('Icon', max_length=15, choices=ICON_CHOICES)
    title = models.CharField('Title', max_length=40)
    description = models.CharField('Description', max_length=150)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Feature(Base):
    ICON_CHOICES = (
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'Laptop-Phone'),
        ('lni-cog', 'Cog'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers'),
    )
    icon = models.CharField('Icon', max_length=19, choices=ICON_CHOICES)
    title = models.CharField('Title', max_length=50)
    description = models.CharField('Description', max_length=100)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.title


class OtherImage(Base):
    name = models.CharField('Name', max_length=50)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb': {'width': 600, 'height': 670,
                                                                                  'crop': True}})

    class Meta:
        verbose_name = 'Other Image'
        verbose_name_plural = 'Other Images'

    def __str__(self):
        return self.name


class Role(Base):
    role = models.CharField('Role', max_length=50)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role


class Employee(Base):
    name = models.CharField('Name', max_length=50)
    role = models.ForeignKey('core.Role', verbose_name='Role', on_delete=models.CASCADE)
    bio = models.CharField('Biography', max_length=100)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480,
                                                                                  'crop': True}})
    facebook_icon = models.CharField('Facebook', max_length=100, default='#')
    twitter_icon = models.CharField('Twitter', max_length=100, default='#')
    instagram_icon = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name
