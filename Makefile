modify-MD:
	python3 vendor/modifyMD.py

pre-Gen-HTML:modify-MD
	bundle exec jekyll build

modify-HTML:pre-Gen-HTML
	python3 vendor/modify.py

pack:modify-HTML
	mkdir _site/fluid/;
	cp _site/*.html _site/fluid/
	tar cf fluid.tar _site/fluid/

preview:modify-MD
	bundle exec jekyll serve -H 0.0.0.0 -t & ;
	sleep 3;
	python3 vendor/modify.py
