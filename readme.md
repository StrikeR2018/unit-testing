flip2 ~/362/unit/in_class_3-master 1045$ python3 -m unittest test_calc.py > readme.md
.F..F...
======================================================================
FAIL: test_add_ (test_calc.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/nfs/stak/users/limingx/362/unit/in-class/test_calc.py", line 10, in test_add_
    self.assertEqual(calc.add(3, 6), 18)
AssertionError: 9 != 18

======================================================================
FAIL: test_mul (test_calc.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/nfs/stak/users/limingx/362/unit/in-class/test_calc.py", line 19, in test_mul
    self.assertEqual(calc.mul(5, 6), 11)
AssertionError: 30 != 11

----------------------------------------------------------------------
Ran 8 tests in 0.003s

FAILED (failures=2)
