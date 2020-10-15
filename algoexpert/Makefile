masters.json: algoexpert.json
	cat $^ | jq '.log.entries | map(select(._resourceType == "xhr" and (.request.url | contains("master.json")))) | .[] .request.url' > $@
