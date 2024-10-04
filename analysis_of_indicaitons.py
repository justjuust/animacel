import pandas as pd
import re

# Import data for analysis.
data_for_consolidation = pd.read_excel("data_for_analysis.xlsx")


def normalize_text(indication_string):
    indication_string = str(indication_string)
    list_of_indications = []

    if re.search(r"\b(OCD|Osteochondritis Disecans)\b", indication_string, re.I):
        list_of_indications.append("OCD")

    if re.search(r"\b(OA|Osteoarthritis|Ostearthritis|Osteoarthrosis|Arthrosis|Asthrosis|Athrosis)\b", indication_string,
                 re.I):
        list_of_indications.append("OA")
    # Arthrosis for elbow.
    if re.search(r"\b(Cubarthrosis|Cubarthorosis|Cuboarthrosis|Cubioarthrosis|Elbow( joint)? arthrosis|(OA (\(Osteoarthritis\))?|Osteoarthritis) Cub(\.|iti) (dex( et. sin)?|sin( et. dex)?)?|arthrosis of (the )?elbow( joints?)?)\b", indication_string, re.I):
        list_of_indications.append("OA")
        list_of_indications.append("Cubarthrosis")
    # Arthrosis for shoulder.
    if re.search(r"\b(Omarthrosis|shoulder (joints? )?Arthrosis|arthrosis( (of|in))?( (the|both))? shoulder( joints?)?)\b", indication_string, re.I):
        list_of_indications.append("OA")
        list_of_indications.append("Omarthrosis")
    # Arthrosis for knee.
    if re.search(r"\b(Gonarthrosis|arthrosis( (of|in))?( (the|both))? knee( joints?)?|knee( joints? )?Arthrosis)\b", indication_string, re.I):
        list_of_indications.append("OA")
        list_of_indications.append("Gonarthrosis")
    # Arthrosis for hip.
    if re.search(r"\b(Coxarthrosis|arthrosis( (of|in))?( (the|both))? hip( joints?)?|hip( joints? )?Arthrosis|(OA (\(Osteoarthritis\))?|Osteoarthritis) gax. (dex( et. sin)?|sin( et. dex)?)?)\b", indication_string, re.I):
        list_of_indications.append("OA")
        list_of_indications.append("Coxarthrosis")
    # cranial cruciate ligament
    if re.search(r"\b(CCL|cranial cruciate ligament)\b", indication_string, re.I):
        list_of_indications.append("CCL")
    # Fragmented Coronoid Process
    if re.search(r"\b(FCP|FPC|Fragmented Coronoid Process)\b", indication_string, re.I):
        list_of_indications.append("FPC")
    # Hip dysplasia.
    if re.search(r"\b(Hip dysplasia|HD|Dysplasia coxae)\b", indication_string, re.I):
        list_of_indications.append("HD")
    # Elbow dysplasia.
    if re.search(r"\b(Elbow joint dysplasia|Elbow dysplasia|ED)\b", indication_string, re.I):
        list_of_indications.append("ED")
    return list(set(list_of_indications))


data_for_consolidation['Indication_list'] = data_for_consolidation['Indication'].apply(normalize_text)
data_for_consolidation['Indication_to_check'] = data_for_consolidation['Indication']
data_for_consolidation.to_excel("check_results.xlsx")
