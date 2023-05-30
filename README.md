# grapgen


python3 -m pip install --upgrade pip wheel setuptools
python3 -m pip install --upgrade acryl-datahub
datahub version


datahub ingest -c ./examples/recipes/example_to_datahub_rest.dhub.yml --dry-run

datahub ingest -c /Users/admin/datahub/docker/ingestion/sample_recipe.yml --dry-run

Python -m datahub ingest -c /Users/admin/datahub/docker/ingestion/sample_recipe.yml


export DATAHUB_GMS_URL=http://localhost:8080


curl --location --request GET 'localhost:8080/openapi/entities/v1/latest?urns=urn:li:dataset:(urn:li:dataPlatform:hive,SampleHiveDataset,PROD)&aspectNames=schemaMetadata' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhY3RvclR5cGUiOiJVU0VSIiwiYWN0b3JJZCI6ImRhdGFodWIiLCJ0eXBlIjoiUEVSU09OQUwiLCJ2ZXJzaW9uIjoiMiIsImp0aSI6IjYyYjkyOWNhLTZlNmUtNGRlYi1hNGE0LTlhZDBiZGNkYmZjOSIsInN1YiI6ImRhdGFodWIiLCJpc3MiOiJkYXRhaHViLW1ldGFkYXRhLXNlcnZpY2UifQ.6C57j6RPjFd0wo83OC-NCml2-WReSkH80hLyKArmXw4'



-----
curl --location --request GET 'http://localhost:9002/openapi/up/' --header 'accept: application/json' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhY3RvclR5cGUiOiJVU0VSIiwiYWN0b3JJZCI6ImRhdGFodWIiLCJ0eXBlIjoiUEVSU09OQUwiLCJ2ZXJzaW9uIjoiMiIsImp0aSI6IjYyYjkyOWNhLTZlNmUtNGRlYi1hNGE0LTlhZDBiZGNkYmZjOSIsInN1YiI6ImRhdGFodWIiLCJpc3MiOiJkYXRhaHViLW1ldGFkYXRhLXNlcnZpY2UifQ.6C57j6RPjFd0wo83OC-NCml2-WReSkH80hLyKArmXw4'


docker compose -f docker-compose-new.yml up

---------------
docker-compose -p datahub -f docker-compose.yml -f docker-compose.override.yml -f docker-compose-without-neo4j.m1.yml -f docker-compose.dev.yml up


docker-compose -p datahub -f docker-compose.dev.yml
  362  docker-compose -p datahub -f docker-compose.dev.yml up
  363  code .
  364  docker-compose -p datahub -f docker-compose.yml -f docker-compose.override.yml -f docker-compose-without-neo4j.m1.yml -f docker-compose.dev.yml up datahub-gms
  365  docker-compose -p datahub -f docker-compose.yml up
  366  docker-compose -p datahub -f docker-compose.yml up datahub-gms
  367  d
 datahub-gms
  368  ls
  369  docker-compose -p datahub -f docker-compose-new.yml up

456NITY-BGIDENM-GHY186-JK702JK-J5ES256I
B5I58GHI-FVRTGT55-GRTRGT-UIOP79-8NJFJR
VFGTE45-RRGEEF54-FTG5W4-GTWE45-G5T5G





rror: Command failed: /Applications/Lens.app/Contents/Resources/x64/helm install datahub/datahub-prerequisites --version 0.0.14 --values /private/var/folders/kk/09j0x2d944l3nht0jktxzy0w0000gp/T/796129a7940274bd57ca297c4a27645e/values.yaml --namespace default --kubeconfig /var/folders/kk/09j0x2d944l3nht0jktxzy0w0000gp/T/kubeconfig-063bc0fe267ea780a78b047acf798344 --generate-name
Error: INSTALLATION FAILED: rendered manifests contain a resource that already exists. Unable to continue with install: PodDisruptionBudget "elasticsearch-master-pdb" in namespace "default" exists and cannot be imported into the current release: invalid ownership metadata; annotation validation error: key "meta.helm.sh/release-name" must equal "datahub-prerequisites-1684385128": current value is "prerequisites"
-----------------------------
```

source:
  type: datahub-business-glossary
  config:
    file: /Users/foongping/datahub-project/datahub/metadata-ingestion/examples/bootstrap_data/business_glossary_fp.yml
    enable_auto_id: True
​
sink:
  type: datahub-rest
  config:
    server: ${DATAHUB_GMS_URL}
    token: ${DATAHUB_GMS_TOKEN}


=============================================
/api/v2/graphql POST

Create Glossary Term:

{
   "operationName":"createGlossaryTerm",
   "variables":{
      "input":{
         "name":"BX Term",
         "parentNode":null,
         "description":"XB **Documentation**"
      }
   },
   "query":"mutation createGlossaryTerm($input: CreateGlossaryEntityInput!) {\n  createGlossaryTerm(input: $input)\n}\n"
}
-----------
BX Term Group:
{
   "operationName":"createGlossaryNode",
   "variables":{
      "input":{
         "name":"BX Term Group",
         "parentNode":null,
         "description":"BX Term Group"
      }
   },
   "query":"mutation createGlossaryNode($input: CreateGlossaryEntityInput!) {\n  createGlossaryNode(input: $input)\n}\n"
}
+++++++
{
   "operationName":"createGlossaryTerm",
   "variables":{
      "input":{
         "name":"BX1",
         "parentNode":"urn:li:glossaryNode:33617c2f-aad5-4abe-b026-942d731cd4ae",
         "description":"BX 1 doc"
      }
   },
   "query":"mutation createGlossaryTerm($input: CreateGlossaryEntityInput!) {\n  createGlossaryTerm(input: $input)\n}\n"
}

*****
{
   "operationName":"addRelatedTerms",
   "variables":{
      "input":{
         "urn":"urn:li:glossaryTerm:b2e71478-c8e0-4c59-a81e-f20e033ca746",
         "termUrns":[
            "urn:li:glossaryTerm:81cefc70-63e4-46f9-b7e3-5b9e5099925c"
         ],
         "relationshipType":"hasA"
      }
   },
   "query":"mutation addRelatedTerms($input: RelatedTermsInput!) {\n  addRelatedTerms(input: $input)\n}\n"
}
--$$$$$$$$$$$$$$$$$
{
   "operationName":"createGlossaryNode",
   "variables":{
      "input":{
         "name":"BX Term Group Two",
         "parentNode":null,
         "description":"### **BX Term Group Two Documentation**"
      }
   },
   "query":"mutation createGlossaryNode($input: CreateGlossaryEntityInput!) {\n  createGlossaryNode(input: $input)\n}\n"
}
-----
{
   "operationName":"createGlossaryNode",
   "variables":{
      "input":{
         "name":"BX Term Group Two 1CG",
         "parentNode":"urn:li:glossaryNode:2b5af742-83cd-42dc-8d18-a09763f5f46e",
         "description":null
      }
   },
   "query":"mutation createGlossaryNode($input: CreateGlossaryEntityInput!) {\n  createGlossaryNode(input: $input)\n}\n"
}
++++++++++++
```
