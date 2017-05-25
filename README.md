# PyScript
PyScript is an alternative syntax and interpreter for Python, allowing for the writing of 'minified' Python. The syntax is distinctly JavaScript-like.

### Why?
Because whitespace dependency is dumb and Guido should have never made Python that way. This aims to put a bandaid over that gross oversight.

### Syntax
```
# comments can use either hashes
// C-style comments
''' python-style multi-line comments '''
/* or C-style multi-line comments

// classes are defined like JS objects
class doSomething () {
    // code here
}

// functions are the same
def something() {
    // code here
}

// conditiionals are of a similar pattern
if ( some == test ) {
    // do the thing
}
```