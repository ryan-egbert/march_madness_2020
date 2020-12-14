# Project 02 - CS 5600
## Author: Ryan Egbert - A01957665

***

### Summary
My project was creating a classification model using random forests to ultimately predict the results to 
basketball games in the annual NCAA "March Madness" Men's Basketball Tournament. To do this, I gathered data
from the past 20 years of NCAA basketball. There were two parts of data gathered: regular season data and tournament 
results.  

To begin, I gathered the data from PDFs (located in the ```data/pdf/``` directory) and converted it to CSVs (located
in the ```data/csv/``` directory).  This data, however was pretty raw and needed quite a bit of processing.  I then
converted all of that data to a Python dictionary and saved it in ```src/pck/data_all_years.pck```.  This dictionary
includes important features such as team name, RPI rank, record, record v top 50 teams, etc.  This data was then
included in the tournament data to better predict winners and losers of individual games.

### Repository Structure
The repository is split into three directories.  The ```data/``` directory contains all the raw data used for in 
preprocessing.  The ```src/``` directory includes all the code as well as CSVs and pickled Python objects that are
directly used in the code base.  The ```results/``` directory contains resulting files.  An Excel file, a PDF and a 
PNG of a decision tree used in the random forest.

### Running the Code
I had to manually precit the results of each round for the 2020 March Madness tournament (a mock bracket of which was 
obtained from [FiveThirtyEight](https://projects.fivethirtyeight.com/2020-march-madness-predictions/)) using the 
```predict_2020.py``` file.  The RF was fitted using the ```predict.py``` file with data from 2000-2019.  The other four
files (```adjust_data.py```,```rewrite_data.py```,```get_data.py```,```combine_data.py```) were used in data acquisition 
and preprocessing.