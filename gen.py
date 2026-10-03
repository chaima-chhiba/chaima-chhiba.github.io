import os
NAV=[("/","Home"),("/about/","About"),("/projects/","Projects"),("/experience/","Experience"),("/#contact","Contact")]
def page(path,title,desc,body,active):
    links="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a></li>' for h,t in NAV)
    url="https://chaima-chhiba.github.io"+path
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#090b0f">
<link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23090b0f'/%3E%3Ctext x='4' y='22' font-family='monospace' font-size='16' fill='%2340d98a'%3ECC%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/css/style.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap nav-in"><a class="logo mono" href="/" aria-label="Chaima Chhiba, home">CC</a>
<button class="burger" aria-expanded="false" aria-controls="menu" aria-label="Open menu"><span></span><span></span></button>
<nav aria-label="Main"><ul id="menu">{links}</ul></nav></div></header>
<main id="main">{body}</main>
<footer class="foot"><div class="wrap"><span class="mono">Chaima Chhiba - Ariana, Tunisia</span><span class="mono">Static site, no trackers.</span></div></footer>
<script src="/assets/js/main.js" defer></script></body></html>'''
    d="."+path
    os.makedirs(d,exist_ok=True)
    open(d+"index.html","w").write(html)
LINKS='''<ul class="links mono"><li><a href="https://github.com/chaima-chhiba" rel="me noopener">GitHub</a></li><li><a href="https://linkedin.com/in/chaima-chhiba" rel="me noopener">LinkedIn</a></li><li><a href="mailto:chhibaachaima@gmail.com">Email</a></li><li><a href="/assets/Chaima-Chhiba-Cv.pdf">CV</a></li></ul>'''
PROJ=[
("AWS Cloud Security & Automated Remediation","Cloud security - 2026","AWS infrastructure provisioned with Terraform and secured through automated monitoring, findings and remediation workflows.",["AWS","Terraform","VPC","EC2","S3","IAM","Lambda"],
"Cloud resources need consistent identity, logging and security controls as the environment grows.","Provision VPC, EC2, S3 and IAM with least-privilege policies, then configure AWS Config, Security Hub and CloudTrail to detect security and compliance issues.","An AWS environment with Lambda-based automated security and compliance remediation.",""),
("Cloud-Native DevSecOps Platform","DevSecOps - 2026","Cloud-native application platform on Kubernetes with infrastructure automation, secure delivery and observability built into the workflow.",["Kubernetes","Terraform","GitHub Actions","Prometheus","Grafana","SBOM"],
"Shipping cloud-native applications safely requires security checks and operational visibility throughout delivery.","Automate infrastructure and deployment with Terraform and CI/CD, integrating secret detection, SAST, dependency analysis, image scanning and SBOM generation.","A Kubernetes platform with Prometheus/Grafana observability and non-root container execution enforced.","https://github.com/chaima-chhiba/secure-cicd-demo"),
("Vulnerability Intelligence Platform","Security engineering - Ooredoo Tunisia","Platform for collecting, normalizing, enriching and prioritizing vulnerability intelligence from NVD, CISA KEV, VulnCheck and GitHub advisories, with real-time alerting.",["Python","FastAPI","PostgreSQL","React","Docker"],
"Vulnerability data arrives through multiple feeds and formats, making it difficult to identify the most urgent threats.","Integrate the sources, normalize their data, handle API rate limits, prioritize findings and expose alerts through a web platform.","A containerized vulnerability intelligence portal with a PostgreSQL backend, React interface and real-time alerts.","https://github.com/chaima-chhiba/Cybersecurity-Vulnerability-Intelligence-Portal"),
("OWASP Juice Shop Penetration Test","Application security - 2026","Security assessment of the OWASP Juice Shop application focused on identifying and documenting common web vulnerabilities.",["OWASP Top 10","Burp Suite","OWASP ZAP","Web security"],
"Modern web applications can expose authentication, injection, access-control and client-side weaknesses.","Assess the application through structured penetration-testing workflows and document reproducible findings with security recommendations.","A penetration-testing report and evidence repository for OWASP Juice Shop vulnerabilities.","https://github.com/chaima-chhiba/owasp-juiceshop-pentest")]
def tags(l): return '<ul class="tags mono">'+"".join(f"<li>{x}</li>" for x in l)+"</ul>"
def repo(url): return f'<p class="mono repo"><a href="{url}" rel="noopener">View repository</a></p>' if url else ""
def card(p): return f'<article class="card rv"><p class="mono dim">{p[1]}</p><h3>{p[0]}</h3><p>{p[2]}</p>{tags(p[3])}{repo(p[7])}</article>'
EXP=[("Ooredoo Tunisia","Cybersecurity & DevOps Engineering Intern","Jul-Aug 2026",["Designed a threat intelligence platform integrating NVD, CISA KEV, VulnCheck and GHSA","Normalized vulnerability data, handled API rate limits, prioritized threats and added real-time alerts","Python / FastAPI, PostgreSQL, React, Docker"]),
("Fresenius Kabi","Cloud & DevOps Intern","Aug-Sep 2025",["Implemented a GitHub Actions and Docker CI/CD pipeline for deployment on a resource-constrained VM","Configured Nginx as a reverse proxy and hardened Linux servers in production"]),
("EdTrust","Full-Stack Developer & DevOps Engineer - Part-time, Remote","Jun 2024-Feb 2025",["Automated onboarding for 40+ clients through HubSpot CRM, including account creation and database initialization","Developed 10+ features, fixed bugs and implemented CI/CD across development, staging and production"]),
("EdTrust","Final-Year Intern - Remote","Feb-May 2024",["Developed EdMin, a MEVN school management platform supporting users, roles, clients, packages and dashboards"]),
("Safran","Software Engineering Intern","Jun-Aug 2023",["Angular, Spring Boot, SQL Server"])]
def tl(full):
    o='<ol class="tl">'
    for c,r,d,w in EXP:
        b="<ul>"+"".join(f"<li>{x}</li>" for x in w)+"</ul>" if full else ""
        o+=f'<li class="rv"><span class="mono dim">{d}</span><div><h3>{c}</h3><p class="role">{r}</p>{b}</div></li>'
    return o+"</ol>"
# HOME
home=f'''<section class="hero wrap"><div class="hero-t">
<p class="mono status"><span class="dot"></span>Open to 6-month PFE opportunities - February 2027</p>
<h1>Building infrastructure<br>that works quietly.</h1>
<p class="sub">Final-year engineering student focused on Cloud, DevOps and Platform Engineering.</p>
<p class="dim">I build and automate cloud infrastructure, delivery pipelines and security-focused engineering workflows.</p>
<div class="cta"><a class="btn pri" href="/projects/">View my work</a><a class="btn" href="/about/">About me</a></div>{LINKS}</div>
<div class="term" role="img" aria-label="Terminal panel: chaima-chhiba, focus cloud, devops, sre, devsecops; stack aws, kubernetes, terraform, linux, ansible, docker, github-actions, argocd; status building and learning">
<div class="term-bar"><i></i><i></i><i></i></div><pre class="mono" aria-hidden="true"><span class="p">$</span> whoami
<b>chaima-chhiba</b>

