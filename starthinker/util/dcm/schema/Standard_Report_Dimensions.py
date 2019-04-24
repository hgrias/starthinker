###########################################################################
#
#  Copyright 2017 Google Inc.
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

Standard_Report_Dimensions_Schema = [
  { "name":"Activity", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Activity_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Activity_Group_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Activity_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Ad", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ad_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Ad_Status", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ad_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"App", "type":"STRING", "mode":"NULLABLE" },
  { "name":"App_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Asset", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Asset_Category", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Asset_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Asset_Orientation", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Attributed_Event_Connection_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Attributed_Event_Environment", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Audience_Targeted", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Browser_Platform", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign_End_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Campaign_External_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Campaign_Start_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"City", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Click_Through_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Companion_Creative", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Companion_Creative_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Companion_Creative_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Connection_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Content_Category", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Content_Classifier", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Country", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_End_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Creative_Field_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_4", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_5", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_6", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_7", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_8", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_9", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_10", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_11", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_12", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Groups_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Groups_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Creative_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Start_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Creative_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Version", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Dbm_Advertiser", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dbm_Advertiser_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Dbm_Creative", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dbm_Creative_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Dbm_Insertion_Order", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dbm_Insertion_Order_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Dbm_Line_Item", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dbm_Line_Item_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Dbm_Partner", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dbm_Partner_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Dbm_Site", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dbm_Site_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Digital_Content_Label", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Designated_Market_Area_Dma", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Domain", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_1_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_2_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_3_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_4_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_5_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_6_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_1_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_2_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_3_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_4_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_5_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_6_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_1_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_2_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_3_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_4_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_5_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_6_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_1_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_2_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_3_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_4_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_5_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_6_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_1_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_2_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_3_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_4_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_5_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_6_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_4", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_5", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_6", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Profile", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Profile_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Environment", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Attributed_Event_Platform_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Exit_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Flight_Booked_Cost", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Flight_Booked_Rate", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Flight_Booked_Units", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Flight_End_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Flight_Start_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Floodlight_Configuration", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Hour", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Keyword", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Landing_Page_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Mobile_Carrier", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Month", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Engine_Country", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Engine_Property", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Landing_Page", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Landing_Page_Query_String", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Processed_Landing_Page", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Processed_Landing_Page_Query_String", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Query", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Operating_System", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Operating_System_Version", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Package_Roadblock", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Package_Roadblock_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Package_Roadblock_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Package_Roadblock_Total_Booked_Units", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad_Group_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Advertiser", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Advertiser_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Agency", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Agency_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Bid_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Bid_Strategy_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Campaign", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Campaign_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Engine_Account", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Engine_Account_Category", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Engine_Account_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Ad_Group_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Ad_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Campaign_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Keyword_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Keyword", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Keyword_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Landing_Page_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Legacy_Keyword_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Match_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Payment_Source", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Compatibility", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Cost_Structure", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_End_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Placement_External_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Placement_Rate", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Start_Date", "type":"DATE", "mode":"NULLABLE" },
  { "name":"Placement_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Tag_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Total_Booked_Units", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Total_Planned_Media_Cost", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Platform_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Playback_Method", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rendering_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Custom_Variable", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rich_Media_Event", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Video_4A_39_S_Ad_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Video_Length", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Served_Pixel_Density", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Site_Dcm", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Site_Site_Directory", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Site_Id_Site_Directory", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Site_Id_Dcm", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Site_Keyname", "type":"STRING", "mode":"NULLABLE" },
  { "name":"State_Region", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Twitter_Campaign_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Twitter_Creative_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Twitter_Creative_Media_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Twitter_Creative_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Twitter_Impression_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Twitter_Line_Item_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Twitter_Placement_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"User_List", "type":"STRING", "mode":"NULLABLE" },
  { "name":"User_List_Current_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"User_List_Description", "type":"STRING", "mode":"NULLABLE" },
  { "name":"User_List_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"User_List_Membership_Life_Span", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Video_Player_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Video_Prominence_Score", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Week", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Zip_Postal_Code", "type":"INTEGER", "mode":"NULLABLE" }
]