var outDiv = $('#outDiv')[0];

var ourRequest = new XMLHttpRequest();
ourRequest.open('GET', 'https://cityofsalinas.opendatasoft.com/api/records/1.0/search/?dataset=libraries&sort=libraryname&facet=apn&facet=libraryname')
ourRequest.onload = function() {
  var ourData = JSON.parse(ourRequest.responseText);

  output = "";

  output += ourData.records[0].fields.libraryname + "<br>";
  output += ourData.records[1].fields.libraryname + "<br>";
  output += ourData.records[2].fields.libraryname + "<br>";

  outDiv.innerHTML = output;

  console.log(ourData);
};
ourRequest.send();