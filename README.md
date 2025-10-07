# Overview

A pre-commit hook using the detect-secrets package helps prevent accidental leaks of sensitive information before a commit.
The main component of this tool is the secrets-baseline, which acts as a whitelist for sensitive data.
Any secrets not listed in this file (ideally it should remain empty) are scanned by various filters and plugins.
These scan the entire repository for potential secrets and block possible leak unless they are explicitly whitelisted in the secrets-baseline, since some secrets may be required for the functionality of the code.

<img width="1684" height="861" alt="image" src="https://github.com/user-attachments/assets/e918ed3d-6ac2-4465-bd7c-6f340481a073" />


# Installation

We provide an installation script that automates the following steps, so they don’t have to be done manually:

- Installation of **Python 3.13.7**
- Setup of the **Pre-commit Framework**
- Installation of **detect-secrets**

To execute the script, download it [here](https://github.com/cw-modernapplicationplatform/tools/tree/master/bash/detect-secrets), navigate to its location, open a PowerShell session, and run:

`.\secrets-bootstrap.ps1`


# Setup (Required for every new project)

In VS Code run the following command:
`hook-init`

This will create two new files in your project:

- .pre-commit-config.yaml
- .secrets.baseline


If you are working in a repository that already contains these two files, it is recommended to run hook-init *again*.

Stage both `.pre-commit-config.yaml` and `.secrets.baseline` to complete the setup.

> **ℹ️ Info**
> 
> If `hook-init` is not found in the current Shell Session, you should be able to update the tools by running
> `. $PFOPILE`
> `Update-SessionPath` 

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

> **ℹ️ Info**  
> Any baseline created inside VS Code using PowerShell will result in UTF-16 encoding, which is undesired.  
> Either run `detect-secrets scan > .secrets.baseline` using CMD to ensure UTF-8 encoding, or save the created baseline as UTF-8 and reload the window (bottom right of the editor).

