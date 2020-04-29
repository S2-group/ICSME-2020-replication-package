import sys
import json
import numpy
from haralyzer import HarParser, HarPage

def get_number_of_requests(har_page, type):
    return len(har_page.filter_entries(request_type=type, status_code='2.*'))

def get_load_time(har_page, type):
    return round(har_page.get_load_time(request_type=type, status_code='2.*', asynchronous=False))


def print_filetype_load_times(har_page):
    print("Image file size: " + str(har_page.image_size_trans) + ' bytes')
    print('Image load time: ' + str(har_page.get_load_time(content_type='image.*', status_code='2.*')) + 'ms')
    print('JSON load time: ' + str(har_page.get_load_time(content_type='json', status_code='2.*')) + 'ms')


def print_request_type_load_time(har_page):
    print('Number of GET requests: ' + str(get_number_of_requests(har_page, 'GET')))
    print('GET load time: ' + str(get_load_time(har_page, 'GET')) + 'ms')
    print('Number of POST requests: ' + str(get_number_of_requests(har_page, 'POST')))
    print('POST load time: ' + str(get_load_time(har_page, 'POST')) + 'ms')
    print('Number of OPTIONS requests: ' + str(get_number_of_requests(har_page, 'OPTIONS')))
    print('OPTIONS load time: ' + str(get_load_time(har_page, 'OPTIONS')) + 'ms')

def do_request_analysis(har_page):
    getRequests = page.filter_entries(request_type='GET', status_code='2.*')
    postRequests = page.filter_entries(request_type='POST', status_code='2.*')
    optionsRequests = page.filter_entries(request_type='OPTIONS', status_code='2.*')

    allRequests = getRequests + postRequests + optionsRequests
    print('Total number of requests: ' + str(len(allRequests)))

    totalTransferSize = 0
    transferSizes = []
    times = []

    for request in allRequests:
        time = 0
        response = request['response']
        transferSize = response['_transferSize']
        timings = request['timings']

        # Add up all the timing components to get the request time
        for key in request['timings']:
            # null values are -1, we do not want those
            if timings[key] >= 0:
                time += timings[key]

        times.append(time)
        totalTransferSize += transferSize
        transferSizes.append(transferSize)
    
    print('Total bytes transferred: ' + str(totalTransferSize))
    print('Total time taken to transfer bytes: ' + str(round(sum(times))) + 'ms')
    print('Mean time taken by requests: ' + str(round(numpy.mean(times))) + 'ms')



# Prints duplicate API requests and their count
def print_duplicate_requests(har_page):
    duplicates = har_page.duplicate_url_request
    for duplicate in duplicates:
        print('URL: ' + duplicate + '\t count: ' + str(duplicates[duplicate]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('This script requires you to specify a .HAR file as input. Please do so.')
        exit(1)

    with open(sys.argv[1], 'r') as f:
        har_parser = HarParser(json.loads(f.read()))

    page = har_parser.pages[0]
    assert(isinstance(page, HarPage))

    print("Showing stats for URL: " + page.url)
    print()

    # print("Duplicate requests to URLs")
    # print_duplicate_requests(page)
    # print()
    print_filetype_load_times(page)
    print()
    print_request_type_load_time(page)
    print()
    do_request_analysis(page)
    print()
    print('Total time taken by browser to load the page: ' + str(page.get_load_time()) + 'ms')

