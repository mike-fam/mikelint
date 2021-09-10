# Table of Contents

* [analysers.encapsulation](#analysers.encapsulation)
  * [EncapsulationAnalyser](#analysers.encapsulation.EncapsulationAnalyser)
    * [check\_private\_attribute\_accessed\_outside\_class](#analysers.encapsulation.EncapsulationAnalyser.check_private_attribute_accessed_outside_class)
    * [check\_private\_attribute\_defined\_outside\_class](#analysers.encapsulation.EncapsulationAnalyser.check_private_attribute_defined_outside_class)
    * [check\_public\_attribute\_defined\_self](#analysers.encapsulation.EncapsulationAnalyser.check_public_attribute_defined_self)

<a name="analysers.encapsulation"></a>
# analysers.encapsulation

Analyse encapsulation violations

<a name="analysers.encapsulation.EncapsulationAnalyser"></a>
## EncapsulationAnalyser Objects

```python
class EncapsulationAnalyser(Analyser)
```

Encapsulation analyser, checks if class members follow best
access control practices

<a name="analysers.encapsulation.EncapsulationAnalyser.check_private_attribute_accessed_outside_class"></a>
#### check\_private\_attribute\_accessed\_outside\_class

```python
 | @register_check("{}:{}: Private attribute `{}` accessed outside class:\n"
 |                     "\t{}")
 | check_private_attribute_accessed_outside_class()
```

Checks if private attribute is accessed outside class

<a name="analysers.encapsulation.EncapsulationAnalyser.check_private_attribute_defined_outside_class"></a>
#### check\_private\_attribute\_defined\_outside\_class

```python
 | @register_check("{}:{}: Private attribute `{}` defined outside class:\n"
 |                     "\t{}")
 | check_private_attribute_defined_outside_class()
```

Checks if private attribute is defined outside class

<a name="analysers.encapsulation.EncapsulationAnalyser.check_public_attribute_defined_self"></a>
#### check\_public\_attribute\_defined\_self

```python
 | @register_check("{}:{}: Public attribute `{}` could have been private:\n"
 |                     "\t{}")
 | check_public_attribute_defined_self()
```

Checks if public attribute could be replaced by a private attribute

