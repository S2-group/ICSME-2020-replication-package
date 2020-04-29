from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os
import json
import statistics
import csv
import sys
import time

def get_lowest_time_to_widget(userTimings):
    lowestTime = -1

    for time in userTimings:
        timestamp = time['startTime']
        if (lowestTime == -1 or timestamp < lowestTime):
            lowestTime = timestamp
    return lowestTime

def get_median_time_to_widget(userTimings):
    if len(userTimings) == 0:
        return -1

    total = 0;
    times = []

    for time in userTimings:
        timestamp = time['startTime']
        times.append(timestamp)

    return statistics.median(times)

if len(sys.argv) < 2:
    print('This script requires you to specify a file as output. Please do so. The file will be saved in ../results and prefixed with ff_')
    exit(1)

ff_options = Options()
ff_options.add_argument("-private")

with open('../results/ff_' + sys.argv[1], 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['page-load-time', 'lowest-time-to-widget', 'median-time-to-widget'])

    for i in range(0, 30):
        print("Running test " + str(i + 1))
        metrics = []

        driver = webdriver.Firefox(options=ff_options)
        driver.get('https://zensie.30mhz.com/ShowcasingZENSIE/dashboard/d3affc8e-084d-11e8-8f86-ebc5ebb30948')

        driver.find_element_by_id('email').send_keys(os.environ["ZENSIE_USER"])
        driver.find_element_by_id('password').send_keys(os.environ["ZENSIE_PASS"])
        driver.find_element_by_id('btn-login').click()

        # This sucks, but there's no way to correctly wait for onLoad in Selenium
        time.sleep(15)

        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")
        plt = loadEventEnd - navigationStart
        domLoading = driver.execute_script("return window.performance.timing.domLoading")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")

        user_timings_raw = str(driver.execute_script("return window.performance.getEntriesByName('time-to-widget')"))
        user_timings_raw = user_timings_raw.replace('\'', '\"')
        user_timings = json.loads(user_timings_raw)

        metrics = [
            plt,
            get_lowest_time_to_widget(user_timings),
            get_median_time_to_widget(user_timings)
        ]

        writer.writerow(metrics)

        driver.close()
        driver.quit()