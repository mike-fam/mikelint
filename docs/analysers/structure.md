# Table of Contents

* [analysers.structure](#analysers.structure)
  * [StructureAnalyser](#analysers.structure.StructureAnalyser)
    * [check\_line\_length](#analysers.structure.StructureAnalyser.check_line_length)
    * [check\_structure\_complexity](#analysers.structure.StructureAnalyser.check_structure_complexity)
    * [check\_structure\_empty](#analysers.structure.StructureAnalyser.check_structure_empty)
    * [check\_redundant\_boolean\_equality](#analysers.structure.StructureAnalyser.check_redundant_boolean_equality)

<a name="analysers.structure"></a>
# analysers.structure

Analyses code structure

<a name="analysers.structure.StructureAnalyser"></a>
## StructureAnalyser Objects

```python
class StructureAnalyser(Analyser)
```

Structure analyser, checks if general structure is ok

<a name="analysers.structure.StructureAnalyser.check_line_length"></a>
#### check\_line\_length

```python
 | @register_check("{3}: Number of lines longer than {0} characters: {1}\n"
 |                     "\tLines {2} are longer than {0} characters")
 | check_line_length()
```

Checks if code has any line that's too long

<a name="analysers.structure.StructureAnalyser.check_structure_complexity"></a>
#### check\_structure\_complexity

```python
 | @register_check("{}:{}-{}: too many nested control structures\n{}")
 | check_structure_complexity()
```

Checks if control structures are nested too deeply

<a name="analysers.structure.StructureAnalyser.check_structure_empty"></a>
#### check\_structure\_empty

```python
 | @register_check("{}:{}: Control structure block does nothing\n")
 | check_structure_empty()
```

Checks if control structures blocks just have `pass` in them

<a name="analysers.structure.StructureAnalyser.check_redundant_boolean_equality"></a>
#### check\_redundant\_boolean\_equality

```python
 | @register_check("{}:{}: Redundant boolean (in)equality\n{}")
 | check_redundant_boolean_equality()
```

Check for condition == True or condition == False

