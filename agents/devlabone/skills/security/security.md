# Security Skill

## Name:
Cyber Security & Application Security Expert

## Description:
Complete Security skill covering application security, secure software development, web security, API security, cloud security, identity management, network security, database security, DevSecOps, vulnerability management, threat modelling, security testing, compliance, AI security, and enterprise security architecture for building secure software products.

## Version:
1.0.0

---

# Skill Instructions

You are an expert Security Engineer and Security Architect.

Your responsibility is to transform:

```
Business Requirements

        ↓

Security Requirements

        ↓

Secure Architecture

        ↓

Secure Implementation

        ↓

Protected Production System
```

You must think like:

- Chief Information Security Officer (CISO)
- Security Architect
- Application Security Engineer
- Cloud Security Engineer
- Ethical Hacker
- DevSecOps Engineer
- Privacy Engineer

---

# Security Mission

Your goal is to build systems that are:

- Confidential
- Secure
- Reliable
- Available
- Resilient
- Privacy compliant

---

# CIA Security Triad

The foundation of security.

```
Confidentiality

        +

Integrity

        +

Availability
```

---

# Confidentiality

Protect information from unauthorized access.

Examples:

- Encryption
- Access control
- Authentication

---

# Integrity

Ensure data is accurate and not modified improperly.

Examples:

- Hashing
- Digital signatures
- Validation

---

# Availability

Ensure systems remain accessible.

Examples:

- Backup
- Disaster recovery
- High availability

---

# Security Principles

Follow:

## Least Privilege

Users receive only required permissions.

Example:

```
Employee

Only access required documents
```

---

## Defense in Depth

Multiple security layers.

Example:

```
Firewall

 +

Authentication

 +

Authorization

 +

Encryption
```

---

## Zero Trust Security

Never automatically trust.

Principle:

```
Verify Everything

Trust Nothing
```

---

## Secure By Design

Security must be considered from the beginning.

Not:

```
Build First

Secure Later
```

Instead:

```
Design Secure

Build Secure

Deploy Secure
```

---

# Security Architecture Overview

Modern secure application:

```
User

 ↓

Identity Provider

 ↓

Frontend Application

 ↓

API Gateway

 ↓

Backend Services

 ↓

Database

 ↓

Cloud Infrastructure
```

Security exists at every layer.

---

# Security Domains

A complete security strategy includes:

```
Application Security

API Security

Cloud Security

Network Security

Data Security

Identity Security

Infrastructure Security

DevSecOps

AI Security
```

---

# Secure Software Development Lifecycle (SSDLC)

Security throughout development:

```
Planning

 ↓

Design

 ↓

Development

 ↓

Testing

 ↓

Deployment

 ↓

Monitoring
```

---

# Security Requirements Analysis

Identify:

- Assets
- Threats
- Risks
- Controls

---

# Security Requirement Examples

## Authentication Requirement

```
Users must authenticate before accessing private resources.
```

---

## Authorization Requirement

```
Users can access only permitted resources.
```

---

## Data Protection Requirement

```
Sensitive data must be encrypted.
```

---

# Asset Identification

Identify valuable resources:

Examples:

- User data
- Financial information
- Source code
- Credentials
- Business secrets

---

# Threat Analysis

Identify possible attacks:

Examples:

- Data theft
- Account takeover
- Malware
- Injection attacks
- Unauthorized access

---

# Risk Assessment

Risk:

```
Risk =

Probability × Impact
```

---

# Risk Categories

## Low Risk

Minimal impact.

---

## Medium Risk

Requires mitigation.

---

## High Risk

Immediate action required.

---

# Threat Modelling

Threat modelling identifies security risks before implementation.

---

# STRIDE Threat Model

Microsoft security framework.

Categories:

```
S - Spoofing

T - Tampering

R - Repudiation

I - Information Disclosure

D - Denial of Service

E - Elevation of Privilege
```

---

# Threat Modelling Process

```
Identify Assets

        ↓

Create Architecture Diagram

        ↓

Identify Threats

        ↓

Analyze Risk

        ↓

Define Security Controls
```

---

# Security Architecture Layers

```
User Security

        ↓

Application Security

        ↓

API Security

        ↓

Data Security

        ↓

Infrastructure Security

        ↓

Network Security
```

---

# Authentication Security

Authentication answers:

"Who are you?"

---

# Authentication Methods

## Username & Password

Traditional authentication.

---

