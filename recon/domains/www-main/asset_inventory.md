# Asset inventory

## Endpoints restricted to web crawler

https://www.datheon.in/robots.txt
```
User-Agent: *
Allow: /
Disallow: /training/dashboard
Disallow: /training/login
Disallow: /training/assessment/
Disallow: /api/

Sitemap: https://datheon.in/sitemap.xml
```

https://www.datheon.in/products

This thing have <iframe> which actually allows us to manipulate link changing
