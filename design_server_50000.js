const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

// Static Files
app.use(express.static(__dirname));
app.use(express.json());

// Root Route
app.get('/', (req, res) => {
  const htmlPath = path.join(__dirname, 'dashboard31.html');
  
  if (fs.existsSync(htmlPath)) {
    res.sendFile(htmlPath);
  } else {
    res.send(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>Design System</title>
        <style>
          body { font-family: system-ui; padding: 20px; background: #f5f5f5; }
          .container { max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; }
          h1 { color: #667eea; }
          code { background: #f0f0f0; padding: 5px 10px; border-radius: 4px; }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>🚀 Design System Server</h1>
          <p>Port: <strong>50000</strong></p>
          <p>Status: <strong style="color: green;">✅ RUNNING</strong></p>
          
          <h2>📁 Dateiupload</h2>
          <p>dashboard31.html nicht gefunden.</p>
          
          <h3>Option 1: Von Mac hochladen</h3>
          <code>scp ~/path/to/dashboard31-Konsole.html root@51.24.14.6:/opt/aicore/dashboard31.html</code>
          
          <h3>Option 2: Erstelle HTML direkt</h3>
          <code>cat > /opt/aicore/dashboard31.html &lt;&lt; 'EOF'</code>
          <p>&lt;!DOCTYPE html&gt;</p>
          <p>... deine HTML hier ...</p>
          <p>EOF</p>
          
          <h2>🔗 API Endpoints</h2>
          <ul>
            <li>GET / → Dashboard HTML</li>
            <li>GET /api/design/templates → Templates</li>
            <li>POST /api/chat/principle → Principle Brain Chat</li>
          </ul>
        </div>
      </body>
      </html>
    `);
  }
});

// API Endpoints (für später)
app.get('/api/status', (req, res) => {
  res.json({
    status: 'online',
    port: 50000,
    timestamp: new Date().toISOString()
  });
});

const PORT = 50000;
app.listen(PORT, () => {
  console.log(`✅ Design System Server on ${PORT}`);
  console.log(`   🌐 http://localhost:${PORT}`);
  console.log(`   🌐 http://51.24.14.6:${PORT}`);
  console.log(`   📁 Warte auf: dashboard31.html`);
});
