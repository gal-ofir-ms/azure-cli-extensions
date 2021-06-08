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


class NetworkInterfaceUpdate(Model):
    """Defines the network interface update.

    :param name: Gets or sets the name of the network interface.
    :type name: str
    :param network_id: Gets or sets the ARM Id of the network resource to
     connect the virtual machine.
    :type network_id: str
    :param nic_type: NIC type. Possible values include: 'vmxnet3', 'vmxnet2',
     'vmxnet', 'e1000', 'e1000e', 'pcnet32'
    :type nic_type: str or
     ~azure.mgmt.vmware.v2020_10_01_preview.models.NICType
    :param power_on_boot: Gets or sets the power on boot. Possible values
     include: 'enabled', 'disabled'
    :type power_on_boot: str or
     ~azure.mgmt.vmware.v2020_10_01_preview.models.PowerOnBootOption
    :param device_key: Gets or sets the device key value.
    :type device_key: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'network_id': {'key': 'networkId', 'type': 'str'},
        'nic_type': {'key': 'nicType', 'type': 'str'},
        'power_on_boot': {'key': 'powerOnBoot', 'type': 'str'},
        'device_key': {'key': 'deviceKey', 'type': 'int'},
    }

    def __init__(self, *, name: str=None, network_id: str=None, nic_type=None, power_on_boot=None, device_key: int=None, **kwargs) -> None:
        super(NetworkInterfaceUpdate, self).__init__(**kwargs)
        self.name = name
        self.network_id = network_id
        self.nic_type = nic_type
        self.power_on_boot = power_on_boot
        self.device_key = device_key