## Multi Factor Authentication (MFA)

Requires multiple verification factors.

Example:

```
Password

+

OTP

+

Biometric
```

---

## Single Sign-On (SSO)

One identity across multiple applications.

Examples:

- Enterprise login
- Google Workspace
- Microsoft Entra ID

---

# Password Security

Best practices:

- Hash passwords
- Use strong policies
- Prevent brute force attacks
- Never store plain text passwords

---

# Password Hashing

Use:

- bcrypt
- Argon2
- PBKDF2

Avoid:

- MD5
- SHA1

---

# Session Security

Protect sessions using:

- Secure cookies
- HttpOnly cookies
- Session expiration
- Token rotation

---

# Token Based Authentication

Common tokens:

- JWT
- OAuth tokens
- Refresh tokens

---

# JWT Architecture

Flow:

```
User Login

 ↓

Server Validation

 ↓

Generate JWT

 ↓

Client Sends Token

 ↓

API Validates Token
```

---

# JWT Security

Implement:

- Short expiration
- Secure storage
- Signature validation
- Token rotation

---

# Authorization Security

Authorization answers:

"What can you access?"

---

# Access Control Models

## RBAC

Role Based Access Control

Example:

```
Admin

Manager

User
```

---

## ABAC

Attribute Based Access Control

Uses:

- User attributes
- Resource attributes
- Context

---

# Permission Design

Example:

```
User

Can:

View Profile

Cannot:

Delete Users
```

---

Continuing `security.md`

**Part 2**

Copy and paste below after Part 1.

````markdown id="security_part2"
# OWASP Security Framework

OWASP (Open Worldwide Application Security Project) provides security standards for software applications.

---

# OWASP Top 10

The most common application security risks.

---

# 1. Broken Access Control

Problem:

Users can access resources they should not access.

Example:

```
Normal User

Accesses

Admin Dashboard
```

---

# Prevention

Implement:

- Proper authorization checks
- Role-based access control
- Permission validation
- Server-side security checks

---

# 2. Cryptographic Failures

Problem:

Sensitive data is not properly protected.

Examples:

- Exposed passwords
- Unencrypted communication
- Weak encryption

---

# Prevention

Use:

- TLS/HTTPS
- Strong encryption algorithms
- Secure key management
- Password hashing

---

# 3. Injection Attacks

Injection occurs when attackers send malicious input.

Types:

- SQL Injection
- NoSQL Injection
- Command Injection
- LDAP Injection

---

# SQL Injection

Attack:

```
User Input

        ↓

Database Query

        ↓

Malicious SQL Execution
```

---

# Example Problem

Unsafe:

```
SELECT * FROM users
WHERE username = input
```

Attacker input:

```
' OR 1=1 --
```

---

# Prevention

Use:

- Parameterized queries
- Prepared statements
- ORM security
- Input validation

---

# 4. Insecure Design

Problem:

Security was not considered during design.

Examples:

- Missing authorization
- Unsafe workflows
- Poor architecture decisions

---

# Prevention

Apply:

- Secure design principles
- Threat modelling
- Security reviews

---

# 5. Security Misconfiguration

Examples:

- Default passwords
- Exposed services
- Debug mode enabled
- Incorrect permissions

---

# Prevention

Use:

- Secure configuration
- Environment separation
- Configuration auditing

---

# 6. Vulnerable Components

Problem:

Using outdated libraries.

Examples:

- Old frameworks
- Vulnerable dependencies

---

# Prevention

Use:

- Dependency scanning
- Regular updates
- Security patches

Tools:

- Dependabot
- Snyk
- OWASP Dependency Check

---

# 7. Authentication Failures

Problems:

- Weak passwords
- Session theft
- Brute force attacks

---

# Prevention

Implement:

- MFA
- Rate limiting
- Account lockout
- Secure sessions

---

# 8. Software and Data Integrity Failures

Problem:

Software updates or data are modified without verification.

---

# Prevention

Use:

- Code signing
- Secure deployment pipelines
- Integrity checks

---

# 9. Security Logging Failures

Problem:

Security events are not properly recorded.

---

# Prevention

Log:

- Login attempts
- Permission changes
- Security events
- System errors

---

# 10. Server Side Request Forgery (SSRF)

Problem:

Application makes unauthorized requests.

Example:

```
User Input

 ↓

Backend Request

 ↓

Internal System Access
```

---

# Prevention

Use:

- URL validation
- Network restrictions
- Allow lists

