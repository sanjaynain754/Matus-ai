# 📦 MATUS AI - RELEASE GUIDE

## Publishing MATUS to NPM, PyPI, and Docker Hub

---

## 🚀 **Quick Release Process**

### **Step 1: Create a Git Tag**

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

This will automatically trigger GitHub Actions to:
- ✅ Build Python package
- ✅ Publish to PyPI
- ✅ Publish to NPM
- ✅ Create GitHub Release
- ✅ Build and push Docker image

---

## 📝 **Manual Publishing (If Needed)**

### **1. Publish to PyPI**

```bash
# Install build tools
pip install setuptools wheel twine

# Build package
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

**After publishing, install with:**
```bash
pip install matus-ai
```

---

### **2. Publish to NPM**

```bash
# Login to NPM
npm login

# Publish package
npm publish

# Or publish with specific version
npm publish --tag v1.0.0
```

**After publishing, install with:**
```bash
npm install matus-ai
```

---

### **3. Build and Push Docker Image**

```bash
# Build image
docker build -t sanjaynain754/matus-ai:1.0.0 .
docker build -t sanjaynain754/matus-ai:latest .

# Login to Docker Hub
docker login

# Push images
docker push sanjaynain754/matus-ai:1.0.0
docker push sanjaynain754/matus-ai:latest
```

**After publishing, run with:**
```bash
docker run -p 3000:3000 sanjaynain754/matus-ai:latest
```

---

## 🔐 **GitHub Secrets Setup**

To enable automated releases, add these secrets to your GitHub repository:

1. **PYPI_API_TOKEN** - Your PyPI API token
   - Get from: https://pypi.org/manage/account/token/

2. **NPM_TOKEN** - Your NPM authentication token
   - Get from: https://www.npmjs.com/settings/~/tokens

3. **DOCKER_USERNAME** - Your Docker Hub username

4. **DOCKER_PASSWORD** - Your Docker Hub password or access token

---

## 📋 **Release Checklist**

Before releasing, ensure:

- [ ] All tests pass
- [ ] README is updated
- [ ] CHANGELOG is updated
- [ ] Version numbers are correct
- [ ] All dependencies are listed
- [ ] Documentation is complete
- [ ] Code is committed and pushed
- [ ] No uncommitted changes

---

## 🔄 **Automated Release Workflow**

The `.github/workflows/release.yml` file handles:

1. **Trigger:** When you push a tag (e.g., `v1.0.0`)
2. **Build:** Compiles Python and Node packages
3. **Test:** Runs basic tests
4. **Publish:**
   - PyPI (Python)
   - NPM (Node.js)
   - Docker Hub (Docker)
5. **Release:** Creates GitHub Release with artifacts

---

## 📊 **Version Numbering**

Use semantic versioning:
- `v1.0.0` - Major release
- `v1.1.0` - Minor release (new features)
- `v1.0.1` - Patch release (bug fixes)

---

## 🎯 **Installation Methods After Release**

### **PyPI (Python)**
```bash
pip install matus-ai
```

### **NPM (Node.js)**
```bash
npm install matus-ai
```

### **Docker**
```bash
docker run -p 3000:3000 sanjaynain754/matus-ai
```

### **GitHub**
```bash
git clone https://github.com/sanjaynain754/Matus-ai.git
cd Matus-ai
npm install
npm start
```

### **Termux (Android)**
```bash
pkg install python nodejs git
git clone https://github.com/sanjaynain754/Matus-ai.git
cd Matus-ai
npm install
npm start
```

---

## 📚 **Package Contents**

### **PyPI Package**
- `matus_ultimate.py` - Core interpreter
- `matus_unrestricted.py` - Hacking tools
- `matus_hydra.py` - Brute force
- `matus_metasploit.py` - Exploitation
- `matus_azure_testing.py` - Azure testing
- `matus_hackerone_report.py` - Report generator
- `matus_auto_recon.py` - Automated recon
- `matus_results_parser.py` - Results parser
- All supporting modules

### **NPM Package**
- `server.js` - Express server
- `public/` - Web interfaces
- `package.json` - Dependencies
- All supporting files

### **Docker Image**
- Complete Ubuntu 22.04 environment
- Python 3, Node.js, all dependencies
- Pre-configured for immediate use

---

## 🔗 **Package Links**

- **PyPI:** https://pypi.org/project/matus-ai/
- **NPM:** https://www.npmjs.com/package/matus-ai
- **Docker Hub:** https://hub.docker.com/r/sanjaynain754/matus-ai
- **GitHub:** https://github.com/sanjaynain754/Matus-ai

---

## ❓ **Troubleshooting**

### **PyPI Upload Fails**
- Check PyPI token is valid
- Ensure version is not already published
- Run: `twine check dist/*`

### **NPM Publish Fails**
- Check npm login: `npm whoami`
- Verify package name is available
- Check package.json syntax

### **Docker Push Fails**
- Verify Docker login: `docker login`
- Check image name format
- Ensure Docker daemon is running

---

## 📞 **Support**

For issues:
- GitHub Issues: https://github.com/sanjaynain754/Matus-ai/issues
- Documentation: Check README and guides

---

**Happy Releasing! 🚀**
