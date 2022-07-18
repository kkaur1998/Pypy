l1 = ['policy_number', 'issue_age', 'state', 'dlm', 'Zipcode', 'Report_group1', 'HHRes_ID_HCH', 'Product_series', 'annualized_premium', 
'new_face_status', 'nf_status', 'issue_age_cat', 'billing_method', 'apv_of_sale', 'application_date', 'issue_date', 'paid_to_date', 'geoMed_Household_Income', 
'geopop_per_sq_mile', 'geourban_density', 'first_purchase', 'customer_tenure', 'agt_firstdif', 'age_asof_apr2018', 'agent_agerange_at_issue', 'agent_tenure',
 'claimcount', 'totalclaimsamount', 'drv_claim_payments', 'final_agent_tenure', 'ct_hh', 'hh_at_issue', 'apv_ifc_atissue', 'apv_ifc_range', 'dollar_apv_income', 
 'apv_income_atissue', 'last_purchase', 'months_since_last_pur', 'ifc', 'lapsed', 'duration_rct_purchase', 'status_prev_pol', 'duration_status', 'lapses_before', 
 'latino', 'dlm_product', 'application_date_format', 'issue_date_format', 'paid_to_date_format', 'datediffmonths', 'year_billingmethod', 'new_lapses_before', 
 'annual_income', 'pop_density_BA2', 'new_state', 'dep_var17', 'pers_sevenmo', 'pers_twomo', 'ihh_at_issue', 'ilatino', 'iagent_agerange_at_issue', 'iagent_tenure',
 'iannual_income', 'ibilling_method', 'icustomer_tenure', 'idlm_product', 'iduration_rct_purchase', 'iissue_age_cat', 'inew_lapses_before', 'ipop_density_BA2', 
 'istate', 'istatus_prev_pol', 'scored_perst', 'phat', 'myGroup']
 
l2 = ['Policy_number', 'HHRes_ID_HCH', 'issue_age_cat', 'issue_age', 'issue_date''', 'issue_date.1', 'application_date', 'paid_to_date', 'ZIPCODE', 'state', 
'dlm', 'Report_group1', 'Product_series', 'billing_method', 'apv_of_sale', 'Annualized_premium', 'first_purchase', 'customer_tenure', 'geoMed_Household_Income', 
'geoPop_Per_Sq_Mile', 'agt_firstdif', 'age_asof_apr2018', 'agent_agerange_at_issue', 'agent_tenure', 'final_agent_tenure', 'claimcount', 'totalclaimsamount', 
'drv_claim_payments', 'ct_hh', 'hh_at_issue', 'apv_ifc_atissue', 'apv_ifc_range', 'last_purchase', 'months_since_last_pur', 'ifc', 'lapsed',
 'duration_rct_purchase', 'status_prev_pol', 'duration_status', 'lapses_before', 'latino', 'New_face_status', 'nf_status', 'datediffmonths', 'dlm_product',
 'new_lapses_before', 'annual_income', 'pop_density_BA2', 'new_state', 'pers_thirteenmo', 'pers_sevenmo', 'pers_twomo', 'ihh_at_issue', 'ilatino',
 'iagent_agerange_at_issue', 'iagent_tenure', 'iannual_income', 'ibilling_method', 'icustomer_tenure', 'idlm_product', 'iduration_rct_purchase', 'iissue_age_cat',
 'inew_lapses_before', 'ipop_density_BA2', 'istate', 'istatus_prev_pol', 'X1', 'phat', 'rank', 'myGroup']

l1 = [x.upper() for x in l1]
l2 = [x.upper() for x in l2]
print(len(l1), len(l2))
k = []
for i in l1:
    if(i in l2):
        continue
    else:
        k.append(i)

print(k)