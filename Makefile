modify-MD:
	python3 vendor/modifyMD.py

pre-Gen-HTML:modify-MD
	bundle exec jekyll build

modify-HTML:pre-Gen-HTML
	python3 vendor/modify.py

pack:modify-MD
	pip3 install PyYaml
	python3 vendor/changeBaseURL.py pack
	bundle exec jekyll build
	python3 vendor/modifyHTML.py
	mkdir -p _site/fluid/assets
	cp _site/*.html _site/fluid/
	cp -r _site/assets/* _site/fluid/assets/
	tar cf fluid.tar _site/fluid/


preview:modify-MD
	pip3 install PyYaml
	python3 vendor/changeBaseURL.py preview
	bundle exec jekyll serve -H 0.0.0.0 -t &
	sleep 5;
	python3 vendor/modifyHTML.py
