MANAGE=django-admin.py
PROJECT=mytest

.PHONY: run
run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --all
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate persons
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) runserver 0.0.0.0:8000

.PHONY: test_persons
test_persons:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) test persons

.PHONY: test_utils
test_utils:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) test utils

.PHONY: test
test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput --all
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) test

.PHONY: model_info
model_info:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) model_info

fixtures:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) dumpdata persons --indent 3 > initial_data.json

.PHONY: migrate
migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate persons