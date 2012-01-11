MANAGE=django-admin.py
PROJECT=mytest
SETTINGS=make_settings

.PHONY: run
run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) syncdb --all
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) migrate persons
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) runserver 0.0.0.0:8000

.PHONY: test_persons

.PHONY: test APP=$(APP)
test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) syncdb --noinput --all
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) test $(APP)

.PHONY: model_info
model_info:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) model_info

fixtures:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) dumpdata persons --indent 3 > initial_data.json

.PHONY: migrate APP=$(APP)
migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE) migrate $(APP)