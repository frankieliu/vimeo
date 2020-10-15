SHELL=bash
hardir=resources/har
playdir=resources/playManifest
videodir=resources/videoclips

# Save all as HAR

$(playdir)/playManifest100.json: $(hardir)/save_06_06_01_01.json
	cat save_06_06_01_01.json | jq '.log.entries | map(select(._resourceType == "xhr" and (.request.url | contains("index.m3u8")))) | .[] .request.url' > playManifest100.json

$(playdir)/playManifest200.json: $(hardir)/save_11_11_02_02.json
	cat $^ | jq '.log.entries | map(select(._resourceType == "xhr" and (.request.url | contains("index.m3u8")))) | .[] .request.url' > $@

$(playdir)/playManifest267.json: $(hardir)/save_15_00_00_00.json
	cat $^ | jq '.log.entries | map(select(._resourceType == "xhr" and (.request.url | contains("index.m3u8")))) | .[] .request.url' > $@

#"_priority": "High",
#        "_resourceType": "fetch",
#        "cache": {},
#        "connection": "66310",
#        "pageref": "page_3",
#        "request": {
#          "method": "GET",
#          "url": "https://learning.oreilly.com/api/v1/videoclips/9780136733461-ROR6_01_01_01_01/",


$(videodir)/videoclips100.json: $(hardir)/save_06_06_01_01.json
	cat $^ | jq '.log.entries | map(select(._resourceType == "fetch" and (.request.url | contains("/api/v1/videoclips/")))) | .[] .request.url' > $@

$(videodir)/videoclips200.json: $(hardir)/save_11_11_02_02.json
	cat $^ | jq '.log.entries | map(select(._resourceType == "fetch" and (.request.url | contains("/api/v1/videoclips/")))) | .[] .request.url' > $@

$(videodir)/videoclips267.json: $(hardir)/save_15_00_00_00.json
	cat $^ | jq '.log.entries | map(select(._resourceType == "fetch" and (.request.url | contains("/api/v1/videoclips/")))) | .[] .request.url' > $@


sorted:
	cd $(videodir); \
	for x in *[0-9].json; do \
	out=$$(basename $$x .json)_sorted.json; \
	sort -u $$x > $$out; \
	wc $$out; \
	done

combined:
	cd $(videodir); \
	cat *_sorted.json | sort -u > combined.json;

srt:
	a=resources/clips; \
	b=resources/manifest/manifestAll; \
	count=0; \
 	for x in $$a/*.json; do \
	count=$$(($$count + 1)); \
	cout=$$(printf %03d $$count); \
	python srt.py $$x > $$b/$$cout.srt; \
	done


		
	for x in *

