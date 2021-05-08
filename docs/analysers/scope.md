# Table of Contents

* [analysers.scope](#analysers.scope)
  * [ScopeAnalyser](#analysers.scope.ScopeAnalyser)
    * [check\_globals](#analysers.scope.ScopeAnalyser.check_globals)
    * [check\_constants\_used](#analysers.scope.ScopeAnalyser.check_constants_used)

<a name="analysers.scope"></a>
# analysers.scope

Analyse scope violations

<a name="analysers.scope.ScopeAnalyser"></a>
## ScopeAnalyser Objects

```python
class ScopeAnalyser(Analyser)
```

Analyser checking for scope violations

<a name="analysers.scope.ScopeAnalyser.check_globals"></a>
#### check\_globals

```python
 | @register_check("Globals used on line {}:\n\t{}")
 | check_globals()
```

Checks if code has any global variables

<a name="analysers.scope.ScopeAnalyser.check_constants_used"></a>
#### check\_constants\_used

```python
 | @register_check("Line {}: Magic values used\n\t{}")
 | check_constants_used()
```

Check if any value that could have been used as constants

