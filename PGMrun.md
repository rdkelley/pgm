```python
from pgmpy.factors.discrete import TabularCPD
```

```python
from pgmpy.models import BayesianModel
```

```python
model = BayesianModel([
    ("Difficulty", "Grade"), 
    ("Intelligence", "Grade"), 
    ("Grade", "Letter"),
    ("Intelligence", "SAT")
])
```

```python
difficulty_cpd = TabularCPD(variable = "Difficulty", variable_card = 2, values = [[.6],[.4]])
```

```python
intelligence_cpd = TabularCPD(variable = "Intelligence", variable_card = 2, values = [[.7],[.3]])
```

```python
sat_cpd = TabularCPD(variable = "SAT", 
                     variable_card = 2, 
                     evidence = ["Intelligence"], 
                     evidence_card = [2], 
                     values = [[.95, 0.2], [.05, .8]])
```

```python
grade_cpd = TabularCPD(variable = "Grade", 
                     variable_card = 3, 
                     evidence = ["Difficulty", "Intelligence"], 
                     evidence_card = [2, 2], 
                     values = [[.3,.05,.9,.5],[.4,.25,.08,.3],[.3,.7,.02,.2]])
```

```python
letter_cpd = TabularCPD(variable = "Letter", 
                     variable_card = 2, 
                     evidence = ["Grade"], 
                     evidence_card = [3], 
                     values = [[.1,.4,.99],[.9,.6,.01]])
```

```python
model.add_cpds(difficulty_cpd, intelligence_cpd, sat_cpd, grade_cpd, letter_cpd)
```

```python
model.get_cpds()
```

    [<TabularCPD representing P(Difficulty:2) at 0x1494d64c160>,
     <TabularCPD representing P(Intelligence:2) at 0x1494d4441c0>,
     <TabularCPD representing P(SAT:2 | Intelligence:2) at 0x1494d5a2250>,
     <TabularCPD representing P(Grade:3 | Difficulty:2, Intelligence:2) at 0x1494d64cb20>,
     <TabularCPD representing P(Letter:2 | Grade:3) at 0x1494d64ce50>]

```python
from pgmpy.inference import VariableElimination
```

```python
infer = VariableElimination(model)
```

```python
getRecc = infer.query(variables = ["Letter"])
print(getRecc)
```

    +-----------+---------------+
    | Letter    |   phi(Letter) |
    +===========+===============+
    | Letter(0) |        0.4320 |
    +-----------+---------------+
    | Letter(1) |        0.5680 |
    +-----------+---------------+
    

```python
intelg3 = infer.query(variables = ["Intelligence"], evidence = {'Grade': 0})
print(intelg3)
```
    +-----------------+---------------------+
    | Intelligence    |   phi(Intelligence) |
    +=================+=====================+
    | Intelligence(0) |              0.8456 |
    +-----------------+---------------------+
    | Intelligence(1) |              0.1544 |
    +-----------------+---------------------+
    

```python
intelg3sat = infer.query(variables = ["Intelligence"], evidence = {'Grade': 0, 'SAT': 1})
print(intelg3sat)
```
    +-----------------+---------------------+
    | Intelligence    |   phi(Intelligence) |
    +=================+=====================+
    | Intelligence(0) |              0.2551 |
    +-----------------+---------------------+
    | Intelligence(1) |              0.7449 |
    +-----------------+---------------------+

```python

