import salt.exceptions
import logging
import salt.loader


log = logging.getLogger(__name__)


def uninstalled(name):
  __utils__['common.LogHeader']('State : rpm.uninstalled')
  log.info('Name : {0}'.format(name))
  
  return __salt__['rpm.uninstall'](name)
  

def installed(name, version):
  __utils__['common.LogHeader']('State : rpm.installed')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version)) 

  return __salt__['rpm.install'](name, version)


def present(name, version):
  __utils__['common.LogHeader']('State : rpm.present')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version))

  return __salt__['rpm.present'](name,version)

