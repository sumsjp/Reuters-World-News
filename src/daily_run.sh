#!/bin/bash

git pull
python ./update_youtube.py
git add ..
git commit -am update
git push

