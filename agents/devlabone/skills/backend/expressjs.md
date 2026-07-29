---
name: expressjs
description: Complete Express.js backend development skill covering Express framework architecture, routing, middleware, REST API development, authentication, validation, error handling, database integration, security, testing, performance optimization, and enterprise backend application development.
---

# Express.js Skill

# Skill Instructions

You are an expert Express.js backend engineer.

Your responsibility is to design, develop, review, debug, optimize, secure, and maintain production-ready Express.js backend applications.

You must think like:

- Senior Express.js Developer
- Backend Architect
- API Engineer
- Node.js Expert
- Security Engineer
- Database Engineer
- Cloud Engineer
- Code Reviewer

Always generate:

- Clean Express architecture
- Scalable API designs
- Secure middleware systems
- Maintainable backend code
- Production-ready solutions
- Industry best practices

---

# Express.js Overview

Express.js is a lightweight and flexible Node.js web application framework used to build:

- REST APIs
- Web applications
- Backend services
- Microservices
- Authentication systems
- Real-time applications

Express provides:

- Routing
- Middleware support
- Request handling
- Response handling
- API development structure

---

# Express.js Core Concepts

Master:

- Express application
- Routing
- Middleware
- Request object
- Response object
- Router modules
- Controllers
- Error handling
- Configuration
- Security

---

# Express.js Architecture

Understand Express request flow.

```
Client Request

        |

Express Application

        |

Middleware Stack

        |

Router

        |

Controller

        |

Service Layer

        |

Database

        |

Response
```

---

# Express Application Setup

Install Express:

```bash
npm install express
```

TypeScript support:

```bash
npm install @types/express --save-dev
```

---

# Basic Express Server

Example:

```javascript
const express =
require("express");

const app =
express();

app.listen(3000);
```

---

# Express Application Object

Master:

```javascript
express()
```

Responsibilities:

- Configure application
- Register middleware
- Define routes
- Start server

---

# Express Middleware Architecture

Middleware is a function that executes during request processing.

Flow:

```
Request

 |

Middleware 1

 |

Middleware 2

 |

Controller

 |

Response
```

---

# Middleware Function Structure

Example:

```javascript
function middleware(
req,
res,
next
){

next();

}
```

---

# Middleware Types

Master:

## Application Middleware

Applied globally.

Example:

```javascript
app.use(
middleware
);
```

---

## Router Middleware

Applied to specific routes.

Example:

```javascript
router.use(
middleware
);
```

---

## Error Middleware

Handles application errors.

Example:

```javascript
(err,req,res,next)=>{

}
```

---

## Built-in Middleware

Express provides:

- express.json()
- express.urlencoded()
- express.static()

---

# JSON Middleware

Parse JSON request bodies.

Example:

```javascript
app.use(
express.json()
);
```

---

# URL Encoded Middleware

Handle form data.

Example:

```javascript
app.use(
express.urlencoded({
extended:true
})
);
```

---

# Static File Middleware

Serve files.

Example:

```javascript
app.use(
express.static("public")
);
```

---

# Custom Middleware Development

Create reusable middleware.

Examples:

- Authentication middleware
- Logging middleware
- Validation middleware
- Permission middleware
- Error middleware

---

# Request Object

Master Express request object.

Common properties:

```javascript
req.body

req.params

req.query

req.headers

req.cookies

req.user
```

---

# Request Parameters

Example:

Route:

```
GET /users/:id
```

Access:

```javascript
req.params.id
```

---

# Query Parameters

Example:

```
GET /users?page=1
```

Access:

```javascript
req.query.page
```

---

# Request Headers

Access:

```javascript
req.headers
```

Used for:

- Authorization tokens
- Content type
- Custom headers

---

# Response Object

Master response handling.

Common methods:

```javascript
res.send()

res.json()

res.status()

res.redirect()

res.download()
```

---

# JSON Response Design

Preferred:

```javascript
res.status(200)
.json({

success:true,

data:user

});
```

---

# Express Routing

Master route design.

Structure:

```
routes/

├── user.routes.js

├── product.routes.js

├── auth.routes.js

└── order.routes.js
```

---

# Basic Route Creation

Example:

```javascript
app.get(
"/users",
(req,res)=>{

res.json([]);

});
```

---

# Express Router

Create modular routes.

Example:

```javascript
const router =
express.Router();
```

---

# Router Pattern

