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
import json
from enum import Enum
from typing_extensions import Self


class DatasetResultType(str, Enum):
    """
    DatasetResultType
    """

    """
    allowed enum values
    """
    BASE64 = 'BASE64'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DatasetResultType from a JSON string"""
        return cls(json.loads(json_str))


