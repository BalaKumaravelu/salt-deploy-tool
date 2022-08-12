import salt.exceptions
import logging
import salt.loader


log = logging.getLogger(__name__)


def uninstalled(name):  
  __utils__['common.LogHeader']('State : msi.uninstalled')
  log.info('Name : {0}'.format(name)) 

  return __salt__['msi.uninstall'](name)
  

def installed(name, version):  
  __utils__['common.LogHeader']('State : msi.installed')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version))

  return __salt__['msi.install'](name,version)


def present(name, version):
  __utils__['common.LogHeader']('State : msi.present')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version))

  return __salt__['msi.present'](name,version)