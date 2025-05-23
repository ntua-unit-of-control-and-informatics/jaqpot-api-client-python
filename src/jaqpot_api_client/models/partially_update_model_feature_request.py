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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from jaqpot_api_client.models.feature_possible_value import FeaturePossibleValue
from jaqpot_api_client.models.feature_type import FeatureType
from typing import Optional, Set
from typing_extensions import Self

class PartiallyUpdateModelFeatureRequest(BaseModel):
    """
    PartiallyUpdateModelFeatureRequest
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=255)] = Field(description="A name for the feature that will appear on top of the form field")
    units: Optional[StrictStr] = Field(default=None, description="The units that this feature is using")
    range: Optional[StrictStr] = Field(default=None, description="The range that this feature is using")
    description: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    feature_type: FeatureType = Field(alias="featureType")
    possible_values: Optional[Annotated[List[FeaturePossibleValue], Field(max_length=1000)]] = Field(default=None, alias="possibleValues")
    __properties: ClassVar[List[str]] = ["name", "units", "range", "description", "featureType", "possibleValues"]

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
        """Create an instance of PartiallyUpdateModelFeatureRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in possible_values (list)
        _items = []
        if self.possible_values:
            for _item_possible_values in self.possible_values:
                if _item_possible_values:
                    _items.append(_item_possible_values.to_dict())
            _dict['possibleValues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PartiallyUpdateModelFeatureRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "units": obj.get("units"),
            "range": obj.get("range"),
            "description": obj.get("description"),
            "featureType": obj.get("featureType"),
            "possibleValues": [FeaturePossibleValue.from_dict(_item) for _item in obj["possibleValues"]] if obj.get("possibleValues") is not None else None
        })
        return _obj


