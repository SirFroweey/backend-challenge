from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        raise Exception('Editing Dimensions is disabled for this assignment')


class Dimension(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="subdimensions")
    name = models.CharField(max_length=100, blank=False)
    has_children = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        raise Exception('Editing Dimensions is disabled for this assignment')

    def get_all_children(self, level, include_self=True):
        """Traverses all children associated with the parent Dimension. 

        :param level (int): defines the depth of the given Dimension models.
        :param include_self (bool): wether we should add ourself to the result.
        """
        r = []
        level += 1

        if include_self:
            r.append('\t' * level + self.name)

        if self.has_children:
            for c in Dimension.objects.filter(parent=self):
                _r = c.get_all_children(level, include_self=True)
                if 0 < len(_r):
                    r.extend(_r)

        return r
