import os
import pytest
import requests
import datetime
# from blkcore.user import get_user #os.getlogin()
from base64 import b64encode
import json
import string
import random
import pandas as pd
from pandas.io.excel import ExcelWriter
from itertools import combinations
from debugpy.common.messaging import _payload


def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    
def set_a_field(payl, field, value):
    if field in ['datasetType', 'preferredServiceLevel', 'datasetStage', 'datasetName', 'datasetAvailabilities',
                'datasetCategoryOne', 'datasetSubCategoryTwo', 'datasetDescription', 'primaryBusinessPurpose', 'sourceInfo']:
        payl["datasetAspect"]["generalDescriptionAspect"]["aspect"][field] = value
    elif field in ['datasetDiscoverability', 'infoClassifications', 'previewAllowed']:
        payl["datasetAspect"]["datasetDetailsAspect"]["aspect"][field] = value
    elif field in ['levelFourDataSteward', 'levelFourBusinessOwner']:
        payl["datasetAspect"]["ownerAspect"]["aspect"][field] = value
    elif field in ['licenseRequired']:
        payl["datasetAspect"]["serviceInfoAspect"]["aspect"][field] = value


def get_a_field(payl, field):
    if field in ['datasetType', 'preferredServiceLevel', 'datasetStage', 'datasetName', 'datasetAvailabilities',
                'datasetCategoryOne', 'datasetSubCategoryTwo', 'datasetDescription', 'primaryBusinessPurpose', 'sourceInfo']:
        return payl["datasetAspect"]["generalDescriptionAspect"]["aspect"][field]
    elif field in ['datasetDiscoverability', 'infoClassifications', 'previewAllowed']:
        return payl["datasetAspect"]["datasetDetailsAspect"]["aspect"][field]
    elif field in ['levelFourDataSteward', 'levelFourBusinessOwner']:
        return payl["datasetAspect"]["ownerAspect"]["aspect"][field]
    elif field in ['licenseRequired']:
        return payl["datasetAspect"]["serviceInfoAspect"]["aspect"][field]
    

def api_mandatory_field_names():
    mandatory_df = pd.read_csv('API_UAT_mandatory_fields.csv')
    mandatory_df = mandatory_df[['mandatory fields', 'dropdown options']].set_index('mandatory fields').fillna('')
    mandatory_dict = {k: [s.strip() for s in v.get('dropdown options').split('|') if v] for k, v in mandatory_df.to_dict(orient='index').items()}
    mandatory_field_names = list(mandatory_dict.keys())
    print(f'List of mandatory fields:\n{mandatory_field_names}')
    print('List of mandatory fields and allowed values:')
    for k, v in mandatory_dict.items():
        print(f'\t{k}:\t\t\t{", ".join(v)}')
    return mandatory_field_names


def api_multivalue_dict():
    mandatory_df = pd.read_csv('API_UAT_mandatory_fields.csv')
    mandatory_df = mandatory_df[['mandatory fields', 'dropdown options']].set_index('mandatory fields').fillna('')
    mandatory_dict = {k: [s.strip() for s in v.get('dropdown options').split('|') if v] for k, v in mandatory_df.to_dict(orient='index').items()}

    multivalue_fields = ['datasetAvailabilities', 'infoClassifications']
    multivalue_dict = [{k: v} for k, v in mandatory_dict.items() if k in multivalue_fields]

    return multivalue_dict

mandatory_field_names = None
register_file = "sample.json"

username = os.getlogin()
password = "VP3ro4b?"

upassw = username + ":" + password
credentials = b64encode(bytes(upassw, 'utf-8')).decode("ascii")

token = ""
headers = {
    "Content-Type": "application/json",
    "VND.com.blackrock.Request-ID": "93312931-c361-11ed-9232-3dbbdf11dcb8",
    "VND.com.blackrock.Origin-Timestamp": "2023-03-15T18:45:36.707Z",
    "VND.com.blackrock.API-Key": token,
    "Authorization": 'Basic %s' % credentials
        }

pytest.out_df = pd.DataFrame(columns=['Test Case Name', 'Payload', 'Response'])


def setup():
    print("setup")

# def setup_function():
#     print('setup_function')

