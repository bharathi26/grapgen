```

https://datahub-frontend.edc-hal.extdns.pac.blackrock.com/
https://datahub-frontend.edc-hal.extdns.dev.blackrock.com/
https://datahub-frontend.edc-hal.extdns.tst.blackrock.com/
```
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
