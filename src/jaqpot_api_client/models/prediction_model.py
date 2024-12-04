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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from jaqpot_api_client.models.feature import Feature
from jaqpot_api_client.models.model_task import ModelTask
from jaqpot_api_client.models.model_type import ModelType
from jaqpot_api_client.models.prediction_doa import PredictionDoa
from jaqpot_api_client.models.transformer import Transformer
from typing import Optional, Set
from typing_extensions import Self

class PredictionModel(BaseModel):
    """
    PredictionModel
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the prediction model")
    dependent_features: List[Feature] = Field(description="List of dependent features for the model", alias="dependentFeatures")
    independent_features: List[Feature] = Field(description="List of independent features for the model", alias="independentFeatures")
    type: ModelType
    raw_model: StrictStr = Field(description="Raw model data in serialized format", alias="rawModel")
    raw_preprocessor: Optional[StrictStr] = Field(default=None, description="Raw preprocessor data in serialized format", alias="rawPreprocessor")
    doas: Optional[List[PredictionDoa]] = Field(default=None, description="List of Domain of Applicability (DoA) configurations")
    selected_features: Optional[List[StrictStr]] = Field(default=None, description="List of feature names selected for the model", alias="selectedFeatures")
    task: ModelTask
    featurizers: Optional[List[Transformer]] = Field(default=None, description="List of featurizer configurations applied to the model")
    preprocessors: Optional[List[Transformer]] = Field(default=None, description="List of preprocessor configurations applied to the model")
    torch_config: Optional[Dict[str, Any]] = Field(default=None, description="Torch configuration settings, optional", alias="torchConfig")
    r_pbpk_ode_solver: Optional[StrictStr] = Field(default=None, alias="rPbpkOdeSolver")
    legacy_additional_info: Optional[Dict[str, Any]] = Field(default=None, description="Legacy additional information settings, optional", alias="legacyAdditionalInfo")
    legacy_prediction_service: Optional[StrictStr] = Field(default=None, description="Legacy prediction service information, if available", alias="legacyPredictionService")
    __properties: ClassVar[List[str]] = ["id", "dependentFeatures", "independentFeatures", "type", "rawModel", "rawPreprocessor", "doas", "selectedFeatures", "task", "featurizers", "preprocessors", "torchConfig", "rPbpkOdeSolver", "legacyAdditionalInfo", "legacyPredictionService"]

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
        """Create an instance of PredictionModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dependent_features (list)
        _items = []
        if self.dependent_features:
            for _item_dependent_features in self.dependent_features:
                if _item_dependent_features:
                    _items.append(_item_dependent_features.to_dict())
            _dict['dependentFeatures'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in independent_features (list)
        _items = []
        if self.independent_features:
            for _item_independent_features in self.independent_features:
                if _item_independent_features:
                    _items.append(_item_independent_features.to_dict())
            _dict['independentFeatures'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in doas (list)
        _items = []
        if self.doas:
            for _item_doas in self.doas:
                if _item_doas:
                    _items.append(_item_doas.to_dict())
            _dict['doas'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in featurizers (list)
        _items = []
        if self.featurizers:
            for _item_featurizers in self.featurizers:
                if _item_featurizers:
                    _items.append(_item_featurizers.to_dict())
            _dict['featurizers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in preprocessors (list)
        _items = []
        if self.preprocessors:
            for _item_preprocessors in self.preprocessors:
                if _item_preprocessors:
                    _items.append(_item_preprocessors.to_dict())
            _dict['preprocessors'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if torch_config (nullable) is None
        # and model_fields_set contains the field
        if self.torch_config is None and "torch_config" in self.model_fields_set:
            _dict['torchConfig'] = None

        # set to None if legacy_additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.legacy_additional_info is None and "legacy_additional_info" in self.model_fields_set:
            _dict['legacyAdditionalInfo'] = None

        # set to None if legacy_prediction_service (nullable) is None
        # and model_fields_set contains the field
        if self.legacy_prediction_service is None and "legacy_prediction_service" in self.model_fields_set:
            _dict['legacyPredictionService'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PredictionModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "dependentFeatures": [Feature.from_dict(_item) for _item in obj["dependentFeatures"]] if obj.get("dependentFeatures") is not None else None,
            "independentFeatures": [Feature.from_dict(_item) for _item in obj["independentFeatures"]] if obj.get("independentFeatures") is not None else None,
            "type": obj.get("type"),
            "rawModel": obj.get("rawModel"),
            "rawPreprocessor": obj.get("rawPreprocessor"),
            "doas": [PredictionDoa.from_dict(_item) for _item in obj["doas"]] if obj.get("doas") is not None else None,
            "selectedFeatures": obj.get("selectedFeatures"),
            "task": obj.get("task"),
            "featurizers": [Transformer.from_dict(_item) for _item in obj["featurizers"]] if obj.get("featurizers") is not None else None,
            "preprocessors": [Transformer.from_dict(_item) for _item in obj["preprocessors"]] if obj.get("preprocessors") is not None else None,
            "torchConfig": obj.get("torchConfig"),
            "rPbpkOdeSolver": obj.get("rPbpkOdeSolver"),
            "legacyAdditionalInfo": obj.get("legacyAdditionalInfo"),
            "legacyPredictionService": obj.get("legacyPredictionService")
        })
        return _obj


