[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


Exercise 5.1 In the BRFSS (see Section 5.4), the distribution of heights is
roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men,
and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and
6’1” (see http://bluemancasting.com). What percentage of the U.S. male
population is in this range? Hint: use scipy.stats.norm.cdf


```
from scipy.stats import norm
import matplotlib.pyplot as plt

def to_cm(f,i):
    return (12.0*f+i)*2.54

mu = 178
sigma = 7.7
bottom = (to_cm(5,10)-mu)/sigma
top = (to_cm(6,1)-mu)/sigma
middle = norm.cdf(top)-norm.cdf(bottom)
middle
```

# result:
34.3%