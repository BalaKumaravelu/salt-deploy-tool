import salt.exceptions
import logging
import salt.loader
import common


log = logging.getLogger(__name__)


def GetFileName(component_name, version):
    common.LogHeader('Utils : rpm.GetFileName')
    log.info('Getting Rpm File Name for Component : {0} - Version : {1}'.format(component_name, version))

    versionFields = version.split(".")

    rpmFileName = "$CompanyID{0}-{1}.{2}.{3}-{4}.x86_64.rpm".format(component_name, versionFields[0],versionFields[1],versionFields[2],versionFields[3])

    log.info('Extracted Rpm File Name : {0}'.format(rpmFileName))
   
    return rpmFileName

