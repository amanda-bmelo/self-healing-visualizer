def print_entry(func):
    def _func(*args, **kw):
        print(func, args, kw)
        return func(*args, **kw)
    
    return _func