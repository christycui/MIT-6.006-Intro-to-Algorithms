## 1. The Role of Algorithms in Computing
### 1.1 Algorithms

- well-defined computational procedure
- an **instance of a problem** consists of the input needed to compute a solution to the problem
- an algorithm is said to be **correct** if it halts with the correct output for every input instance
- Characters of problems solved by algorithm
    + many candidate solutions -> find "best" one
    + practical applications

### 1.2 Algorithms as a technology

## 3. Growth of Functions
**asymptotic** efficiency of algorithms: we are concerned with how the running time of an algorithm increases with the size of the input *in the limit*, as the size of the input increases without bound

### 3.1 Asymptotic notation
- \theta-notation: upper-bound and lower-bound. 0 <= c1g(n) <= f(n) <= c2g(n)
    + g(n) is **asymptotically tight bound** for f(n)
    + the definition requires that every member of f(n) be **asymptotically nonnegative**
    + the important thing is *some* choices exist for c1 and c2
- O-notation
    + when we have only an **asymptotic upper bound: 0 <= f(n) <= cg(n)
    + note that f(n) = \theta(g(n)) implies that f(n) = O(g(n))
- \omega-notation
    + **asymptotically lower bound**: 0 <= cg(n) <= f(n)
    + f(n) = \theta(g(n)) implies that f(n) = O(g(n)) and f(n) = \omega(g(n))
- asymptotic notation in equations and inequalities
    + there is *some* function f(n) E \Theta(n) such that 2n^2 + 3n + 1 = 2n^2 + f(n)
    + for *any* function g(n) E \Theta(n), there is *some* function h(n) E \Theta(n^2) such that 2n^2 + g(n) = h(n)
- o-notation: an upper bound that is not asymptotically tight
- w-notation: an lower bound that is not asymptotically tight
- Comparing functions
    + Transitivity
    + Reflexivity
    + Symmetry: f(n) = \Theta(g(n)) if and only if g(n) = \Theta(f(n))
    + Transpose symmetry

### 3.2 Standard notations and common functions
- Exponentials: any exponential function with a base strictly greater than 1 grows faster than any polynomial function
- Logarithms: any positive polynomial function grows faster than any polylogarithmic function
    + a = b^(log^b a)
    + We say that a function f(n) is polylogarithmically bounded if f(n) = O(lg^k n) for some constant k.
    + lg^b n = o(n^a) for any constant a > 0. 
- Factorial
    + n! = o(n^n)
    + n! = w(2^n)
    + lg(n!) = \Theta(n lgn)
- functional iteration and the iterated log function
- Fibonacci numbers grow exponentially