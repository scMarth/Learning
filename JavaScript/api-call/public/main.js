// following calls ArcGIS REST API
// fetch('/api/family-data')
//   .then(response => response.json())  // <-- convert the response into JSON
//   .then(data => {
//     console.log('family data:', data); // <-- now you will see the actual features!
//   })
//   .catch(error => console.error('Error fetching family data:', error));

// database query
fetch('/api/members')
  .then(res => res.json())
  .then(data => console.log(data));