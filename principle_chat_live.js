const express = require('express');
const app = express();

app.use(express.json());

// ============ PRINCIPLE BRAIN CHAT ============
app.post('/api/chat/principle', async (req, res) => {
  const { message, userId, context } = req.body;

  if (!message) {
    return res.status(400).json({ error: 'Message required' });
  }

  // SYSTEMAI PROCESSING
  const response = await processWithPrinciple(message, context);

  res.json({
    success: true,
    message: message,
    userId: userId || 'anonymous',
    response: response.text,
    action: response.action,
    data: response.data,
    timestamp: new Date().toISOString()
  });
});

// ============ CHAT CONTEXT ============
app.post('/api/chat/context/set', (req, res) => {
  const { userId, workspace, tenant, context } = req.body;
  
  // Speichere Context für User-Session
  const session = {
    userId,
    workspace,
    tenant,
    context,
    createdAt: new Date().toISOString()
  };

  res.json({
    success: true,
    session: session,
    message: 'Context set for chat'
  });
});

// ============ CHAT HISTORY ============
app.get('/api/chat/history/:userId', (req, res) => {
  // Mock: würde aus DB kommen
  res.json({
    userId: req.params.userId,
    messages: [
      {
        role: 'user',
        message: 'Erstelle einen Report für Mandant NEURO-GLOBAL',
        timestamp: new Date(Date.now() - 3600000).toISOString()
      },
      {
        role: 'principle',
        message: 'Report erstellt: 312 aktive Mandanten, € 842,3 Mio Umsatz',
        action: 'generate_report',
        timestamp: new Date(Date.now() - 3500000).toISOString()
      }
    ]
  });
});

// ============ SYSTEM MONITORING + AUTOFIX ============
app.post('/api/system/monitor', async (req, res) => {
  const { workspace, action } = req.body;

  // MONITOR MODE: Überwache System & erkenne Probleme
  const status = await monitorSystem();

  if (status.issues.length > 0 && action === 'autofix') {
    // AUTOFIX MODE: Behebe Probleme automatisch
    const fixes = await autoFixIssues(status.issues);
    return res.json({
      mode: 'AUTOFIX',
      issues: status.issues,
      fixes: fixes,
      timestamp: new Date().toISOString()
    });
  }

  res.json({
    mode: 'MONITOR',
    status: status,
    timestamp: new Date().toISOString()
  });
});

// ============ DUMMY FUNCTIONS ============

async function processWithPrinciple(message, context) {
  // Parse user intent
  const intent = parseIntent(message);

  // Route zu richtigem Handler
  let response;
  
  if (intent.type === 'report') {
    response = await generateReport(intent);
  } else if (intent.type === 'search') {
    response = await searchData(intent);
  } else if (intent.type === 'config') {
    response = await updateConfig(intent);
  } else if (intent.type === 'onboarding') {
    response = await startOnboarding(intent);
  } else {
    response = await generalChat(message);
  }

  return response;
}

function parseIntent(message) {
  const lower = message.toLowerCase();
  
  if (lower.includes('report') || lower.includes('zusammenfassung')) {
    return { type: 'report', entity: extractEntity(message) };
  }
  if (lower.includes('suche') || lower.includes('find')) {
    return { type: 'search', query: message };
  }
  if (lower.includes('config') || lower.includes('einstell')) {
    return { type: 'config', setting: extractEntity(message) };
  }
  if (lower.includes('onboarding') || lower.includes('neu')) {
    return { type: 'onboarding', entity: extractEntity(message) };
  }
  
  return { type: 'general', query: message };
}

function extractEntity(message) {
  const entities = ['mandant', 'project', 'user', 'tenant', 'benutzer'];
  for (let e of entities) {
    if (message.toLowerCase().includes(e)) return e;
  }
  return 'unknown';
}

async function generateReport(intent) {
  return {
    text: `📊 Report für ${intent.entity}:\n- Aktive Mandanten: 312\n- Globaler Umsatz: € 842,3 Mio\n- Systemalarme: 3\n- Auslastung: 86%`,
    action: 'display_report',
    data: {
      type: 'report',
      entity: intent.entity,
      format: 'json'
    }
  };
}

async function searchData(intent) {
  return {
    text: `🔍 Suchergebnisse für: ${intent.query}`,
    action: 'display_results',
    data: {
      query: intent.query,
      results: []
    }
  };
}

async function updateConfig(intent) {
  return {
    text: `⚙️ Konfiguration aktualisiert: ${intent.setting}`,
    action: 'update_config',
    data: {
      setting: intent.setting,
      status: 'success'
    }
  };
}

async function startOnboarding(intent) {
  return {
    text: `🚀 Onboarding-Assistent gestartet für ${intent.entity}`,
    action: 'start_wizard',
    data: {
      wizard: 'onboarding',
      step: 1,
      steps: 5
    }
  };
}

async function generalChat(message) {
  return {
    text: `Ich bin Principle Brain. Ich kann dir helfen mit Reports, Suche, Konfiguration und Onboarding. Frag mich einfach!`,
    action: 'general_response',
    data: {}
  };
}

async function monitorSystem() {
  return {
    healthy: true,
    issues: [
      // { id: 'API_LATENCY', severity: 'low', message: 'API Response Zeit > 500ms' }
    ],
    services: {
      backend: 'healthy',
      database: 'healthy',
      cache: 'healthy'
    }
  };
}

async function autoFixIssues(issues) {
  return issues.map(issue => ({
    issue: issue.id,
    action: 'AUTO_FIX_APPLIED',
    result: 'success'
  }));
}

// ============ WORKSPACE INTEGRATION ============

// Mandanten Workspace
app.get('/api/workspace/mandanten', (req, res) => {
  res.json({
    workspace: 'mandanten',
    title: 'Mandanten & Projekte',
    description: 'Mandantenverwaltung mit AI-Unterstützung',
    chatEnabled: true,
    chatPrompt: 'Frag mich nach Mandanten, Projekten oder Onboarding',
    sections: [
      {
        id: 'mandanten-overview',
        title: 'Mandantenübersicht',
        template: 'tenantCard',
        dataSource: '/api/tenants'
      },
      {
        id: 'projekte',
        title: 'Projekte',
        template: 'tableTemplate',
        dataSource: '/api/projects'
      },
      {
        id: 'onboarding',
        title: 'Onboarding-Assistent',
        template: 'accordionTemplate',
        chatIntegration: true
      }
    ]
  });
});

// Technologie Workspace
app.get('/api/workspace/system-technik', (req, res) => {
  res.json({
    workspace: 'system-technik',
    title: 'System & Technik',
    description: 'Monitoring, AutoFix, Performance',
    chatEnabled: true,
    monitorMode: true,
    sections: [
      {
        id: 'system-health',
        title: 'System Health',
        template: 'kpiCard',
        monitoring: true
      },
      {
        id: 'alerts',
        title: 'Systemalarme',
        template: 'tableTemplate',
        autoFixAvailable: true
      }
    ]
  });
});

app.listen(8001, () => {
  console.log('✅ Principle Brain Chat LIVE on 8001');
  console.log('   💬 POST /api/chat/principle');
  console.log('   🔄 POST /api/system/monitor');
  console.log('   📊 GET /api/workspace/:id');
});
