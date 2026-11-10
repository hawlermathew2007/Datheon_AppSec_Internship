# Datheon Attack Surface

## Application Entry Points

- Observe how the browser communicates with the server when loading pages or submitting data.
- Parameters
- Hidden field
- Document the requested pages, important parameters, request methods, authentication usage, TLS implementation, or multi-step processes to facilitate further testing.
- Request and Response

## Path Execution Through Application

any potential path like login user processes (document those)

## Web Application Framework

Web Stack:

- Programming language
- API tech
- Authentication Provider
- CMS Platform
- Payment Gateway
- Framework
- Database
- Tech used by web
- Cache

Find them through:

- HTTP headers - Look at response headers to find server or framework information.
- Cookies → Chec- cookie names and values that may indicate specific technologies.
- HTML source code - Inspect the page source for comments, meta tags, or linked files.
- Specific files an- folders → Look for common framework files or directories (e.g., /admin, /wp-content, etc.).
- File extensions - Observe extensions like .php, .aspx, .jsp, which may reveal backend technology.
- Error messages - Analyze error messages that might disclose server or framework details.

## Security Components

- WAF and Firewall (nmap)
- Web server
- Analyze key response headers such as Server, HTTP protocol version, and security-related headers (curl -I -v).
- Check for the presence or absence of common security headers (e.g., HSTS, X-Frame-Options, Content-Security-Policy).
- Document and evaluate the findings as part of the web server fingerprinting process.

## Network Components

- Load balancer
- CDN (nslookup)

## Source
https://medium.com/@angelinasalim_/information-gathering-mapping-the-web-application-structure-and-attack-surface-f7821d5c5886