<span class="p">$</span> focus
cloud / devops / sre / devsecops

<span class="p">$</span> stack
aws / kubernetes / terraform
linux / ansible / docker
github-actions / argocd

<span class="p">$</span> status
building &amp; learning<span class="cur">_</span></pre></div></section>
<section class="wrap sec"><h2 class="rv">What I do</h2><div class="grid3">
<article class="card rv"><h3>Cloud &amp; Infrastructure</h3><p>Designing and operating practical cloud environments with AWS, Linux, networking and infrastructure as code.</p></article>
<article class="card rv"><h3>DevOps &amp; SRE</h3><p>Building repeatable delivery workflows with CI/CD, containers, Kubernetes, observability and automation.</p></article>
<article class="card rv"><h3>DevSecOps</h3><p>Integrating security checks, vulnerability intelligence and security controls into engineering workflows.</p></article></div></section>
<section class="wrap sec"><h2 class="rv">Selected work</h2><div class="grid2">{"".join(card(p) for p in PROJ)}</div><p class="more"><a href="/projects/">See all projects and write-ups</a></p></section>
<section class="wrap sec"><h2 class="rv">Experience</h2>{tl(False)}<p class="more"><a href="/experience/">View full experience</a></p></section>
<section class="wrap sec contact" id="contact"><h2 class="big rv">Let's build something<br>reliable.</h2>{LINKS}</section>'''
page("/","Chaima Chhiba - Cloud, DevOps & Platform Engineering","Final-year engineering student at TEK-UP focused on Cloud, DevOps, Platform Engineering and DevSecOps. Looking for a 6-month PFE starting February 2027.",home,"/")
# ABOUT
tk=[("Cloud & Infrastructure","AWS, Terraform, Linux, Ansible"),("Containers & Platform","Kubernetes, Docker, Nginx, ArgoCD"),("CI/CD & Observability","GitHub Actions, Jenkins, Prometheus, Grafana"),("Security","DevSecOps, AWS Security Hub, CIS AWS Benchmark, OWASP Top 10, Burp Suite, OWASP ZAP"),("Development","Python, Node.js, TypeScript, Java, Vue.js, PostgreSQL, MongoDB")]
kit="".join(f'<div class="row rv"><h3 class="mono">{a}</h3>{tags(b.split(", "))}</div>' for a,b in tk)
certs=["AWS Certified Solutions Architect - Associate (SAA-C03)","Red Hat Certified Engineer (RHCE)","Red Hat Certified Developer in Cloud-native Applications","Red Hat Certified System Administrator (RHCSA)"]
about=f'''<section class="wrap sec first"><h1 class="rv">Engineer by training,<br>builder by curiosity.</h1>
<div class="two"><h2 class="rv">About me</h2><div class="prose rv">
<p>I'm a final-year engineering student at TEK-UP University, working on cloud infrastructure, DevOps, Platform Engineering and DevSecOps. I like systems that are automated, reproducible and boring to operate.</p>
<p>My day-to-day tools are AWS, Linux, Kubernetes, Terraform and CI/CD pipelines. I've worked at Ooredoo Tunisia, Fresenius Kabi, EdTrust and Safran, shipping everything from a vulnerability intelligence platform to Dockerized deployments behind Nginx.</p>
<p>I'm looking for a 6-month PFE starting February 2027.</p>{LINKS}</div></div></section>
<section class="wrap sec"><div class="two"><h2 class="rv">Technical toolkit</h2><div>{kit}</div></div></section>
<section class="wrap sec"><div class="two"><h2 class="rv">Education</h2><div>
<div class="row rv"><h3>TEK-UP University</h3><p>Engineering Degree - Network Security &amp; Cybersecurity</p><p class="mono dim">2024 - September 2027</p><p class="dim">Ranked 5th/30</p></div>
<div class="row rv"><h3>ISI Mahdia</h3><p>Bachelor's Degree in Computer Science</p><p class="mono dim">2021 - 2024</p></div></div></div></section>
<section class="wrap sec"><div class="two"><h2 class="rv">Certifications</h2><ul class="clist rv">{"".join(f"<li>{c}</li>" for c in certs)}</ul></div></section>
<section class="wrap sec"><div class="two"><h2 class="rv">Languages</h2><ul class="clist rv"><li>Arabic - Native</li><li>French - Fluent</li><li>English - Fluent</li></ul></div></section>'''
page("/about/","About - Chaima Chhiba","Final-year engineering student at TEK-UP University working on cloud infrastructure, DevOps, Platform Engineering and DevSecOps.",about,"/about/")
# PROJECTS
pj=""
for i,p in enumerate(PROJ,1):
    pj+=f'''<article class="proj rv"><div class="pn mono">{i:02d}</div><div><p class="mono dim">{p[1]}</p><h2>{p[0]}</h2><p class="lead">{p[2]}</p>{tags(p[3])}
<dl><dt class="mono">Problem</dt><dd>{p[4]}</dd><dt class="mono">Approach</dt><dd>{p[5]}</dd><dt class="mono">What was built</dt><dd>{p[6]}</dd></dl>
{repo(p[7])}</div></article>'''
page("/projects/","Projects - Chaima Chhiba","Selected cloud, DevOps and application security projects: AWS security, DevSecOps, vulnerability intelligence and penetration testing.",f'<section class="wrap sec first"><h1 class="rv">Projects</h1><p class="dim rv">Infrastructure, pipelines and security tooling.</p>{pj}</section>',"/projects/")
page("/experience/","Experience - Chaima Chhiba","Internships and work at Ooredoo Tunisia, Fresenius Kabi, EdTrust and Safran across cybersecurity, cloud, DevOps and software engineering.",f'<section class="wrap sec first"><h1 class="rv">Experience</h1>{tl(True)}</section>',"/experience/")
open("404.html","w").write(open("index.html").read().replace("<title>Chaima Chhiba - Cloud, DevOps &amp; Platform Engineering</title>","<title>Not found</title>"))
nf=f'<section class="wrap sec first"><p class="mono dim">404</p><h1>Page not found.</h1><p class="dim">That path doesn\'t exist. Try the <a href="/">home page</a> or <a href="/projects/">projects</a>.</p></section>'
page("/","Page not found - Chaima Chhiba","Page not found.",nf,"")
os.replace("index.html","404.html")
page("/","Chaima Chhiba - Cloud, DevOps & Platform Engineering","Final-year engineering student at TEK-UP focused on Cloud, DevOps, Platform Engineering and DevSecOps. Looking for a 6-month PFE starting February 2027.",home,"/")
