#project variables:

MANAGE=django-admin.py
PROJECT=mytest
SETTINGS=make_settings
DBNAME=test_db.sqlite
APPS = persons utils

MANAGE_COMMAND=PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).$(SETTINGS) $(MANAGE)

ifndef APP
    TESTAPP=$(APPS)
else
    TESTAPP=$(APP)
endif

ifeq ($(APP),all)
    TESTAPP= 
endif

run: syncdb
	$(MANAGE_COMMAND) runserver 0.0.0.0:8000

.PHONY: test APP=$(APP)
test:
	$(MANAGE_COMMAND) syncdb --noinput --all
	$(MANAGE_COMMAND) test $(TESTAPP)

.PHONY: model_info
model_info:
	$(MANAGE_COMMAND) model_info

fixtures: 
	$(MANAGE_COMMAND) dumpdata persons --indent 3 > initial_data.json

.PHONY: migrate APP=$(APP)
migrate:
	$(MANAGE_COMMAND) migrate $(APP)

syncdb:
	$(if $(wildcard $(DBNAME)), $(MANAGE_COMMAND) migrate, )
	$(MANAGE_COMMAND) syncdb --all	
