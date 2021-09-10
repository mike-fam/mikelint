# Table of Contents

* [analysers.scope](#analysers.scope)
  * [ScopeAnalyser](#analysers.scope.ScopeAnalyser)
    * [check\_globals](#analysers.scope.ScopeAnalyser.check_globals)
    * [check\_magic\_numbers\_used](#analysers.scope.ScopeAnalyser.check_magic_numbers_used)

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
 | @register_check("{}:{}: Globals used:\n\t{}")
 | check_globals()
```

Checks if code has any global variables

<a name="analysers.scope.ScopeAnalyser.check_magic_numbers_used"></a>
#### check\_magic\_numbers\_used

```python
 | @register_check("{}:{}: Magic number used\n\t{}")
 | check_magic_numbers_used()
```

Check if any magic number has been used

