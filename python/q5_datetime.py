# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

import datetime

date_start = '01-02-2013'    
date_stop = '07-28-2015'

def dashTimeMDY(s):
    return datetime.datetime.strptime(s,'%m-%d-%Y')

difference = dashTimeMDY(date_stop) - dashTimeMDY(date_start)
print difference

date_start = '12312013'  
date_stop = '05282015'  


difference = datetime.datetime.strptime(date_stop,'%m%d%Y') - datetime.datetime.strptime(date_start,'%m%d%Y')
print difference


date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
d = lambda t: datetime.datetime.strptime(t,'%d-%b-%Y')
print d(date_stop)-d(date_start)