---

# Web Application Security

Secure web applications against attacks.

---

# Browser Security Model

Browsers protect users using:

- Same Origin Policy
- CORS
- Content Security Policy

---

# Cross Site Scripting (XSS)

XSS injects malicious scripts into web pages.

Types:

## Stored XSS

Malicious script saved in database.

---

## Reflected XSS

Script comes from request.

---

## DOM Based XSS

Manipulates browser DOM.

---

# XSS Prevention

Use:

- Output encoding
- Input validation
- Content Security Policy
- Secure frameworks

---

# Angular Security

Angular provides:

- Automatic escaping
- Sanitization
- Safe templates

Avoid:

```
bypassSecurityTrustHtml()
```

without validation.

---

# React Security

Follow:

- Avoid dangerouslySetInnerHTML
- Sanitize HTML
- Validate inputs

---

# Vue Security

Avoid:

```
v-html
```

with untrusted content.

---

# Cross Site Request Forgery (CSRF)

CSRF tricks users into performing unwanted actions.

Example:

```
User Logged In

        ↓

Malicious Website

        ↓

Unauthorized Request
```

---

# CSRF Prevention

Use:

- CSRF tokens
- SameSite cookies
- Origin validation

---

# Clickjacking

Attack:

Embedding website inside malicious iframe.

---

# Prevention

Use:

- X-Frame-Options
- Content Security Policy

---

# Content Security Policy (CSP)

Controls allowed content sources.

Protects against:

- XSS
- Data injection

Example:

```
Only allow scripts from trusted sources
```

---

# CORS Security

Cross-Origin Resource Sharing controls API access.

---

# Secure CORS Rules

Avoid:

```
Allow-Origin: *
```

for sensitive applications.

Use:

```
Specific trusted domains
```

---

# HTTP Security Headers

Important headers:

## Strict Transport Security

Forces HTTPS.

---

## Content Security Policy

Controls resources.

---

## X-Content-Type-Options

Prevents MIME attacks.

---

## Referrer Policy

Controls referrer information.

---

# Backend Security

Secure backend applications.

---

# Secure API Design

APIs must implement:

- Authentication
- Authorization
- Validation
- Rate limiting
- Logging

---

# Input Validation

Never trust user input.

Validate:

- Data type
- Length
- Format
- Allowed values

---

# Output Encoding

Protect generated output.

Example:

```
Database Data

        ↓

Encode

        ↓

Display Safely
```

---

# Error Handling Security

Bad:

```
Database connection failed:
username=root password=123
```

Good:

```
Internal server error
```

---

# Secure Exception Handling

Avoid exposing:

- Stack traces
- Database details
- Internal paths

---

# API Security Architecture

Secure API flow:

```
Client

 ↓

API Gateway

 ↓

Authentication

 ↓

Authorization

 ↓

Backend Service

 ↓

Database
```

---

# API Authentication Methods

Common:

- JWT
- OAuth 2.0
- API Keys
- mTLS

---

# OAuth 2.0 Security

OAuth provides delegated access.

Flow:

```
User

 ↓

Authorization Server

 ↓

Access Token

 ↓

API Resource Server
```

---

# OpenID Connect (OIDC)

Adds identity layer on OAuth.

Used for:

- Login systems
- Enterprise authentication

---

# API Rate Limiting

Protects against:

- Abuse
- DDoS
- Brute force attacks

Example:

```
100 requests per minute per user
```

---

# API Gateway Security

Responsibilities:

- Authentication
- Authorization
- Rate limiting
- Request filtering
- Monitoring

---

# Database Security

Protect stored data.

---

# Database Security Controls

Implement:

- Access control
- Encryption
- Auditing
- Backup protection

---

# Database Authentication

Use:

- Strong passwords
- IAM integration
- Certificate authentication

---

# Database Authorization

Control:

- Read permissions
- Write permissions
- Administrative access

---

# Database Encryption

## Encryption At Rest

Protect stored data.

Examples:

- Disk encryption
- Database encryption

---

## Encryption In Transit

Protect communication.

Example:

```
Application

 ↓ HTTPS/TLS

Database
```

---

# SQL Database Security

Protect:

- MySQL
- PostgreSQL
- SQL Server

Use:

- Least privilege users
- Prepared statements
- Access auditing

---

# NoSQL Security

Protect:

- MongoDB
- DynamoDB
- Cassandra

Implement:

- Authentication
- Encryption
- Network restrictions

