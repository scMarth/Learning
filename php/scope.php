<?php

/*

// https://stackoverflow.com/questions/16959576/reference-what-is-variable-scope-which-variables-are-accessible-from-where-and

How is a scope defined in PHP?

Very simple: PHP has function scope. That's the only kind of scope separator that exists in PHP. Variables inside a function are only available inside that function. Variables outside of functions are available anywhere outside of functions, but not inside any function. This means there's one special scope in PHP: the global scope. Any variable declared outside of any function is within this global scope.

*/


$foo = 'bar';

function myFunc() {
    $baz = 42;

/*

$foo is in the global scope, $baz is in a local scope inside myFunc. Only code inside myFunc has access to $baz. Only code outside myFunc has access to $foo. Neither has access to the other:

*/

$foo = 'bar';

function myFunc() {
    $baz = 42;

    echo $foo;  // doesn't work
    echo $baz;  // works
}

echo $foo;  // works
echo $baz;  // doesn't work



/*

File boundaries do not separate scope:

a.php

<?php

$foo = 'bar';

---------------------------

b.php

<?php

include 'a.php';

echo $foo;  // works!

The same rules apply to included code as applies to any other code: only functions separate scope. For the purpose of scope, you may think of including files like copy and pasting code:

c.php

<?php

function myFunc() {
    include 'a.php';

    echo $foo;  // works
}

myFunc();

echo $foo;  // doesn't work!

Every new function declaration introduces a new scope, it's that simple.

(anonymous) functions inside functions
function foo() {
    $foo = 'bar';

    $bar = function () {
        // no access to $foo
        $baz = 'baz';
    };

    // no access to $baz
}

Extending the scope of variables into anonymous functions
$foo = 'bar';

$baz = function () use ($foo) {
    echo $foo;
};

$baz();
The anonymous function explicitly includes $foo from its surrounding scope. Note that this is not the same as global scope.

The wrong way: global
As said before, the global scope is somewhat special, and functions can explicitly import variables from it:

$foo = 'bar';

function baz() {
    global $foo;
    echo $foo;
    $foo = 'baz';
}
This function uses and modifies the global variable $foo. Do not do this! (Unless you really really really really know what you're doing, and even then: don't!)

All the caller of this function sees is this:

baz(); // outputs "bar"
unset($foo);
baz(); // no output, WTF?!
baz(); // outputs "baz", WTF?!?!!
There's no indication that this function has any side effects, yet it does. This very easily becomes a tangled mess as some functions keep modifying and requiring some global state. You want functions to be stateless, acting only on their inputs and returning defined output, however many times you call them.

You should avoid using the global scope in any way as much as possible; most certainly you should not be "pulling" variables out of the global scope into a local scope.

*/

?>

