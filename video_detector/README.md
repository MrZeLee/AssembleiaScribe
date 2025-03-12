- keep selenium as backup (still not working)
- use curl

```shell
curl 'https://arfrontend.livemeans.com/programs.jsonp?op=1004&progID=14&pgNum=0' | \
jq . > output.json
```