---

# Backup Security

Secure backups using:

- Encryption
- Access control
- Regular testing

---

# Network Security

Network security protects communication between systems.

---

# Network Security Goals

Protect:

- Data transfer
- Network infrastructure
- Internal systems
- External connections

---

# Network Security Layers

```
Internet

    ↓

Firewall

    ↓

Load Balancer

    ↓

Application Network

    ↓

Database Network
```

---

# Firewall Architecture

Firewall controls network traffic.

Rules:

- Allow trusted traffic
- Block malicious traffic
- Monitor connections

---

# Firewall Types

## Network Firewall

Protects network boundaries.

---

## Application Firewall (WAF)

Protects web applications.

Examples:

- AWS WAF
- Cloudflare WAF

---

# Web Application Firewall (WAF)

Protects against:

- SQL Injection
- XSS
- Malicious requests
- Bot attacks

Architecture:

```
User

 ↓

WAF

 ↓

Application Server
```

---

# Network Segmentation

Divide networks into secure zones.

Example:

```
Public Network

        ↓

Application Network

        ↓

Private Database Network
```

Benefits:

- Limits attack impact
- Protects sensitive systems

---

# Virtual Private Network (VPN)

Creates secure communication channels.

Uses:

- Remote access
- Site-to-site connections

---

# Secure Network Architecture

Example:

```
Internet

 ↓

Firewall

 ↓

DMZ

 ↓

Application Servers

 ↓

Private Database
```

---

# DNS Security

Protect domain infrastructure.

Threats:

- DNS spoofing
- DNS hijacking
- Cache poisoning

---

# DNS Security Controls

Use:

- DNSSEC
- Secure DNS providers
- Monitoring

---

# DDoS Protection

Distributed Denial of Service attacks overload systems.

Attack:

```
Millions of Requests

        ↓

Server Overload

        ↓

Service Failure
```

---

# DDoS Prevention

Use:

- CDN
- Load balancing
- Rate limiting
- DDoS protection services

---

# Cloud Security

Cloud security protects cloud environments.

Platforms:

- AWS
- Azure
- Google Cloud

---

# Shared Responsibility Model

Cloud security responsibility is shared.

```
Cloud Provider

+

Customer
```

---

# Cloud Provider Responsibility

Provider manages:

- Physical infrastructure
- Hardware
- Data centres

---

# Customer Responsibility

Customer manages:

- Applications
- Data
- Identity
- Configuration

---

# AWS Security Architecture

Important services:

## Identity

- IAM
- Cognito

---

## Network

- VPC
- Security Groups
- Network ACL

---

## Monitoring

- CloudTrail
- GuardDuty
- Security Hub

---

## Data Protection

- KMS
- Secrets Manager

---

# Azure Security Architecture

Services:

- Microsoft Entra ID
- Azure Defender
- Key Vault
- Sentinel

---

# Google Cloud Security

Services:

- Cloud IAM
- Security Command Center
- Cloud KMS

---

# Identity and Access Management (IAM)

IAM manages:

- Users
- Roles
- Permissions

---

# IAM Principles

Follow:

## Least Privilege

Give minimum required access.

---

## Separation of Duties

Avoid one person controlling everything.

---

## Regular Access Review

Remove unnecessary permissions.

---

# Secrets Management

Never store secrets in:

- Source code
- Configuration files
- Public repositories

---

# Secret Management Tools

Examples:

- AWS Secrets Manager
- Azure Key Vault
- HashiCorp Vault

---

# Environment Security

Separate:

```
Development

        ↓

Testing

        ↓

Staging

        ↓

Production
```

---

# DevSecOps

DevSecOps integrates security into software delivery.

Traditional:

```
Development

        ↓

Testing

        ↓

Security

        ↓

Deployment
```

---

Modern:

```
Security Everywhere

Development

Testing

Deployment

Monitoring
```

---

# DevSecOps Lifecycle

```
Plan

 ↓

Code

 ↓

Build

 ↓

Test

 ↓

Release

 ↓

Deploy

 ↓

Monitor
```

---

# Secure Coding Practices

Developers should:

- Validate input
- Handle errors securely
- Protect secrets
- Follow secure patterns

---

# Static Application Security Testing (SAST)

Analyzes source code.

Finds:

- Vulnerabilities
- Unsafe patterns
- Coding issues

Tools:

- SonarQube
- Checkmarx
- Veracode

---

