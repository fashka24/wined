# python debugger

import ast

def get_variables_and_values_from_code(code):
    class VariableVisitor(ast.NodeVisitor):
        def __init__(self):
            self.variables = {}

        def visit_Assign(self, node):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    var_name = target.id

                    value = node.value
                    self.variables[var_name] = value
            self.generic_visit(node)

    tree = ast.parse(code)
    visitor = VariableVisitor()
    visitor.visit(tree)

    variables_with_values = {}
    for var, value_node in visitor.variables.items():
        variables_with_values[var] = ast.dump(value_node)

    return variables_with_values

def get_functions_from_code(code):
    class FunctionVisitor(ast.NodeVisitor):
        def __init__(self):
            self.functions = {}

        def visit_FunctionDef(self, node):
            func_name = node.name

            params = [arg.arg for arg in node.args.args]
            self.functions[func_name] = params
            self.generic_visit(node)

    tree = ast.parse(code)
    visitor = FunctionVisitor()
    visitor.visit(tree)

    return visitor.functions