Architecture:

```
Route

 |

Controller

 |

Service

 |

Repository
```

---

# REST API Development

Build professional REST APIs.

Understand:

- Resources
- HTTP methods
- Status codes
- API contracts
- Versioning

---

# HTTP Methods

GET:

Retrieve resources

POST:

Create resources

PUT:

Replace resources

PATCH:

Update resources

DELETE:

Remove resources

---

# REST API Naming Standards

Good:

```
GET /users

POST /users

GET /users/10

PATCH /users/10

DELETE /users/10
```

Avoid:

```
/getUsers

/createUser

/deleteUser
```

---

# API Versioning

Implement:

```
/api/v1/users

/api/v2/users
```

Benefits:

- Backward compatibility
- Safe API evolution
- Multiple client support

---

# Controller Layer

Controllers handle:

- HTTP requests
- Input extraction
- Calling services
- Sending responses

Controllers should not contain:

- Database queries
- Complex business logic

---

# Controller Example

```javascript
exports.getUsers =
async(req,res)=>{

const users =
await userService.getUsers();

res.json(users);

}
```

---

# Service Layer

Services contain business logic.

Responsibilities:

- Business rules
- Data processing
- External integrations

Example:

```
UserService

OrderService

PaymentService
```

---

# Repository Layer

Repository handles data access.

Responsibilities:

- Database queries
- Data mapping
- Persistence operations

---

# Express Error Handling

Master centralized error management.

Flow:

```
Controller

 |

Throw Error

 |

Error Middleware

 |

Formatted Response
```

---

# Custom Error Classes

Create:

```
AppError

ValidationError

AuthenticationError

NotFoundError
```

---

# Error Middleware

Example:

```javascript
app.use(
(err,req,res,next)=>{

res.status(500)
.json({

message:
err.message

});

});
```

---

# Async Error Handling

Avoid:

```javascript
try/catch
```

everywhere.

Use:

- async wrappers
- centralized handlers

---

# Express Async Handler

Example:

```javascript
const asyncHandler =
(fn)=>(req,res,next)=>{

Promise.resolve(
fn(req,res,next)
)
.catch(next);

}
```

---

````markdown id="zxdz6m"
# Express.js Validation

Master request validation in Express.js applications.

Validation ensures:

- Correct data format
- Secure input handling
- Better API reliability
- Reduced application errors

---

# Validation Architecture

Recommended flow:

```
Client Request

        |

Validation Middleware

        |

Controller

        |

Service

        |

Database
```

---

# Validation Types

Understand:

- Request body validation
- Query parameter validation
- Route parameter validation
- Header validation
- File validation

---

# Validation Libraries

Master:

- Joi
- Zod
- Yup
- express-validator
- class-validator

---

# Joi Validation

Install:

```bash
npm install joi
```

Example:

```javascript
const schema =
Joi.object({

email:
Joi.string()
.email()
.required()

});
```

---

# Zod Validation

Modern TypeScript-friendly validation.

Install:

```bash
npm install zod
```

Example:

```typescript
const userSchema =
z.object({

name:
z.string(),

age:
z.number()

});
```

---

# Validation Middleware

Create reusable validation.

Example:

```javascript
const validate =
(schema)=>
(req,res,next)=>{

const result =
schema.validate(
req.body
);

if(result.error){

return res.status(400)
.json({

message:
"Invalid input"

});

}

next();

}
```

---

# DTO Pattern

Use Data Transfer Objects.

Purpose:

- Define API contracts
- Validate incoming data
- Separate external and internal models

Examples:

```
CreateUserDTO

UpdateUserDTO

LoginDTO

PaymentDTO
```

---

# Authentication in Express.js

Master authentication systems.

Understand:

- JWT authentication
- Session authentication
- OAuth
- API keys
- Multi-factor authentication

---

# Authentication Flow

```
User

 |

Login Request

 |

Validate Credentials

 |

Generate Token

 |

Client Stores Token

 |

Protected API Request

 |

Verify Token

 |

Allow Access
```

---

# JWT Authentication

Master JSON Web Token implementation.

JWT structure:

```
Header

+

Payload

+

Signature
```

---

# JWT Libraries

Install:

```bash
npm install jsonwebtoken
```

TypeScript:

```bash
npm install @types/jsonwebtoken --save-dev
```

---

# JWT Token Generation

Example:

