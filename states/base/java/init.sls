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

java_stopped:
  java.stopped:
    - name: {{pillar['component']}}

java_has_shutdown:
  java.has_shutdown:
    - name: {{pillar['component']}}

rpm_uninstalled:
  rpm.uninstalled:
    - name:  {{pillar['component']}}

rpm_installed:
  rpm.installed:
    - name:  {{pillar['component']}}
    - version: {{pillar['version']}}

java_running:
  java.running:
    - name: {{pillar['component']}}