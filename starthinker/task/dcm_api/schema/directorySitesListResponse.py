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

directorySitesListResponse_Schema = [
  {
    "mode": "NULLABLE", 
    "type": "STRING", 
    "description": "", 
    "name": "nextPageToken"
  }, 
  {
    "mode": "NULLABLE", 
    "type": "STRING", 
    "description": "", 
    "name": "kind"
  }, 
  {
    "fields": [
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
        "name": "name"
      }, 
      [
        {
          "type": "BOOLEAN", 
          "name": "interstitialPlacementAccepted", 
          "mode": "NULLABLE"
        }, 
        {
          "type": "BOOLEAN", 
          "name": "activeViewOptOut", 
          "mode": "NULLABLE"
        }, 
        {
          "type": "BOOLEAN", 
          "name": "instreamVideoPlacementAccepted", 
          "mode": "NULLABLE"
        }, 
        [
          {
            "type": "BOOLEAN", 
            "name": "publisherPortalOnly", 
            "mode": "NULLABLE"
          }, 
          {
            "mode": "NULLABLE", 
            "type": "STRING", 
            "description": "", 
            "name": "dfpNetworkCode"
          }, 
          {
            "type": "BOOLEAN", 
            "name": "pubPaidPlacementAccepted", 
            "mode": "NULLABLE"
          }, 
          {
            "type": "BOOLEAN", 
            "name": "programmaticPlacementAccepted", 
            "mode": "NULLABLE"
          }, 
          {
            "mode": "NULLABLE", 
            "type": "STRING", 
            "description": "", 
            "name": "dfpNetworkName"
          }
        ]
      ], 
      {
        "mode": "NULLABLE", 
        "type": "STRING", 
        "description": "", 
        "name": "url"
      }, 
      {
        "fields": {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "IFRAME_JAVASCRIPT_INPAGE, INTERNAL_REDIRECT_INPAGE, JAVASCRIPT_INPAGE, STANDARD", 
          "name": "inpageTagFormats"
        }, 
        "type": "RECORD", 
        "name": "inpageTagFormats", 
        "mode": "REPEATED"
      }, 
      {
        "mode": "NULLABLE", 
        "type": "INT64", 
        "description": "", 
        "name": "id"
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
        "type": "BOOLEAN", 
        "name": "active", 
        "mode": "NULLABLE"
      }, 
      {
        "fields": {
          "mode": "NULLABLE", 
          "type": "STRING", 
          "description": "IFRAME_JAVASCRIPT_INTERSTITIAL, INTERNAL_REDIRECT_INTERSTITIAL, JAVASCRIPT_INTERSTITIAL", 
          "name": "interstitialTagFormats"
        }, 
        "type": "RECORD", 
        "name": "interstitialTagFormats", 
        "mode": "REPEATED"
      }
    ], 
    "type": "RECORD", 
    "name": "directorySites", 
    "mode": "REPEATED"
  }
]
