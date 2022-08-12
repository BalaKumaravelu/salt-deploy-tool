response_file_present:
  response_file.present:
    - name: {{pillar['component']}}
    - EnvName: {{ saltenv }}
    - instance_index: {{grains['instance_index']}}
    - is_rpm: False

msi_file_present:
  msi.present:
    - name: {{pillar['component']}}
    - version: {{pillar['version']}}


{% set component_name = pillar['component'] %}

{% if pillar[component_name]['service_name']  != '' %}
windows_service_stopped:
  service.dead:
    - name: {{pillar[component_name]['service_name']}}  
{% endif %}

msi_uninstalled:
  msi.uninstalled:
    - name: {{pillar[component_name]['product_code']}} 

msi_installed:
  msi.installed:
    - name: {{pillar['component']}}
    - version: {{pillar['version']}}

{% if pillar[component_name]['service_name']  != '' %}
windows_service_running:
  service.running:
    - name: {{pillar[component_name]['service_name']}} 
{% endif %}