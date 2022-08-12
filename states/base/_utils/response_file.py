import salt.exceptions
import logging
import salt.loader
import common

log = logging.getLogger(__name__)


def GetSourceFileName(component_name, EnvName, instance_index, is_rpm):
    common.LogHeader('Utils : response_file.GetSourceFileName')
    log.info('Component Name : {0}'.format(component_name))
    log.info('Lane : {0}'.format(EnvName))
    log.info('Instance Index : {0}'.format(instance_index))
    log.info('IsRpm : {0}'.format(is_rpm))

    sourceResponseFileName = 'response.{0}.{1}'.format(component_name, EnvName)

    if is_rpm:
      sourceResponseFileName = 'response.$CompanyID{0}.{1}'.format(component_name, EnvName)
    else:
      sourceResponseFileName = 'response.{0}.{1}'.format(component_name, EnvName)

    if instance_index!=0:
      sourceResponseFileName=sourceResponseFileName+".s{0}".format(instance_index)

    log.info('Source Response File Name : {0}'.format(sourceResponseFileName))    
       
    return sourceResponseFileName



def GetDestinationFileName(component_name, is_rpm):
    common.LogHeader('Utils : response_file.GetDestinationFileName')
    log.info('Component Name : {0}'.format(component_name))
    log.info('IsRpm : {0}'.format(is_rpm))

    destinationFileName = '{0}.ini'.format(component_name)
    if is_rpm:
      destinationFileName = '{0}.response'.format(component_name)
        
    log.info('Destination Response File Name : {0}'.format(destinationFileName))
    return destinationFileName






