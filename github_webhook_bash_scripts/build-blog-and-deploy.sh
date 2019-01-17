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

echo $msg: Checking if blog-site directory exists
if [ ! -d "blog-site" ]; then
	echo $msg: Cloning git repository for blog-site
	git clone https://github.com/edmondchuc/blog-site.git
fi

echo $msg: Changing directoy to blog-site
cd blog-site/

echo $msg: Pulling from git repository for updates
git pull

echo $msg: Install pelican via pip3
pip3 install pelican

#TODO: check if this command results in any error. there should be a
#	command to check the previous application's exit code
#TODO: stop the script if it does not build correctly and exit.
echo $msg: Build the content with 'pelican content' command
pelican content

echo $msg: Check if ~/var/www/edmondchuc.com/html/blog/ exists
if [ ! -d "/var/www/edmondchuc.com/html/blog/" ]; then
	echo $msg: ERROR! Directory does not exist. Please create it manually with sudo and assign permissions correctly to the user.
	exit 1
fi

echo $msg: Removing existing files in ~/var/www/edmondchuc.com/html/blog/
rm -r /var/www/edmondchuc.com/html/blog/*

echo $msg: Copying output of pelican to ~/var/www/edmondchuc.com/html/blog/
cp -r output/* /var/www/edmondchuc.com/html/blog

echo Built and deployed successfully
