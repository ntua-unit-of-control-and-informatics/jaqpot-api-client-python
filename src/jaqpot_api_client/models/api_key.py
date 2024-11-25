# coding: utf-8

"""
    Jaqpot API

    A modern RESTful API for model management and prediction services, built using Spring Boot and Kotlin. Supports seamless integration with machine learning workflows.

    The version of the OpenAPI document: 1.0.0
    Contact: upci.ntua@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiKey(BaseModel):
    """
    ApiKey
    """ # noqa: E501
    client_key: Optional[StrictStr] = Field(default=None, description="The generated API key", alias="clientKey")
    note: Optional[StrictStr] = Field(default=None, description="A note for the API key")
    user_id: Optional[StrictStr] = Field(default=None, description="The ID of the user associated with the API key", alias="userId")
    expires_at: Optional[datetime] = Field(default=None, description="The expiration time of the API key (if any)", alias="expiresAt")
    expiration_time: StrictStr = Field(alias="expirationTime")
    last_used: Optional[datetime] = Field(default=None, description="The last time the API key was used", alias="lastUsed")
    last_used_ip: Optional[StrictStr] = Field(default=None, description="The IP address from which the API key was last used", alias="lastUsedIp")
    enabled: Optional[StrictBool] = Field(default=None, description="Whether the API key is active or disabled")
    __properties: ClassVar[List[str]] = ["clientKey", "note", "userId", "expiresAt", "expirationTime", "lastUsed", "lastUsedIp", "enabled"]

    @field_validator('expiration_time')
    def expiration_time_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['THREE_MONTHS', 'SIX_MONTHS']):
            raise ValueError("must be one of enum values ('THREE_MONTHS', 'SIX_MONTHS')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expiresAt'] = None

        # set to None if last_used (nullable) is None
        # and model_fields_set contains the field
        if self.last_used is None and "last_used" in self.model_fields_set:
            _dict['lastUsed'] = None

        # set to None if last_used_ip (nullable) is None
        # and model_fields_set contains the field
        if self.last_used_ip is None and "last_used_ip" in self.model_fields_set:
            _dict['lastUsedIp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientKey": obj.get("clientKey"),
            "note": obj.get("note"),
            "userId": obj.get("userId"),
            "expiresAt": obj.get("expiresAt"),
            "expirationTime": obj.get("expirationTime"),
            "lastUsed": obj.get("lastUsed"),
            "lastUsedIp": obj.get("lastUsedIp"),
            "enabled": obj.get("enabled")
        })
        return _obj

