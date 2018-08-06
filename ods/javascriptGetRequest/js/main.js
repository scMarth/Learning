var outDiv = $('#outDiv')[0];

var ourRequest = new XMLHttpRequest();
ourRequest.open('GET', 'https://data.opendatasoft.com/api/records/1.0/search/?dataset=marktacke-yta%40helsingborg');
ourRequest.onload = function() {
  var ourData = JSON.parse(ourRequest.responseText);

  console.log(ourData);
};
ourRequest.send();