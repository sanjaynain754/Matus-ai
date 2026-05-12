import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import { spawn } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/api/execute', async (req, res) => {
  const { code, type = 'matus' } = req.body;

  if (!code) {
    return res.status(400).json({ error: 'No code provided' });
  }

  try {
    const result = await executeCode(code, type);
    return res.status(200).json({ success: true, output: result });
  } catch (error) {
    return res.status(500).json({ success: false, error: error.message });
  }
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/advanced', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'advanced.html'));
});

function executeCode(code, type) {
  return new Promise((resolve, reject) => {
    let output = '';
    let errorOutput = '';

    const pythonScript = `
import sys
sys.path.insert(0, '${__dirname}')
try:
    from matus_ultimate import MatusUltimate
    from matus_advanced_hacking import *
    matus = MatusUltimate()
    result = matus.execute("""${code.replace(/"/g, '\\"').replace(/\n/g, '\\n')}""")
    print(result)
except Exception as e:
    import traceback
    print(f"Error: {str(e)}")
    traceback.print_exc()
`;

    const process = spawn('python3', ['-c', pythonScript], {
      cwd: __dirname,
      timeout: 30000,
    });

    process.stdout.on('data', (data) => {
      output += data.toString();
    });

    process.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });

    process.on('close', (code) => {
      if (code !== 0 && !output) {
        reject(new Error(errorOutput || 'Execution failed'));
      } else {
        resolve(output || errorOutput);
      }
    });

    process.on('error', (err) => {
      reject(err);
    });

    setTimeout(() => {
      process.kill();
      reject(new Error('Execution timeout'));
    }, 30000);
  });
}

app.listen(PORT, () => {
  console.log(`
╔════════════════════════════════════════╗
║   MATUS ULTIMATE - Server Running      ║
║   http://localhost:${PORT}                  ║
║   Advanced: http://localhost:${PORT}/advanced ║
║   Status: Ready for Execution          ║
╚════════════════════════════════════════╝
  `);
});
