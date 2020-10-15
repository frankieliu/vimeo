SHELL=bash
heights:
	for x in [0-9][0-9]*; do \
	if [ -d $$x ]; then \
	for y in $$x/*.mkv; do \
	echo $$y $$'\t' $$(ffprobe-height.sh $$y) $$(ffprobe-duration.sh $$y) $$(file-size.sh $$y); \
	done; \
	fi; \
	done
