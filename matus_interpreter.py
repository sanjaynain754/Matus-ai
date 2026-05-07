import sys
import re
from matus_hacking import inject_hacking_tools

class MatusInterpreter:
    def __init__(self):
        self.variables = {}
        inject_hacking_tools(self)

    def execute(self, code):
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line.startswith('//'):
                i += 1
                continue
            
            if line.startswith('if '):
                condition_part = line[3:-1].strip()
                condition = eval(condition_part, {}, self.variables)
                if not condition:
                    i += 1
                    while i < len(lines) and not (lines[i].startswith('else:') or lines[i].strip() == ''):
                        i += 1
                    if i < len(lines) and lines[i].startswith('else:'):
                        i += 1
                        continue
                else:
                    i += 1
                    continue
            elif line.startswith('else:'):
                i += 1
                while i < len(lines) and not (lines[i].strip() == ''):
                    i += 1
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
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        if expr.isdigit():
            return int(expr)
        
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
                for a in args:
                    print(a)
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
        print("Matus Interpreter v0.1")
        while True:
            try:
                line = input("matus > ")
                interpreter.execute(line)
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
