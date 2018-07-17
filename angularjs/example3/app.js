var Person = function(firstname, lastname){
   this.firstname = firstname;
   this.lastname = lastname;
}
/*
// THIS IS BAD

function logPerson(){
   var john = new Person('John', 'Doe');
   console.log(john);
}
*/

function logPerson(person){
   console.log(person)
}

var john = new Person('John', 'Doe');
logPerson(john);