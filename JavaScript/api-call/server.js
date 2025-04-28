const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
const port = 3000;

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


