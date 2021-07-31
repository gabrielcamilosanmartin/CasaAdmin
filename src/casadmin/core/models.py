from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(
            deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):

        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModelBase(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)
    readonly_fields = ('deleted_at')

    all_objects = SoftDeletionManager(alive_only=False)
    objects = SoftDeletionManager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModelBase, self).delete()
