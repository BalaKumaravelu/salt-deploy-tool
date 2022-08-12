import salt.exceptions
import logging
import salt.loader
import common

log = logging.getLogger(__name__)


def sleep(name):
  __utils__['common.LogHeader']('Module : common.sleep')
  log.info('Name : {0}'.format(name))

  returnValue = __utils__['common.Sleep'](name)
  return returnValue

