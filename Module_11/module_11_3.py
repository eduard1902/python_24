import inspect
def introspection_info(obj):
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    try:
        module = inspect.getmodule(obj).__name__
    except:
        module = 'None'

    return {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': methods,
        'module': module
    }


number_info = introspection_info(42)
print(number_info)

# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}