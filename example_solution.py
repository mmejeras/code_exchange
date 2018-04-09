import json
import numpy as np

def parse_basket(basket_filename='default.json'):
    """ Input: Filename of JSON file with baskets info
        Output: List of average, median, top and bottom quartile of basket sizes
    """
    ## Ingest the JSON file contents
    try:
        with open(basket_filename) as json_data:
            json_obj = json.load(json_data)
            #print(json_obj)

            basket_sizes = []
            ## Get baskets one by one from the JSON contents
            for basket in json_obj:
                #print(basket)
                basket_size = 0
                ## For each basket, get all items and calculate the total cost for each item
                ## We assume that unitprice is the price before the discount and discountpercent is in percent (0.8=80%)
                for item in basket['items']:
                    #print(item['name'])
                    total = float(item['quantity']) * (float(item['unitprice']) * (1 - float(item['discountpercent'])))
                    #print(total)
                    basket_size = basket_size + total
                    print(basket_size)
                basket_sizes.append(basket_size)

            #print(basket_sizes)
            baskets_average = np.average(basket_sizes)
            baskets_median = np.median(basket_sizes)
            baskets_top_quartile = np.percentile(basket_sizes, 75)
            baskets_bottom_quartile = np.percentile(basket_sizes, 25)

            baskets_info = {}
            baskets_info['average'] = baskets_average
            baskets_info['median'] = baskets_median
            baskets_info['top_quartile'] = baskets_top_quartile
            baskets_info['bottom_quartile'] = baskets_bottom_quartile

            return baskets_info

    except Exception as e:
        print("An exception occured: {}".format(e))
        return {}

baskets_info = parse_basket('basket-data.json')

if baskets_info != {}:
    print('Average of basket sizes: ', str(baskets_info['average']))
    print('Median of basket sizes: ', str(baskets_info['median']))
    print('Top quartile of basket sizes: ', str(baskets_info['top_quartile']))
    print('Bottom quartile of basket sizes: ', str(baskets_info['bottom_quartile']))
    print(baskets_info)