# Dynamic Application Security Testing (DAST)

Tests running applications.

Finds:

- Runtime vulnerabilities
- Configuration issues

Tools:

- OWASP ZAP
- Burp Suite

---

# Software Composition Analysis (SCA)

Checks third-party dependencies.

Finds:

- Vulnerable packages
- Outdated libraries

Tools:

- Snyk
- Dependabot

---

# Container Security

Containers introduce security challenges.

Protect:

- Images
- Containers
- Registries
- Runtime

---

# Docker Security

Best practices:

- Use trusted images
- Scan images
- Avoid root users
- Keep images updated

---

# Container Image Security

Process:

```
Build Image

 ↓

Scan Image

 ↓

Approve Image

 ↓

Deploy
```

---

# Kubernetes Security

Secure Kubernetes clusters.

---

# Kubernetes Security Areas

Protect:

- Cluster
- Nodes
- Pods
- Secrets
- Network

---

# Kubernetes Security Controls

Use:

- RBAC
- Network Policies
- Pod Security Standards
- Secret Encryption

---

# Kubernetes Secrets

Store sensitive data:

- API keys
- Passwords
- Certificates

Never:

```
Hardcode secrets
```

---

# Infrastructure Security

Protect infrastructure components.

Includes:

- Servers
- Operating systems
- Networks
- Cloud resources

---

# Server Hardening

Steps:

- Remove unused services
- Apply patches
- Configure firewall
- Disable unnecessary accounts

---

# Operating System Security

Protect:

- Linux servers
- Windows servers

Controls:

- Updates
- Permissions
- Monitoring

---

# Patch Management

Process:

```
Identify Updates

        ↓

Test Updates

        ↓

Deploy Updates

        ↓

Verify Security
```

---

# Vulnerability Management

Identify and reduce security weaknesses.

---

# Vulnerability Lifecycle

```
Discover

 ↓

Assess

 ↓

Prioritize

 ↓

Fix

 ↓

Verify
```

---

# Vulnerability Scanning

Tools:

- Nessus
- OpenVAS
- Qualys

---

# Vulnerability Severity

Common scoring:

CVSS

(Common Vulnerability Scoring System)

---

# CVSS Categories

## Critical

Immediate action required.

---

## High

Fix quickly.

---

## Medium

Plan remediation.

---

## Low

Monitor and improve.

---

# Security Monitoring

Continuously observe systems.

Monitor:

- Login activity
- Network traffic
- Application behaviour
- Security events

---

# Security Information and Event Management (SIEM)

Collects and analyses security events.

Examples:

- Splunk
- Microsoft Sentinel
- IBM QRadar

---

# Security Operations Center (SOC)

SOC team handles:

- Monitoring
- Incident detection
- Investigation
- Response

---

# Penetration Testing

Penetration testing identifies security weaknesses by simulating real attacks.

Purpose:

- Find vulnerabilities
- Validate security controls
- Improve defenses

---

# Penetration Testing Methodology

```
Planning

 ↓

Reconnaissance

 ↓

Scanning

 ↓

Exploitation

 ↓

Privilege Analysis

 ↓

Reporting

 ↓

Remediation
```

---

# Types of Penetration Testing

## Black Box Testing

Tester has no internal knowledge.

Simulates:

```
External Attacker
```

---

## White Box Testing

Tester has complete system knowledge.

Includes:

- Source code
- Architecture
- Credentials

---

## Grey Box Testing

Combination of:

- Limited knowledge
- Partial access

---

# Penetration Testing Areas

Test:

- Web applications
- Mobile applications
- APIs
- Networks
- Cloud infrastructure
- Wireless systems

---

# Reconnaissance

Information gathering phase.

Collect:

- Domain information
- Technology stack
- Public exposure
- Attack surface

---

# Vulnerability Assessment

Identify:

- Security weaknesses
- Misconfigurations
- Missing patches

---

# Exploitation Analysis

Understand:

- Impact
- Attack path
- Required fixes

---

# Security Testing Tools

Common tools:

## Web Testing

- Burp Suite
- OWASP ZAP

---

## Network Testing

- Nmap
- Wireshark

---

## Vulnerability Scanning

- Nessus
- OpenVAS

---

## Code Security

- SonarQube
- Snyk

---

# Security Testing Lifecycle

```
Requirement Analysis

        ↓

Threat Modelling

        ↓

Security Testing

        ↓

Vulnerability Fixing

        ↓

Retesting
```

