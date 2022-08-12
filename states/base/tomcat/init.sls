response_file_present:
  response_file.present:
    - name: {{pillar['component']}}
    - EnvName: {{ saltenv }}
    - instance_index: {{grains['instance_index']}}
    - is_rpm: 'True'

rpm_file_present:
  rpm.present:
    - name: {{pillar['component']}}
    - version: {{pillar['version']}}

tomcat_stopped:
  tomcat.stopped:
    - name: {{pillar['component']}}

tomcat_has_shutdown:
  tomcat.has_shutdown:
    - name: {{pillar['component']}}

rpm_uninstalled:
  rpm.uninstalled:
    - name:  {{pillar['component']}}

rpm_installed:
  rpm.installed:
    - name:  {{pillar['component']}}
    - version: {{pillar['version']}}

tomcat_running:
  tomcat.running:
    - name: {{pillar['component']}}