# Overview

A pre-commit hook using the detect-secrets package helps prevent accidental leaks of sensitive information before a commit.
The main component of this tool is the secrets-baseline, which acts as a whitelist for sensitive data.
Any secrets not listed in this file (ideally it should remain empty) are scanned by various filters and plugins.
These scan the entire repository for potential secrets and block possible leak unless they are explicitly whitelisted in the secrets-baseline, since some secrets may be required for the functionality of the code.

For more information check: [Wiki-Article](https://wiki.controlware.de:8443/spaces/ITID/pages/330443336/Verhindern+das+Passw%C3%B6rter+in+Github+landen)

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

`hook-init` is a custom function written inside the windows `$PROFILE` that executes basic `detect-secrets` commands
- installs pre-commit
- installs detect-secrets from our fork
- creates pre-commit-config.yaml
- creates baseline

> Run `hook-init` every time you are working on a new repository - it is ok to run the command multiple times inside the same repository

# .pre-commit-config.yaml

```
repos:
-   repo: https://github.com/cw-public/detect-secrets.git
    rev: 6a1ec2f3287a029d703ea9f9527cf164318caaf6
    hooks:
    -   id: detect-secrets
        args: ["--baseline", ".secrets.baseline"]
        exclude: package.lock.json

```

The pre-commit configuration file. It enables the remote execution from a remote repository
- rev : the hashid of the most recent commit
- repo: reference to the remote tool
- hooks: Tool parameter

# .secrets.baseline

```
{
  "version": "1.5.0",
  "plugins_used": [
    {
      "name": "ArtifactoryDetector"
    },
    {
      "name": "AWSKeyDetector"
    },
    {
      "name": "AzureStorageKeyDetector"
    },
    {
      "name": "Base64HighEntropyString",
      "limit": 4.5
    },
    {
      "name": "BasicAuthDetector"
    },
    {
      "name": "CloudantDetector"
    },
    {
      "name": "DiscordBotTokenDetector"
    },
    {
      "name": "GitHubTokenDetector"
    },
    {
      "name": "GitLabTokenDetector"
    },
    {
      "name": "HexHighEntropyString",
      "limit": 3.0
    },
    {
      "name": "IbmCloudIamDetector"
    },
    {
      "name": "IbmCosHmacDetector"
    },
    {
      "name": "IPPublicDetector"
    },
    {
      "name": "JwtTokenDetector"
    },
    {
      "name": "KeywordDetector",
      "keyword_exclude": ""
    },
    {
      "name": "MailchimpDetector"
    },
    {
      "name": "NpmDetector"
    },
    {
      "name": "OpenAIDetector"
    },
    {
      "name": "PrivateKeyDetector"
    },
    {
      "name": "PypiTokenDetector"
    },
    {
      "name": "SendGridDetector"
    },
    {
      "name": "SlackDetector"
    },
    {
      "name": "SoftlayerDetector"
    },
    {
      "name": "SquareOAuthDetector"
    },
    {
      "name": "StripeDetector"
    },
    {
      "name": "TelegramBotTokenDetector"
    },
    {
      "name": "TwilioKeyDetector"
    },
    {
      "name": "VaultTokenDetector"
    }
  ],
  "filters_used": [
    {
      "path": "detect_secrets.filters.allowlist.is_line_allowlisted"
    },
    {
      "path": "detect_secrets.filters.common.is_ignored_due_to_verification_policies",
      "min_level": 2
    },
    {
      "path": "detect_secrets.filters.heuristic.is_indirect_reference"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_likely_id_string"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_lock_file"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_not_alphanumeric_string"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_potential_uuid"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_prefixed_with_dollar_sign"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_sequential_string"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_swagger_file"
    },
    {
      "path": "detect_secrets.filters.heuristic.is_templated_secret"
    },
    {
      "path": "detect_secrets.filters.regex.should_exclude_file",
      "pattern": [
        ".pre-commit-config.yaml"
      ]
    }
  ],
  "results": {},
  "generated_at": "2025-10-14T08:06:47Z"
}
```

The `.secrets.baseline` acts as an "allowlist". Detect-secrets is a scanning Tool every time something gets pushed the entire codebase gets scanned.
Since its not possible to detect 100% of all secrets it might happen that something triggers a so called *False Positive*. Its basically something
that looks like a secret but is not. Lets say a random hash needed in a Code. Every time the scan would run that hash would be a reason for the Commit to not go through.
To avoid those cases this hash would get registered in the `.secrets.baseline` everything inside there is assumed to be something that might look sensitive but in reality is not.

If you are working in a repository that already contains these two files, it is recommended to run hook-init *again*.

! Stage both `.pre-commit-config.yaml` and `.secrets.baseline` to complete the setup. !

> **⚠️ WARNING**
> 
> The Scope of detect-secrets is narrowed down to ONLY Git-tracked files. Anything that got created recently inside the new Session and hasnt been pushed
> wont show up in a basic `detect-secrets scan > .secrets.baseline` or `detect-secrets scan .` means if you run one of those two commands and dont see specific
> files, make sure that they have been staged !

> **ℹ️ Info**
> 
> If `hook-init` is not found in the current Shell Session, you should be able to update the tools by running
> `. $PROFILE`
> `Update-SessionPath`

`Update-SessionPath` is another custom function inside `$PROFILE` the purpose of this function is to enable `hook-init` by communicating the updated PATH variables in the current working Session.
The reason for that is to avoid having to restart VSCode.

# Usage

Once the setup is complete, every future commit will be checked by the detect-secrets package.

If potential secrets or sensitive data are found, the commit will be blocked.

All flagged findings will be displayed in the console.

You then have two ways to deal with them:

1) Remove the secret from the codebase if it was unintentionally added.

2) Keep the secret if it is intentionally part of the codebase. In this case, you can create exceptions:


Marks a line as an exception so it will be ignored in future scans.

`# pragma: allowlist secret`

Creates a new baseline including all currently detected secrets, ensuring they won’t block future commits.

`detect-secrets scan > .secrets.baseline` or
`hook-init`

You can run a test scan of the current folder to check if there might be sensitive data that could block future commits run:

`detect-secrets scan .`

> **ℹ️ Info**  
> Any baseline created inside VS Code using PowerShell will result in UTF-16 encoding, which is undesired.  
> Either run `detect-secrets scan > .secrets.baseline` using CMD to ensure UTF-8 encoding, or save the created baseline as UTF-8 and reload the window (bottom right of the editor).

