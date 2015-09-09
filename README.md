# Generic relations

Example of Polymorphic associations in Django.

- 1 Reduction has n Scans
- Job has a FK for either Reduction or Scan

Implemented in django with:
```python
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


content_type = models.ForeignKey(ContentType)
object_id = models.PositiveIntegerField()
content_object = GenericForeignKey('content_type', 'object_id')
```

Note to have reverse generic relations, on the models for which the FK is PK, we must add:
```python
<attribute name> = GenericRelation(<Model name>)
```

**Code**
```
reduction/models.py
reduction/test.py
```
