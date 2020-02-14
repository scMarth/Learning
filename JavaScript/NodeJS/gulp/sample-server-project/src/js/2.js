saySomething(test, second);
console.log('What it do playa');
console.log('Hey alright');

$.getJSON("./json/data.json", function(data){
    console.log(data);
}).fail(function(){
    console.log('error getting data.json');
});