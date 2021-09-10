# Table of Contents

* [analysers.naming](#analysers.naming)
  * [NamingAnalyser](#analysers.naming.NamingAnalyser)
    * [check\_variable\_snake\_case](#analysers.naming.NamingAnalyser.check_variable_snake_case)
    * [check\_method\_snake\_case](#analysers.naming.NamingAnalyser.check_method_snake_case)
    * [check\_attribute\_snake\_case](#analysers.naming.NamingAnalyser.check_attribute_snake_case)
    * [check\_potential\_bad\_variable\_names](#analysers.naming.NamingAnalyser.check_potential_bad_variable_names)
    * [check\_hungarian\_notation\_variable](#analysers.naming.NamingAnalyser.check_hungarian_notation_variable)
    * [check\_hungarian\_notation\_attribute](#analysers.naming.NamingAnalyser.check_hungarian_notation_attribute)
    * [check\_hungarian\_notation\_method](#analysers.naming.NamingAnalyser.check_hungarian_notation_method)
    * [check\_constant\_naming](#analysers.naming.NamingAnalyser.check_constant_naming)

<a name="analysers.naming"></a>
# analysers.naming

Naming analyser, checks everything name related

<a name="analysers.naming.NamingAnalyser"></a>
## NamingAnalyser Objects

```python
class NamingAnalyser(Analyser)
```

Analyse good naming

<a name="analysers.naming.NamingAnalyser.check_variable_snake_case"></a>
#### check\_variable\_snake\_case

```python
 | @register_check(error_format="{}:{}: Non snake-case variable '{}':\n\t{}")
 | check_variable_snake_case()
```

Checks for non snake-case variable naming

<a name="analysers.naming.NamingAnalyser.check_method_snake_case"></a>
#### check\_method\_snake\_case

```python
 | @register_check(error_format="{}:{}: Non snake-case function/method name "
 |                                  "'{}':\n\t{}")
 | check_method_snake_case()
```

Checks for non snake-case function and method naming

<a name="analysers.naming.NamingAnalyser.check_attribute_snake_case"></a>
#### check\_attribute\_snake\_case

```python
 | @register_check(error_format="{}:{}: Non snake-case attribute '{}':\n\t{}")
 | check_attribute_snake_case()
```

Checks for non snake-case attribute naming

<a name="analysers.naming.NamingAnalyser.check_potential_bad_variable_names"></a>
#### check\_potential\_bad\_variable\_names

```python
 | @register_check(error_format="{}:{}: Potential bad variable name '{}':\n"
 |                                  "\t{}")
 | check_potential_bad_variable_names()
```

Checks for potential bad naming, i.e. names with 1-2 characters

<a name="analysers.naming.NamingAnalyser.check_hungarian_notation_variable"></a>
#### check\_hungarian\_notation\_variable

```python
 | @register_check(error_format="{}:{}: Hungarian notation variable '{}':\n"
 |                                  "\t{}")
 | check_hungarian_notation_variable()
```

Checks for variable names with hungarian notation

<a name="analysers.naming.NamingAnalyser.check_hungarian_notation_attribute"></a>
#### check\_hungarian\_notation\_attribute

```python
 | @register_check(error_format="{}:{}: Hungarian notation attribute '{}':\n"
 |                                  "\t{}")
 | check_hungarian_notation_attribute()
```

Checks for attribute names with hungarian notation

<a name="analysers.naming.NamingAnalyser.check_hungarian_notation_method"></a>
#### check\_hungarian\_notation\_method

```python
 | @register_check(error_format="{}:{}: Hungarian notation in function/method "
 |                                  "name '{}':\n\t{}")
 | check_hungarian_notation_method()
```

Checks for hungarian notation function and method naming

<a name="analysers.naming.NamingAnalyser.check_constant_naming"></a>
#### check\_constant\_naming

```python
 | @register_check("{}:{}: Variables defined at global scope should be "
 |                     "treated as constants:\n\t{}")
 | check_constant_naming()
```

Checks if constants are named in UPPER_SNAKE_CASE

