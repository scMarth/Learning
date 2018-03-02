var outDiv = $("#outputDiv")[0];

$(window).on("load", function(){
   main();
});

function convertSpacesForQuery(str){
   var result = "";
   for (var i=0; i<str.length; i++){
      if (str[i] != " "){
         result += str[i];
      }else{
         result += "%20";
      }
   }
   return result;
}

function main(){
   //outDiv.insertAdjacentHTML('beforeend', "sdfasdfadsfasdfadsfer ffffffffffffffffffffffffffff");

   var request = new XMLHttpRequest();

   var addressToQuery = "243 cross ave salinas";
   var queryString = "https://maps.googleapis.com/maps/api/geocode/json?&address=";
   var apiKeyString = "&key=";

   queryString += convertSpacesForQuery(addressToQuery) + apiKeyString;
   console.log(queryString);

   request.open("GET", queryString);
   request.onload = function(){
      var jsonData = JSON.parse(request.responseText);
      console.log(jsonData.results[0].formatted_address);

   };

   request.send();
}