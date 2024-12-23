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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetAllApiKeysForUser200ResponseInner(BaseModel):
    """
    GetAllApiKeysForUser200ResponseInner
    """ # noqa: E501
    client_key: Optional[StrictStr] = Field(default=None, description="The API key", alias="clientKey")
    note: Optional[StrictStr] = Field(default=None, description="Description of the API key")
    created_at: Optional[datetime] = Field(default=None, description="Creation timestamp of the API key", alias="createdAt")
    expires_at: Optional[datetime] = Field(default=None, description="Expiration timestamp of the API key (optional)", alias="expiresAt")
    enabled: Optional[StrictBool] = Field(default=None, description="Whether the API key is active or disabled")
    __properties: ClassVar[List[str]] = ["clientKey", "note", "createdAt", "expiresAt", "enabled"]

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
        """Create an instance of GetAllApiKeysForUser200ResponseInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetAllApiKeysForUser200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientKey": obj.get("clientKey"),
            "note": obj.get("note"),
            "createdAt": obj.get("createdAt"),
            "expiresAt": obj.get("expiresAt"),
            "enabled": obj.get("enabled")
        })
        return _obj


