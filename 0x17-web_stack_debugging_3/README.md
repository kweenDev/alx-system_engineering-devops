# 0x17 Web Stack Debugging #3

## Description

This project is part of the Holberton School curriculum and focuses on debugging web stack issues, specifically dealing with a WordPress website running on a LAMP (Linux, Apache, MySQL, PHP) stack. The task involves using tools like `strace` and `Puppet` to diagnose and automate the resolution of issues causing a 500 Internal Server Error.

## Tasks

1. **0-strace_is_your_friend.pp**: Using `strace`, identify and fix the issue causing Apache to return a 500 error. Then automate the fix using Puppet.

## How to Use

1. Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/0x17-web_stack_debugging_3.git
```

2. Navigate to the project directory:
```bash
cd 0x17-web_stack_debugging_3
```

3. Run Puppet to apply the fix:
```bash
puppet apply 0-strace_is_your_friend.pp
```

## Files

- `0-strace_is_your_friend.pp`: Puppet manifest for fixing the Apache 500 error using `strace` and automation.

## Author

- [kweenDev](https://github.com/kweenDev)
