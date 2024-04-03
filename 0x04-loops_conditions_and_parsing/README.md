# 0x04. Loops, conditions and parsing

## Table of Contents

- [Project Overview](#project-overview)
- [Background Context](#background-context)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Create a SSH RSA key pair](#task-0-create-a-ssh-rsa-key-pair)
  - [For Best School loop](#task-1-for-best-school-loop)
  - [While Best School loop](#task-2-while-best-school-loop)
  - [Until Best School loop](#task-3-until-best-school-loop)
  - [If 9, say Hi!](#task-4-if-9-say-hi)
  - [4 bad luck, 8 is your chance](#task-5-4-bad-luck-8-is-your-chance)
  - [Superstitious numbers](#task-6-superstitious-numbers)
  - [Clock](#task-7-clock)
  - [For ls](#task-8-for-ls)
  - [To file, or not to file](#task-9-to-file-or-not-to-file)
  - [FizzBuzz](#task-10-fizzbuzz)
  - [Read and cut](#task-11-read-and-cut)
  - [Tell the story of passwd](#task-12-tell-the-story-of-passwd)
  - [Let's parse Apache logs](#task-13-lets-parse-apache-logs)
  - [Dig the data](#task-14-dig-the-data)

---

## Project Overview

This project focuses on loops, conditions, and parsing in Bash scripting. It covers topics such as SSH key generation, loop constructs (for, while, until), if statements, file manipulation, and log parsing.

---

## Background Context

The project aims to enhance your understanding and proficiency in Bash scripting for DevOps purposes. You will work on various tasks that involve creating scripts to automate tasks, manipulate files, and parse logs.

---

## Learning Objectives

By completing this project, you are expected to be able to:

- Create SSH keys
- Use various loop constructs (for, while, until)
- Implement if, else, elif, and case condition statements
- Utilize file and comparison operators
- Write portable Bash scripts
- Pass Shellcheck without errors

---

## Requirements

- Allowed editors: vi, vim, emacs
- Interpretation on Ubuntu 20.04 LTS
- Files should end with a new line
- Include a README.md file at the root
- All Bash script files must be executable
- Use `#!/usr/bin/env bash` as the first line in your scripts
- Avoid using `awk`
- Scripts must pass Shellcheck without errors
- Avoid publishing project content or plagiarizing

---

## Tasks

### Task 0: Create a SSH RSA key pair

Create a SSH RSA key pair and share the public key in your answer file `0-RSA_public_key.pub`.

### Task 1: For Best School loop

Write a Bash script that displays "Best School" 10 times using the for loop.

### Task 2: While Best School loop

Write a Bash script that displays "Best School" 10 times using the while loop.

### Task 3: Until Best School loop

Write a Bash script that displays "Best School" 10 times using the until loop.

### Task 4: If 9, say Hi!

Write a Bash script that displays "Best School" 10 times, but for the 9th iteration, displays "Hi" on a new line.

### Task 5: 4 bad luck, 8 is your chance

Write a Bash script that loops from 1 to 10 and displays "bad luck" for the 4th loop iteration, "good luck" for the 8th loop iteration, and "Best School" for other iterations.

### Task 6: Superstitious numbers

Write a Bash script that displays numbers from 1 to 20 and:

- Displays "bad luck from China" for the 4th loop iteration
- Displays "bad luck from Japan" for the 9th loop iteration
- Displays "bad luck from Italy" for the 17th loop iteration

### Task 7: Clock

Write a Bash script that displays the time for 12 hours and 59 minutes.

### Task 8: For ls

Write a Bash script that displays the content of the current directory in a list format where only the part of the name after the first dash is displayed.

### Task 9: To file, or not to file

Write a Bash script that gives information about the school file's existence, emptiness, and regularity.

### Task 10: FizzBuzz

Write a Bash script that displays numbers from 1 to 100 and:

- Displays "FizzBuzz" for multiples of 3 and 5
- Displays "Fizz" for multiples of 3
- Displays "Buzz" for multiples of 5
- Otherwise, displays the number itself

### Task 11: Read and cut

Write a Bash script that displays the username, user ID, and home directory path of the current user.

### Task 12: Tell the story of passwd

Write a Bash script that parses `passwd` file and displays username, user ID, and home directory path for each user.

### Task 13: Let's parse Apache logs

Write a Bash script that displays the IP addresses and HTTP status codes from an Apache log file.

### Task 14: Dig the data

Write a Bash script that extracts information from the output of the `dig` command and displays it in a specific format.

---

**Authors**
*kweenDev*
