# Table of Contents

* [analysers.class\_instance](#analysers.class_instance)
  * [ClassInstanceAnalyser](#analysers.class_instance.ClassInstanceAnalyser)
    * [check\_method\_call](#analysers.class_instance.ClassInstanceAnalyser.check_method_call)

<a name="analysers.class_instance"></a>
# analysers.class\_instance

Analyser for class vs instance usage

<a name="analysers.class_instance.ClassInstanceAnalyser"></a>
## ClassInstanceAnalyser Objects

```python
class ClassInstanceAnalyser(Analyser)
```

Checks violations in class vs instance usages

<a name="analysers.class_instance.ClassInstanceAnalyser.check_method_call"></a>
#### check\_method\_call

```python
 | @register_check("Line {}: Method call treated as function instead of "
 |                     "member of instance:\n\t{}")
 | check_method_call()
```

Checks if method call is treated as regular function instead of
member of class instance

