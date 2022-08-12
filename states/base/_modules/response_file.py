import salt.exceptions
import logging
import salt.loader
import os


log = logging.getLogger(__name__)


def present(name, EnvName, is_rpm=True, instance_index=0):
  __utils__['common.LogHeader']('Module : response_file.present')
  log.info('Name : {0}'.format(name))
  log.info('Lane : {0}'.format(EnvName))
  log.info('Is Rrpm : {0}'.format(is_rpm))
  log.info('Instance Index : {0}'.format(instance_index))

  sourceResponseFileName = __utils__['response_file.GetSourceFileName'](name, EnvName, instance_index, is_rpm)
  destinationResponseFileName = __utils__['response_file.GetDestinationFileName'](name, is_rpm)

  src_sum = {
    'hash_type' : 'md5',
    'hsum': 'md5'
  }

  destinationDir = "~"
  
  if not is_rpm:
    destinationDir = os.getenv('windir')

  isPresent = __salt__['file.manage_file']("{0}/{1}".format(destinationDir, destinationResponseFileName), '', None, "salt://binaries/response_files/{0}".format(sourceResponseFileName), src_sum, 'root', 'root', '755', '', EnvName, '')

  log.info("Result : {0}".format(isPresent['result']))
  log.info('Commandline : {0}'.format(str(isPresent)))

  log.info('isPresent : ' + str(isPresent))
  log.info('Response File : ' + sourceResponseFileName)

  return isPresent