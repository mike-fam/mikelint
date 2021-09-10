# Table of Contents

* [formatters.formatter\_](#formatters.formatter_)
  * [Formatter](#formatters.formatter_.Formatter)
    * [\_\_init\_\_](#formatters.formatter_.Formatter.__init__)
    * [format](#formatters.formatter_.Formatter.format)
    * [get\_config](#formatters.formatter_.Formatter.get_config)
    * [get\_check\_output](#formatters.formatter_.Formatter.get_check_output)

<a name="formatters.formatter_"></a>
# formatters.formatter\_

Abstract formatter
Used to convert error outputs to user friendly output to be displayed on user
interface

<a name="formatters.formatter_.Formatter"></a>
## Formatter Objects

```python
class Formatter()
```

Abstract formatter

<a name="formatters.formatter_.Formatter.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(config: Config, check_output: CheckOutput)
```

Constructor

**Arguments**:

- `config` - configuration file that links criteria to tests
- `check_output` - output from checkers

<a name="formatters.formatter_.Formatter.format"></a>
#### format

```python
 | format() -> str
```

Returns formatted string to be displayed on screen

<a name="formatters.formatter_.Formatter.get_config"></a>
#### get\_config

```python
 | get_config() -> Config
```

Returns configuration object

<a name="formatters.formatter_.Formatter.get_check_output"></a>
#### get\_check\_output

```python
 | get_check_output()
```

Returns check output from analysers

