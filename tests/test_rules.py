import ast
from pyrefactor.rules import detect_long_functions, detect_unused_imports

def test_detect_long_functions():
    src = '''
def short():
    pass

def long():
    a = 0
''' + ("\n    a+=1\n" * 60)
    tree = ast.parse(src)
    res = detect_long_functions(tree, min_lines=50)
    assert any("long" in s for s in res)

def test_detect_unused_imports():
    src = '''
import os
import sys
from math import sin, cos

print(sys.platform)
'''
    tree = ast.parse(src)
    res = detect_unused_imports(tree)
    # os and math.cos should be reported as unused in this simple heuristic
    assert "os" in res or "math.cos" in res
