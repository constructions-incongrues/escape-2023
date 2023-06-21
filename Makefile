gif:
	for file in ./public/media/video/*.mp4; do \
		test -f ./public/media/gif/$$(basename $$file .mp4).gif || ffmpeg -i $$file ./public/media/gif/$$(basename $$file .mp4).gif; \
	done

ascii: gif
	for file in ./public/media/gif/*.gif; do \
			test -f ./public/media/ascii/$$(basename $$file) || ./bin/asciiplayer encode --out ./public/media/ascii/$$(basename $$file) $$file; \
	done

clean:
	rm -vf ./public/media/ascii/* ./public/media/gif/*

serve: ascii

dev:
	live-server ./public