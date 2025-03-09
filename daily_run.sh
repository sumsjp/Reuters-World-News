#!/bin/bash

git pull
python src/update_youtube.py
git add .
git commit -am .
git push

