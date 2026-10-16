# Lab 5: Static Code Analysis

## Issue Documentation

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Subprocess with shell=True | Security — High | 51–52 | Shell execution was used to run a scene script constructed from a variable. | Replaced shell execution with argument-list execution and validated the scene filename. |
| Binding to all interfaces | Security — Medium | 4 | The hub was configured to listen on all network interfaces. | Changed the host to 127.0.0.1 for local-only access. |
| Hardcoded password | Security — Low | 7 | The hub password was stored directly in the source code. | Read the password from an environment variable. |
| Mutable default argument | Code quality | 11 | The settings dictionary used a mutable default value. | Changed the default to None and initialized a new dictionary inside the function. |
| Long line | Code style | Verify in original Flake8 report | A line exceeded the configured line-length limit. | Reformatted the code to comply with the style rules. |

## Verification Results

- Pylint: 10.00/10
- Bandit: No issues identified in the latest report.
- Flake8: No style violations reported.

## Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-style violations.

### 2. What did you learn from Pylint, Bandit, and Flake8?

Pylint helps identify code-quality problems, Bandit detects potential security issues, and Flake8 checks Python formatting and style conventions.

### 3. Why is static code analysis useful?

It helps developers identify problems early, improve maintainability, and reduce the likelihood of defects and security vulnerabilities.

### 4. What challenges did you encounter?

Some warnings required understanding the underlying code before choosing an appropriate fix. After making changes, the tools had to be run again to verify the results.