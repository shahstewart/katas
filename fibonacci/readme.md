## Fibonacci Number

#### Description
A Fibonacci number is an integer from a sequence of positive integers called _Fibonacci Sequence_, commonly written as _**F<sub>n</sub>**_ for the _**n<sup>th</sup>**_ number in the sequence.  
Fibonacci sequence starts with 0 , 1 and each subsequent number is the sum of previous 2 numbers in the sequence. Therefore, 

  _**F<sub>0</sub> = 0, &nbsp; F<sub>0</sub> = 1 &nbsp;&nbsp; and &nbsp; for n > 2,  &nbsp;&nbsp; F<sub>n</sub> = &nbsp; F<sub>n-1</sub> + F<sub>n-2</sub>**_  

To give you a better idea, this is how the beginning of Fibonacci sequence looks:  
**0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...**  

&nbsp;

#### Solutions
I have added 3 solutions plus some variations of them here. All solutions, as expected for any function that works with a series, are recursive. However, the solutions use different algorithms, and have large performance differences.  

- **simple recursive:**
  This is a very simple solution, but it has a poor performance because it is exponential (_O(2<sup>n</sup>)_).  
    

- **recursive with use of a global variable:**  
  This solution mitigates the poor performance of the simple recursive solution by storing the fibonacci numbers it has already calculated in a global variable. This leads to massive gains in performance as the solution now has a linear complexity (O(n)). However, even though the value look up for arrays/lists seems to be single operation in most higher-level languages, it is not so at the assembly level, leading to some hit in the performance as the value of _n_ becomes larger. Storing the computation results in a global var will also hog up non-trivial amount of memory where _n_ is large.
    

- **forward recursive variants:**
  This algorithm mitigates the necessity of storing computational results in a global   variable by using forward recursion, and passing the result of the computation to the next iteration of computation. It has complexity of (O(n)), and we don't have to worry about using global variables. These solutions seem to be the best suited for computing Fibonacci numbers.  
  &nbsp;  
  

  
**_Notes:_**
* Please keep in mind that not all languages are designed to crunch large numbers.  
    

* When running calculations in JavaScript, all operations involving numbers larger than `Number.MAX_SAFE_INTEGER` (9007199254740991) will be inaccurate as all numbers larger than the max_safe number are automatically rounded. This explains why Fibonacci calculations in our js scripts return value of fibonacci(100) as `354224848179262000000` instead of `354224848179261915075` as returned by Python scripts.  
There are ways to bypass this issue using the `BigInt` data type. However, we are not going to go into that here.

&nbsp;

#### Tests
_JavaScript:_ with _mocha_, run `mocha test.js` from the js folder (`katas/fibonacci/js`)

_Python:_ with _pytest_,  run `py.test` from the python folder (`katas/fibonacci/python`)

_php:_ with _phpunit_, run  `..\..\vendor\bin\phpunit TestFibonacci.php` from the php folder (`katas/fibonacci/php`)  
