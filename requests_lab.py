#! /usr/bin/env python3
import requests, os
feedback_dir = '/data/feedback/'
list_feedback = os.listdir(feedback_dir)
content_list = []

for file in list_feedback:
    print("Working Dir/File: {}".format(file))
    with open(feedback_dir + file, 'r') as f:
        content = f.readlines()
        content_dict = {
            'title': content[0].strip(),
            'name': content[1].strip(),
            'date': content[2].strip(),
            'feedback': content[3].strip()
        }
        content_list.append(content_dict)

for file_to_send in content_list:
    response = requests.post('http://34.82.93.29/feedback/', json=file_to_send)
    if not response.ok:
        raise Exception('POST failed! Error: {}'.format(response.status_code)) 
    print('Feedback uploaded successfully!')
    