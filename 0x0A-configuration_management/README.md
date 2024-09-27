# 0x0A. Configuration Management

## Overview
This project focuses on configuration management, DevOps practices, system administration, scripting, and continuous integration/continuous deployment (CI/CD). It includes tasks related to Puppet, a configuration management tool, and covers fundamental concepts and practical exercises.

## Background Context
During my time at SlideShare, I worked on an auto-remediation tool named Skynet, which monitored, scaled, and fixed cloud infrastructure. I utilized MCollective, a parallel job-execution system, to execute commands across multiple servers simultaneously. However, a bug in the code led to an incident where a mistaken action caused significant downtime. Thanks to Puppet, we were able to restore our infrastructure efficiently.

## Resources
- [Intro to Configuration Management](#)
- [Puppet resource type: file](#)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](#)
- [Puppet lint](#)
- [Puppet emacs mode](#)

## Requirements
### General
- All files will be interpreted on Ubuntu 20.04 LTS.
- All files should end with a new line.
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a comment explaining the manifest's purpose.
- Your Puppet manifests files must end with the extension .pp.

### Note on Versioning
- Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install Puppet
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

### Install puppet-lint
```bash
$ gem install puppet-lint
```

## Tasks
1. *Create a file*
	- Using Puppet, create a file in /tmp.
	- File path is /tmp/school
	- File permission is 0744
	- File owner is www-data
	- File group is www-data
	- File contains "I love Puppet"

2. *Install a package*
	- Using Puppet, install Flask from pip3.
	- Version must be 2.1.0

3. *Execute a command*
	- Using Puppet, create a manifest that kills a process named killmenow.
	- Must use the exec Puppet resource
	- Must use pkill

### Author
_kweenDev_ (Refiloe Radebe)
