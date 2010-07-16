from django.forms.util import ValidationError
from django import forms
from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext as _

import uuid

class UUIDField(models.CharField):
    
    def __init__(self, auto=False, *args, **kwargs):
        if kwargs.get('primary_key', False):
            assert auto, _("Must pass auto=True when using UUIDField as primary key")
        
        self.auto = auto
        
        kwargs['max_length'] = 32
        if auto:
            kwargs['editable'] = False
            kwargs['blank'] = True
            kwargs['null'] = True
        
        super(UUIDField, self).__init__(*args, **kwargs)
        
    
    def db_type(self):
        return 'uuid'
    
    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if not value and self.auto:
            value = uuid.uuid4().hex
            setattr(model_instance, self.attname, value)
        return super(UUIDField, self).pre_save(model_instance, add)
    
    def to_python(self, value):
        if not value:
            return None
        if len(value) != 32:
            value = value.replace('-', '')
        assert len(value) == 32
        return value
    
    
    def value_to_string(self, obj):
        val = self._get_val_from_obj(obj)
        if val is None:
            data = ''
        else:
            data = unicode(val)
        return data
    
try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass
else:
    add_introspection_rules([
        (
            [UUIDField], # Class(es) these apply to
            [],         # Positional arguments (not used)
            {           # Keyword argument
                "auto": ["auto", {"default": "False"}],
            },
        ),
    ], ["^uuidfield\.fields\.UUIDField"]) # XXX Change this to where yours is stored. Better solution?