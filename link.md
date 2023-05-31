```
--------------------
mutation createGlossaryNode($input: CreateGlossaryEntityInput!) {
createGlossaryNode(input: $input)
}

{
      "input":{
         "name":"TransactionX",
         "parentNode":null,
         "description":"Captures trades in Aladdin and the corresponding trade metadata"
      }
 }

response:
{
  "data": {
    "createGlossaryNode": "urn:li:glossaryNode:bfd4adfe-df4a-4c26-89da-b0cf5833fd84"
  },
  "extensions": {}
}
----

mutation createGlossaryTerm($input: CreateGlossaryEntityInput!) 
{ createGlossaryTerm(input: $input)
}

{
      "input":{
         "name":"transaction_id",
         "parentNode":"urn:li:glossaryNode:bfd4adfe-df4a-4c26-89da-b0cf5833fd84",
         "description":"X **Documentation**"
      }
   }

response:
{
  "data": {
    "createGlossaryTerm": "urn:li:glossaryTerm:a67ee24d-6f9f-4cdb-a761-b2d8c18ada29"
  },
  "extensions": {}
}
---

mutation createGlossaryNode($input: CreateGlossaryEntityInput!) {
createGlossaryNode(input: $input)
}

{
      "input":{
         "name":"Transaction",
         "parentNode":null,
         "description":"Captures trades in Aladdin and the corresponding trade metadata"
      }
   }
```
