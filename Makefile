.PHONY: run
run:
	python mytest/manage.py syncdb
	python mytest/manage.py runserver 0.0.0.0:8000

.PHONY: test_persons
test_persons:
	python mytest/manage.py test persons

.PHONY: test
test:
	python mytest/manage.py test