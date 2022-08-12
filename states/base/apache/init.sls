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

rpm_uninstalled:
  rpm.uninstalled:
    - name:  {{pillar['component']}}

rpm_installed:
  rpm.installed:
    - name:  {{pillar['component']}}
    - version: {{pillar['version']}}

start_apache:
  service.running:
    - name: httpd
    - enable: True
