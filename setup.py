#!/usr/bin/env python
# Generated by jaraco.develop 2.15.1
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools
import platform
import collections

with io.open('README.txt', encoding='utf-8') as readme:
	long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []

platform_reqs = collections.defaultdict(list,
	Windows = ['jaraco.windows>=2.13']
)[platform.system()]

setup_params = dict(
	name='jaraco.media',
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description = 'DVD and other multimedia tools',
	long_description=long_description,
	url="https://bitbucket.org/jaraco/jaraco.media",
	packages=setuptools.find_packages(),
	include_package_data=True,
	install_requires=[
		'jaraco.itertools',
		'jaraco.text',
		'jaraco.ui',
		'jaraco.context',
		'httpagentparser',
		'six',
		'more_itertools',
		'path',
	] + platform_reqs,
	setup_requires=[
		'setuptools_scm',
	] + pytest_runner + sphinx,
	tests_require=[
		'pytest',
		'cherrypy',
		'mock',
		'genshi',
	],
	license='MIT',
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points = {
		'console_scripts': [
			'encode-dvd = jaraco.media.dvd:encode_dvd',
			'rip-subtitles = jaraco.media.dvd:rip_subtitles',
			'crop-detect = jaraco.media.cropdetect:execute',
			'dvd-info = jaraco.media.dvd_info:main',
			'transcode = jaraco.media.dvd:transcode',
			'fix-fourcc = jaraco.media.dvd:fix_fourcc',
			'serve-index = jaraco.media.index:serve',
			'multibrake = jaraco.media.handbrake:multibrake',
			'quick-brake = jaraco.media.handbrake:quick_brake',
			'mkv-to-mp4 = jaraco.media.matroska:handle_command_line',
			'adjust-sub = jaraco.media.srt:AdjustCommand.run',
			'update-anydvd = jaraco.media.dvd:update_anydvd',
		],
	},
)

if __name__ == '__main__':
	setuptools.setup(**setup_params)