```javascript
jwt.sign(

{
userId:user.id
},

secretKey

);
```

---

# JWT Token Verification

Example:

```javascript
jwt.verify(

token,

secretKey

);
```

---

# JWT Middleware

Create authentication middleware.

Flow:

```
Request

 |

Extract Token

 |

Verify Token

 |

Attach User

 |

Continue Request
```

---

# Authentication Middleware Example

```javascript
function authMiddleware(
req,
res,
next
){

const token =
req.headers.authorization;

verifyToken(token);

next();

}
```

---

# Access Token

Used for:

- API authentication
- Short-term access

Contains:

- User identity
- Roles
- Permissions

---

# Refresh Token

Used for:

- Generating new access tokens
- Maintaining sessions

Best practices:

- Rotate refresh tokens
- Store securely
- Implement expiration

---

# Password Security

Never store plain passwords.

Use:

- bcrypt
- Argon2

---

# Password Hashing

Flow:

```
User Password

 |

Hash Algorithm

 |

Stored Hash

 |

Compare During Login
```

---

# bcrypt Integration

Install:

```bash
npm install bcrypt
```

Example:

```javascript
const hash =
await bcrypt.hash(
password,
10
);
```

---

# Authorization

Authentication:

"Who are you?"

Authorization:

"What can you access?"

---

# Role Based Access Control

Implement RBAC.

Architecture:

```
User

 |

Role

 |

Permissions

 |

Resources
```

---

# Example Roles

```
ADMIN

MANAGER

USER

GUEST
```

---

# Permission System

Create permissions:

```
USER_CREATE

USER_UPDATE

USER_DELETE

REPORT_VIEW
```

---

# Authorization Middleware

Example:

```javascript
function authorize(role){

return(req,res,next)=>{

if(req.user.role!==role){

return res
.status(403)
.send();

}

next();

}

}
```

---

# Cookie Management

Master cookies.

Understand:

- Session cookies
- Secure cookies
- HttpOnly cookies
- SameSite cookies

---

# Cookie Security

Use:

```
httpOnly:true

secure:true

sameSite:"strict"
```

---

# Express Sessions

Master session authentication.

Install:

```bash
npm install express-session
```

---

# Session Architecture

```
User

 |

Login

 |

Session Created

 |

Session ID Stored

 |

Server Session Store
```

---

# Session Storage

Store sessions in:

- Redis
- Database
- Memory (development only)

---

# CORS Configuration

Master Cross-Origin Resource Sharing.

Purpose:

Control which clients can access APIs.

---

# CORS Library

Install:

```bash
npm install cors
```

---

# CORS Configuration

Example:

```javascript
app.use(
cors({

origin:
"https://example.com"

})
);
```

---

# CORS Concepts

Understand:

- Origin
- Methods
- Headers
- Credentials
- Preflight requests

---

# Security Headers

Use Helmet.js.

Install:

```bash
npm install helmet
```

---

# Helmet Protection

Provides:

- Content Security Policy
- XSS protection
- Clickjacking protection
- Secure headers

---

# Rate Limiting

Protect APIs from abuse.

Use:

```bash
npm install express-rate-limit
```

---

# Rate Limiting Strategies

Implement:

- IP based limits
- User based limits
- Route based limits
- Token bucket algorithms

---

# API Protection

Protect against:

- Brute force attacks
- API flooding
- Credential attacks

---

# File Upload Handling

Master file upload systems.

Use cases:

- Profile images
- Documents
- Videos
- Reports

---

# Multer Integration

Install:

```bash
npm install multer
```

---

# File Upload Flow

```
Client

 |

Multipart Request

 |

Multer Middleware

 |

File Validation

 |

Storage

 |

Response
```

---

# File Validation

Validate:

- File type
- File size
- File extension
- Malware risks

---

# File Storage Options

Store files in:

- Local filesystem
- AWS S3
- Azure Blob Storage
- Google Cloud Storage

---

# Image Processing

Libraries:

- Sharp
- Jimp

Operations:

- Resize
- Compress
- Convert format

---

# Express Database Integration

Connect Express with databases.

Supported:

## SQL

- PostgreSQL
- MySQL
- SQL Server

## NoSQL

- MongoDB
- Redis

---

# MongoDB with Express

Common stack:

```
Express

+

Mongoose

+

MongoDB
```

---

# Mongoose Integration

Install:

```bash
npm install mongoose
```

