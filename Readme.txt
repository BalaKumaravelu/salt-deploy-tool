# Deployment 
salt min* state.apply saltenv=QAEnv pillar="{ 'version': '3.0.14.54', 'component': 'WindowsAppB'}"
salt min* state.apply saltenv=QAEnv pillar="{ 'version': '3.0.15.15', 'component': 'WindowsAppB'}"


salt min* state.apply saltenv=ProductionEnv pillar="{ 'version': '1.6.0.30', 'component': 'JavaAppB'}"
salt min* state.apply saltenv=ProductionEnv pillar="{ 'version': '1.6.0.37', 'component': 'JavaAppB'}"

salt min* state.apply saltenv=StagingEnv pillar="{ 'version': '1.33.0.11', 'component': 'TomcatAppB'}"
salt min* state.apply saltenv=StagingEnv pillar="{ 'version': '1.33.0.13', 'component': 'TomcatAppB'}"


python scripts/Wrapper.py -l QAEnv -c WindowsAppB -v 3.0.14.54
python scripts/Wrapper.py -l StagingEnv -c TomcatAppB -v 1.33.0.13
python scripts/Wrapper.py -EnvName DevEnv -component TomcatAppA -version '1.2.3.4'

