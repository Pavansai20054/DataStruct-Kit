# DataStruct-Kit Security Policy

---

## Table of Contents
- [DataStruct-Kit Security Policy](#datastruct-kit-security-policy)
  - [Table of Contents](#table-of-contents)
  - [Reporting Security Vulnerabilities](#reporting-security-vulnerabilities)
    - [Reporting Process](#reporting-process)
  - [Vulnerability Response Process](#vulnerability-response-process)
  - [Security Response SLAs](#security-response-slas)
  - [Supported Versions](#supported-versions)
  - [Security Best Practices](#security-best-practices)
  - [Security Updates](#security-updates)
  - [Vulnerability Disclosure Policy](#vulnerability-disclosure-policy)
  - [Security Acknowledgments](#security-acknowledgments)

---

## Reporting Security Vulnerabilities

The **DataStruct-Kit** team takes security issues seriously. We appreciate your efforts to responsibly disclose your findings and will make every effort to acknowledge and address valid reports promptly.

> **DO NOT** create public GitHub issues for security vulnerabilities.

### Reporting Process
To report a security vulnerability, please email: **pavansai.20066@gmail.com**

Your report should include:
- **Description**: Clear and concise explanation of the vulnerability.
- **Affected Version(s)**: Specify which versions of DataStruct-Kit are affected.
- **Reproduction Steps**: Detailed steps to reproduce the vulnerability.
- **Impact**: Potential impact of the vulnerability if exploited.
- **Suggested Fix**: (Optional) Recommendations for addressing the issue.
- **Your Contact Information**: For follow-up communication.

We encourage the use of **encrypted communication**. Our PGP key is available upon request.

---

## Vulnerability Response Process

The DataStruct-Kit team follows a structured process to handle reported vulnerabilities:

1. **Acknowledgment**: We will acknowledge receipt of your vulnerability report within the SLA timeframe.
2. **Validation**: Our security team will validate the vulnerability and determine its severity.
3. **Resolution Development**: A fix for the vulnerability will be developed.
4. **Security Release**: A security release will be issued with the fix.
5. **Public Disclosure**: The vulnerability will be publicly disclosed after the fix is deployed.

---

## Security Response SLAs

We strive to respond to and address security vulnerabilities based on their severity:

| **Severity** | **Description**                                | **Initial Response** | **Target Resolution** |
|--------------|------------------------------------------------|-----------------------|------------------------|
| **Critical** | Remote code execution, authentication bypass, data loss | 24 hours             | 1 week                 |
| **High**     | SQL injection, XSS, privilege escalation       | 72 hours             | 2 weeks               |
| **Medium**   | Information disclosure, denial of service      | 1 week               | 1 month               |
| **Low**      | Minor issues with limited impact               | 2 weeks              | Next release          |

> Severity is assessed based on the **Common Vulnerability Scoring System (CVSS)**.

---

## Supported Versions

| **Version** | **Supported** | **End of Support**        |
|-------------|---------------|---------------------------|
| **0.2.x**   | ✅             | TBD                       |
| **0.1.x**   | ✅             | After **0.3.0** release   |
| **< 0.1.0** | ❌             | Unsupported               |

> We recommend always using the latest version of **DataStruct-Kit**.

---

## Security Best Practices

When using **DataStruct-Kit**, consider these security best practices:
- **Keep Updated**: Always use the latest version to benefit from security fixes.
- **Input Validation**: Validate all input data before processing with DataStruct-Kit algorithms.
- **Resource Limits**: Set appropriate limits when using algorithms with potentially high resource usage.
- **Dependency Scanning**: Regularly scan your project's dependencies for vulnerabilities.

---

## Security Updates

Security updates will be published through:
- **GitHub Security Advisories**
- **Release Notes**
- **PyPI Package Updates**
- Announcements on our **official channels**

---

## Vulnerability Disclosure Policy

Our policy follows **responsible disclosure principles**:
1. Security issues are initially kept **private**.
2. Fixes are developed privately and tested thoroughly.
3. **CVE IDs** are requested for significant vulnerabilities.
4. **Coordinated disclosure** occurs after fixes are available.
5. Credit is given to the reporter unless they wish to remain anonymous.

---

## Security Acknowledgments

We would like to thank the following individuals for responsibly disclosing security vulnerabilities:

> This section will be updated as contributors report security issues.

---

This security policy may be updated periodically. Please check back for changes.  
_Last updated: May 17, 2025_