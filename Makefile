gif:
	mkdir -p ./var/
	for file in ./media/video/*.mp4; do \
		test -f ./var/$$(basename $$file .mp4).gif || ffmpeg -i $$file ./var/$$(basename $$file .mp4).gif; \
	done

ascii: gif
	for file in ./var/*.gif; do \
			test -f ./public/scenes/$$(basename $$file .gif)/animation.gif || ./bin/asciiplayer encode --out ./public/scenes/$$(basename $$file .gif)/animation.gif $$file; \
	done

clean:
	rm -vf ./public/scenes/*/animation.gif ./var/*

serve:
	-pkill -f http.server
	python3 -m http.server --directory ./public/scenes &

dev:
	live-server ./public/scenes

udev:
	cat ./etc/udev.rules | sudo tee /etc/udev/rules.d/00-escape-2023.rules
	sudo udevadm control --reload

kiosk:
	DISPLAY=:0 chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:8000/00/

unclutter:
	DISPLAY=:0 unclutter &

start: udev serve kiosk unclutter
