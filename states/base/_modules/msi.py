import salt.exceptions
import logging
import salt.loader
import os

log = logging.getLogger(__name__)


def get_installed_version(name):
  __utils__['common.LogHeader']('Module : msi.get_installed_version')
  log.info('Name : {0}'.format(name))

  installedRpmVersion = ''

 
  return installedRpmVersion


def uninstall(name):
  __utils__['common.LogHeader']('Module : msi.uninstall')
  log.info('Product Code : {0}'.format(name))

  tempDir = os.getenv('TEMP')
  
  states = salt.loader.states(__opts__, __salt__, None, None)
  cmdResult=states['cmd.run']('msiexec.exe /x {0} /qn /l*v {1}\\uninstall_{0}.log'.format(name, tempDir))

  log.info('cmdResult : {0}'.format(str(cmdResult)))
  log.info('Commandline : {0}'.format(str(cmdResult['name'])))  
  log.info("Return Code : {0}".format(cmdResult['changes']['retcode']))
  log.info('Output : {0}'.format(cmdResult['changes']['stdout']))
  log.info('Error : {0}'.format(cmdResult['changes']['stderr'])) 

  return cmdResult

def install(name, version):  
  __utils__['common.LogHeader']('Module : msi.install')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version))

  tempDir = os.getenv('TEMP')
  msiFileName = __utils__['msi.GetFileName'](name)

  states = salt.loader.states(__opts__, __salt__, None, None)
  cmdResult=states['cmd.run']('msiexec.exe /i {0}\\{1} /qn /l*v {0}\\{1}.log'.format(tempDir, msiFileName))

  log.info('cmdResult : {0}'.format(str(cmdResult)))
  log.info('Commandline : {0}'.format(str(cmdResult['name'])))  
  log.info("Return Code : {0}".format(cmdResult['changes']['retcode']))
  log.info('Output : {0}'.format(cmdResult['changes']['stdout']))
  log.info('Error : {0}'.format(cmdResult['changes']['stderr'])) 

  return cmdResult

def present(name, version):
  __utils__['common.LogHeader']('Module : msi.present')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version))

  src_sum = {
    'hash_type' : 'md5',
    'hsum': 'md5'
  }

  tempDir = os.getenv('TEMP')

  msiFileName = __utils__['msi.GetFileName'](name)

  isPresent = __salt__['file.manage_file']("{0}/{1}".format(tempDir,msiFileName), '', None, "salt://binaries/packages/msi/WindowsAppID/{0}/{1}".format(version, msiFileName), src_sum, 'root', 'root', '755', 'base', '')

  log.info("Result : {0}".format(isPresent['result']))
  log.info('Commandline : {0}'.format(str(isPresent)))

  return isPresent