import salt.exceptions
import logging
import salt.loader
import time

log = logging.getLogger(__name__)

def Sleep(duration):
  LogHeader('Sleep')
  log.info('Duration : '.format(duration))
  time.sleep(duration)
  
  return True

def LogHeader(heading):
  log.info('')
  log.info('--------------------------------------------------------------------------------------')
  log.info(heading)
  log.info('--------------------------------------------------------------------------------------')








