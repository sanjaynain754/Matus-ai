import sys
import re
from matus_hacking import inject_hacking_tools
from matus_mythos import inject_mythos_tools
from matus_updater import inject_updater_tools
from matus_admin import inject_admin_tools
from matus_auto import inject_auto_tools

class MatusInterpreter:
    def __init__(self):
        self.variables = {}
        self.custom_functions = {}
        inject_hacking_tools(self)
        inject_mythos_tools(self)
        inject_updater_tools(self)
        inject_admin_tools(self)
        inject_auto_tools(self)

    def execute(self, code):
        lines = code.split('\n')
        self.execute_block(lines)

    def execute_block(self, lines):
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line.startswith('//'):
                i += 1
                continue
            
            # Function Definition
            if line.startswith('func '):
                func_header = line[5:-1].strip()
                func_name = func_header.split('(')[0].strip()
                params = [p.strip() for p in func_header.split('(')[1].split(')')[0].split(',') if p.strip()]
                
                func_body = []
                i += 1
                while i < len(lines) and (lines[i].startswith('    ') or lines[i].strip() == ''):
                    func_body.append(lines[i][4:] if lines[i].startswith('    ') else lines[i])
                    i += 1
                self.custom_functions[func_name] = {'params': params, 'body': func_body}
                continue

            # For Loop
            if line.startswith('for '):
                parts = line[4:-1].split(' in ')
                var_name = parts[0].strip()
                iterable_expr = parts[1].strip()
                iterable = self.evaluate_expr(iterable_expr)
                
                loop_body = []
                i += 1
                while i < len(lines) and (lines[i].startswith('    ') or lines[i].strip() == ''):
                    loop_body.append(lines[i][4:] if lines[i].startswith('    ') else lines[i])
                    i += 1
                
                for val in iterable:
                    self.variables[var_name] = val
                    self.execute_block(loop_body)
                continue

            # If Statement
            if line.startswith('if '):
                condition_part = line[3:-1].strip()
                condition = self.evaluate_expr(condition_part)
                
                if_body = []
                i += 1
                while i < len(lines) and (lines[i].startswith('    ') or lines[i].strip() == ''):
                    if_body.append(lines[i][4:] if lines[i].startswith('    ') else lines[i])
                    i += 1
                
                else_body = []
                if i < len(lines) and lines[i].strip() == 'else:':
                    i += 1
                    while i < len(lines) and (lines[i].startswith('    ') or lines[i].strip() == ''):
                        else_body.append(lines[i][4:] if lines[i].startswith('    ') else lines[i])
                        i += 1
                
                if condition:
                    self.execute_block(if_body)
                else:
                    self.execute_block(else_body)
                continue

            self.evaluate(line)
            i += 1

    def evaluate(self, line):
        line = line.strip()
        if '=' in line and '(' not in line.split('=')[0]:
            parts = line.split('=', 1)
            var_name = parts[0].strip()
            var_value = parts[1].strip()
            self.variables[var_name] = self.evaluate_expr(var_value)
            return self.variables[var_name]
        else:
            return self.evaluate_expr(line)

    def evaluate_expr(self, expr):
        expr = expr.strip()
        if not expr: return None
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        if expr.isdigit():
            return int(expr)
        
        # Function Call
        if '(' in expr and expr.endswith(')'):
            func_name = expr.split('(', 1)[0].strip()
            args_str = expr[expr.find('(')+1:-1].strip()
            
            args = []
            if args_str:
                parts = []
                current = []
                bracket_level = 0
                quote = False
                for char in args_str:
                    if char == '"': quote = not quote
                    if not quote:
                        if char == '[': bracket_level += 1
                        if char == ']': bracket_level -= 1
                    if char == ',' and bracket_level == 0 and not quote:
                        parts.append("".join(current).strip())
                        current = []
                    else:
                        current.append(char)
                parts.append("".join(current).strip())
                for p in parts:
                    args.append(self.evaluate_expr(p))
            
            if func_name == 'print':
                # Convert all args to string for better printing
                str_args = [str(a) for a in args]
                print(" ".join(str_args))
                return None
            
            if func_name == 'range':
                return list(range(*args))

            if func_name in self.custom_functions:
                func = self.custom_functions[func_name]
                old_vars = self.variables.copy()
                for param, arg in zip(func['params'], args):
                    self.variables[param] = arg
                self.execute_block(func['body'])
                # Very basic: return last evaluated or None (proper return not implemented yet)
                return None

            if func_name in self.variables and callable(self.variables[func_name]):
                return self.variables[func_name](*args)
        
        if expr in self.variables:
            return self.variables[expr]
        
        try:
            return eval(expr, {}, self.variables)
        except:
            return expr

    def run_file(self, filename):
        with open(filename, 'r') as f:
            code = f.read()
            self.execute(code)

if __name__ == "__main__":
    interpreter = MatusInterpreter()
    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        print("Matus Interpreter v0.2")
        while True:
            try:
                line = input("matus > ")
                interpreter.execute(line)
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
