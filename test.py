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
            'ak2uqfavwgmjrvtu.onion',
            'yn6ocmvu4ok3k3al.onion',
            'acabtd4btrxjjrvr.onion',
            '5r4bjnjug3apqdii.onion',
            '2dermafialks7aai.onion',
            'ymi7h25hgp3bj63v.onion',
            'ppdz5djzpo3w5k2z.onion',
            'pltloztihmfrg2sw.onion',
            'ur5b2b4brz427ygh.onion',
            'w6csjytbrl273che.onion',
            'abkjckdgoabr7bmm.onion',
            'bqs3dobnazs7h4u4.onion',
            'fkut2p37apcg6l7f.onion',
            '6iolddfbfinntq2b.onion',
            'nzh3fv6jc6jskki3.onion',
            'cwoiopiifrlzcuos.onion',
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

print 'Start %s' % (time.time())

urls, unix_times = url_to_unixtime(pool_one)

returned_unixtime = (len(urls))
print 'Returned unixtimes: %s' % (returned_unixtime)

for i in range(0, len(urls)):
   print '"%s" %s' % (urls[i], unix_times[i])

print 'End %s' % (time.time())
