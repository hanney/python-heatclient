# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from heatclient.openstack.common.apiclient import base


class Discovery(base.Resource):
    def __repr__(self):
        return "<Discovery %s>" % self._info

    def init(self):
        return self.manager.init()

    def dump(self, **fields):
        return self.manager.dump(**fields)


class DiscoveryManager(base.BaseManager):
    resource_class = Discovery

    def init(self):
        resp, body = self.client.json_request('GET', '/discovery/init')
        return body

    def dump(self, **kwargs):
        resp, body = self.client.json_request('POST', '/discovery/dump',
                                              data=kwargs)
        return body['template']
