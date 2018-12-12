require(["esri/tasks/Locator"], function(Locator){

  locator = new Locator("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer");

  address = {
    SingleLine: "200 Lincoln Ave Salinas CA"
  };
  var options = {
    address: address,
    outFields: ["*"]
  };

  locator.addressToLocations(options).then(function(evt){
    console.log(evt);
  });

});