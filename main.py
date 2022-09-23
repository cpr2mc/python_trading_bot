import numpy
import pandas
import xlsxwriter
import requests
import math
from secrets import IEX_API_CLOUD_TOKEN

stocks = pandas.read_csv('sp_500_stocks.csv')

stocks