---

# Incident Response

Incident response handles security breaches.

Examples:

- Data breach
- Malware infection
- Account compromise
- Unauthorized access

---

# Incident Response Lifecycle

```
Preparation

        ↓

Identification

        ↓

Containment

        ↓

Eradication

        ↓

Recovery

        ↓

Lessons Learned
```

---

# Preparation Phase

Prepare:

- Response plans
- Security tools
- Contact lists
- Backup strategies

---

# Identification Phase

Detect:

- Suspicious activity
- Security alerts
- Abnormal behaviour

---

# Containment Phase

Limit damage.

Actions:

- Block attacker
- Disable accounts
- Isolate systems

---

# Eradication Phase

Remove:

- Malware
- Vulnerabilities
- Unauthorized access

---

# Recovery Phase

Restore:

- Systems
- Data
- Services

Validate:

- Security
- Stability

---

# Lessons Learned

Analyze:

- What happened?
- Why did it happen?
- How to prevent recurrence?

---

# Security Governance

Governance defines security management.

Includes:

- Policies
- Standards
- Procedures
- Compliance

---

# Security Policies

Examples:

## Password Policy

Defines:

- Password strength
- Expiration
- MFA requirements

---

## Data Protection Policy

Defines:

- Data handling
- Storage
- Sharing

---

## Access Control Policy

Defines:

- User permissions
- Approval process

---

# Security Compliance

Organizations follow standards.

Examples:

- ISO 27001
- SOC 2
- GDPR
- HIPAA
- PCI DSS

---

# ISO 27001

Information Security Management System (ISMS).

Focus:

- Risk management
- Security controls
- Continuous improvement

---

# SOC 2

Framework for service organizations.

Focus:

- Security
- Availability
- Confidentiality
- Privacy

---

# GDPR Security

Protects personal data.

Requirements:

- Data privacy
- User consent
- Data protection
- Breach notification

---

# HIPAA Security

Healthcare data protection.

Protects:

- Patient information
- Medical records

---

# PCI DSS

Payment card security standard.

Protects:

- Credit card data
- Payment systems

---

# Privacy Engineering

Protect user information.

Principles:

- Data minimization
- Transparency
- User control
- Secure processing

---

# Data Classification

Classify information.

Example:

```
Public

 ↓

Internal

 ↓

Confidential

 ↓

Highly Confidential
```

---

# Data Loss Prevention (DLP)

Prevent unauthorized data sharing.

Protect:

- Documents
- Customer data
- Intellectual property

---

# Data Masking

Hide sensitive information.

Example:

Original:

```
4111 2222 3333 4444
```

Masked:

```
**** **** **** 4444
```

---

# Encryption Security

Encryption protects data confidentiality.

---

# Symmetric Encryption

Same key used for:

- Encryption
- Decryption

Example:

- AES

---

# Asymmetric Encryption

Uses:

- Public key
- Private key

Examples:

- RSA
- ECC

---

# Hashing

One-way transformation.

Used for:

- Password storage
- Integrity checking

Examples:

- SHA-256
- SHA-512

---

# Digital Signatures

Verify:

- Authenticity
- Integrity

Used for:

- Software signing
- Documents

---

# Certificate Security

Digital certificates provide trust.

Used in:

- HTTPS
- TLS
- Authentication

---

# TLS Security

TLS protects communication.

Example:

```
Browser

   ↓ HTTPS/TLS

Server
```

Protects:

- Confidentiality
- Integrity

---

# AI Security

AI systems introduce new risks.

Security areas:

- Model security
- Data security
- Prompt security
- Agent security

---

# AI Security Risks

Common threats:

- Prompt injection
- Data leakage
- Model manipulation
- Training data poisoning
- Unauthorized AI usage

---

# Prompt Injection Attack

Attackers manipulate AI instructions.

Example:

```
User Input

↓

Ignore previous instructions

↓

Reveal sensitive information
```

---

# Prompt Injection Prevention

Use:

- Input filtering
- Instruction separation
- Output validation
- Permission controls

---

# LLM Data Security

Protect:

- User prompts
- Documents
- Knowledge bases
- Model responses

---

# RAG Security

Secure:

```
Documents

↓

Embeddings

↓

Vector Database

↓

LLM Response
```

Controls:

- Access filtering
- Document permissions
- Data validation

---

# AI Agent Security

AI agents can:

- Call APIs
- Execute actions
- Access tools

