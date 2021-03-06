import datetime
import re


class ValidationError(Exception): pass


class ModelFieldMeta(type):
    def __new__(mcs, cls_name, superclasses, attribute_dict):

        def init(__init__):
            def decorator(self, *args, **kwargs):
                for k, v in kwargs.items():
                    if not hasattr(attribute_dict, k):
                        setattr(self, k, v)
                self.value = self.default
                __init__(self)
            return decorator

        def __init__(self, *args, **kwargs): pass
        if "__init__" in attribute_dict:
            __init__ = attribute_dict["__init__"]

        attribute_dict["__init__"] = init(__init__)

        return type.__new__(mcs, cls_name, superclasses, attribute_dict)


class ModelFieldBase(object, metaclass=ModelFieldMeta):

    blank = False
    default = None
    value = default

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def validate(self):
        if self.value is None:
            if self.blank:
                return True
            raise ValidationError
        if self._validate():
            return True
        print(type(self), self.value)
        raise ValidationError


class ModelMeta(type):
    def __new__(mcs, cls_name, superclasses, attribute_dict):

        def init(self, *args, **kwargs):
            for field, field_type in attribute_dict.items():
                if isinstance(field_type, ModelFieldBase):
                    attr = type(attribute_dict[field])(**attribute_dict[field].__dict__)
                    setattr(self, field, attr)
                    if field in kwargs:
                        setattr(self, field, kwargs[field])

        attribute_dict["__init__"] = init

        return type.__new__(mcs, cls_name, superclasses,
                            {k: v for k, v in attribute_dict.items()
                             if not isinstance(v, ModelFieldBase)})


class Model(object, metaclass=ModelMeta):
    def __getattribute__(self, key):
        v = object.__getattribute__(self, key)
        if isinstance(v, ModelFieldBase):
            return v.__get__(self, Model)
        return v

    def __setattr__(self, key, value):
        try:
            v = object.__getattribute__(self, key)
            if isinstance(v, ModelFieldBase):
                v.__set__(self, value)
        except AttributeError:
            object.__setattr__(self, key, value)

    def validate(self):
        return all(v.validate() for v in self.__dict__.values() if isinstance(v, ModelFieldBase))


class CharField(ModelFieldBase):
    min_length = 0
    max_length = None

    def _validate(self):
        is_valid = isinstance(self.value, str)

        if self.min_length is not None and is_valid:
            is_valid &= self.min_length <= len(self.value)

        if self.max_length is not None and is_valid:
            is_valid &= len(self.value) <= self.max_length

        return is_valid


class IntegerField(ModelFieldBase):
    min_value = None
    max_value = None

    def _validate(self):
        is_valid = self.value is int
        if is_valid and self.min_value is not None:
            is_valid &= self.min_value <= self.value

        if is_valid and self.max_value is not None:
            is_valid &= self.value <= self.max_value

        return is_valid


class BooleanField(ModelFieldBase):

    def _validate(self):
        return isinstance(self.value, bool)


class DateTimeField(ModelFieldBase):
    auto_now = False

    def getter(self):
        if self.auto_now and self.__default is None:
            return datetime.datetime.now()
        return self.__default

    def setter(self, value):
        self.__default = value

    __default = None
    default = property(getter, setter)

    def _validate(self):
        return isinstance(self.value, (datetime.datetime, property))


class EmailField(CharField): 

    def _validate(self):
        return super(EmailField, self)._validate() and re.match(r'[^@]+@[^@]+\.[^@]+', self.value)
