# Table of Contents

* [analysers.docstrings](#analysers.docstrings)
  * [DocstringAnalyser](#analysers.docstrings.DocstringAnalyser)
    * [check\_class\_docstrings](#analysers.docstrings.DocstringAnalyser.check_class_docstrings)
    * [check\_methods\_function\_docstrings](#analysers.docstrings.DocstringAnalyser.check_methods_function_docstrings)
    * [check\_method\_docstring\_unexpected\_missing](#analysers.docstrings.DocstringAnalyser.check_method_docstring_unexpected_missing)
    * [check\_method\_docstring\_missing\_type](#analysers.docstrings.DocstringAnalyser.check_method_docstring_missing_type)
    * [check\_docstring\_correct\_format](#analysers.docstrings.DocstringAnalyser.check_docstring_correct_format)

<a name="analysers.docstrings"></a>
# analysers.docstrings

Docstring analyser

<a name="analysers.docstrings.DocstringAnalyser"></a>
## DocstringAnalyser Objects

```python
class DocstringAnalyser(Analyser)
```

Analyses anything docstring related

<a name="analysers.docstrings.DocstringAnalyser.check_class_docstrings"></a>
#### check\_class\_docstrings

```python
 | @register_check("{}:{}: Class {} missing docstring")
 | check_class_docstrings()
```

Checks if classes missing docstrings

<a name="analysers.docstrings.DocstringAnalyser.check_methods_function_docstrings"></a>
#### check\_methods\_function\_docstrings

```python
 | @register_check("{}:{}: Method/Function {} missing docstring")
 | check_methods_function_docstrings()
```

Checks if methods or functions missing docstrings

<a name="analysers.docstrings.DocstringAnalyser.check_method_docstring_unexpected_missing"></a>
#### check\_method\_docstring\_unexpected\_missing

```python
 | @register_check("{}:{}: Missing/extra fields in docstrings of "
 |                     "function/method:\n"
 |                     "\tFunction/Method name: {}\n"
 |                     "\tMissing fields: {}\n"
 |                     "\tExtra fields: {}\n")
 | check_method_docstring_unexpected_missing()
```

Checks if docstring has missing or extra fields

<a name="analysers.docstrings.DocstringAnalyser.check_method_docstring_missing_type"></a>
#### check\_method\_docstring\_missing\_type

```python
 | @register_check("{}:{}: Missing parameter types in docstrings of "
 |                     "function/method:"
 |                     "\n\tFunction/Method name: {}\n"
 |                     "\tFields that lack param type: {}\n")
 | check_method_docstring_missing_type()
```

Checks if docstrings have all the parameter types necessary

<a name="analysers.docstrings.DocstringAnalyser.check_docstring_correct_format"></a>
#### check\_docstring\_correct\_format

```python
 | @register_check("{}:{}: Cannot parse docstring of function/method:\n"
 |                     "\t{}")
 | check_docstring_correct_format()
```

Checks if docstring can be parsed correctly

