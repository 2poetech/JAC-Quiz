# Copyright 2017, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from google.cloud import datastore

project_id = os.getenv('GCLOUD_PROJECT')


"""
Persists initial questions into datastore
"""
def main():

    """
    Create an array of dicts defining questions
    """
    questions = [
        {
            'quiz': u'JAC Cloud Fellows',
            'author': u'Cherie',
            'title': u'Who are the JAC Cloud Fellows?',
            'answer1': u'Cherie',
            'answer2': u'Justice',
            'answer3': u'Aliyah',
            'answer4': u'All of the above',
            'correctAnswer': 4,
            'imageUrl': u''
        },
        {
            'quiz': u'JAC Cloud Fellows',
            'author': u'Cherie',
            'title': u'Who is from Chicago?',
            'answer1': u'Cherie',
            'answer2': u'Justice',
            'answer3': u'Aliyah',
            'answer4': u'All of the above',
            'correctAnswer': 1,
            'imageUrl': u''
        },
        {
            'quiz': u'JAC Cloud Fellows',
            'author': u'Cherie',
            'title': u'Who has a dog?',
            'answer1': u'Cherie',
            'answer2': u'Justice',
            'answer3': u'Aliyah',
            'answer4': u'All of the above',
            'correctAnswer': 2,
            'imageUrl': u''
        },
        {
            'quiz': u'JAC Cloud Fellows',
            'author': u'Cherie',
            'title': u'Who names begins with a vowel?',
            'answer1': u'Cherie',
            'answer2': u'Justice',
            'answer3': u'Aliyah',
            'answer4': u'All of the above',
            'correctAnswer': 3,
            'imageUrl': u''
        },
    ]

    client = datastore.Client(project_id)

    """
    Create and persist and entity for each question
    """
    for q_info in questions:
        key = client.key('Question')
        q_entity = datastore.Entity(key=key)
        for q_prop, q_val in q_info.items():
            q_entity[q_prop] = q_val
        client.put(q_entity)

if __name__ == '__main__':
    main()
