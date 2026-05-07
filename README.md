# Matus Programming Language

Matus is a versatile, Python-inspired programming language designed for general-purpose coding and ethical hacking.

## Features
- **Simple Syntax:** Indentation-based, easy to read and write.
- **Hacking Modules:** Built-in support for network scanning, IP resolution, and system commands.
- **Mythos AI Module:** AI-powered vulnerability analysis and exploit path suggestion.
- **Cross-Platform:** Runs on any system with Python, and includes an Android wrapper.

## Installation

### Desktop
1. Clone the repository:
   ```bash
   git clone https://github.com/sanjaynain754/Matus-ai.git
   ```
2. Run the interpreter:
   ```bash
   python3 matus_interpreter.py your_script.matus
   ```

### Android
You can build the APK using Buildozer:
```bash
buildozer android debug
```
The APK will be generated in the `bin/` directory.

## Example Usage
```matus
// Resolve an IP
ip = get_ip("google.com")
print(ip)

// Scan ports
scan_ports("127.0.0.1", [80, 443, 22])

// System command
run_cmd("uname -a")
```

## Language Design
For detailed specifications, see [matus_language_design.md](./matus_language_design.md).
