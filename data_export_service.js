const express = require('express');
const app = express();

app.use(express.json());

// Export Customer Data (NO AI/System tech)
app.post('/api/export/customer-data', (req, res) => {
  const { customerId, format } = req.body;
  
  // Export nur Kundendaten
  const exportData = {
    customerId,
    dataPoints: 1250,
    projects: 5,
    chat_history: 340,
    timestamp: new Date().toISOString(),
    format: format || 'json'
  };
  
  res.json({
    status: 'ready',
    exportData,
    download_url: `/exports/${customerId}_${Date.now()}.zip`,
    message: 'Only customer data exported. No system technology included.'
  });
});

// Customer SOT Template (leere Master-Struktur)
app.get('/api/sot/customer-template', (req, res) => {
  const sotTemplate = {
    version: '1.0.0',
    timestamp: new Date().toISOString(),
    customer: {
      id: 'customer_xxx',
      name: 'Your Company',
      region: 'EU',
      endpoints: []
    },
    data_schema: {
      users: [],
      projects: [],
      transactions: [],
      analytics: []
    },
    monitoring: {
      enabled: true,
      api_key: 'your_monitoring_key',
      endpoints: [
        'https://monitor.systemai.io/api/health',
        'https://monitor.systemai.io/api/logs'
      ]
    },
    note: 'This is an empty master SOT template. Fill it with your own data and run independently.'
  };
  
  res.json(sotTemplate);
});

app.listen(8002, () => console.log('✅ Data Export Service on 8002'));
