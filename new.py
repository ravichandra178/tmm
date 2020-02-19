try:
    import builtins
except ImportError:
    import __builtin__ as builtins
def fake_input():
    return '89'
builtins.input = fake_input
