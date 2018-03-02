var outDiv = $("#outputDiv")[0];

$(window).on("load", function(){
   main();
});

function main(){
   //outDiv.insertAdjacentHTML('beforeend', "sdfasdfadsfasdfadsfer ffffffffffffffffffffffffffff");

   var request = new XMLHttpRequest();
   
   var addressToQuery = "243 cross ave salinas";
   var queryString = "https://maps.googleapis.com/maps/api/geocode/json?&address=";
   var apiKeyString = "&key=";

   queryString += addressToQuery + apiKeyString;

   request.open("GET", queryString);
   request.onload = function(){
      var jsonData = JSON.parse(request.responseText);
      console.log(jsonData);
   };

   request.send();
}