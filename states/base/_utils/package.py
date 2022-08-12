import salt.exceptions
import logging
import salt.loader
import rpm
import msi
import common

log = logging.getLogger(__name__)


def GetPackageFileName(component_name, version, isMsi):
    common.LogHeader('Utils : package.GetPackageFileName')
    log.info('Component : {0}'.format(component_name))
    log.info('Version : {0}'.format(version))
    log.info('IsMsi : {0}'.format(isMsi))

    packageFileName = ''

    if isMsi:      
      packageFileName = msi.GetFileName(component_name)
    else:
      packageFileName = rpm.GetFileName(component_name, version)      

    log.info('Extracted Package File Name : {0}'.format(packageFileName))
    return packageFileName







