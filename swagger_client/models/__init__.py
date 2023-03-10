# coding: utf-8

# flake8: noqa
"""
    Compass - Request Tracker

    API documentation for Compass - Request Tracker. This document contains a complete list of fields for a Compass request accessible to an admin. An authorized user may only read, write, and update certain fields or delete based on their role. All requests require a valid OAuth2 Bearer Token passed as a header that is associated with a Cisco CEC user account.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: compass-devcx@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.account_name_schema import AccountNameSchema
from swagger_client.models.advisor_assigned_schema import AdvisorAssignedSchema
from swagger_client.models.advisor_notes_schema import AdvisorNotesSchema
from swagger_client.models.api_transaction_id_schema import ApiTransactionIdSchema
from swagger_client.models.appliance_id_schema import ApplianceIdSchema
from swagger_client.models.bcs_estimate_schema import BcsEstimateSchema
from swagger_client.models.be_geo_id_schema import BeGeoIdSchema
from swagger_client.models.bulk_patch_response import BulkPatchResponse
from swagger_client.models.campaign_name_schema import CampaignNameSchema
from swagger_client.models.cav_id_schema import CavIdSchema
from swagger_client.models.column_config import ColumnConfig
from swagger_client.models.column_name_schema import ColumnNameSchema
from swagger_client.models.column_values_schema import ColumnValuesSchema
from swagger_client.models.compass_ppt_url_schema import CompassPptUrlSchema
from swagger_client.models.compass_url_schema import CompassUrlSchema
from swagger_client.models.completed_dtm_schema import CompletedDtmSchema
from swagger_client.models.concierge_account_team_notes_schema import ConciergeAccountTeamNotesSchema
from swagger_client.models.concierge_advisor_assigned_schema import ConciergeAdvisorAssignedSchema
from swagger_client.models.concierge_business_objective_schema import ConciergeBusinessObjectiveSchema
from swagger_client.models.concierge_external_readout_dt_schema import ConciergeExternalReadoutDtSchema
from swagger_client.models.concierge_external_readout_result_schema import ConciergeExternalReadoutResultSchema
from swagger_client.models.concierge_internal_readout_dt_schema import ConciergeInternalReadoutDtSchema
from swagger_client.models.concierge_internal_result_schema import ConciergeInternalResultSchema
from swagger_client.models.concierge_requested_flag_schema import ConciergeRequestedFlagSchema
from swagger_client.models.contract_number_schema import ContractNumberSchema
from swagger_client.models.coverage_report_requested_flag_schema import CoverageReportRequestedFlagSchema
from swagger_client.models.cr_party_id_schema import CrPartyIdSchema
from swagger_client.models.cr_party_name_schema import CrPartyNameSchema
from swagger_client.models.customer_identifier_schema import CustomerIdentifierSchema
from swagger_client.models.deal_id_schema import DealIdSchema
from swagger_client.models.declined_reason_schema import DeclinedReasonSchema
from swagger_client.models.distribution_list_schema import DistributionListSchema
from swagger_client.models.ea_estimate_schema import EaEstimateSchema
from swagger_client.models.ec_estimate_schema import EcEstimateSchema
from swagger_client.models.email_sent_flag_schema import EmailSentFlagSchema
from swagger_client.models.email_sent_to_ssx_flag_schema import EmailSentToSsxFlagSchema
from swagger_client.models.error_response import ErrorResponse
from swagger_client.models.error_response_reason import ErrorResponseReason
from swagger_client.models.estimator_value_schema import EstimatorValueSchema
from swagger_client.models.failure_details_schema import FailureDetailsSchema
from swagger_client.models.final_estimate_sent_schema import FinalEstimateSentSchema
from swagger_client.models.final_oppty_value_schema import FinalOpptyValueSchema
from swagger_client.models.gu_id_schema import GuIdSchema
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inventory_name_schema import InventoryNameSchema
from swagger_client.models.is_public_flag_schema import IsPublicFlagSchema
from swagger_client.models.items_recommended_schema import ItemsRecommendedSchema
from swagger_client.models.latest_view_id_schema import LatestViewIdSchema
from swagger_client.models.low_volume_count_schema import LowVolumeCountSchema
from swagger_client.models.modified_by_schema import ModifiedBySchema
from swagger_client.models.modified_dtm_schema import ModifiedDtmSchema
from swagger_client.models.next_steps_schema import NextStepsSchema
from swagger_client.models.oa_package_type_schema import OaPackageTypeSchema
from swagger_client.models.offer_creator_coverage_report_url_schema import OfferCreatorCoverageReportUrlSchema
from swagger_client.models.offer_creator_declined_reason_schema import OfferCreatorDeclinedReasonSchema
from swagger_client.models.offer_creator_email_schema import OfferCreatorEmailSchema
from swagger_client.models.offer_creator_notes_schema import OfferCreatorNotesSchema
from swagger_client.models.offer_creator_readout_dt_schema import OfferCreatorReadoutDtSchema
from swagger_client.models.offer_creator_readout_status_schema import OfferCreatorReadoutStatusSchema
from swagger_client.models.op_url_schema import OpUrlSchema
from swagger_client.models.oppty_id_schema import OpptyIdSchema
from swagger_client.models.oppty_name_schema import OpptyNameSchema
from swagger_client.models.page_limit_schema import PageLimitSchema
from swagger_client.models.pagination import Pagination
from swagger_client.models.partner_approved_entitlements_schema import PartnerApprovedEntitlementsSchema
from swagger_client.models.partner_loa_content_schema import PartnerLoaContentSchema
from swagger_client.models.partner_loa_metadata import PartnerLoaMetadata
from swagger_client.models.partner_name_schema import PartnerNameSchema
from swagger_client.models.partner_requested_entitlements_schema import PartnerRequestedEntitlementsSchema
from swagger_client.models.readout_delivery_status_schema import ReadoutDeliveryStatusSchema
from swagger_client.models.readout_done_dt_schema import ReadoutDoneDtSchema
from swagger_client.models.report_exist_flag_schema import ReportExistFlagSchema
from swagger_client.models.report_type_schema import ReportTypeSchema
from swagger_client.models.request import Request
from swagger_client.models.request_created_by_schema import RequestCreatedBySchema
from swagger_client.models.request_id_schema import RequestIdSchema
from swagger_client.models.request_type_schema import RequestTypeSchema
from swagger_client.models.requested_dtm_schema import RequestedDtmSchema
from swagger_client.models.requester_comments_schema import RequesterCommentsSchema
from swagger_client.models.requester_function_schema import RequesterFunctionSchema
from swagger_client.models.requester_name_schema import RequesterNameSchema
from swagger_client.models.risk_score_schema import RiskScoreSchema
from swagger_client.models.rr_internal_schema import RrInternalSchema
from swagger_client.models.sales_cx_team_schema import SalesCxTeamSchema
from swagger_client.models.sales_level1_schema import SalesLevel1Schema
from swagger_client.models.sales_level2_schema import SalesLevel2Schema
from swagger_client.models.sales_level3_schema import SalesLevel3Schema
from swagger_client.models.sales_level4_schema import SalesLevel4Schema
from swagger_client.models.sales_level5_schema import SalesLevel5Schema
from swagger_client.models.sales_level6_schema import SalesLevel6Schema
from swagger_client.models.sav_id_schema import SavIdSchema
from swagger_client.models.session_cache_entry import SessionCacheEntry
from swagger_client.models.sessions_metadata import SessionsMetadata
from swagger_client.models.sntc_estimate_schema import SntcEstimateSchema
from swagger_client.models.ssp_schema import SspSchema
from swagger_client.models.ssp_unsubscribed_schema import SspUnsubscribedSchema
from swagger_client.models.sspt_estimate_schema import SsptEstimateSchema
from swagger_client.models.st_estimate_schema import StEstimateSchema
from swagger_client.models.status_schema import StatusSchema
from swagger_client.models.tableau_project_name_schema import TableauProjectNameSchema
from swagger_client.models.target_request_id_schema import TargetRequestIdSchema
from swagger_client.models.target_request_type_schema import TargetRequestTypeSchema
from swagger_client.models.targeted_fiscal_month_schema import TargetedFiscalMonthSchema
from swagger_client.models.transaction import Transaction
from swagger_client.models.transaction_changes import TransactionChanges
from swagger_client.models.transaction_changes_field_name import TransactionChangesFieldName
from swagger_client.models.unsubscribed_user_info import UnsubscribedUserInfo
from swagger_client.models.user_info import UserInfo
from swagger_client.models.version_info import VersionInfo
from swagger_client.models.view import View
from swagger_client.models.view_base_columns import ViewBaseColumns
from swagger_client.models.view_description_schema import ViewDescriptionSchema
from swagger_client.models.view_filters import ViewFilters
from swagger_client.models.view_filters_az_az09 import ViewFiltersAzAZ09
from swagger_client.models.view_name_schema import ViewNameSchema
from swagger_client.models.view_sort import ViewSort
from swagger_client.models.written_loa_url_for_patch_schema import WrittenLoaUrlForPatchSchema
from swagger_client.models.written_loa_url_schema import WrittenLoaUrlSchema
