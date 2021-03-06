#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2018 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# the lib use python logging can get it if the following is set in your
# Ansible config.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_system_csf
short_description: Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure system feature and csf category.
      Examples includes all options and need to be adjusted to datasources before usage.
      Tested with FOS v6.0.2
version_added: "2.8"
author:
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Requires fortiosapi library developed by Fortinet
    - Run as a local_action in your playbook
requirements:
    - fortiosapi>=0.9.8
options:
    host:
       description:
            - FortiOS or FortiGate ip adress.
       required: true
    username:
        description:
            - FortiOS or FortiGate username.
        required: true
    password:
        description:
            - FortiOS or FortiGate password.
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
        type: bool
        default: false
    system_csf:
        description:
            - Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
        default: null
        suboptions:
            configuration-sync:
                description:
                    - Configuration sync mode.
                choices:
                    - default
                    - local
            fabric-device:
                description:
                    - Fabric device configuration.
                suboptions:
                    device-ip:
                        description:
                            - Device IP.
                    device-type:
                        description:
                            - Device type.
                        choices:
                            - fortimail
                    login:
                        description:
                            - Device login name.
                    name:
                        description:
                            - Device name.
                        required: true
                    password:
                        description:
                            - Device login password.
            fixed-key:
                description:
                    - Auto-generated fixed key used when this device is the root. (Will automatically be generated if not set.)
            group-name:
                description:
                    - Security Fabric group name. All FortiGates in a Security Fabric must have the same group name.
            group-password:
                description:
                    - Security Fabric group password. All FortiGates in a Security Fabric must have the same group password.
            management-ip:
                description:
                    - Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric.
            management-port:
                description:
                    - Overriding port for management connection (Overrides admin port).
            status:
                description:
                    - Enable/disable Security Fabric.
                choices:
                    - enable
                    - disable
            trusted-list:
                description:
                    - Pre-authorized and blocked security fabric nodes.
                suboptions:
                    action:
                        description:
                            - Security fabric authorization action.
                        choices:
                            - accept
                            - deny
                    downstream-authorization:
                        description:
                            - Trust authorizations by this node's administrator.
                        choices:
                            - enable
                            - disable
                    ha-members:
                        description:
                            - HA members.
                    serial:
                        description:
                            - Serial.
                        required: true
            upstream-ip:
                description:
                    - IP address of the FortiGate upstream from this FortiGate in the Security Fabric.
            upstream-port:
                description:
                    - The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric (default = 8013).
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    fortios_system_csf:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      system_csf:
        configuration-sync: "default"
        fabric-device:
         -
            device-ip: "<your_own_value>"
            device-type: "fortimail"
            login: "<your_own_value>"
            name: "default_name_8"
            password: "<your_own_value>"
        fixed-key: "<your_own_value>"
        group-name: "<your_own_value>"
        group-password: "<your_own_value>"
        management-ip: "<your_own_value>"
        management-port: "14"
        status: "enable"
        trusted-list:
         -
            action: "accept"
            downstream-authorization: "enable"
            ha-members: "<your_own_value>"
            serial: "<your_own_value>"
        upstream-ip: "<your_own_value>"
        upstream-port: "22"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: string
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: string
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: string
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: string
  sample: "key1"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: string
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: string
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: string
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: string
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: string
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: string
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: string
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule

fos = None


def login(data):
    host = data['host']
    username = data['username']
    password = data['password']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password)


def filter_system_csf_data(json):
    option_list = ['configuration-sync', 'fabric-device', 'fixed-key',
                   'group-name', 'group-password', 'management-ip',
                   'management-port', 'status', 'trusted-list',
                   'upstream-ip', 'upstream-port']
    dictionary = {}

    for attribute in option_list:
        if attribute in json:
            dictionary[attribute] = json[attribute]

    return dictionary


def system_csf(data, fos):
    vdom = data['vdom']
    system_csf_data = data['system_csf']
    filtered_data = filter_system_csf_data(system_csf_data)
    return fos.set('system',
                   'csf',
                   data=filtered_data,
                   vdom=vdom)


def fortios_system(data, fos):
    login(data)

    methodlist = ['system_csf']
    for method in methodlist:
        if data[method]:
            resp = eval(method)(data, fos)
            break

    fos.logout()
    return not resp['status'] == "success", resp['status'] == "success", resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": "False"},
        "system_csf": {
            "required": False, "type": "dict",
            "options": {
                "configuration-sync": {"required": False, "type": "str",
                                       "choices": ["default", "local"]},
                "fabric-device": {"required": False, "type": "list",
                                  "options": {
                                      "device-ip": {"required": False, "type": "str"},
                                      "device-type": {"required": False, "type": "str",
                                                      "choices": ["fortimail"]},
                                      "login": {"required": False, "type": "str"},
                                      "name": {"required": True, "type": "str"},
                                      "password": {"required": False, "type": "str"}
                                  }},
                "fixed-key": {"required": False, "type": "str"},
                "group-name": {"required": False, "type": "str"},
                "group-password": {"required": False, "type": "str"},
                "management-ip": {"required": False, "type": "str"},
                "management-port": {"required": False, "type": "int"},
                "status": {"required": False, "type": "str",
                           "choices": ["enable", "disable"]},
                "trusted-list": {"required": False, "type": "list",
                                 "options": {
                                     "action": {"required": False, "type": "str",
                                                "choices": ["accept", "deny"]},
                                     "downstream-authorization": {"required": False, "type": "str",
                                                                  "choices": ["enable", "disable"]},
                                     "ha-members": {"required": False, "type": "str"},
                                     "serial": {"required": True, "type": "str"}
                                 }},
                "upstream-ip": {"required": False, "type": "str"},
                "upstream-port": {"required": False, "type": "int"}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)
    try:
        from fortiosapi import FortiOSAPI
    except ImportError:
        module.fail_json(msg="fortiosapi module is required")

    global fos
    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_system(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
