#!/usr/bin/bash

cat $1 | jq -r ".log.entries | map(select(._resourceType == \"xhr\" and (.request.url | contains(\"$2\")))) | .[] .request.url"

