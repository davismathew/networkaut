import cling
import logging

LOG=logging.getLogger(__name__)
LOG.addHandler(logging.NullHandler())

try:
    ch = cling.Cling(hostname='172.29.248.10',
                     personality='ios',
                     username='cisco',
                     password='cisco')
    LOG.debug('%s: Sending: %s')
    ch.login()
    
    print ch.run_command('show version')
    ch.logout()
except cling.Error as e:
    print e
