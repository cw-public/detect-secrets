# Overview

<img width="1684" height="861" alt="image" src="https://github.com/user-attachments/assets/e918ed3d-6ac2-4465-bd7c-6f340481a073" />


# Installation

We provide an installation script that automates the following steps, so they don’t have to be done manually:

- Installation of **Python 3.13.7**
- Setup of the **Pre-commit Framework**
- Installation of **detect-secrets**

To execute the script, download it [here], navigate to its location, open a PowerShell session, and run:

`.\bootstrap.ps1`


# Setup (Required for every new project)

In VS Code, open a new terminal (if you already have a session running, please open an additional one).

Run the following command:

`hook-init`

This will create two new files in your project:

- .pre-commit-config.yaml
- .secrets.baseline

Open the file .pre-commit-config.yaml and add the following comment in line 3, next to the rev parameter:

`# pragma: allowlist secret`


If you are working in a repository that already contains these two files, it is recommended to run hook-init *again*.

Stage both `.pre-commit-config.yaml` and `.secrets.baseline` to complete the setup.

# Usage

Once the setup is complete, every future commit will be checked by the detect-secrets package.

If potential secrets or sensitive data are found, the commit will be blocked.

All flagged findings will be displayed in the console.

You then have two ways to deal with them:

1) Remove the secret from the codebase if it was unintentionally added.

2) Keep the secret if it is intentionally part of the codebase. In this case, you can create exceptions:

`# pragma: allowlist secret`

Marks a line as an exception so it will be ignored in future scans.

`detect-secrets scan > .secrets.baseline`

Creates a new baseline including all currently detected secrets, ensuring they won’t block future commits.
