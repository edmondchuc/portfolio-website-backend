#!/usr/bin/env bash

msg='webhook-api'

echo $msg: Changing directory to ~
cd ~

if [ ! -d "projects" ]; then
        echo $msg: Creating directory ~/projects
        mkdir ~/projects
fi

echo $msg: Changing directoy to ~/projects.
cd ~/projects

if [ ! -d "portfolio-website" ]; then
        echo $msg: Cloning from https://github.com/edmondchuc/portfolio-website.git
        git clone https://github.com/edmondchuc/portfolio-website.git
fi

echo $msg: Changing directory to portfolio-website
cd portfolio-website

echo $msg: Pulling from https://github.com/edmondchuc/portfolio-website.git
git pull

# Note: this expects the destination directory already exists. Otherwise, manually create using sudo.
echo $msg: Copying index.html to /var/www/edmondchuc/html
cp index.html /var/www/edmondchuc.com/html

echo $msg: Copying static/css to /var/www/edmondchuc.com/html/static/css
cp static/css/* /var/www/edmondchuc.com/html/static/css

echo $msg: Copying static/img to /var/www/edmondchuc.com/html/static/img
cp static/img/* /var/www/edmondchuc.com/html/static/img

echo $msg: Successfully finished webhook event 'for' edmondchuc/portfolio-website.