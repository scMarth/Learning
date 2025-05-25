const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
const port = 3000;

const sql = require('mssql');
// SQL Server configuration
const config = {
  user: process.env.LOCAL_SQLEXPRESS_USER,
  password: process.env.LOCAL_SQLEXPRESS_PW,
  database: 'FamilyTree',
  server: 'localhost',
  port: 1433,
  options: {
    trustServerCertificate: true,
    trustedConnection: false, // Set to true if using Windows Authentication
    encrypt: false // for azure
  },
};


async function getMembers(){
  try {
    // Connect to the database
    const pool = await sql.connect(config);
    const result = await pool.request().query('select * from Members');
    console.log(result);

    return result.recordset;
  } catch (err) {
    console.error('SQL error', err);
    throw err;
  }
}

app.get('/api/members', async (req, res) => {
  try {
    const members = await getMembers();
    res.json(members);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch members from database' });
  }
});

// Serve static files from public folder
app.use(express.static(path.join(__dirname, 'public')));

// Secrets (use .env in real projects)
const arcgisUsername = process.env.ATLAS_INTEGRATION_USER;
const arcgisPassword = process.env.DEV1_ATLAS_INTEGRATION_PASSWORD;
const portalUrl = process.env.DEV1_PORTAL_URL;

// Helper: get token
async function getToken() {
  const url = `${portalUrl}/tokens/generateToken`;

  const params = new URLSearchParams();
  params.append('username', arcgisUsername);
  params.append('password', arcgisPassword);
  params.append('client', 'requestip');
  params.append('f', 'json');

  const response = await axios.post(url, params);
  return response.data.token;
}

// API route
app.get('/api/family-data', async (req, res) => {
  try {
    // console.log('trying to get the token');
    const token = await getToken();
    console.log('got the token:', token);

    const layerUrl = `${portalUrl}/rest/services/RBA/ReceiptByApplication/FeatureServer/1/query`;
    console.log('layerUrl', layerUrl);

    const params = new URLSearchParams();
    params.append('where', '1=1');
    params.append('outFields', '*');
    params.append('token', token);
    params.append('f', 'json');


    const response = await axios.post(layerUrl, params);
    console.log('response:', response.data.features);
    res.json(response.data.features);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to fetch family data' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Backend server running at http://localhost:${port}`);
});

