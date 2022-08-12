
base:
  'min*':
    - tomcat

DevEnv:
  'TomcatAppB*-DevEnv* or TomcatAppC*-DevEnv* or TomcatAppA*-DevEnv*':
    - tomcat 
  'JavaAppA*-DevEnv*':
    - java
  'web-DevEnv* or ApacheAppA*-DevEnv*':
    - apache
  '$WindowsAppAID*-DevEnv*':
    - windows
  
QAEnv:
  'min*':
    - deploy
  'TomcatAppB*-QAEnv* or TomcatAppC*-QAEnv* or TomcatAppA*-QAEnv*':
    - tomcat 
  'JavaAppA*-QAEnv*':
    - java
  'web-QAEnv* or ApacheAppA*-QAEnv*':
    - apache
  '$WindowsAppAID*-QAEnv*':
    - windows


PerformanceEnv:
  'min*':
    - apache
  'TomcatAppB*-PerformanceEnv* or TomcatAppC*-PerformanceEnv* or TomcatAppA*-PerformanceEnv*':
    - tomcat 
  'JavaAppA*-PerformanceEnv*':
    - java
  'web-PerformanceEnv* or ApacheAppA*-PerformanceEnv*':
    - apache
  '$WindowsAppAID*-PerformanceEnv*':
    - windows

StagingEnv:
  'min*':
    - tomcat
  'TomcatAppB*-StagingEnv* or TomcatAppC*-StagingEnv* or TomcatAppA*-StagingEnv*':
    - tomcat 
  'JavaAppA*-StagingEnv*':
    - java
  'web*1-StagingEnv* or ApacheAppA*-StagingEnv*':
    - apache
  '$WindowsAppAID*-StagingEnv*':
    - windows

ProductionEnv:
  'min*':
    - java
    'TomcatAppB*-ProductionEnv* or TomcatAppC*-ProductionEnv* or TomcatAppA*-ProductionEnv*':
    - tomcat 
  'JavaAppA0*-ProductionEnv*':
    - java
  'web-ProductionEnv* or ApacheAppA*-ProductionEnv*':
    - apache
  '$WindowsAppAID*-ProductionEnv*':
    - windows
