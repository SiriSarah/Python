# Installing pip and importing libraries from pip packages

import pandas as pd # Yes, library can be called with nicknames

# Run this program only with the importing the library.
# If this gives error (ModuleNotFoundError: No module named 'pandas'), install the library
# pip install pandas
# or
# pip3 install pandas
# If you don't have pip, then run these commands on your terminal / Command Prompt
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py
# Once it is done, run the above command to install pandas library
# After the installation of pandas package, reboot your IDE/Terminal/IDLE
# If need more help, check https://pandas.pydata.org/getting_started.html

df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]}, index=['falcon', 'dog'])
print(df)

# Repeat the same steps to install matplotlib, theano, scipy, tensorflow, and pytorch.
# You may not need all of them, but it will get your system ready for machine learning. 