#!/usr/bin/env python
"""
If no cache is found, will screape the ProgrammingPraxis website.

Otherwise will output details of a dojo task.

If passed in the argument 'refresh', the script will scrape the
ProgrammingPraxis website for new tasks.
"""
import sys
import random
import json
import requests
import html2text
from bs4 import BeautifulSoup


def scrape(tasks):
    """
    Scrapes ProgrammingPraxis for tasks, parses them and, if they don't already
    exist in the task list, adds them to it. At the end, saves the task list
    as a JSON file.
    """
    known_tasks = set([task['url'].lower().strip() for task in tasks])
    target = 'http://programmingpraxis.com/page/{}/'
    counter = 0
    new_exercises = True
    while new_exercises:
        target_url = target.format(counter)
        response = requests.get(target_url)
        print('Grabbing URL: {}'.format(target_url))
        if counter == 0:
            # We get weird Wordpress errors for page 1. Go figure.
            counter = 1
        counter += 1
        if response.ok:
            soup = BeautifulSoup(response.text)
            exercises = soup.find_all('div', 'entry')
            for exercise in exercises:
                try:
                    title = exercise.find('h2').text
                    date = exercise.find('h3').text
                    url = exercise.find('h2').find('a').attrs['href']
                    h2t = html2text.HTML2Text()
                    description = h2t.handle(exercise.find('div', 'entrybody').prettify())
                except Exception as ex:
                    pass  # Easiest to pass over malformed HTML for tasks.
                if url not in known_tasks:
                    tasks.append({
                        'url': url,
                        'title': title,
                        'date': date,
                        'description': description,
                    })
                    known_tasks.add(url)
                else:
                    new_exercises = False
                    break
            print('Number of tasks scraped: {}'.format(len(tasks)))
        else:
            new_exercises = False
            break
    json.dump(tasks, open('tasks.json', 'wb'), indent=2)


if __name__ == '__main__':
    refresh = False
    if len(sys.argv) > 1 and sys.argv[1] == 'refresh':
        refresh = True
    tasks = []
    try:
        tasks = json.load(open('tasks.json'))
    except:
        refresh = True
    if refresh:
        scrape(tasks)
    task = random.choice(tasks)
    print(task['title'] + '\n')
    print(task['date'] + ' - ' + task['url'] + '\n\n')
    print(task['description'])
