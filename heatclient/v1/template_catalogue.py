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


class TemplateCatalogue(base.Resource):
    def __repr__(self):
        return "<Template Catalogue %s>" % self._info

    def delete(self):
        return self.manager.delete(deployment_id=self.id)


class TemplateCatalogueManager(base.BaseManager):
    resource_class = TemplateCatalogue

    def list(self):
        return self._list('/template_catalogue', "template_catalogues")

    def create(self, **kwargs):
        headers = self.client.credentials_headers()
        resp, body = self.client.json_request('POST', '/template_catalogue',
                                              data=kwargs, headers=headers)
        return TemplateCatalogue(self, body['template_catalogue'])

    def delete(self, template_catalogue_id):
        self._delete("/template_catalogue/%s" % template_catalogue_id)

    def get(self, template_catalogue_id):
        resp, body = self.client.json_request('GET', '/template_catalogue/%s' %
                                                     template_catalogue_id)
        return TemplateCatalogue(self, body['template_catalogue'])
