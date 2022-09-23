import numpy
import pandas
import xlsxwriter
import requests
import math
from api_secrets import IEX_CLOUD_API_TOKEN

stocks = pandas.read_csv('sp_500_stocks.csv')

stocks
