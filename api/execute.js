import { spawn } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

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
}

function executeCode(code, type) {
  return new Promise((resolve, reject) => {
    let output = '';
    let errorOutput = '';

    const pythonScript = `
import sys
sys.path.insert(0, '${__dirname.replace(/\\/g, '\\\\')}')
from matus_ultimate import MatusUltimate

matus = MatusUltimate()
result = matus.execute("""${code.replace(/"/g, '\\"').replace(/\n/g, '\\n')}""")
print(result)
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
      if (code !== 0) {
        reject(new Error(errorOutput || 'Execution failed'));
      } else {
        resolve(output);
      }
    });

    process.on('error', (err) => {
      reject(err);
    });
  });
}
