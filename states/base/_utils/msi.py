import salt.exceptions
import logging
import salt.loader
import rpm
import common

log = logging.getLogger(__name__)

def GetFileName(component_name): 
  common.LogHeader('Utils : msi.GetFileName')
  log.info('Component : {0}'.format(component_name))
  msiFileName = component_name+".msi"
  log.info('MsiFileName : {0}'.format(msiFileName))
  return msiFileName








