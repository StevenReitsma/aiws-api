import sys
import numpy as np
sys.path.append('../')
import time

from aiws import api
api.authenticate('test','test')

def test_random_requests():
    run_id = 0


    for request_number in xrange(1000):

        s = time.time()
        context = api.get_context(run_id, request_number)
        #print context['context'].values(), time.time()-s


        offer = {
            'header': [5, 15, 35],
            'language': ['NL', 'EN', 'GE'],
            'adtype': ['skyscraper', 'square', 'banner'],
            'color': ['green', 'blue', 'red', 'black', 'white'],
            'price': map(lambda x: 1+float(x),range(50))
        }
        # Random choice
        offer = {key: np.random.choice(val) for key, val in offer.iteritems()}
        #print offer

        s = time.time()
        result = api.serve_page(run_id, request_number,
            header=offer['header'],
            language=offer['language'],
            adtype=offer['adtype'],
            color=offer['color'],
            price=offer['price'])


        #print result, offer['price'] * result['success'], time.time()-s


if __name__ == "__main__":
    test_random_requests()