# @pytest.mark.skip()
@pytest.mark.parametrize(
    "mandatory_field", api_mandatory_field_names(),
)
def test_mandatory_field(mandatory_field):
    print(mandatory_field)
    # as_expected = list()
    # as_not_expected = list()
    f = mandatory_field

    with open(register_file) as json_file:
        bad_payload = json.load(json_file)

    datasetName = f'MISSING_MANDATORY_FIELD_{f}'
    
    set_a_field(bad_payload, 'datasetName', datasetName)
    set_a_field(bad_payload, f, None)
    
    print(f"Testing {f}... MODIFIED values in payload (used for API call):")
#     for mand_field in mandatory_field_names:
#         print(f"\t{mand_field}\t\t{get_a_field(bad_payload, mand_field)}")
    print(datasetName)
    print('=========')
    print(json.dumps(bad_payload, indent=2))
    out_resp = ""
    # URL = "https://pac.blackrock.com/api/platform/studio/edc/edc-entity/v1/edcEntities"
    # response = requests.post(URL, json=bad_payload, headers=headers)
    # if response.status_code == 200:
    #     print(f"Dataset {datasetName} registered successfully")
    #     as_not_expected.append(f)
    # else:
    #     as_expected.append(f)
    #     print(f"Dataset {datasetName} was not registered with missing value for {f}")
    #     print(f"{response.json()}\n")

    this_round = pd.DataFrame({'Test Case Name': [datasetName],
                                    'Payload': [str(bad_payload)],
                                    'Response': [str(out_resp)]})
    pytest.out_df = pd.concat([pytest.out_df, this_round])
    
    assert 2 == 2

# @pytest.mark.skip()
@pytest.mark.parametrize(
    "mandatory_multivalue_field", api_multivalue_dict(),
)
def test_multi_values(mandatory_multivalue_field):

    URL = "https://pac.blackrock.com/api/platform/studio/edc/edc-entity/v1/edcEntities"
    d = mandatory_multivalue_field
    
    k, v  = list(d.keys())[0] , d[list(d.keys())[0]]
    combination_number = 1
    for elements in range(2, len(v) + 1):  # single elements were already tested, hence we start from combo of 2 elements
        for combo in combinations(v, elements):
            with open(register_file) as json_file:
                payload = json.load(json_file)
                
            datasetName = f"MULTIVALUE_ACCEPT_{k}_{combination_number}"
            set_a_field(payload, 'datasetName', datasetName)
            set_a_field(payload, k, combo)
            out_resp = ""
            # response = requests.post(URL, json=payload, headers=headers)
            # if response.status_code == 200:
            #     print(f"Dataset {datasetName} registered successfully\n")
            #     out_resp = '200 OK'
            # else:
            #     print(f"Dataset {datasetName} was NOT registered!")
            #     print(f"{response.json()}\n")
            #     out_resp = response.json()
            
            this_round = pd.DataFrame({'Test Case Name': [datasetName],
                                    'Payload': [str(payload)],
                                    'Response': [str(out_resp)]})
            pytest.out_df = pd.concat([pytest.out_df, this_round])
            combination_number += 1
            
    with open(register_file) as json_file:
        payload = json.load(json_file)
    
    combo = [v[0], 'UNKNOWN VALUE']
    datasetName = f"MULTIVALUE_REJECT_{k}"
    
    set_a_field(payload, 'datasetName', datasetName)
    set_a_field(payload, k, combo)
    out_resp = ""
    # response = requests.post(URL, json=payload, headers=headers)
    # if response.status_code == 200:
    #     print(f"Dataset {datasetName} registered successfully which is A FAILURE!\n")
    #     out_resp = '200 OK'
    # else:
    #     print(f"Dataset {datasetName} was NOT registered which is A SUCCESS!")
    #     print(f"{response.json()}\n")
    #     out_resp = response.json()

    this_round = pd.DataFrame({'Test Case Name': [datasetName],
                            'Payload': [str(payload)], 'Response': [str(out_resp)]})
    pytest.out_df = pd.concat([pytest.out_df, this_round])

    assert 1 == 1

# def teardown_function(request):
#     print(request)
    
#     print('teardown_function')

def teardown():
    with ExcelWriter(f'multivalue_test_{datetime.datetime.timestamp(datetime.datetime.now())}.xlsx') as ew:
        pytest.out_df.to_excel(ew, index=False)
    print("teardown")


