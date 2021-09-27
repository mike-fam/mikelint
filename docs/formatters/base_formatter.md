# Table of Contents

* [formatters.base\_formatter](#formatters.base_formatter)
  * [SimpleFormatter](#formatters.base_formatter.SimpleFormatter)
    * [format\_violation](#formatters.base_formatter.SimpleFormatter.format_violation)

<a name="formatters.base_formatter"></a>
# formatters.base\_formatter

A simple formatter to display analyser output in similar format as testrunner

<a name="formatters.base_formatter.SimpleFormatter"></a>
## SimpleFormatter Objects

```python
class SimpleFormatter(Formatter)
```

Simple formatter with output similar to testrunner

<a name="formatters.base_formatter.SimpleFormatter.format_violation"></a>
#### format\_violation

```python
 | @staticmethod
 | format_violation(violation: BaseViolation)
```

Gets a meaningful string containing information about a violation

**Arguments**:

- `violation` - BaseViolation information
  
- `Returns` - a meaningful string containing information about a violation