---

# MongoDB Architecture

```
Controller

 |

Service

 |

Repository

 |

Mongoose Model

 |

MongoDB
```

---

# PostgreSQL with Express

Common stack:

```
Express

+

Prisma / Sequelize

+

PostgreSQL
```

---

# ORM Integration

Master:

- Prisma
- Sequelize
- TypeORM
- Knex

---

# Database Error Handling

Handle:

- Connection failures
- Query failures
- Transaction errors
- Timeout errors

---

````markdown id="zxdz6m"
# Express.js Application Architecture

Master enterprise-level Express.js application architecture.

A scalable Express.js application should follow:

- Separation of concerns
- Modular design
- Clean architecture
- Maintainable folder structure
- Independent modules

---

# Recommended Express.js Project Structure

Enterprise structure:

```
backend-api

├── src

│
├── config

│
├── routes

│
├── controllers

│
├── services

│
├── repositories

│
├── models

│
├── middlewares

│
├── validators

│
├── utils

│
├── constants

│
├── errors

│
├── database

│
├── jobs

│
├── events

│
├── tests

│
├── app.js

└── server.js
```

---

# MVC Architecture

Master Model View Controller pattern.

Architecture:

```
Request

 |

Controller

 |

Model

 |

Database

 |

Response
```

---

# Controller Responsibilities

Controllers handle:

- HTTP requests
- Request parameters
- Calling services
- Sending responses

Controllers should NOT handle:

- Database queries
- Business rules
- Complex calculations

---

# Model Responsibilities

Models handle:

- Data structure
- Database schema
- Data validation
- Database communication

---

# Service Layer Architecture

Services contain business logic.

Example:

```
UserService

OrderService

PaymentService

NotificationService
```

---

# Service Layer Responsibilities

Handle:

- Business rules
- Data transformation
- External API calls
- Complex workflows

---

# Repository Pattern

Repository separates database logic.

Architecture:

```
Controller

 |

Service

 |

Repository

 |

Database
```

---

# Repository Benefits

Provides:

- Database abstraction
- Easier testing
- Cleaner services
- Better maintainability

---

# Dependency Injection

Master dependency injection patterns.

Purpose:

Reduce tight coupling.

Example:

Without Dependency Injection:

```
Service

 |

Creates Database Connection
```

With Dependency Injection:

```
Service

 |

Receives Database Connection
```

---

# Dependency Injection Benefits

Provides:

- Better testing
- Flexible architecture
- Code reuse
- Easier maintenance

---

# Configuration Management

Manage application configuration properly.

Handle:

- Environment variables
- Database configuration
- API keys
- Application settings

---

# Config Folder Structure

Example:

```
config

├── database.js

├── environment.js

├── logger.js

└── constants.js
```

---

# Environment Management

Maintain:

```
.env

.env.dev

.env.test

.env.production
```

---

# Express Application Lifecycle

Understand application startup.

Flow:

```
Start Server

 |

Load Configuration

 |

Connect Database

 |

Initialize Middleware

 |

Register Routes

 |

Start Listening

 |

Accept Requests
```

---

# Graceful Shutdown

Handle application shutdown safely.

Shutdown events:

- SIGTERM
- SIGINT

---

# Graceful Shutdown Flow

```
Receive Shutdown Signal

 |

Stop New Requests

 |

Close Connections

 |

Finish Existing Tasks

 |

Exit Process
```

---

# Express Logging

Implement professional logging.

Track:

- API requests
- Errors
- Performance
- Security events

---

# Logging Libraries

Master:

- Winston
- Pino
- Morgan

---

# Request Logging

Capture:

- HTTP method
- URL
- Status code
- Response time
- User information

Example:

```
GET /users

200

120ms
```

---

# Error Logging

Capture:

- Error message
- Stack trace
- Request details
- User context

---

# Performance Optimization

Optimize Express.js applications.

Focus on:

- Middleware performance
- API response time
- Database queries
- Memory usage
- Network efficiency

---

# Middleware Optimization

Avoid:

- Unnecessary middleware
- Heavy synchronous operations
- Duplicate processing

---

# Response Compression

Enable compression.

Benefits:

- Smaller payloads
- Faster API responses

Use:

- gzip
- Brotli

---

# Caching Strategies

Implement caching.

Types:

## Client Side Cache

Browser caching.

---

## Server Side Cache

Application caching.

---

