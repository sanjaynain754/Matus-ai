"""
DATYA - The Central AI Agent of Matus AI
Single AI Agent that controls all agents, tools, web access, and admin control.
Admin: Sanjay
"""

import os
import sys
import json
import re
import time
from io import StringIO
from datetime import datetime


class DatyaAgent:
    """
    Datya - Central AI Agent Controller
    Manages all sub-agents: Auto, Mythos, Hacking, Admin, Web, Updater
    Admin: Sanjay
    """

    VERSION = "2.0.0"
    AGENT_NAME = "Datya"
    ADMIN = "Sanjay"
    PROJECT = "Matus AI"

    def __init__(self):
        self.tools = {}
        self.history = []
        self.variables = {}
        self.active_agents = []
        self._load_all_agents()

    # ============================================================
    # AGENT LOADING
    # ============================================================
    def _load_all_agents(self):
        """Load all sub-agents and register their tools"""
        try:
            from datya_hacking import HackingAgent
            agent = HackingAgent()
            self.tools.update(agent.get_tools())
            self.active_agents.append("Hacking")
        except Exception as e:
            print(f"[Datya] Hacking agent warning: {e}")

        try:
            from datya_web import WebAgent
            agent = WebAgent()
            self.tools.update(agent.get_tools())
            self.active_agents.append("Web")
        except Exception as e:
            print(f"[Datya] Web agent warning: {e}")

        try:
            from datya_admin import AdminAgent
            agent = AdminAgent()
            self.tools.update(agent.get_tools())
            self.active_agents.append("Admin")
        except Exception as e:
            print(f"[Datya] Admin agent warning: {e}")

        try:
            from datya_auto import AutoAgent
            agent = AutoAgent()
            self.tools.update(agent.get_tools())
            self.active_agents.append("Auto")
        except Exception as e:
            print(f"[Datya] Auto agent warning: {e}")

        try:
            from datya_mythos import MythosAgent
            agent = MythosAgent()
            self.tools.update(agent.get_tools())
            self.active_agents.append("Mythos")
        except Exception as e:
            print(f"[Datya] Mythos agent warning: {e}")

        # Built-in tools always available
        self.tools["datya_help"] = self._cmd_help
        self.tools["datya_status"] = self._cmd_status
        self.tools["datya_info"] = self._cmd_info
        self.tools["datya_history"] = self._cmd_history
        self.tools["datya_clear"] = self._cmd_clear
        self.tools["datya_exec"] = self._cmd_exec
        self.tools["datya_run"] = self._cmd_run
        self.tools["datya_agents"] = self._cmd_agents

    # ============================================================
    # CORE EXECUTION ENGINE
    # ============================================================
    def process(self, user_input):
        """Main entry point - process user input and route to appropriate tool"""
        if not user_input or not user_input.strip():
            return ""

        user_input = user_input.strip()
        self._add_history("user", user_input)

        output = self._execute_command(user_input)

        self._add_history("datya", output)
        return output

    def _execute_command(self, command):
        """Execute a command by parsing and routing"""
        # Parse command: name(args) or name arg1 arg2
        command = command.strip()

        # Handle function-style calls: command(args)
        if '(' in command and command.endswith(')'):
            func_name = command.split('(', 1)[0].strip()
            args_str = command[command.find('(') + 1:-1].strip()
            args = self._parse_args(args_str)
        # Handle space-separated: command arg1 arg2
        else:
            parts = command.split(None, 1)
            func_name = parts[0]
            args = [parts[1]] if len(parts) > 1 else []

        # Execute the tool
        if func_name in self.tools:
            try:
                result = self.tools[func_name](*args)
                return str(result) if result is not None else "Done."
            except TypeError:
                # Wrong number of args - try with full args string
                try:
                    return str(self.tools[func_name](command.split(None, 1)[1] if ' ' in command else ""))
                except:
                    return f"Usage error. Try: {func_name}('argument')"
            except Exception as e:
                return f"[Datya Error] {func_name}: {str(e)}"
        else:
            return self._suggest_tool(func_name)

    def _parse_args(self, args_str):
        """Parse arguments from comma-separated string, handling quotes"""
        if not args_str:
            return []
        args = []
        current = []
        in_quote = False
        quote_char = None
        depth = 0

        for char in args_str:
            if not in_quote and char in ('"', "'"):
                in_quote = True
                quote_char = char
            elif in_quote and char == quote_char:
                in_quote = False
                quote_char = None
            elif not in_quote:
                if char in ('(', '[', '{'):
                    depth += 1
                elif char in (')', ']', '}'):
                    depth -= 1
                elif char == ',' and depth == 0:
                    val = ''.join(current).strip()
                    args.append(self._eval_value(val))
                    current = []
                    continue
            current.append(char)

        if current:
            val = ''.join(current).strip()
            args.append(self._eval_value(val))

        return args

    def _eval_value(self, val):
        """Evaluate a value string - handle strings, numbers, variables"""
        if not val:
            return None
        # String literal
        if (val.startswith('"') and val.endswith('"')) or \
           (val.startswith("'") and val.endswith("'")):
            return val[1:-1]
        # Number
        try:
            if '.' in val:
                return float(val)
            return int(val)
        except ValueError:
            pass
        # Boolean
        if val.lower() == 'true':
            return True
        if val.lower() == 'false':
            return False
        if val.lower() == 'none':
            return None
        # Variable lookup
        if val in self.variables:
            return self.variables[val]
        # List literal
        if val.startswith('[') and val.endswith(']'):
            try:
                return json.loads(val)
            except:
                pass
        return val

    # ============================================================
    # BUILT-IN DATYA COMMANDS
    # ============================================================
    def _cmd_help(self, category=""):
        """Show available commands and tools"""
        help_text = f"""╔═══════════════════════════════════════════╗
║  MATUS AI - Datya Agent v{self.VERSION}     ║
║  Admin: {self.ADMIN}                          ║
╠═══════════════════════════════════════════╣
║  Active Agents: {', '.join(self.active_agents):22s}║
║  Total Tools: {len(self.tools):30d}║
╚═══════════════════════════════════════════╝

Available Tools:"""
        for tool_name in sorted(self.tools.keys()):
            help_text += f"\n  • {tool_name}"

        help_text += """

Usage: tool_name(arguments)
Examples:
  datya_status()
  datya_agents()
  scan_ports('google.com', '80,443,8080')
  web_fetch('https://example.com')
  admin_sys_info()"""

        return help_text

    def _cmd_status(self):
        """Show Datya system status"""
        return f"""╔═══════════════════════════════════════════╗
║  DATYA STATUS REPORT                      ║
╠═══════════════════════════════════════════╣
║  Version:    {self.VERSION}                          ║
║  Admin:      {self.ADMIN}                          ║
║  Project:    {self.PROJECT}                     ║
║  Time:       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}       ║
║  OS:         {sys.platform:22s}║
║  Python:     {sys.version.split()[0]:22s}║
║  Active Agents: {', '.join(self.active_agents):16s}║
║  Tools Loaded:  {len(self.tools):21d}║
║  History:       {len(self.history):21d}║
╚═══════════════════════════════════════════╝"""

    def _cmd_info(self):
        """Show Datya agent information"""
        return (
            f"MATUS AI | Datya v{self.VERSION}\n"
            f"Single AI Agent controlling all systems\n"
            f"Admin: {self.ADMIN} | Project: {self.PROJECT}\n"
            f"Modules: {', '.join(self.active_agents)}\n"
            f"Capabilities: Hacking, Web, Admin, Auto AI, Security Analysis"
        )

    def _cmd_history(self, count="10"):
        """Show command history"""
        try:
            n = int(count)
        except:
            n = 10
        entries = self.history[-n:]
        result = f"=== Last {len(entries)} entries ===\n"
        for entry in entries:
            prefix = ">" if entry["role"] == "user" else "Datya:"
            result += f"  {prefix} {entry['content'][:80]}\n"
        return result

    def _cmd_clear(self):
        """Clear history and variables"""
        self.history.clear()
        self.variables.clear()
        return "History and variables cleared."

    def _cmd_exec(self, code):
        """Execute Python code safely"""
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        try:
            exec(code, {"__builtins__": __builtins__}, self.variables)
            output = mystdout.getvalue()
        except Exception as e:
            output = f"[Exec Error] {str(e)}"
        finally:
            sys.stdout = old_stdout
        return output or "Executed (no output)."

    def _cmd_run(self, code):
        """Execute Matus language code"""
        output = StringIO()
        old_stdout = sys.stdout
        sys.stdout = output
        try:
            lines = code.split('\n')
            for line in lines:
                line = line.strip()
                if not line or line.startswith('//'):
                    continue
                # Variable assignment
                if '=' in line and '(' not in line.split('=')[0] and not line.startswith('if'):
                    parts = line.split('=', 1)
                    var_name = parts[0].strip()
                    var_val = parts[1].strip()
                    if var_val.startswith('"') and var_val.endswith('"'):
                        var_val = var_val[1:-1]
                    self.variables[var_name] = self._eval_value(var_val)
                # Print
                elif line.startswith('print(') and line.endswith(')'):
                    msg = line[6:-1].strip()
                    val = self._eval_value(msg)
                    print(val)
                # Variable use
                elif line in self.variables:
                    print(self.variables[line])
        except Exception as e:
            print(f"[Matus Error] {str(e)}")
        finally:
            sys.stdout = old_stdout
        return output.getvalue()

    def _cmd_agents(self):
        """List all active agents"""
        result = "╔═══════════════════════════════════════════╗\n"
        result += "║  ACTIVE AGENTS - DATYA CONTROLLER         ║\n"
        result += "╠═══════════════════════════════════════════╣\n"
        agent_details = {
            "Hacking": "Port scan, IP lookup, command exec, file ops",
            "Web": "URL fetch, web scrape, API calls, search",
            "Admin": "System info, process list/kill, disk usage",
            "Auto": "AI-powered autonomous task execution",
            "Mythos": "Security analysis, vulnerability assessment"
        }
        for agent in self.active_agents:
            desc = agent_details.get(agent, "Unknown")
            result += f"║ [{agent:8s}] {desc:32s}║\n"
        result += "╚═══════════════════════════════════════════╝"
        return result

    def _suggest_tool(self, func_name):
        """Suggest similar tool names"""
        similar = [t for t in self.tools.keys() if func_name.lower() in t.lower() or t.lower() in func_name.lower()]
        if similar:
            return f"Tool '{func_name}' not found. Did you mean: {', '.join(similar[:5])}?"
        return f"Tool '{func_name}' not found. Use datya_help() to see all tools."

    # ============================================================
    # HISTORY MANAGEMENT
    # ============================================================
    def _add_history(self, role, content):
        self.history.append({
            "role": role,
            "content": content,
            "time": datetime.now().isoformat()
        })
        # Keep last 100 entries
        if len(self.history) > 100:
            self.history = self.history[-100:]

    def get_all_tool_names(self):
        """Return list of all available tool names"""
        return sorted(self.tools.keys())


# Singleton instance
_datya = None

def get_datya():
    """Get the global Datya instance"""
    global _datya
    if _datya is None:
        _datya = DatyaAgent()
    return _datya

def reset_datya():
    """Reset the global Datya instance"""
    global _datya
    _datya = DatyaAgent()
    return _datya
