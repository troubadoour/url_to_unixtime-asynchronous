#!/usr/bin/env python

from url_to_unixtime import url_to_unixtime
import time, random

pool_one = ['dtsxnd3ykn32ywv6.onion',
            'znig4bc5rlwyj4mz.onion',
            'vtjkwwcq5osuo6uq.onion',
            '33y6fjyhs3phzfjj.onion',
            'y6xjgkgwj47us5ca.onion',
            'strngbxhwyuu37a3.onion',
            'swdi5ymnwmrqhycl.onion',
            'dqeasamlf3jld2kz.onion',
            'pubdrop4dw6rk3aq.onion',
            'hkjpnjbvhrxjvikd.onion',
            'v6gdwmm7ed4oifvd.onion',
            'vbmwh445kf3fs2v4.onion',
            'poulsensqiv6ocq4.onion',
            'tigas3l7uusztiqu.onion',
            'w6csjytbrl273che.onion',
            'ak2uqfavwgmjrvtu.onion']

pool_two =  ['yn6ocmvu4ok3k3al.onion',
            'acabtd4btrxjjrvr.onion',
            '5r4bjnjug3apqdii.onion',
            '2dermafialks7aai.onion',
            'ymi7h25hgp3bj63v.onion',
            'ppdz5djzpo3w5k2z.onion',
            'pltloztihmfrg2sw.onion',
            'ur5b2b4brz427ygh.onion',
            'abkjckdgoabr7bmm.onion',
            'bqs3dobnazs7h4u4.onion',
            'fkut2p37apcg6l7f.onion',
            '6iolddfbfinntq2b.onion',
            'nzh3fv6jc6jskki3.onion']

pool_three = ['cwoiopiifrlzcuos.onion',
            'zsolxunfmbfuq7wf.onion',
            'yfm6sdhnfbulplsw.onion',
            'j6uhdvbhz74oefxf.onion',
            '3g2upl4pq6kufc4m.onion',
            'dju2peblv7upfz3q.onion',
            'msydqstlz2kzerdg.onion',
            'uj3wazyk5u4hnvtk.onion',
            'wi7qkxyrdpu5cmvr.onion',
            'ic6au7wa3f6naxjq.onion',
            'timaq4ygg2iegci7.onion',
            '344c6kbnjnljjzlz.onion',
            'fncuwbiisyh6ak3i.onion']


returned_unixtimes = 0

already_picked_index_pool_one = []
already_picked_index_pool_two = []
already_picked_index_pool_three = []
already_picked_index_dummy_pool = []

pool_one_done = False
pool_two_done = False
pool_three_done = False
dummy_pool_done = False
url_random_pool_one = []
url_random_pool_two = []
url_random_pool_three = []
url_random_dummy_pool = []

print 'Start %s' % (time.time())

while returned_unixtimes < 3:
    urls = []
    unixtimes = []
    url_random = []

    url_index = []

    if not pool_one_done:
        while True:
            ## Pick a random pool index.
            url_index = random.sample(xrange(len(pool_one)), 1)

            ## Reset to prevent infinite loop, next condition would never be met.
            if len(already_picked_index_pool_one) == len(pool_one):
                already_picked_index_pool_one = []

            ## Was this index used?
            if url_index not in already_picked_index_pool_one:
                ## No, add to used indexes.
                already_picked_index_pool_one.append(url_index)
                ## Add it to the pool url list.
                url_random_pool_one.append(pool_one[url_index[0]])
                ## Add it to the url list to fetch.
                url_random.append(pool_one[url_index[0]])
                break

    if not pool_two_done:
        while True:
            url_index = random.sample(xrange(len(pool_two)), 1)

            if len(url_random_pool_two) == len(pool_two):
                already_picked_index_pool_two = []

            if url_index not in already_picked_index_pool_two:
                already_picked_index_pool_two.append(url_index)
                url_random_pool_two.append(pool_two[url_index[0]])
                url_random.append(pool_two[url_index[0]])
                break

    if not pool_three_done:
        while True:
            url_index = random.sample(xrange(len(pool_three)), 1)

            if len(url_random_pool_three) == len(pool_three) - 1:
                already_picked_index_pool_three = []

            if url_index not in already_picked_index_pool_three:
                already_picked_index_pool_three.append(url_index)
                url_random_pool_three.append(pool_three[url_index[0]])
                url_random.append(pool_three[url_index[0]])
                break

    print 'pool 1 picked urls %s' % url_random_pool_one
    print 'pool 2 picked urls %s' % url_random_pool_two
    print 'pool 3 picked urls %s' % url_random_pool_three
    print 'random urls %s' % url_random

    ## Fetch remotes.
    if url_random > 0:
        urls, unix_times = url_to_unixtime(url_random)
    else:
        ## Add code here.
        sys.exit(1)

    if not pool_one_done:
        ## Is last element in the pool in returned urls?
        pool_one_done = url_random_pool_one[len(url_random_pool_one) - 1] in urls

    if not pool_two_done:
        pool_two_done = url_random_pool_two[len(url_random_pool_two) - 1] in urls

    if not pool_three_done:
        pool_three_done = url_random_pool_three[len(url_random_pool_three) - 1] in urls

    returned_unixtimes = len(urls)
    print 'Returned unixtimes: %s' % (returned_unixtimes)

for i in range(0, len(urls)):
    print '"%s" %s' % (urls[i], unix_times[i])

print 'End %s' % (time.time())
