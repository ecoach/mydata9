#!/bin/bash

#export SCRIPT_DIR=$(pwd)

echo 'begin script'
cd ~jtritz/bitbucket/ecoach_webapps/mydata4/mts4
svn update
source ~jtritz/virtualenv/v1/bin/activate
python ~jtritz/bitbucket/ecoach_webapps/manage.py collectstatic --noinput --settings=mydata4.settings
echo 'end of script'




