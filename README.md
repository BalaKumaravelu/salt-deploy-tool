# salt-deploy-tool
Tool to deploy rpm and msi packages using Salt

Tool to deploy rpm and msi packages using Salt This tool uses Salt to deploy rpm and msi packages. There is a wrapper script that needs to be called with the environment name, product name and the associated version that needs to be deployed. It will go ahead and uninstall the older version and install the specified version and start the corresponding service

Deployment

python scripts/Wrapper.py -l QAEnv -c WindowsAppB -v 3.0.14.54 

python scripts/Wrapper.py -l StagingEnv -c TomcatAppB -v 1.33.0.13 

python scripts/Wrapper.py -EnvName DevEnv -component TomcatAppA -version '1.2.3.4'
