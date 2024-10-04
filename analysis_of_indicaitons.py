import pandas as pd
import re

# Import data for analysis.
data_for_consolidation = pd.read_excel("data_for_analysis.xlsx")


def normalize_text(indication_string):
    indication_string = str(indication_string)
    list_of_indications = []

    if re.search("\b(OCD|Osteochondritis Disecans)\b", indication_string, re.I):
        list_of_indications.append("OCD")

    if re.search("\b(OA|Osteoarthritis|Ostearthritis|Osteoarthrosis|Arthrosis|Asthrosis|Athrosis)\b", indication_string,
                 re.I):
        list_of_indications.append("OA")
    # Arthrosis for elbow.
    if re.search("\b(Cubarthrosis|Cubarthorosis|Cuboarthrosis|Cubioarthrosis)\b", indication_string, re.I):
        list_of_indications.append("OA")
    # Arthrosis for shoulder.
    if re.search("\b(Omarthrosis)\b", indication_string, re.I):
        list_of_indications.append("OA")
    # Arthrosis for knee.
    if re.search("\b(Gonarthrosis)\b", indication_string, re.I):
        list_of_indications.append("OA")
    # Arthrosis for hip.
    if re.search("\b(Coxarthrosis)\b", indication_string, re.I):
        list_of_indications.append("OA")
    # cranial cruciate ligament
    if re.search("\b(CCL|cranial cruciate ligament)\b", indication_string, re.I):
        list_of_indications.append("CCL")
    # Fragmented Coronoid Process
    if re.search("\b(FCP|FPC|Fragmented Coronoid Process)\b", indication_string, re.I):
        list_of_indications.append("FPC")
    # Hip dysplasia.
    if re.search("\b(Hip dysplasia|HD)\b", indication_string, re.I):
        list_of_indications.append("HD")
    # Elbow dysplasia.
    if re.search("\b(Elbow joint dysplasia|Elbow dysplasia|ED)\b", indication_string, re.I):
        list_of_indications.append("ED")
    return list_of_indications


data_for_consolidation['Indication_list'] = data_for_consolidation['Indication'].apply(normalize_text)
data_for_consolidation['Indication_to_check'] = data_for_consolidation['Indication']
data_for_consolidation.to_excel("check_results.xlsx")
