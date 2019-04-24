import data515_hw2 as hw2
from IPython.core.display import display

startdate = '2019-03-01'
enddate = '2019-03-31'

mtstrailwestofi90bikecountinformation = hw2.getbikecountinformation(startdate,enddate)
#display(mtstrailwestofi90bikecountinformation.head(10))

print(hw2.test_create_dataframe(mtstrailwestofi90bikecountinformation))