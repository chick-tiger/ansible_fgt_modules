#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
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
module: fortios_firewall.service_group
short_description: Configure service groups.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure firewall.service feature and group category.
      Examples includes all options and need to be adjusted to datasources before usage.
      Tested with FOS: v6.0.2
version_added: "2.6"
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
        default: "root"
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
    firewall.service_group:
        description:
            - Configure service groups.
        default: null
        suboptions:
            color:
                description:
                    - Color of icon on the GUI.
            comment:
                description:
                    - Comment.
            member:
                description:
                    - Service objects contained within the group.
                suboptions:
                    name:
                        description:
                            - Address name. Source: firewall.service.custom.name firewall.service.group.name.
                        required: true
            name:
                description:
                    - Address group name.
                required: true
            proxy:
                description:
                    - Enable/disable web proxy service group.
                choices:
                    - enable
                    - disable
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure service groups.
    fortios_firewall.service_group:
      host:  "{{  host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{  vdom }}"
      firewall.service_group:
        state: "present"
        color: "3"
        comment: "Comment."
        member:
         -
            name: "default_name_6 (source: firewall.service.custom.name firewall.service.group.name)"
        name: "default_name_7"
        proxy: "enable"
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


def filter_firewall.service_group_data(json):
    option_list = ['color', 'comment', 'member',
                   'name', 'proxy']
    dictionary = {}

    for attribute in option_list:
        if attribute in json:
            dictionary[attribute] = json[attribute]

    return dictionary


def firewall.service_group(data, fos):
    vdom = data['vdom']
    firewall.service_group_data = data['firewall.service_group']
    filtered_data = filter_firewall.service_group_data(
        firewall.service_group_data)

    if firewall.service_group_data['state'] == "present":
        return fos.set('firewall.service',
                       'group',
                       data=filtered_data,
                       vdom=vdom)

    elif firewall.service_group_data['state'] == "absent":
        return fos.delete('firewall.service',
                          'group',
                          mkey=filtered_data['id'],
                          vdom=vdom)


def fortios_firewall.service(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    fos.https('off')
    fos.login(host, username, password)

    methodlist = ['firewall.service_group']
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
        "https": {"required": False, "type": "bool", "default": "True"},
        "firewall.service_group": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str"},
                "color": {"required": False, "type": "int"},
                "comment": {"required": False, "type": "str"},
                "member": {"required": False, "type": "list",
                           "options": {
                               "name": {"required": True, "type": "str"}
                           }},
                "name": {"required": True, "type": "str"},
                "proxy": {"required": False, "type": "str",
                          "choices": ["enable", "disable"]}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)
    try:
        from fortiosapi import FortiOSAPI
    except ImportError:
        module.fail_json(msg="fortiosapi module is required")

    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_firewall.service(
        module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()