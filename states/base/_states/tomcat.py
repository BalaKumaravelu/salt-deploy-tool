import salt.exceptions
import logging
import salt.loader


log = logging.getLogger(__name__)

def running(name):  
  __utils__['common.LogHeader']('State : tomcat.running')
  log.info('Name : {0}'.format(name))
  user=__pillar__[name]['user']
  log.info('User : {0}'.format(user))

  return __salt__['tomcat.start'](name, user)
  
  
def stopped(name):  
  __utils__['common.LogHeader']('State : tomcat.stopped')
  log.info('Name : {0}'.format(name))
  user=__pillar__[name]['user']
  log.info('User : {0}'.format(user))

  return __salt__['tomcat.stop'](name, user)


def has_shutdown(name):  
  __utils__['common.LogHeader']('State : tomcat.has_shutdown')
  log.info('Name : {0}'.format(name))

  return __salt__['tomcat.has_shutdown'](name)
