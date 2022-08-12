import os
import yaml
import sys
import argparse
from subprocess import call
import subprocess
import ConfigParser


def ParseCommandLine():
  print '\nParseCommandLine'
  print 'Command line : ', str(sys.argv)
  parser = argparse.ArgumentParser(description='Command Line for deployment')
  parser.add_argument('-EnvName', type=str, help='The EnvName to deploy to' )
  parser.add_argument('-component', type=str, help='The Component to deploy' )
  parser.add_argument('-version', type=str, help='The Version of the Component to deploy' )
  args=parser.parse_args()
  print args.EnvName
  print args.component
  print args.version
  return args

def GetInstanceAlias(component):
  print '\nGetInstanceAlias'
  print 'Component : ', component
  instanceAlias = component
  
  scriptFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.ini')
  print('ScriptFilePath : ', scriptFilePath)

  config = ConfigParser.ConfigParser()
  config.read(scriptFilePath)
  if config.has_option('instance_alias', component):
    instanceAlias=config.get('instance_alias', component)
    
  print 'Instance Alias : ', instanceAlias
 
  return instanceAlias

def GetTargetMapping(instanceAlias, EnvName):
  print '\nGetTargetMapping'
  print 'InstanceAlias : ', instanceAlias
  print 'Lane : ', EnvName

  targetMapping = None

  if EnvName == 'production':
    targetMapping = "{0}0*.$CompanyName.com".format(instanceAlias)
  else:
    targetMapping = "{0}0*-{1}*".format(instanceAlias,EnvName)
  
  return targetMapping


def Deploy(component, version, EnvName, targetMapping):  
  print '\nDeploy'
  print 'Component : ', component
  print 'Version : ', version
  print 'Lane : ', EnvName
  print 'Target Mapping : ', targetMapping

  result=None
  pillar = {
    "component" : "{0}".format(component),
    "version": "{0}".format(version)
  }

  cmdLine = ["salt", targetMapping, "state.apply", "saltenv={0}".format(EnvName),  "pillar={0}".format(pillar) ]
  print 'Command Line : ', str(cmdLine)

  try:
    result=subprocess.check_output(cmdLine)
  except subprocess.CalledProcessError as deployProcess:                                                                                                   
    print "Error Code :", deployProcess.returncode, deployProcess.output, deployProcess.cmd

  print '\nDeploy Output'
  print result



# Main Program
args = ParseCommandLine()
instanceAlias = GetInstanceAlias(args.component)
targetMapping = GetTargetMapping(instanceAlias, args.EnvName)
print 'Target Mapping : ', targetMapping

if(targetMapping != None):
  print 'Good to go'
  Deploy(args.component, args.version, args.EnvName, targetMapping)  
else:
  print 'No Good, Cannot get Target Mapping'






