## Annual cost of downtime caused by simultaneous run of 2 jobs
<br>  

### Description
**The scenario:**  
Every night between 7pm and midnight, 2 independent computing jobs from different sources
get randomly started. Each lasts exactly 1 hour. When the jobs run simultaneously, they 
cause failure in other nightly jobs, resulting in downtime that costs $1000 to the company
on an average.

The CEO needs a single number representing the estimated annual cost of this issue to decide
if it is worth fixing. Write a function to simulate the problem and return the annual 
estimated cost of the issue.

**In short:**
The problem basically involves getting the probability of a temporal overlap between the 2 
events, each lasting 60 minutes, within the time-window of 5 hours (300 minutes).

<br><br>
### Solutions
Here, the same solution is presented in both python and R. It basically involves simulating 10000
job1 and job2 start times by generating a random int between 1 and 300 (5 hours). If the 2 start 
times lie within 60 minutes, they overlap. 10000 is fairly large number, allowing us to accurately 
calculate the probability of the overlap using this simulation.

Using the probability, annual cost is estimated as:  
365 x overlap_probability x cost_per_downtime 

<br><br>
### Tests
We test this solution using a Monte Carlo simulations (n=100) with an error threshold of 5%.  

**Python:**   
Using _pytest_.  
Run `py.test` from `katas/programming/temporal_overlap_probability/python`

**R**  
Using _testthis_.  
Run `testthat::test_file('test-test_temporal_overlap.R')` from `katas\programming\temporal_overlap_probability\R`

<br><br>
