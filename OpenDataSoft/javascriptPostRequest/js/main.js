// Works

var ourRequest = new XMLHttpRequest();
ourRequest.open('POST', 'https://cityofsalinas.opendatasoft.com/api/records/1.0/search/');
ourRequest.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
ourRequest.onload = function() {
  var ourData = JSON.parse(ourRequest.responseText);

  console.log(ourData);
};

ourRequest.send('dataset=anonymized-crime-data');

/*

// Doesn't work

var ourRequest = new XMLHttpRequest();
ourRequest.open('POST', 'https://cityofsalinas.opendatasoft.com/api/records/1.0/search/');
ourRequest.setRequestHeader('Content-type', 'application/json');
ourRequest.onload = function() {
  var ourData = JSON.parse(ourRequest.responseText);

  console.log(ourData);
};

// ourRequest.send('dataset=anonymized-crime-data'); // doesn't work
// ourRequest.send({dataset:'anonymized-crime-data'}); // doesn't work
ourRequest.send(JSON.stringify({dataset:'anonymized-crime-data'})); // doesn't work

*/

/*

// Doesn't work

var ourRequest = new XMLHttpRequest();
ourRequest.open('POST', 'https://cityofsalinas.opendatasoft.com/api/records/1.0/search/');
ourRequest.onload = function() {
  var ourData = JSON.parse(ourRequest.responseText);

  console.log(ourData);
};

// ourRequest.send('dataset=anonymized-crime-data'); // doesn't work
// ourRequest.send({dataset:'anonymized-crime-data'}); // doesn't work
ourRequest.send(JSON.stringify({dataset:'anonymized-crime-data'})); // doesn't work
*/