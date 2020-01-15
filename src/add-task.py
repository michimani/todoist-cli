#!/usr/bin/env python
import argparse
import configparser
import os
import sys
import todoist

p = argparse.ArgumentParser()
p.add_argument('task_name', help='task name for new task')
p.add_argument('-p', '--project_id', default='',
               help='project ID for new task added')
args = p.parse_args()

c = configparser.ConfigParser()
c.read(os.path.dirname(os.path.abspath(__file__)) + '/../config.ini', 'UTF-8')
TODOIST_TOKEN = c.get('todoist', 'token')


def add_task(task_name, project_id=''):
    api = todoist.TodoistAPI(TODOIST_TOKEN)
    if project_id != '':
        item = api.add_item(task_name, project_id=project_id)
    else:
        item = api.add_item(task_name)

    api.commit()


if __name__ == '__main__':
    add_task(args.task_name, args.project_id)
