import contextlib

@contextlib.contextmanager
def propagator(name, propagate=False):
    try:
        yield
        print(name, 'exited normally')
    except Exception as e:
        print(name, 'received an exception:', str(e))
        if propagate:
            raise

# Example usage:
try:
    with propagator("MyContext", propagate=True):
        # Code that may raise an exception
        result = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("ZeroDivisionError handled outside the context manager")
