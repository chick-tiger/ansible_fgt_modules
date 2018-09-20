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
module: fortios_web-proxy_profile
short_description: Configure web proxy profiles.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure web-proxy feature and profile category.
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
    web-proxy_profile:
        description:
            - Configure web proxy profiles.
        default: null
        suboptions:
            header-client-ip:
                description:
                    - Action to take on the HTTP client-IP header in forwarded requests: forwards (pass), adds, or removes the HTTP header.
                choices:
                    - pass
                    - add
                    - remove
            header-front-end-https:
                description:
                    - Action to take on the HTTP front-end-HTTPS header in forwarded requests: forwards (pass), adds, or removes the HTTP header.
                choices:
                    - pass
                    - add
                    - remove
            header-via-request:
                description:
                    - Action to take on the HTTP via header in forwarded requests: forwards (pass), adds, or removes the HTTP header.
                choices:
                    - pass
                    - add
                    - remove
            header-via-response:
                description:
                    - Action to take on the HTTP via header in forwarded responses: forwards (pass), adds, or removes the HTTP header.
                choices:
                    - pass
                    - add
                    - remove
            header-x-authenticated-groups:
                description:
                    - Action to take on the HTTP x-authenticated-groups header in forwarded requests: forwards (pass), adds, or removes the HTTP header.
                choices:
                    - pass
                    - add
                    - remove
            header-x-authenticated-user:
                description:
                    - Action to take on the HTTP x-authenticated-user header in forwarded requests: forwards (pass), adds, or removes the HTTP header.
                choices:
                    - pass
                    - add
                    - remove
            header-x-forwarded-for:
                description:
                    - Action to take on the HTTP x-forwarded-for header in forwarded requests: forwards (pass), adds, or removes the HTTP header.
                choices:
                    - pass
                    - add
                    - remove
            headers:
                description:
                    - Configure HTTP forwarded requests headers.
                suboptions:
                    action:
                        description:
                            - Action when HTTP the header forwarded.
                        choices:
                            - add-to-request
                            - add-to-response
                            - remove-from-request
                            - remove-from-response
                    content:
                        description:
                            - HTTP header's content.
                    id:
                        description:
                            - HTTP forwarded header id.
                        required: true
                    name:
                        description:
                            - HTTP forwarded header name.
                        required: true
            log-header-change:
                description:
                    - Enable/disable logging HTTP header changes.
                choices:
                    - enable
                    - disable
            name:
                description:
                    - Profile name.
                required: true
            strip-encoding:
                description:
                    - Enable/disable stripping unsupported encoding from the request header.
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
  - name: Configure web proxy profiles.
    fortios_web-proxy_profile:
      host:  "{{  host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{  vdom }}"
      web-proxy_profile:
        state: "present"
        header-client-ip: "pass"
        header-front-end-https: "pass"
        header-via-request: "pass"
        header-via-response: "pass"
        header-x-authenticated-groups: "pass"
        header-x-authenticated-user: "pass"
        header-x-forwarded-for: "pass"
        headers:
         -
            action: "add-to-request"
            content: "<your_own_value>"
            id:  "13"
            name: "default_name_14"
        log-header-change: "enable"
        name: "default_name_16"
        strip-encoding: "enable"
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


def filter_web-proxy_profile_data(json):
    option_list = ['header-client-ip', 'header-front-end-https', 'header-via-request',
                   'header-via-response', 'header-x-authenticated-groups', 'header-x-authenticated-user',
                   'header-x-forwarded-for', 'headers', 'log-header-change',
                   'name', 'strip-encoding']
    dictionary = {}

    for attribute in option_list:
        if attribute in json:
            dictionary[attribute] = json[attribute]

    return dictionary


def web-proxy_profile(data, fos):
    vdom = data['vdom']
    web-proxy_profile_data = data['web-proxy_profile']
    filtered_data = filter_web-proxy_profile_data(web-proxy_profile_data)

    if web-proxy_profile_data['state'] == "present":
        return fos.set('web-proxy',
                       'profile',
                       data=filtered_data,
                       vdom=vdom)

    elif web-proxy_profile_data['state'] == "absent":
        return fos.delete('web-proxy',
                          'profile',
                          mkey=filtered_data['id'],
                          vdom=vdom)


def fortios_web-proxy(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    fos.https('off')
    fos.login(host, username, password)

    methodlist = ['web-proxy_profile']
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
        "web-proxy_profile": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str"},
                "header-client-ip": {"required": False, "type": "str",
                                     "choices": ["pass", "add", "remove"]},
                "header-front-end-https": {"required": False, "type": "str",
                                           "choices": ["pass", "add", "remove"]},
                "header-via-request": {"required": False, "type": "str",
                                       "choices": ["pass", "add", "remove"]},
                "header-via-response": {"required": False, "type": "str",
                                        "choices": ["pass", "add", "remove"]},
                "header-x-authenticated-groups": {"required": False, "type": "str",
                                                  "choices": ["pass", "add", "remove"]},
                "header-x-authenticated-user": {"required": False, "type": "str",
                                                "choices": ["pass", "add", "remove"]},
                "header-x-forwarded-for": {"required": False, "type": "str",
                                           "choices": ["pass", "add", "remove"]},
                "headers": {"required": False, "type": "list",
                            "options": {
                                "action": {"required": False, "type": "str",
                                           "choices": ["add-to-request", "add-to-response", "remove-from-request",
                                                       "remove-from-response"]},
                                "content": {"required": False, "type": "str"},
                                "id": {"required": True, "type": "int"},
                                "name": {"required": True, "type": "str"}
                            }},
                "log-header-change": {"required": False, "type": "str",
                                      "choices": ["enable", "disable"]},
                "name": {"required": True, "type": "str"},
                "strip-encoding": {"required": False, "type": "str",
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

    is_error, has_changed, result = fortios_web-proxy(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()