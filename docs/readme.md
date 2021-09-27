# How this works
This project utilises the [astroid](http://pylint.pycqa.org/projects/astroid/en/latest/)
package, which is a library wrapping the built-in [ast](https://docs.python.org/3/library/ast.html)
module. AST provides a toolbox to process trees of the Python abstract syntax grammar.

## Analysers
Analysers are classes that directly perform static analysis on the target file. 
The analysers are defined in the `analysers` package. All analysers must be subclasses 
of the `Analyser` class in `analysers.Analyser`. There are currently 6 analysers, namely:
* `ClassInstanceAnalyser`
* `DocstringAnalyser`
* `EncapsulationAnalyser`
* `NamingAnalyser`
* `ScopeAnalyser`
* `StructureAnalyser`

### Implementation
To define a new analyser, write a new class that's a subclass of `Analyser`. An analyser
class **must** have a docstring to explain what that analyser is used for. The docstring
will be included in the final analyser output.

Analysers have *checkers*, which are methods that analyse the source code, similar to
how unit test cases have test methods. Checker methods **should** have their name
starting with `check_` and **must** be under the `register_check` decorator. The checkers
must satisfy the following criteria:

1. The argument passed to the `@register_check` decorator is a format template string.

2. The checker method must return a list of tuples, each tuple containing values that
    need to be formatted in the template string.
   
3. They must take in no arguments other than `self`.
   
See the following analyser for example
```python
# remember to inherit from Analyser
class FooAnalyser(Analyser): 
    """Analyser description, required"""
    @register_check("Violation found:\n    Line {}: {}")
    def check_something(self):
        """Checker description"""
        # return a list of values that can be used to format the string above
        return [(23, "x = 3"), (34, "a = 4")]
```

To help you analyse the source code more easily, analysers have these helper attributes:
* `_tree`: A `SyntaxTree` object, defined in `utils.tree`. You can perform preorder
    traversal and postorder traversal on the nodes using this object.
  
* `_source`: A list of strings, with each string being a line in the source code.

The analysers have a `get_results` method, which returns an `AnalyserResult`, which is
a dictionary with keys as the names of the checkers and values as a list of violations
found by the corresponding checker.

## Formatters
Formatters take the output from analysers and converts it to a user-friendly string.
All formatters must be subclasses of the abstract class `Formatter`, in 
`linter.formatters.formatter_`. There are currently a single formatter, 
namely `SimpleFormatter`.

### Implementation
All formatters must override the `format` method from the abstract superclass.
Formatters have an attribute called `_check_output`, which is a dictionary with 
keys as the names of the analysers, and values as the result of the corresponding
analyser, as described above. You need to convert this information to a human 
friendly string and return that string in the `format` method.
