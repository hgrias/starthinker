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

pricingSchedulePricingPeriod_Schema = [
  {
    "mode": "NULLABLE", 
    "type": "INT64", 
    "description": "", 
    "name": "units"
  }, 
  {
    "mode": "NULLABLE", 
    "type": "INT64", 
    "description": "", 
    "name": "rateOrCostNanos"
  }, 
  {
    "mode": "NULLABLE", 
    "type": "DATE", 
    "description": "", 
    "name": "startDate"
  }, 
  {
    "mode": "NULLABLE", 
    "type": "DATE", 
    "description": "", 
    "name": "endDate"
  }, 
  {
    "mode": "NULLABLE", 
    "type": "STRING", 
    "description": "", 
    "name": "pricingComment"
  }
]
