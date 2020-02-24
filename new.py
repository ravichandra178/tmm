try:
    import builtins
except ImportError:
    import __builtin__ as builtins
def fake_input():
    return 'toxicvapor'
builtins.input = fake_input
a = input()
print(a[::-1]