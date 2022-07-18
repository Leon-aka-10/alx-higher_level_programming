#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as alphnum:
        sys.stderr.write("Exception: {}\n".format(alphnum))
        result = None

    return (result)
