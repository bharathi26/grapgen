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

pytest.out_df = pd.DataFrame(columns=['Test Case Name', 'Payload', 'Response'])
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

def get_testcase_data():
    df = pd.read_excel("EDC Dataset Registration Testing.xlsx" , engine='openpyxl')
    df = df[df['Test Scope'].isin(['API registration mandatory fields'])]
    records = df[["ID","URL", "Test Scope","Test Case Name","Payload"]].to_dict('records')
    return records

def teardown():
    with ExcelWriter(f'multivalue_test_{datetime.datetime.timestamp(datetime.datetime.now())}.xlsx') as ew:
        pytest.out_df.to_excel(ew, index=False)
    print("teardown")

@pytest.mark.parametrize(
    "record", get_testcase_data(),
)
def test_api_payload(record):
    print(record['ID'])
    payload = json.loads(json.dumps(record['Payload']))
    print(record['URL'])
    datasetName = record["Test Case Name"]
    out_resp = ""

    URL = record['URL']
    # response = requests.post(URL, json=payload, headers=headers)
    # if response.status_code == 200:
    #     print(f"Dataset {datasetName} registered successfully")
    #     as_not_expected.append(f)
    # else:
    #     as_expected.append(f)
    #     print(f"Dataset {datasetName} was not registered with missing value for {f}")
    #     print(f"{response.json()}\n")

    this_round = pd.DataFrame({'Test Case Name': [datasetName],
                                    'Payload': [str(payload)],
                                    'Response': [str(out_resp)]})
    pytest.out_df = pd.concat([pytest.out_df, this_round])
    assert 1==1

# @pytest.mark.skip()
# def test_df():
    
#     for i, row in df.iterrows():
#         print(row['ID'])
#         print(row['Test Scope'])
#         json_object = json.loads(json.dumps(row['Payload']))
#         # print(json_object)
#         print(row['URL'])
#         try:
#             if len(row['URL'].hyperlink.target)  > 0:
#                 print(row['URL'].hyperlink.target)
#                 print('----------')
#         except:
#             pass

#     assert 1 == 1
