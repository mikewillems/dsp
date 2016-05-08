[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```
import math
cd = (fwm - owm) / math.sqrt((firsts.totalwgt_lb.var()*firsts.size + \
                    others.totalwgt_lb.var()*others.size) / 
                             (firsts.size + others.size))
cd
-0.08867292707260202
```
