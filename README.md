Ansible Libvirt Engine
=========

Simple Role with Libvirt Modules, Filters and Plugins.

Requirements
------------

```
xmltodict >= 0.11.0
```

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

```YAML
- name: "Libvirt Modules, Filters and Plugins"
  hosts: libvirt

  roles:
    - victorock.libvirt-engine

  vars:
    libvirt_compute_domain_device_controller_sata:
      "@type":        "sata"
      "@index":       "0"
      address:
        "@type":      "pci"
        "@domain":    "0x0000"
        "@bus":       "0x00"
        "@slot":      "0x03"
        "@function":  "0x0"

  tasks:
    - name: "Generate XML for Sata Controller"
      set_fact:
        xmlspec_libvirt_controller_sata: "{{ libvirt_compute_domain_device_controller_sata | to_xml }}"
```

License
-------

GPLv3

Author Information
------------------

Victor da Costa
