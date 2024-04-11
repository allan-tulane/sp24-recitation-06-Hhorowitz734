# CMPS 2200 Recitation 06
## Answers

**Name:** Benjamin Horowitz


Place all written answers from `recitation-07.md` here for easier grading.



![Answers to 2 and 3](answers_23.png)


- **4)** We can clearly see from the counts array that certain problems are solved multiple times, which means that the recursive approach to this problem is inherently inefficient. For example, when computing fib_recursive(5), fib_recursive(2) is computed when solving fib_recursive(3) and fib_recursive(4). In dynamic programming, we can reduce this inefficiency.

- **6)** The approach used by fib_top_down using memoization to remove the auxillary computations. This reduces the amount of calls to i for fib_top_down(i). Therefore, this intuitively means that the work of this algorithm is O(n), a great reduction to our previous approach. This approach does not reduce the span as the tree will be just as tall, so the span of this approach is O(n) just like the recursive approach.

- **8)** This approach is essentially the iterative version of the fibs_top_down function. It avoids recomputing values as is done in the original recursive method, which reduces work to O(n) just like fib_top_down. The span is also O(n) for the same reason.
