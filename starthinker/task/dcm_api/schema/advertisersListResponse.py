###########################################################################
#
#  Copyright 2019 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

advertisersListResponse_Schema = [
  {
    "mode": "NULLABLE", 
    "type": "STRING", 
    "description": "", 
    "name": "nextPageToken"
  }, 
  {
    "fields": [
      {
        "mode": "NULLABLE", 
        "type": "STRING", 
        "description": "APPROVED, ON_HOLD", 
        "name": "status"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "STRING", 
        "description": "", 
        "name": "kind"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "subaccountId"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "STRING", 
        "description": "", 
        "name": "name"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "defaultClickThroughEventTagId"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "originalFloodlightConfigurationId"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "STRING", 
        "description": "", 
        "name": "clickThroughUrlSuffix"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "floodlightConfigurationId"
      }, 
      {
        "type": "BOOLEAN", 
        "name": "suspended", 
        "mode": "NULLABLE"
      }, 
      [
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "kind"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "value"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "dimensionName"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "etag"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "BEGINS_WITH, CONTAINS, EXACT, WILDCARD_EXPRESSION", 
          "name": "matchType"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "id"
        }
      ], 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "advertiserGroupId"
      }, 
      [
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "kind"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "value"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "dimensionName"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "etag"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "BEGINS_WITH, CONTAINS, EXACT, WILDCARD_EXPRESSION", 
          "name": "matchType"
        }, 
        {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "", 
          "name": "id"
        }
      ], 
      {
        "mode": "NULLABLE", 
        "type": "STRING", 
        "description": "", 
        "name": "defaultEmail"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "id"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "accountId"
      }
    ], 
    "type": "RECORD", 
    "name": "advertisers", 
    "mode": "REPEATED"
  }, 
  {
    "mode": "NULLABLE", 
    "type": "STRING", 
    "description": "", 
    "name": "kind"
  }
]