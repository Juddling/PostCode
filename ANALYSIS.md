The Python code was profiled using the cProfile module

`python3 -m cProfile -s tottime part_3.py`

```shell
python3 -m cProfile -s tottime part_3.py 
12916959 function calls (12916416 primitive calls) in 17.756 seconds
```

## Compiling the Regular Expression

The results show that 4.8 seconds are spent checking for regular expression matches.

Compiling the regular expression reduces this time to 3.0 seconds.

## Sorting lists

Sorting the lists in place is faster than constructing a new list