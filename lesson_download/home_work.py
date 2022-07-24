import os.path
import time
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
from PyPDF2 import PdfReader
import openpyxl
import xlrd
from zipfile import ZipFile


#сбор файлов
browser.open('https://google.com/search')

