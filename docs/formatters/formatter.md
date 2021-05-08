# Table of Contents

* [formatters.formatter](#formatters.formatter)
  * [Formatter](#formatters.formatter.Formatter)
    * [\_\_init\_\_](#formatters.formatter.Formatter.__init__)
    * [format](#formatters.formatter.Formatter.format)
    * [get\_config](#formatters.formatter.Formatter.get_config)
    * [get\_check\_output](#formatters.formatter.Formatter.get_check_output)

<a name="formatters.formatter"></a>
# formatters.formatter

Abstract formatter
Used to convert error outputs to user friendly output to be displayed on user
interface

<a name="formatters.formatter.Formatter"></a>
## Formatter Objects

```python
class Formatter()
```

Abstract formatter

<a name="formatters.formatter.Formatter.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(config: Config, check_output: CheckOutput)
```

Constructor

**Arguments**:

- `config` - configuration file that links criteria to tests
- `check_output` - output from checkers

<a name="formatters.formatter.Formatter.format"></a>
#### format

```python
 | format() -> str
```

Returns formatted string to be displayed on screen

<a name="formatters.formatter.Formatter.get_config"></a>
#### get\_config

```python
 | get_config() -> Config
```

Returns configuration object

<a name="formatters.formatter.Formatter.get_check_output"></a>
#### get\_check\_output

```python
 | get_check_output()
```

Returns check output from analysers

