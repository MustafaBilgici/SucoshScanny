import ast
import re

class SqlQueryVisitor(ast.NodeVisitor):
    def __init__(self):
        self.has_injection = False
        
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.BitOr):
            if isinstance(node.right, ast.Str) and re.search(r"(--|\"|')", node.right.s):
                self.has_injection = True
        elif isinstance(node.op, ast.BitAnd):
            if isinstance(node.right, ast.Str) and re.search(r"(--|\"|')", node.right.s):
                self.has_injection = True

def is_sql_injection(query):
    try:
        node = ast.parse(query)
    except SyntaxError:
        return False
    visitor = SqlQueryVisitor()
    visitor.visit(node)
    return visitor.has_injection