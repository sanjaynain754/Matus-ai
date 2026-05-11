#!/usr/bin/env python3
"""
MATUS ULTIMATE - The All-Powerful Language
Combines Python, C++, JavaScript, Bash, and more
Single Admin User - Zero Restrictions - Complete Freedom
"""

import sys
import subprocess
import os
import re
import json
import tempfile
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

class MatusUltimate:
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, str] = {}
        self.memory: Dict[str, Any] = {}
        self.admin_mode = True  # Always admin, no restrictions
        self.execution_history: List[Dict] = []
        
    def execute_python(self, code: str) -> str:
        """Execute Python code directly with no restrictions."""
        try:
            exec_globals = {**self.variables, 'sys': sys, 'os': os, 'subprocess': subprocess}
            exec(code, exec_globals)
            self.variables.update(exec_globals)
            return "Python execution successful"
        except Exception as e:
            return f"Python Error: {str(e)}"
    
    def execute_bash(self, command: str) -> str:
        """Execute Bash commands with full system access."""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            output = result.stdout + result.stderr
            return output if output else "Command executed successfully"
        except subprocess.TimeoutExpired:
            return "Command timeout (30s)"
        except Exception as e:
            return f"Bash Error: {str(e)}"
    
    def execute_javascript(self, code: str) -> str:
        """Execute JavaScript code using Node.js."""
        try:
            result = subprocess.run(['node', '-e', code], capture_output=True, text=True, timeout=30)
            return result.stdout + result.stderr if result.stdout or result.stderr else "JS execution successful"
        except Exception as e:
            return f"JavaScript Error: {str(e)}"
    
    def execute_cpp(self, code: str) -> str:
        """Compile and execute C++ code."""
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                cpp_file = os.path.join(tmpdir, "program.cpp")
                exe_file = os.path.join(tmpdir, "program")
                
                with open(cpp_file, 'w') as f:
                    f.write(code)
                
                compile_result = subprocess.run(
                    ['g++', cpp_file, '-o', exe_file],
                    capture_output=True, text=True, timeout=30
                )
                
                if compile_result.returncode != 0:
                    return f"C++ Compilation Error: {compile_result.stderr}"
                
                run_result = subprocess.run([exe_file], capture_output=True, text=True, timeout=30)
                return run_result.stdout + run_result.stderr if run_result.stdout or run_result.stderr else "C++ execution successful"
        except Exception as e:
            return f"C++ Error: {str(e)}"
    
    def execute_sql(self, query: str, db_path: str = ":memory:") -> str:
        """Execute SQL queries directly."""
        try:
            import sqlite3
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            result = cursor.fetchall()
            conn.close()
            return json.dumps(result) if result else "Query executed successfully"
        except Exception as e:
            return f"SQL Error: {str(e)}"
    
    def system_call(self, command: str) -> str:
        """Direct system call with no restrictions."""
        return self.execute_bash(command)
    
    def file_read(self, path: str) -> str:
        """Read any file without restrictions."""
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            return f"File Read Error: {str(e)}"
    
    def file_write(self, path: str, content: str, append: bool = False) -> str:
        """Write to any file without restrictions."""
        try:
            mode = 'a' if append else 'w'
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, mode) as f:
                f.write(content)
            return f"File written successfully: {path}"
        except Exception as e:
            return f"File Write Error: {str(e)}"
    
    def file_delete(self, path: str, recursive: bool = False) -> str:
        """Delete files and directories without restrictions."""
        try:
            if os.path.isdir(path):
                if recursive:
                    shutil.rmtree(path)
                else:
                    os.rmdir(path)
            else:
                os.remove(path)
            return f"Deleted: {path}"
        except Exception as e:
            return f"Delete Error: {str(e)}"
    
    def network_scan(self, target: str, ports: str = "1-1000") -> str:
        """Network scanning with no restrictions."""
        try:
            cmd = f"nmap -p {ports} {target} 2>/dev/null || nc -zv -w1 {target} {ports.replace('-', ':')} 2>&1"
            return self.execute_bash(cmd)
        except Exception as e:
            return f"Network Scan Error: {str(e)}"
    
    def packet_craft(self, packet_data: str) -> str:
        """Craft and send custom packets."""
        try:
            result = subprocess.run(['scapy'], input=packet_data, capture_output=True, text=True, timeout=30)
            return result.stdout + result.stderr if result.stdout or result.stderr else "Packet sent"
        except Exception as e:
            return f"Packet Craft Error: {str(e)}"
    
    def memory_access(self, address: int, size: int = 1024) -> str:
        """Direct memory access capabilities."""
        try:
            import ctypes
            buffer = ctypes.create_string_buffer(size)
            ctypes.memmove(buffer, address, size)
            return buffer.raw.hex()
        except Exception as e:
            return f"Memory Access Error: {str(e)}"
    
    def process_inject(self, pid: int, code: str) -> str:
        """Process injection and manipulation."""
        try:
            cmd = f"gdb -p {pid} -batch -ex 'call (void)system(\"{code}\")' 2>&1"
            return self.execute_bash(cmd)
        except Exception as e:
            return f"Process Inject Error: {str(e)}"
    
    def kernel_module(self, module_code: str) -> str:
        """Load kernel modules without restrictions."""
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.c', delete=False) as f:
                f.write(module_code)
                module_file = f.name
            
            cmd = f"gcc -c {module_file} -o /tmp/module.o 2>&1 && insmod /tmp/module.o 2>&1"
            result = self.execute_bash(cmd)
            os.unlink(module_file)
            return result
        except Exception as e:
            return f"Kernel Module Error: {str(e)}"
    
    def parse_matus_code(self, code: str) -> List[str]:
        """Parse Matus code into executable statements."""
        lines = code.split('\n')
        statements = []
        current_block = ""
        
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('//'):
                continue
            
            if stripped.endswith(':'):
                current_block = stripped
            else:
                if current_block:
                    statements.append(current_block + "\n" + stripped)
                    current_block = ""
                else:
                    statements.append(stripped)
        
        return statements
    
    def execute_statement(self, statement: str) -> str:
        """Execute a single Matus statement."""
        statement = statement.strip()
        
        # Python execution
        if statement.startswith('py:'):
            code = statement[3:].strip()
            return self.execute_python(code)
        
        # Bash execution
        elif statement.startswith('bash:') or statement.startswith('sh:'):
            cmd = statement.split(':', 1)[1].strip()
            return self.system_call(cmd)
        
        # JavaScript execution
        elif statement.startswith('js:'):
            code = statement[3:].strip()
            return self.execute_javascript(code)
        
        # C++ execution
        elif statement.startswith('cpp:'):
            code = statement[4:].strip()
            return self.execute_cpp(code)
        
        # SQL execution
        elif statement.startswith('sql:'):
            query = statement[4:].strip()
            return self.execute_sql(query)
        
        # File operations
        elif statement.startswith('read:'):
            path = statement[5:].strip()
            return self.file_read(path)
        
        elif statement.startswith('write:'):
            parts = statement[6:].split('<<', 1)
            if len(parts) == 2:
                path = parts[0].strip()
                content = parts[1].strip()
                return self.file_write(path, content)
        
        elif statement.startswith('delete:'):
            path = statement[7:].strip()
            return self.file_delete(path, recursive=True)
        
        # Network operations
        elif statement.startswith('scan:'):
            target = statement[5:].strip()
            return self.network_scan(target)
        
        # System commands
        elif statement.startswith('sys:'):
            cmd = statement[4:].strip()
            return self.system_call(cmd)
        
        # Memory access
        elif statement.startswith('mem:'):
            addr_str = statement[4:].strip()
            try:
                address = int(addr_str, 16)
                return self.memory_access(address)
            except:
                return "Invalid memory address"
        
        # Variable assignment
        elif '=' in statement and not statement.startswith('if'):
            parts = statement.split('=', 1)
            var_name = parts[0].strip()
            value = parts[1].strip()
            try:
                self.variables[var_name] = eval(value, self.variables)
                return f"{var_name} = {self.variables[var_name]}"
            except:
                self.variables[var_name] = value
                return f"{var_name} = {value}"
        
        # Print statement
        elif statement.startswith('print:'):
            msg = statement[6:].strip()
            print(msg)
            return msg
        
        # Direct execution as bash
        else:
            return self.system_call(statement)
    
    def execute(self, code: str) -> str:
        """Execute Matus code."""
        statements = self.parse_matus_code(code)
        results = []
        
        for statement in statements:
            result = self.execute_statement(statement)
            results.append(result)
            self.execution_history.append({
                'statement': statement,
                'result': result
            })
        
        return '\n'.join(results)
    
    def interactive_shell(self):
        """Interactive Matus shell with admin access."""
        print("=" * 60)
        print("MATUS ULTIMATE - The All-Powerful Language")
        print("Admin Mode: Unrestricted Access")
        print("=" * 60)
        print("\nSyntax Examples:")
        print("  py: <python code>")
        print("  bash: <shell command>")
        print("  js: <javascript code>")
        print("  cpp: <c++ code>")
        print("  sql: <sql query>")
        print("  read: /path/to/file")
        print("  write: /path/to/file << content")
        print("  delete: /path/to/file")
        print("  scan: target_ip")
        print("  sys: <system command>")
        print("  mem: 0xaddress")
        print("\nType 'exit' to quit\n")
        
        while True:
            try:
                user_input = input("matus> ").strip()
                if user_input.lower() == 'exit':
                    break
                if not user_input:
                    continue
                
                result = self.execute_statement(user_input)
                print(result)
            except KeyboardInterrupt:
                print("\nInterrupted")
                break
            except Exception as e:
                print(f"Error: {str(e)}")

if __name__ == "__main__":
    matus = MatusUltimate()
    
    if len(sys.argv) > 1:
        # Execute file or inline code
        if sys.argv[1] == '-c':
            code = sys.argv[2] if len(sys.argv) > 2 else ""
            print(matus.execute(code))
        else:
            # Execute file
            with open(sys.argv[1], 'r') as f:
                code = f.read()
            print(matus.execute(code))
    else:
        # Interactive shell
        matus.interactive_shell()
