# coding: utf-8

# flake8: noqa
"""
    Jaqpot API

    A modern RESTful API for model management and prediction services, built using Spring Boot and Kotlin. Supports seamless integration with machine learning workflows.

    The version of the OpenAPI document: 1.0.0
    Contact: upci.ntua@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from jaqpot_api_client.models.api_key import ApiKey
from jaqpot_api_client.models.archive_model200_response import ArchiveModel200Response
from jaqpot_api_client.models.binary_classification_scores import BinaryClassificationScores
from jaqpot_api_client.models.bounding_box_doa import BoundingBoxDoa
from jaqpot_api_client.models.city_block_doa import CityBlockDoa
from jaqpot_api_client.models.create_api_key201_response import CreateApiKey201Response
from jaqpot_api_client.models.create_invitations_request import CreateInvitationsRequest
from jaqpot_api_client.models.dataset import Dataset
from jaqpot_api_client.models.dataset_csv import DatasetCSV
from jaqpot_api_client.models.dataset_result_type import DatasetResultType
from jaqpot_api_client.models.dataset_type import DatasetType
from jaqpot_api_client.models.doa import Doa
from jaqpot_api_client.models.doa_method import DoaMethod
from jaqpot_api_client.models.docker_config import DockerConfig
from jaqpot_api_client.models.error_code import ErrorCode
from jaqpot_api_client.models.error_response import ErrorResponse
from jaqpot_api_client.models.feature import Feature
from jaqpot_api_client.models.feature_possible_value import FeaturePossibleValue
from jaqpot_api_client.models.feature_type import FeatureType
from jaqpot_api_client.models.get_all_api_keys_for_user200_response_inner import GetAllApiKeysForUser200ResponseInner
from jaqpot_api_client.models.get_datasets200_response import GetDatasets200Response
from jaqpot_api_client.models.get_models200_response import GetModels200Response
from jaqpot_api_client.models.kernel_based_doa import KernelBasedDoa
from jaqpot_api_client.models.lead import Lead
from jaqpot_api_client.models.leverage_doa import LeverageDoa
from jaqpot_api_client.models.library import Library
from jaqpot_api_client.models.mahalanobis_doa import MahalanobisDoa
from jaqpot_api_client.models.mean_var_doa import MeanVarDoa
from jaqpot_api_client.models.model import Model
from jaqpot_api_client.models.model_scores import ModelScores
from jaqpot_api_client.models.model_summary import ModelSummary
from jaqpot_api_client.models.model_task import ModelTask
from jaqpot_api_client.models.model_type import ModelType
from jaqpot_api_client.models.model_visibility import ModelVisibility
from jaqpot_api_client.models.multiclass_classification_scores import MulticlassClassificationScores
from jaqpot_api_client.models.organization import Organization
from jaqpot_api_client.models.organization_invitation import OrganizationInvitation
from jaqpot_api_client.models.organization_summary import OrganizationSummary
from jaqpot_api_client.models.organization_user import OrganizationUser
from jaqpot_api_client.models.organization_user_association_type import OrganizationUserAssociationType
from jaqpot_api_client.models.organization_visibility import OrganizationVisibility
from jaqpot_api_client.models.partial_update_organization_request import PartialUpdateOrganizationRequest
from jaqpot_api_client.models.partially_update_model_feature_request import PartiallyUpdateModelFeatureRequest
from jaqpot_api_client.models.partially_update_model_request import PartiallyUpdateModelRequest
from jaqpot_api_client.models.prediction_doa import PredictionDoa
from jaqpot_api_client.models.prediction_model import PredictionModel
from jaqpot_api_client.models.prediction_request import PredictionRequest
from jaqpot_api_client.models.prediction_response import PredictionResponse
from jaqpot_api_client.models.r_pbpk_config import RPbpkConfig
from jaqpot_api_client.models.regression_scores import RegressionScores
from jaqpot_api_client.models.scores import Scores
from jaqpot_api_client.models.transformer import Transformer
from jaqpot_api_client.models.unarchive_model200_response import UnarchiveModel200Response
from jaqpot_api_client.models.update_api_key200_response import UpdateApiKey200Response
from jaqpot_api_client.models.update_api_key_request import UpdateApiKeyRequest
from jaqpot_api_client.models.user import User
from jaqpot_api_client.models.user_settings import UserSettings
