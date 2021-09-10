# Table of Contents

* [analysers.analyser](#analysers.analyser)
  * [register\_check](#analysers.analyser.register_check)
  * [Analyser](#analysers.analyser.Analyser)
    * [\_\_init\_\_](#analysers.analyser.Analyser.__init__)
    * [register\_checker](#analysers.analyser.Analyser.register_checker)
    * [get\_results](#analysers.analyser.Analyser.get_results)
    * [add\_violations](#analysers.analyser.Analyser.add_violations)
    * [get\_line](#analysers.analyser.Analyser.get_line)
    * [run](#analysers.analyser.Analyser.run)

<a name="analysers.analyser"></a>
# analysers.analyser

Abstract analyser

<a name="analysers.analyser.register_check"></a>
#### register\_check

```python
register_check(error_format: str)
```

Registers a new checker to an analyser

**Arguments**:

- `error_format` - error format of violation

<a name="analysers.analyser.Analyser"></a>
## Analyser Objects

```python
class Analyser()
```

Abstract base analyser

<a name="analysers.analyser.Analyser.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(sources: dict[str, AnalyserHelper])
```

Constructor

**Arguments**:

- `tree` - syntax tree
- `source` - list of lines from source code

<a name="analysers.analyser.Analyser.register_checker"></a>
#### register\_checker

```python
 | register_checker(name: str, description: str, error_format: str)
```

Registers a new checker to this analyser

**Arguments**:

- `name` - name of the checker, typically the method name
- `description` - description of this checker
- `error_format` - format string used to display violations

<a name="analysers.analyser.Analyser.get_results"></a>
#### get\_results

```python
 | get_results() -> AnalyserResults
```

Returns results of all checkers of this analyser

<a name="analysers.analyser.Analyser.add_violations"></a>
#### add\_violations

```python
 | add_violations(checker_name: str, results: list[ViolationResult]) -> None
```

Adds violation results to a checker

**Arguments**:

- `checker_name` - name of the checker
- `results` - list of violation results

<a name="analysers.analyser.Analyser.get_line"></a>
#### get\_line

```python
 | get_line(file_name: str, line_number: int) -> str
```

Returns line given line number

<a name="analysers.analyser.Analyser.run"></a>
#### run

```python
 | run()
```

Runs all checkers

