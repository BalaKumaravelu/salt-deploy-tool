import salt.exceptions
import logging
import salt.loader


log = logging.getLogger(__name__)


def present(name, EnvName, is_rpm=True, instance_index=0):
  __utils__['common.LogHeader']('State : response_file.present')
  log.info('Name : {0}'.format(name))
  log.info('Lane : {0}'.format(EnvName))
  log.info('IsRpm : {0}'.format(is_rpm))
  log.info('Instance Index : {0}'.format(instance_index))
  
  return __salt__['response_file.present'](name,EnvName, is_rpm, instance_index)
