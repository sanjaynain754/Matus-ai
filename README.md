# Matus AI v2.0

**Single AI Agent | All Tools | All Access | Admin Control**

> **Project:** Matus AI  
> **Agent:** Datya v2.0  
> **Admin:** Sanjay  
> **Platform:** Android (APK)

---

## Overview

Matus AI v2.0 is a professional Android application powered by a single AI agent named **Datya**. Datya controls all sub-agents, tools, web access, and admin functions from one unified interface.

## Architecture

```
+---------------------------------------------+
|              DATYA (v2.0)                    |
|         Central AI Agent Controller          |
|              Admin: Sanjay                   |
+----------+----------+------------------------+
|  Hacking |   Web    |     Admin              |
|  Agent   |  Agent   |     Agent              |
|          |          |                        |
|  Port    |  Fetch   |  System Info           |
|  Scan    |  Scrape  |  Process List          |
|  IP      |  Search  |  Disk Usage            |
|  Ping    |  API     |  Battery               |
|  DNS     |          |  Device Control        |
+----------+----------+------------------------+
|           AUTO AGENT                         |
|     AI-Powered Task Execution                |
|     (Requires OpenAI API Key)                |
+----------------------------------------------+
|           MYTHOS AGENT                       |
|     Security and Vulnerability Analysis      |
+----------------------------------------------+
```

## Features

### Datya Agent - All Tools (34 Total)

| Category | Tools |
|----------|-------|
| **Hacking** | scan_ports, get_ip, run_cmd, read_file, write_file, ping_host, dns_lookup |
| **Web** | web_fetch, web_scrape, web_api_json, web_search, web_get_status |
| **Admin** | admin_sys_info, admin_list_procs, admin_kill_proc, admin_is_root, admin_disk_usage, admin_battery, admin_set_brightness, admin_vibrate |
| **Auto** | auto_task, auto_analyze, auto_generate_code |
| **Mythos** | mythos_scan_code, mythos_basic_check, mythos_report |
| **Datya** | datya_help, datya_status, datya_info, datya_history, datya_clear, datya_exec, datya_run, datya_agents |

### Usage Examples

```
datya_status()          -> Full system status
datya_agents()          -> List all active agents
scan_ports('google.com', '80,443,8080')  -> Port scan
get_ip('github.com')    -> DNS resolution
web_fetch('https://example.com')  -> Fetch webpage
web_search('cybersecurity')  -> Web search
admin_sys_info()        -> System information
admin_battery()         -> Battery status
auto_task('Analyze this code...')  -> AI task
mythos_scan_code('import os; exec(input())')  -> Security scan
```

## Tech Stack

- **Python 3.14** (via python-for-android)
- **Kivy** (UI Framework)
- **Cython 3.1.4** (Build)
- **NDK 25b** (Native Compilation)
- **SDK 33** (Android API)

## Project Structure

```
Matus-ai/
|-- main.py              # Kivy UI - Main App Entry
|-- datya_core.py        # Datya Agent Engine
|-- datya_hacking.py     # Hacking Tools Agent
|-- datya_web.py         # Web Access Agent
|-- datya_admin.py       # Admin Control Agent
|-- datya_auto.py        # AI Auto Agent
|-- datya_mythos.py      # Security Analysis Agent
|-- icon.png             # App Icon
|-- buildozer.spec       # APK Build Config
|-- requirements.txt     # Python Dependencies
+-- .github/workflows/
    +-- build-apk.yml    # GitHub Actions CI/CD
```

## Build APK

### Locally
```bash
pip install buildozer cython
buildozer android debug
```

### GitHub Actions
Push to main/master branch -> Auto APK build via workflow.

## License

MIT License
