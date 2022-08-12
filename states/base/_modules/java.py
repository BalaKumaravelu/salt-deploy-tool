import salt.exceptions
import logging
import salt.loader
import os

log = logging.getLogger(__name__)


def start(name, user):  
  __utils__['common.LogHeader']('Module : java.start')
  return process(name, user, "start")

def stop(name, user):  
  __utils__['common.LogHeader']('Module : java.stop')
  return process(name, user, "stop")

def status(name, user):  
  __utils__['common.LogHeader']('Module : java.status')
  return process(name, user, "status")

# ToDo Cleanup the return values ,check we are catching error
def process(name, user, operation):
  __utils__['common.LogHeader']('Module : java - Java Process')
  log.info('Name : {0}'.format(name))
  log.info('User : {0}'.format(user))
  log.info('Operation : {0}'.format(operation))
  
  states = salt.loader.states(__opts__, __salt__, None, None)
  fileExists = os.path.isfile('/export/home/$CompanyID{0}-ROOT/$CompanyID/{0}/run.sh'.format(name))

  result = {
    'name': name,
    'changes': {'old': 'RPM absent', 'new': 'RPM absent', 'retcode' : '0' },
    'result': True,
    'comment': 'Rpm is not installed',
    'pchanges': {},
  }
  
  if fileExists:
    result=states['cmd.run']("su - {0} -c '/export/home/$CompanyID{1}-ROOT/$CompanyID/{1}/run.sh {1} {2}'".format(user, name, operation))
  else:
    log.info('File : /export/home/$CompanyID{0}-ROOT/$CompanyID/{0}/run.sh does not exist'.format(name))
    if(operation == 'stop'):
      log.info('Trying to stop absent installation, skipping the step')
    else:
      log.info('Error : Trying to {0} absent installation'.format(operation))
      result['result'] = False  

  log.info('Commandline : {0}'.format(str(result['name'])))
  log.info('Command Result : {0}'.format(str(result))) 
  
  if (operation == 'start') and (result['changes']['retcode'] == 2):
    log.info('Java is running already running')
    result['result'] = True    
  
  if(result['result'] == True):        
    log.info('Java process was successful - Name : {0} - Operation : {1} - Return Code : {2}'.format(name, operation, result['changes']['retcode']))
  else:
    log.info('Java process was un-successful - Name : {0}  - Operation : {1} -  Return Code : {2}'.format(name, operation, result['changes']['retcode']))

  return result


def has_shutdown(name):
  __utils__['common.LogHeader']('Module : java.has_shutdown')
  log.info('Name : {0}'.format(name))  

  # can use pgrep java
  states = salt.loader.states(__opts__, __salt__, None, None)  
  result=states['cmd.run']("ps -ef | grep [j]ava | grep {0}".format(name))

  log.info('Commandline : {0}'.format(str(result['name'])))
  log.info('Command Result : {0}'.format(str(result))) 

  if(result['changes']['retcode'] == 0):        
    log.info('Java is running - Name : {0} -  Return Code : {1}'.format(name, result['changes']['retcode'])) 
    result['result']=False    
  else:
    log.info('Java is Shutdown - Name : {0} - Return Code : {1}'.format(name, result['changes']['retcode']))  
    result['result']=True  

  return result

