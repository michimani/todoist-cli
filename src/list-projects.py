#!/usr/bin/env python
import argparse
import configparser
import json
import os
import shutil
import todoist

p = argparse.ArgumentParser()
p.add_argument('-f', '--full_sync', default='0',
               help='"1" for full sync')
args = p.parse_args()

c = configparser.ConfigParser()
c.read(os.path.dirname(os.path.abspath(__file__)) + '/../config.ini', 'UTF-8')
TODOIST_TOKEN = c.get('todoist', 'token')
CACHE_DIR = os.path.dirname(os.path.abspath(
    __file__)) + '/../caches/sync_cache/'
SYNC_CACHE_FILE = CACHE_DIR + TODOIST_TOKEN + '.json'
LIST_LINE_FORMAT = '{id: <15}: {name: <30}'


def list_projects():
    if args.full_sync == '1' and os.path.exists(CACHE_DIR):
        shutil.rmtree(CACHE_DIR)

    if os.path.exists(SYNC_CACHE_FILE):
        with open(SYNC_CACHE_FILE) as f:
            sync_data = json.load(f)
    else:
        api = todoist.TodoistAPI(TODOIST_TOKEN, cache=CACHE_DIR)
        sync_data = api.sync()

    projects = sync_data['projects']

    print('\n')
    print(LIST_LINE_FORMAT.format(id='PROJECT ID', name='PROJECT NAME'))
    print('{s:-<15}:{s:-<30}'.format(s=''))
    for project in projects:
        print(LIST_LINE_FORMAT.format(id=project['id'], name=project['name']))
    print('\n')


if __name__ == '__main__':
    list_projects()
