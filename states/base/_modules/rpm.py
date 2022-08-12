import salt.exceptions
import logging
import salt.loader


log = logging.getLogger(__name__)


def get_installed_rpm_version(name):
  __utils__['common.LogHeader']('Module : rpm.get_installed_rpm_version')
  log.info('Name : {0}'.format(name))

  installedRpmVersion = ''

  states = salt.loader.states(__opts__, __salt__, None, None)
  cmdResult=states['cmd.run']("rpm -qa | grep $CompanyID{0}".format(name),ignore_retcode=True)

  if(cmdResult['result']):    
    installedRpmVersion=cmdResult['changes']['stdout']
    log.info('{0} is installed on the system : {1}'.format(name, installedRpmVersion))
  else:
    log.info('{0} is not installed on the system'.format(name))
  
  log.info('Installed Rpm Version  : {0}'.format(installedRpmVersion))

  return installedRpmVersion


def uninstall(name):
  __utils__['common.LogHeader']('Module : rpm.uninstall')
  log.info('Name : {0}'.format(name))
  
  installedRpmVersion = get_installed_rpm_version(name)
  result = {
    'name': name,
    'changes': {'old': installedRpmVersion, 'new': installedRpmVersion, },
    'result': True,
    'comment': 'Rpm is not installed',
    'pchanges': {},
  }

  if installedRpmVersion == '':
    log.info('{0} is not Installed, skipping uninstallation'.format(name))    
  else:
    log.info('{0} is Installed, going to uninstall'.format(installedRpmVersion))
    states = salt.loader.states(__opts__, __salt__, None, None)
    result=states['cmd.run']("rpm -e {0}".format(installedRpmVersion))
    
    if result['changes']['retcode']==0:
      log.info('Uninstalled successfully')
    else:
      log.info('Cannot Uninstall')

    log.info('Commandline : {0}'.format(str(result['name'])))
    log.info("Return Code : {0}".format(result['changes']['retcode']))
    log.info('Output : {0}'.format(result['changes']['stdout']))
    log.info('Error : {0}'.format(result['changes']['stderr']))

  return result


def install(name, version):
  __utils__['common.LogHeader']('Module : rpm.install')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version))

  rpmFileName = __utils__['rpm.GetFileName'](name, version)
  log.info('RpmFileName : {0}'.format(rpmFileName))

  states = salt.loader.states(__opts__, __salt__, None, None)
  isInstalled=states['cmd.run']("rpm --prefix /export/home/$CompanyID{0}-ROOT -ivh /root/{1}".format(name, rpmFileName))

  if(isInstalled['changes']['retcode']) == 0:
    isInstalled['changes'] = {'old': '', 'new': version}
    isInstalled['comment'] = 'Rpm is Installed'
    log.info('{0} - {1} is installed '.format(name, version))
  else:
    log.info('Error : Cannot Install {0} - {1}'.format(name, version))   
  
  log.info('Commandline : {0}'.format(str(isInstalled['name'])))
  log.info("Return Code : {0}".format(str(isInstalled)))
  log.info('Output : {0}'.format(isInstalled['result']))

  return isInstalled

def present(name, version):
  __utils__['common.LogHeader']('Module : rpm.present')
  log.info('Name : {0}'.format(name))
  log.info('Version : {0}'.format(version))

  rpmFileName = __utils__['rpm.GetFileName'](name, version)
  
  src_sum = {
    'hash_type' : 'md5',
    'hsum': 'md5'
  }

  isPresent = __salt__['file.manage_file']("~/{0}".format(rpmFileName), '', None, "salt://binaries/rpm/{0}/{1}".format(name, rpmFileName), src_sum, 'root', 'root', '755', '', 'base', '')

  log.info("Result : {0}".format(isPresent['result']))
  log.info('Commandline : {0}'.format(str(isPresent)))

  return isPresent