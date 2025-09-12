import decimal


def default_orjson_serializer(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError