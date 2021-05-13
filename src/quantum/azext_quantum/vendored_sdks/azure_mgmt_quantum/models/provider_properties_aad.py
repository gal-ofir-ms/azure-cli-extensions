# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProviderPropertiesAad(Model):
    """Azure Active Directory info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar application_id: Provider's application id.
    :vartype application_id: str
    :ivar tenant_id: Provider's tenant id.
    :vartype tenant_id: str
    """

    _validation = {
        'application_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProviderPropertiesAad, self).__init__(**kwargs)
        self.application_id = None
        self.tenant_id = None
