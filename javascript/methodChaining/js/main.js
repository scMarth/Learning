var Kitten = function() {
    this.name = 'Garfield';
    this.color = 'brown';
    this.gender = 'male';
};

Kitten.prototype.setName = function(name) {
    this.name = name;
    return this;
};

Kitten.prototype.setColor = function(color) {
    this.color = color;
    return this;
};

Kitten.prototype.setGender = function(gender) {
    this.gender = gender;
    return this;
};

Kitten.prototype.save = function() {
    console.log(
        'saving ' + this.name + ', the ' +
        this.color + ' ' + this.gender + ' kitten...'
    );

    // save to database here...

    return this;
};


// Without Chaining
var bob = new Kitten();
bob.setName('Bob');
bob.setColor('black');
bob.setGender('male');
bob.save();

// With Chaining
new Kitten() // but you can't reference this variable later
  .setName('Bob2')
  .setColor('black')
  .setGender('male')
  .save();

var bastwick = new Kitten() // you can use chaining and still reference this var later
  .setName('Bastwick')
  .setColor('leapord')
  .setGender('male')
  .save();

console.log(bob);
console.log(bastwick);

