# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CommunicationError(msrest.serialization.Model):
    """The Communication Services error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar code: Required. The error code.
    :vartype code: str
    :ivar message: Required. The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: Further details about specific errors that led to this error.
    :vartype details: list[~azure.communication.phonenumbers.siprouting.models.CommunicationError]
    :ivar inner_error: The inner error if any.
    :vartype inner_error: ~azure.communication.phonenumbers.siprouting.models.CommunicationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CommunicationError]'},
        'inner_error': {'key': 'innererror', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        **kwargs
    ):
        """
        :keyword code: Required. The error code.
        :paramtype code: str
        :keyword message: Required. The error message.
        :paramtype message: str
        """
        super(CommunicationError, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = None
        self.details = None
        self.inner_error = None


class CommunicationErrorResponse(msrest.serialization.Model):
    """The Communication Services error.

    All required parameters must be populated in order to send to Azure.

    :ivar error: Required. The Communication Services error.
    :vartype error: ~azure.communication.phonenumbers.siprouting.models.CommunicationError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        error: "CommunicationError",
        **kwargs
    ):
        """
        :keyword error: Required. The Communication Services error.
        :paramtype error: ~azure.communication.phonenumbers.siprouting.models.CommunicationError
        """
        super(CommunicationErrorResponse, self).__init__(**kwargs)
        self.error = error


class SipConfiguration(msrest.serialization.Model):
    """Represents a SIP configuration.
When a call is being routed the routes are applied in the same order as in the routes list.
A route is matched by its number pattern.
Call is then directed into route's first available trunk, based on the order in the route's trunks list.

    :ivar trunks: SIP trunks for routing calls.
     Map key is trunk's FQDN (1-249 characters).
    :vartype trunks: dict[str,
     ~azure.communication.phonenumbers.siprouting.models.SipTrunkInternal]
    :ivar routes: Trunk routes for routing calls.
    :vartype routes: list[~azure.communication.phonenumbers.siprouting.models.SipTrunkRoute]
    """

    _attribute_map = {
        'trunks': {'key': 'trunks', 'type': '{SipTrunkInternal}'},
        'routes': {'key': 'routes', 'type': '[SipTrunkRoute]'},
    }

    def __init__(
        self,
        *,
        trunks: Optional[Dict[str, "SipTrunkInternal"]] = None,
        routes: Optional[List["SipTrunkRoute"]] = None,
        **kwargs
    ):
        """
        :keyword trunks: SIP trunks for routing calls.
         Map key is trunk's FQDN (1-249 characters).
        :paramtype trunks: dict[str,
         ~azure.communication.phonenumbers.siprouting.models.SipTrunkInternal]
        :keyword routes: Trunk routes for routing calls.
        :paramtype routes: list[~azure.communication.phonenumbers.siprouting.models.SipTrunkRoute]
        """
        super(SipConfiguration, self).__init__(**kwargs)
        self.trunks = trunks
        self.routes = routes


class SipTrunkInternal(msrest.serialization.Model):
    """Represents a SIP trunk for routing calls. See RFC 4904.

    All required parameters must be populated in order to send to Azure.

    :ivar sip_signaling_port: Required. Gets or sets SIP signaling port of the trunk.
    :vartype sip_signaling_port: int
    """

    _validation = {
        'sip_signaling_port': {'required': True},
    }

    _attribute_map = {
        'sip_signaling_port': {'key': 'sipSignalingPort', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        sip_signaling_port: int,
        **kwargs
    ):
        """
        :keyword sip_signaling_port: Required. Gets or sets SIP signaling port of the trunk.
        :paramtype sip_signaling_port: int
        """
        super(SipTrunkInternal, self).__init__(**kwargs)
        self.sip_signaling_port = sip_signaling_port


class SipTrunkRoute(msrest.serialization.Model):
    """Represents a trunk route for routing calls.

    All required parameters must be populated in order to send to Azure.

    :ivar description: Gets or sets description of the route.
    :vartype description: str
    :ivar name: Required. Gets or sets name of the route.
    :vartype name: str
    :ivar number_pattern: Required. Gets or sets regex number pattern for routing calls. .NET regex
     format is supported.
     The regex should match only digits with an optional '+' prefix without spaces.
     I.e. "^+[1-9][0-9]{3,23}$".
    :vartype number_pattern: str
    :ivar trunks: Gets or sets list of SIP trunks for routing calls. Trunks are represented as
     FQDN.
    :vartype trunks: list[str]
    """

    _validation = {
        'description': {'max_length': 1024, 'min_length': 0},
        'name': {'required': True, 'max_length': 256, 'min_length': 0},
        'number_pattern': {'required': True, 'max_length': 1024, 'min_length': 0},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'number_pattern': {'key': 'numberPattern', 'type': 'str'},
        'trunks': {'key': 'trunks', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        name: str,
        number_pattern: str,
        description: Optional[str] = None,
        trunks: Optional[List[str]] = None,
        **kwargs
    ):
        """
        :keyword description: Gets or sets description of the route.
        :paramtype description: str
        :keyword name: Required. Gets or sets name of the route.
        :paramtype name: str
        :keyword number_pattern: Required. Gets or sets regex number pattern for routing calls. .NET
         regex format is supported.
         The regex should match only digits with an optional '+' prefix without spaces.
         I.e. "^+[1-9][0-9]{3,23}$".
        :paramtype number_pattern: str
        :keyword trunks: Gets or sets list of SIP trunks for routing calls. Trunks are represented as
         FQDN.
        :paramtype trunks: list[str]
        """
        super(SipTrunkRoute, self).__init__(**kwargs)
        self.description = description
        self.name = name
        self.number_pattern = number_pattern
        self.trunks = trunks