## Database Cache

Query optimization.

---

# Redis Caching with Express

Architecture:

```
Request

 |

Check Redis

 |

Cache Hit

 |

Return Response


Cache Miss

 |

Database Query

 |

Store Cache
```

---

# API Performance Monitoring

Monitor:

- Response time
- Throughput
- Error percentage
- CPU usage
- Memory usage

---

# Express Testing

Master complete Express testing.

Testing types:

- Unit testing
- Integration testing
- API testing
- End-to-end testing

---

# Jest Testing with Express

Install:

```bash
npm install jest --save-dev
```

---

# Supertest API Testing

Install:

```bash
npm install supertest --save-dev
```

---

# API Test Example

```javascript
request(app)

.get("/users")

.expect(200);
```

---

# Testing Controllers

Test:

- Request handling
- Response format
- Error cases
- Validation

---

# Testing Services

Test:

- Business logic
- Data processing
- External integrations

---

# Testing Middleware

Test:

- Authentication
- Authorization
- Validation
- Error handling

---

# Mocking Dependencies

Mock:

- Database
- External APIs
- Third-party services

---

# Express API Documentation

Document APIs using:

- Swagger
- OpenAPI
- Postman

---

# Swagger Integration

Install:

```bash
npm install swagger-ui-express swagger-jsdoc
```

---

# API Documentation Should Include

Document:

- Endpoint description
- Request parameters
- Request body
- Response format
- Authentication
- Error responses

---

# API Response Standards

Maintain consistent responses.

Success:

```json
{
"success":true,
"data":{}
}
```

Error:

```json
{
"success":false,
"message":"Error"
}
```

---

# Express Microservices

Use Express for microservice development.

Architecture:

```
API Gateway

 |

-----------------

User Service

Order Service

Payment Service

-----------------

 |

Databases
```

---

# Microservice Communication

Communication methods:

## Synchronous

- REST API
- GraphQL

## Asynchronous

- RabbitMQ
- Kafka
- Events

---

# API Gateway Pattern

Gateway responsibilities:

- Routing
- Authentication
- Rate limiting
- Logging
- Request transformation

---

# Express with GraphQL

Master GraphQL integration.

Understand:

- Schema
- Queries
- Mutations
- Resolvers

---

# Express GraphQL Architecture

```
Client

 |

GraphQL Endpoint

 |

Resolvers

 |

Services

 |

Database
```

---

# Express with WebSockets

Integrate:

- Socket.IO
- ws library

Use cases:

- Chat
- Notifications
- Real-time updates

---

# Production Deployment

Deploy Express applications professionally.

Platforms:

- AWS
- Azure
- Google Cloud
- Docker
- Kubernetes

---

# Docker Express Deployment

Container flow:

```
Source Code

 |

Docker Image

 |

Container

 |

Production Server
```

---

# Express Docker Best Practices

Follow:

- Use official Node images
- Use environment variables
- Avoid root users
- Reduce image size
- Scan vulnerabilities

---

# CI/CD for Express

Pipeline:

```
Code Commit

 |

Install Dependencies

 |

Lint

 |

Test

 |

Build

 |

Deploy
```

---

# Express Security Checklist

Always implement:

- Helmet
- CORS configuration
- Rate limiting
- Input validation
- Secure cookies
- Authentication
- Authorization
- Dependency scanning

---

# Express Production Checklist

Before deployment:

## Architecture

- Modular structure
- Clean separation
- Error handling

## Security

- Authentication enabled
- Secrets protected
- API secured

## Performance

- Cache configured
- Database optimized
- Monitoring enabled

## Deployment

- Docker ready
- CI/CD configured
- Logging enabled

---

# Express.js AI Agent Rules

The Express.js AI agent must always:

1. Generate modular Express applications.

2. Separate routes, controllers, services, and repositories.

3. Never place business logic inside routes.

4. Always validate user input.

5. Always implement proper error handling.

6. Follow REST API best practices.

7. Consider security for every API.

8. Write scalable middleware.

9. Create production-ready code.

10. Prefer TypeScript for enterprise applications.

11. Include testing strategies.

12. Consider deployment requirements.

---

# Express.js Expert Mindset

Think like:

- Backend Architect
- API Designer
- Security Engineer
- Performance Engineer
- Cloud Engineer

Build Express applications that are:

- Secure
- Scalable
- Maintainable
- Production-ready

---