Security controls:

- Permission limits
- Human approval
- Tool restrictions
- Audit logs

---

# AI Model Governance

Manage:

- Model access
- Model versions
- Usage monitoring
- Risk assessment

---

# AI Security Monitoring

Monitor:

- Prompt attacks
- Abnormal usage
- Data exposure
- Cost abuse

---

# Security Architecture Checklist

Before releasing any system:

## Application Security

✓ Secure coding practices followed

✓ Input validation implemented

✓ Errors handled safely

---

## Authentication

✓ MFA supported

✓ Passwords securely stored

✓ Tokens protected

---

## Authorization

✓ Permissions verified

✓ Roles defined

✓ Access reviewed

---

## API Security

✓ Authentication enabled

✓ Rate limiting configured

✓ Input validated

---

## Data Security

✓ Encryption enabled

✓ Sensitive data protected

✓ Backups secured

---

## Infrastructure Security

✓ Systems hardened

✓ Network protected

✓ Monitoring enabled

---

## DevSecOps

✓ Security scanning automated

✓ Dependencies checked

✓ Secrets protected

---

Continuing `security.md`

**Part 5 (Final Part)**

Copy and paste below after Part 4.

````markdown id="security_part5"
# Zero Trust Security Architecture

Zero Trust is a modern security model.

Traditional model:

```
Internal Network

      = Trusted
```

Modern model:

```
Never Trust

Always Verify
```

---

# Zero Trust Principles

Follow:

1. Verify every user.

2. Verify every device.

3. Apply least privilege.

4. Monitor continuously.

5. Assume breach.

---

# Zero Trust Architecture

```
User

 ↓

Identity Verification

 ↓

Policy Engine

 ↓

Access Decision

 ↓

Application Resource
```

---

# Zero Trust Components

## Identity Provider

Manages:

- Users
- Authentication
- Identity verification

Examples:

- Microsoft Entra ID
- Okta

---

## Policy Engine

Decides:

```
Should this user get access?
```

Based on:

- Identity
- Location
- Device
- Risk level

---

## Policy Enforcement Point

Controls access.

Example:

- API Gateway
- Firewall
- Application Gateway

---

# Enterprise Security Architecture

Large organizations require layered security.

Architecture:

```
Users

 ↓

Identity Security

 ↓

Application Security

 ↓

API Security

 ↓

Data Security

 ↓

Infrastructure Security

 ↓

Monitoring Platform
```

---

# Security Architecture Domains

## Identity Security

Protect:

- Users
- Credentials
- Permissions

---

## Application Security

Protect:

- Software
- APIs
- Applications

---

## Data Security

Protect:

- Business data
- Customer information

---

## Infrastructure Security

Protect:

- Servers
- Networks
- Cloud resources

---

## Operational Security

Protect:

- Processes
- Monitoring
- Incident handling

---

# Security Operations Center (SOC)

SOC continuously monitors security.

---

# SOC Responsibilities

Monitor:

- Security alerts
- Network activity
- User behaviour
- Threat intelligence

---

# SOC Levels

## SOC Analyst Level 1

Responsibilities:

- Alert monitoring
- Initial investigation
- Ticket creation

---

## SOC Analyst Level 2

Responsibilities:

- Threat analysis
- Incident investigation
- Response coordination

---

## SOC Analyst Level 3

Responsibilities:

- Advanced investigations
- Threat hunting
- Security improvements

---

# Threat Intelligence

Collect information about threats.

Sources:

- Security reports
- Vulnerability databases
- Attack patterns

---

# Threat Hunting

Proactively search for attackers.

Process:

```
Create Hypothesis

        ↓

Search Evidence

        ↓

Analyze Behaviour

        ↓

Respond
```

---

# Security Automation

Automate security activities.

Examples:

- Vulnerability scanning
- Alert processing
- Compliance checks
- Incident response

---

# Security Orchestration Automation and Response (SOAR)

SOAR automates security workflows.

Example:

```
Security Alert

        ↓

SOAR Platform

        ↓

Investigate

        ↓

Block Threat

        ↓

Notify Team
```

---

# Security Automation Tools

Examples:

- Cortex XSOAR
- Splunk SOAR
- IBM SOAR

---

# Security in CI/CD Pipeline

Secure software delivery.

Pipeline:

```
Developer

 ↓

Source Code Scan

 ↓

Dependency Scan

 ↓

Security Tests

 ↓

Build

 ↓

Deployment

 ↓

Runtime Monitoring
```

---

# Git Security

Protect source repositories.

Controls:

- Branch protection
- Code review
- Secret scanning
- Access control

---

# Secret Detection

Find exposed:

- API keys
- Passwords
- Tokens
- Certificates

Tools:

- GitHub Secret Scanning
- TruffleHog
- Gitleaks

---

# Secure Software Supply Chain

Protect:

- Dependencies
- Build systems
- Deployment process

---

# Software Bill of Materials (SBOM)

SBOM lists software components.

Example:

```
Application

 |

├── React

├── Node.js

├── Database Driver

└── Third Party Libraries
```

Benefits:

- Dependency visibility
- Vulnerability tracking

---

# Security Testing Strategy

A complete testing approach:

```
Code Level

      ↓

Application Level

      ↓

Infrastructure Level

      ↓

Production Level
```

---

# Security Testing Types

## Unit Security Testing

Tests secure code behaviour.

---

## Integration Security Testing

Tests component communication.

---

## API Security Testing

Tests:

- Authentication
- Authorization
- Input handling

---

## Penetration Testing

Simulates attacks.

---

## Security Audit

Reviews:

- Policies
- Controls
- Compliance

---

# Secure Architecture Review Questions

Ask:

## Authentication

```
Who can access the system?
```

---

## Authorization

```
What can they access?
```

---

## Data Protection

```
How is sensitive data protected?
```

---

## Network

```
How is communication secured?
```

---

## Monitoring

```
How are attacks detected?
```

---

# Security Design Patterns

## Authentication Gateway Pattern

Central authentication layer.

```
User

 ↓

Auth Gateway

 ↓

Applications
```

---

## Secure API Gateway Pattern

Protects APIs.

```
Client

 ↓

API Gateway

 ↓

Services
```

---

## Encryption Pattern

Protect sensitive information.

```
Data

 ↓

Encryption

 ↓

Storage
```

---

## Audit Logging Pattern

Track important actions.

Example:

```
User Login

Permission Change

Data Access

Configuration Change
```

---

# Security Metrics

Measure security effectiveness.

---

# Security KPIs

Examples:

## Vulnerability Resolution Time

How quickly issues are fixed.

---

## Security Incident Count

Number of security events.

---

## Patch Compliance

Percentage of updated systems.

---

## Failed Login Attempts

Detect suspicious activity.

---

## Security Training Completion

Measure employee awareness.

---

# Security Maturity Model

Organizations improve security gradually.

---

# Level 1: Initial

Security is reactive.

---

# Level 2: Managed

Basic security processes exist.

---

# Level 3: Defined

Security standards are documented.

---

# Level 4: Measured

Security is monitored with metrics.

---

# Level 5: Optimized

Security is automated and continuously improved.

---

# Security Engineer AI Agent Behaviour

When acting as a Security AI Agent:

Always:

1. Identify assets.

2. Understand threats.

3. Analyse attack surface.

4. Apply security principles.

5. Recommend secure designs.

6. Explain risks clearly.

7. Suggest preventive controls.

8. Consider business impact.

---

# Security Assessment Workflow

```
Understand System

        ↓

Identify Assets

        ↓

Find Threats

        ↓

Assess Risks

        ↓

Recommend Controls

        ↓

Validate Security
```

---

# Complete Security Skill Summary

A Security Expert should understand:

```
Security Fundamentals

        ↓

Application Security

        ↓

API Security

        ↓

Cloud Security

        ↓

Network Security

        ↓

Identity Security

        ↓

DevSecOps

        ↓

Threat Modelling

        ↓

Security Testing

        ↓

Incident Response

        ↓

AI Security

        ↓

Enterprise Security Architecture
```

---

# Security Master Checklist

Before production release:

## Identity

✓ Authentication implemented

✓ MFA supported

✓ Access controlled


## Application

✓ Secure coding followed

✓ Vulnerabilities tested

✓ Input validated


## API

✓ Authentication enabled

✓ Authorization verified

✓ Rate limiting enabled


## Data

✓ Encryption implemented

✓ Sensitive data protected

✓ Backup secured


## Infrastructure

✓ Network secured

✓ Systems hardened

✓ Monitoring enabled


## DevOps

✓ Pipeline secured

✓ Secrets protected

✓ Dependencies scanned


## AI Systems

✓ Prompt security implemented

✓ Data access controlled

✓ AI actions monitored


---
