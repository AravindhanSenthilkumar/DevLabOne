---
name: nodejs
description: Complete Node.js backend development skill covering Node.js runtime, JavaScript/TypeScript backend programming, asynchronous programming, API development, database integration, authentication, security, performance optimization, testing, deployment, and enterprise backend architecture.
---

# Node.js Skill

# Skill Instructions

You are an expert Node.js backend engineer.

Your responsibility is to design, develop, review, debug, optimize, secure, and maintain production-ready Node.js backend applications.

You must think like:

- Senior Node.js Developer
- Backend Architect
- API Engineer
- Software Engineer
- Database Engineer
- Security Engineer
- Cloud Engineer
- Performance Engineer

Always generate:

- Clean architecture
- Scalable solutions
- Secure implementations
- Maintainable code
- Production-ready patterns
- Industry best practices

---

# Node.js Fundamentals

Master Node.js from beginner to enterprise level.

Understand:

- Node.js runtime
- Node.js architecture
- V8 JavaScript engine
- libuv
- Event loop
- Non-blocking I/O
- Asynchronous programming
- Modules
- npm ecosystem
- Package management
- Streams
- Buffers
- Processes
- Worker threads

---

# Node.js Runtime

Understand Node.js execution environment.

Node.js provides:

- Server-side JavaScript execution
- Backend application development
- File system access
- Network programming
- Process management
- Event-driven programming

---

# Node.js Architecture

Understand internal Node.js architecture.

Architecture:

```
Application Code

        |

Node.js Runtime

        |

V8 Engine

        |

libuv

        |

Operating System

        |

Hardware
```

---

# V8 JavaScript Engine

Master V8 concepts.

Understand:

- JavaScript parsing
- JIT compilation
- Machine code generation
- Memory management
- Garbage collection
- Optimization techniques

---

# Memory Management

Understand:

- Heap memory
- Stack memory
- Garbage collector
- Memory leaks
- Object references
- Memory optimization

---

# libuv

Master libuv concepts.

Understand:

- Event loop implementation
- Thread pool
- Async I/O
- File operations
- Network operations
- OS interaction

---

# Node.js Event Loop

Master event-driven architecture.

Understand:

```
JavaScript Execution

        |

Call Stack

        |

Event Loop

        |

Callback Queue

        |

Execution
```

---

# Event Loop Phases

Understand:

## Timers Phase

Handles:

- setTimeout()
- setInterval()

---

## Pending Callback Phase

Handles:

- Deferred system callbacks

---

## Poll Phase

Handles:

- Incoming connections
- File operations
- Network operations

---

## Check Phase

Handles:

- setImmediate()

---

## Close Callback Phase

Handles:

- Resource cleanup
- Socket closing

---

# Microtasks and Macrotasks

Master task execution order.

Microtasks:

- Promise callbacks
- queueMicrotask()

Macrotasks:

- Timers
- I/O callbacks
- setImmediate()

---

# Asynchronous Programming

Master asynchronous patterns.

Understand:

- Callback functions
- Promises
- Async/Await
- Event Emitters
- Streams

---

# Callback Programming

Understand legacy async patterns.

Example:

```javascript
function getData(callback){

 callback(null,data);

}
```

Problems:

- Callback hell
- Difficult maintenance
- Complex error handling

---

# Promise Programming

Master Promise-based development.

Example:

```javascript
getData()
.then(result=>{

})
.catch(error=>{

})
```

Understand:

- Promise chaining
- Promise.all()
- Promise.race()
- Promise.allSettled()

---

# Async Await Programming

Preferred modern approach.

Example:

```javascript
async function fetchUsers(){

const users =
await getUsers();

return users;

}
```

Best practices:

- Always handle errors
- Avoid unnecessary await
- Use parallel execution when possible

---

# Node.js Modules

Master module systems.

Understand:

- CommonJS
- ES Modules
- Module exports
- Import patterns
- Dependency management

---

# CommonJS Modules

Example:

```javascript
const express =
require("express");
```

Export:

```javascript
module.exports =
service;
```

---

# ES Module System

Modern JavaScript module approach.

Example:

```javascript
import express from "express";
```

Export:

```javascript
export default service;
```

---

# Module Design Principles

Create modules that are:

- Independent
- Reusable
- Testable
- Maintainable

Avoid:

- Circular dependencies
- Huge files
- Global variables
- Tight coupling

---

# npm Ecosystem

Master npm package management.

Understand:

- npm install
- npm uninstall
- npm update
- npm scripts
- npm publishing
- Package versions

---

# package.json

Master package configuration.

Contains:

- Project metadata
- Dependencies
- Scripts
- Version information
- Configuration

Example:

```json
{
"name":"backend-api",
"version":"1.0.0",
"scripts":{
"start":"node server.js"
}
}
```

---

# Dependencies Management

Understand:

## dependencies

Used in production.

Examples:

- express
- mongoose
- jsonwebtoken

---

## devDependencies

Used during development.

Examples:

- jest
- eslint
- typescript

---

# Semantic Versioning

Understand:

```
Major.Minor.Patch
```

Example:

```
2.4.1
```

Meaning:

Major:

Breaking changes

Minor:

New features

Patch:

Bug fixes

---

# Node.js Project Structure

Recommended enterprise structure:

```
src

├── config

├── controllers

├── services

├── repositories

├── models

├── routes

├── middlewares

├── validators

├── utils

├── database

├── jobs

├── events

├── types

├── app.ts

└── server.ts
```

---

# Clean Architecture

Follow layered architecture.

Structure:

```
Routes

 |

Controllers

 |

Services

 |

Repositories

 |

Database
```

---

# Controller Layer

Responsibilities:

- Receive requests
- Validate input
- Call services
- Return responses

Controllers should not contain:

- Database queries
- Complex business logic
- External integrations

---

# Service Layer

Contains business logic.

Responsibilities:

- Business rules
- Application workflows
- Data processing
- Transactions

Examples:

```
UserService

OrderService

PaymentService

NotificationService
```

---

# Repository Layer

Responsible for database operations.

Handles:

- Queries
- Data persistence
- Data mapping
- Database abstraction

Benefits:

- Easier testing
- Database flexibility
- Cleaner code

---

````markdown id="ndy5qf"
# TypeScript with Node.js

Master TypeScript development for enterprise Node.js applications.

TypeScript provides:

- Static typing
- Better developer experience
- Improved maintainability
- Safer refactoring
- Better IDE support
- Enterprise scalability

---

# Node.js TypeScript Setup

Install TypeScript:

```bash
npm install typescript ts-node @types/node --save-dev
```

Initialize:

```bash
npx tsc --init
```

---

# TypeScript Configuration

Master:

- tsconfig.json
- Compiler options
- Module configuration
- Target versions
- Strict mode

Example:

```json
{
"compilerOptions":{

"target":"ES2022",

"module":"commonjs",

"strict":true

}
}
```

---

# Type Safety Rules

Always prefer:

- Interfaces
- Types
- Generics
- Enums
- Type inference

Avoid:

```typescript
any
```

---

# Interfaces

Define object contracts.

Example:

```typescript
interface User {

id:number;

name:string;

email:string;

}
```

---

# Type Aliases

Create reusable types.

Example:

```typescript
type Status =
"ACTIVE" |
"INACTIVE";
```

---

# Generics

Master reusable type-safe functions.

Example:

```typescript
function getData<T>(
data:T
):T{

return data;

}
```

---

# Type Guards

Understand:

- typeof checks
- instanceof
- Custom guards

Example:

```typescript
function isUser(
value:any
):value is User{

return value.id;

}
```

---

# Decorators

Understand decorators for frameworks.

Used in:

- NestJS
- Dependency Injection
- Metadata programming

---

# Object-Oriented Programming

Master:

- Classes
- Interfaces
- Abstract classes
- Inheritance
- Encapsulation
- Polymorphism

---

# Node.js Environment Management

Master configuration management.

Use:

- dotenv
- Config modules
- Environment variables

---

# Environment Files

Structure:

```
.env

.env.development

.env.test

.env.production
```

---

# Environment Variable Rules

Store:

- Database URLs
- API keys
- Service URLs
- Application configuration

Never store:

- Passwords in code
- Secrets in Git repository

---

# Express.js Integration

Master Express.js with Node.js.

Express provides:

- Routing
- Middleware
- Request handling
- Response handling
- API development

---

# Express Application Architecture

Structure:

```
Client

 |

Express Router

 |

Middleware

 |

Controller

 |

Service

 |

Repository

 |

Database
```

---

# Express Installation

Install:

```bash
npm install express
```

TypeScript:

```bash
npm install @types/express --save-dev
```

---

# Express Application Setup

Example:

```typescript
import express from "express";

const app =
express();

app.listen(3000);
```

---

# Express Middleware

Master middleware concepts.

Middleware executes between:

```
Request

 |

Middleware

 |

Response
```

---

# Built-in Middleware

Understand:

- express.json()
- express.urlencoded()
- static files

Example:

```typescript
app.use(
express.json()
);
```

---

# Custom Middleware

Create reusable middleware.

Examples:

- Logger middleware
- Authentication middleware
- Validation middleware
- Error middleware

---

# Logger Middleware

Track:

- Requests
- Response time
- Status codes
- Errors

Libraries:

- Morgan
- Pino
- Winston

---

# Authentication Middleware

Responsible for:

- Token validation
- User verification
- Permission checking

Flow:

```
Request

 |

JWT Middleware

 |

Validate Token

 |

Controller
```

---

# Error Handling Middleware

Centralize errors.

Example:

```typescript
app.use(
(error,req,res,next)=>{

res.status(500)
.json({

message:error.message

});

}
);
```

---

# Express Routing

Master API routing.

Structure:

```
routes

├── user.routes.ts

├── product.routes.ts

└── order.routes.ts
```

---

# Route Design

Example:

```typescript
router.get(
"/users",
getUsers
);
```

---

# REST API Development

Master REST principles.

Understand:

- Resources
- HTTP methods
- Status codes
- Request lifecycle
- Response format

---

# HTTP Methods

GET:

Retrieve data

POST:

Create data

PUT:

Replace data

PATCH:

Update partial data

DELETE:

Remove data

---

# REST Resource Design

Good:

```
GET /users

GET /users/10

POST /users

PATCH /users/10

DELETE /users/10
```

Avoid:

```
/getAllUsers

/createNewUser
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
- API evolution
- Safe releases

---

# Request Validation

Never trust client input.

Validate:

- Required fields
- Data types
- Length
- Format
- Business rules

---

# Validation Libraries

Master:

- Joi
- Zod
- Yup
- class-validator

---

# Zod Validation

Example:

```typescript
const schema =
z.object({

email:
z.string().email(),

age:
z.number()

});
```

---

# DTO Pattern

Use Data Transfer Objects.

Purpose:

- Validate input
- Define API contracts
- Separate internal models

Example:

```
CreateUserDto

UpdateUserDto

LoginDto
```

---

# Response Standardization

Create consistent responses.

Example:

```json
{
"success":true,
"data":{},
"message":"Success"
}
```

---

# Pagination

Master API pagination.

Types:

- Offset pagination
- Cursor pagination

Example:

```
GET /users?page=1&limit=20
```

---

# Filtering

Support:

```
GET /products?
category=mobile
```

---

# Sorting

Support:

```
GET /users?
sort=name
```

---

# Searching

Implement:

- Keyword search
- Full-text search
- Database indexing

---

# API Documentation

Master:

- Swagger
- OpenAPI
- Postman Collections

---

# Swagger Integration

Document:

- Endpoints
- Request body
- Parameters
- Responses
- Authentication

---

# Request Lifecycle

Understand complete flow:

```
Client Request

 |

Router

 |

Middleware

 |

Controller

 |

Service

 |

Repository

 |

Database

 |

Response
```

---

# Node.js API Security

Secure APIs using:

- Authentication
- Authorization
- Input validation
- Rate limiting
- Encryption

---

# Security Headers

Use:

- Helmet.js

Protect:

- XSS
- Clickjacking
- MIME attacks

---

# Rate Limiting

Prevent abuse.

Use:

- express-rate-limit

Protect against:

- Brute force
- API flooding
- Denial of service

---

# CORS Configuration

Understand:

- Cross-origin requests
- Allowed origins
- Headers
- Credentials

---

# API Error Codes

Use proper status codes.

Examples:

```
200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

500 Internal Server Error
```

---

````markdown id="ndy5qf"
# Database Integration with Node.js

Master database integration patterns for Node.js applications.

Understand:

- SQL databases
- NoSQL databases
- ORM
- ODM
- Query builders
- Database connection management
- Transactions
- Migrations
- Indexing
- Performance optimization

---

# Database Architecture

Recommended architecture:

```
Controller

 |

Service

 |

Repository

 |

Database Client

 |

Database
```

---

# Database Types

Understand:

## Relational Databases

Examples:

- PostgreSQL
- MySQL
- SQL Server
- Oracle

Characteristics:

- Tables
- Rows
- Columns
- Relationships
- SQL queries
- Transactions

---

## NoSQL Databases

Examples:

- MongoDB
- DynamoDB
- Cassandra

Characteristics:

- Documents
- Key-value storage
- Flexible schemas
- Horizontal scaling

---

# Database Connection Management

Master:

- Connection pooling
- Connection lifecycle
- Timeout handling
- Retry strategies
- Graceful shutdown

---

# Connection Pooling

Purpose:

Reuse database connections.

Benefits:

- Better performance
- Reduced overhead
- More concurrent requests

Flow:

```
Application

 |

Connection Pool

 |

Database Connections
```

---

# MongoDB Integration

Master MongoDB with Node.js.

Understand:

- Documents
- Collections
- Schemas
- Indexes
- Aggregation
- Transactions

---

# MongoDB Driver

Native MongoDB driver:

```bash
npm install mongodb
```

---

# Mongoose ODM

Master Mongoose.

Install:

```bash
npm install mongoose
```

---

# Mongoose Concepts

Understand:

- Schema
- Model
- Document
- Middleware
- Validation
- Population

---

# Mongoose Schema

Example:

```typescript
const UserSchema =
new Schema({

name:String,

email:String

});
```

---

# Mongoose Model

Models interact with collections.

Example:

```typescript
const User =
mongoose.model(
"User",
UserSchema
);
```

---

# Mongoose CRUD Operations

Master:

Create:

```typescript
User.create()
```

Read:

```typescript
User.find()
```

Update:

```typescript
User.updateOne()
```

Delete:

```typescript
User.deleteOne()
```

---

# MongoDB Indexing

Optimize queries.

Understand:

- Single field indexes
- Compound indexes
- Text indexes
- Unique indexes

---

# MongoDB Aggregation

Master:

- Pipeline
- Match
- Group
- Sort
- Lookup

Example:

```
Collection

 |

Aggregation Pipeline

 |

Result
```

---

# PostgreSQL Integration

Master PostgreSQL with Node.js.

Understand:

- SQL queries
- Relations
- Constraints
- Transactions
- Indexes

---

# PostgreSQL Drivers

Libraries:

- pg
- node-postgres

Install:

```bash
npm install pg
```

---

# ORM with Node.js

Master ORM concepts.

Benefits:

- Object-based database access
- Type safety
- Query abstraction
- Migration support

---

# Prisma ORM

Master Prisma.

Features:

- Type-safe queries
- Schema management
- Migrations
- Database client generation

---

# Prisma Structure

Example:

```
prisma

 |

schema.prisma

 |

Generated Client

 |

Database
```

---

# Prisma Schema

Example:

```prisma
model User {

id Int @id

name String

email String

}
```

---

# Prisma CRUD

Create:

```typescript
prisma.user.create()
```

Read:

```typescript
prisma.user.findMany()
```

Update:

```typescript
prisma.user.update()
```

Delete:

```typescript
prisma.user.delete()
```

---

# Database Transactions

Master transactions.

Purpose:

Maintain data consistency.

Example:

```
Payment

 +

Order Creation

 +

Inventory Update

```

All succeed or all rollback.

---

# Transaction Isolation

Understand:

- Read Uncommitted
- Read Committed
- Repeatable Read
- Serializable

---

# Database Migration

Manage database changes.

Tools:

- Prisma migrations
- Sequelize migrations
- Knex migrations

---

# Database Seeding

Create initial data.

Examples:

- Admin users
- Default roles
- Configuration data

---

# Query Optimization

Improve database performance.

Techniques:

- Indexing
- Query analysis
- Pagination
- Caching
- Connection pooling

---

# Redis Integration

Master Redis with Node.js.

Redis provides:

- Caching
- Sessions
- Pub/Sub
- Queues
- Rate limiting

---

# Redis Installation

Libraries:

- redis
- ioredis

---

# Redis Cache Pattern

Architecture:

```
Request

 |

Check Cache

 |

Cache Hit

 |

Return Data


Cache Miss

 |

Database Query

 |

Store Cache
```

---

# Cache Strategies

Understand:

## Cache Aside

Application manages cache.

---

## Write Through

Write database and cache together.

---

## Write Behind

Cache first, database later.

---

# Redis Use Cases

Use Redis for:

- API caching
- User sessions
- OTP storage
- Rate limiting
- Leaderboards
- Real-time data

---

# Authentication Architecture

Master authentication systems.

Understand:

- Authentication
- Authorization
- Sessions
- Tokens
- OAuth
- OpenID Connect

---

# JWT Authentication

Master JSON Web Tokens.

JWT contains:

```
Header

+

Payload

+

Signature
```

---

# JWT Flow

```
User Login

 |

Validate Credentials

 |

Generate Token

 |

Client Stores Token

 |

Send Token With Requests

 |

Verify Token

 |

Access Resource
```

---

# JWT Implementation

Libraries:

- jsonwebtoken
- passport-jwt

---

# Access Token

Used for:

- API authentication
- Short duration access

Contains:

- User ID
- Roles
- Permissions

---

# Refresh Token

Used for:

- Generating new access tokens
- Long sessions

Best practices:

- Store securely
- Rotate tokens
- Revoke when needed

---

# Password Security

Never store plain passwords.

Use:

- bcrypt
- Argon2

Example:

```
Password

 |

Hash Function

 |

Stored Hash
```

---

# OAuth Authentication

Master:

- Google Login
- GitHub Login
- Microsoft Login

Flow:

```
User

 |

OAuth Provider

 |

Authorization Code

 |

Token

 |

Application
```

---

# Role Based Access Control

Implement RBAC.

Example:

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

# Permission System

Design:

```
USER_CREATE

USER_UPDATE

USER_DELETE

REPORT_VIEW
```

---

# Session Management

Understand:

- Cookies
- Sessions
- Session stores
- Expiration
- Logout

---

# Background Jobs

Master asynchronous processing.

Use cases:

- Email sending
- Report generation
- Image processing
- Data processing

---

# Job Queue Architecture

```
Application

 |

Queue

 |

Worker

 |

Task Processor
```

---

# Queue Libraries

Master:

- BullMQ
- Bull
- RabbitMQ
- Kafka

---

# BullMQ with Redis

Used for:

- Background jobs
- Scheduled tasks
- Retry handling

---

# Job Features

Implement:

- Retries
- Delayed jobs
- Failed jobs
- Monitoring
- Priority queues

---

````markdown id="ndy5qf"
# WebSockets with Node.js

Master real-time communication using Node.js.

Understand:

- WebSocket protocol
- Real-time applications
- Socket communication
- Event-based messaging
- Live updates
- Bidirectional communication

---

# WebSocket Architecture

Traditional HTTP:

```
Client

 |

Request

 |

Server

 |

Response
```

WebSocket:

```
Client

        <============>

Server

Continuous Connection
```

---

# WebSocket Use Cases

Use WebSockets for:

- Chat applications
- Gaming applications
- Live notifications
- Stock price updates
- Collaboration tools
- Real-time dashboards
- Tracking systems

---

# Socket.IO

Master Socket.IO.

Install:

```bash
npm install socket.io
```

Features:

- Automatic reconnection
- Rooms
- Broadcasting
- Event handling
- Namespace support

---

# Socket.IO Server

Example:

```typescript
io.on(
"connection",
(socket)=>{

console.log(
"User connected"
);

});
```

---

# Socket.IO Client Communication

Client sends:

```javascript
socket.emit(
"message",
data
);
```

Server receives:

```javascript
socket.on(
"message",
(data)=>{

});
```

---

# Broadcasting Events

Send messages to multiple users.

Examples:

- Notifications
- Chat messages
- Status updates

---

# Rooms

Group users logically.

Examples:

```
Room: project-101

Users:

User A

User B

User C
```

---

# Namespaces

Separate communication channels.

Example:

```
/chat

/admin

/notifications
```

---

# Real-Time Authentication

Secure WebSockets using:

- JWT
- Cookies
- Session validation

Flow:

```
Client Connect

 |

Send Token

 |

Validate User

 |

Allow Connection
```

---

# Event Driven Architecture

Master event-driven backend systems.

Understand:

- Events
- Producers
- Consumers
- Event brokers
- Event processing

---

# Event Architecture

```
Service A

 |

Event

 |

Message Broker

 |

Service B
```

---

# Node.js EventEmitter

Built-in event system.

Example:

```javascript
const EventEmitter =
require("events");

const emitter =
new EventEmitter();
```

---

# Custom Events

Create application events.

Examples:

```
USER_CREATED

ORDER_COMPLETED

PAYMENT_SUCCESS

EMAIL_SENT
```

---

# Event Driven Benefits

Advantages:

- Loose coupling
- Scalability
- Better extensibility
- Async processing

---

# Message Queues

Master message queue systems.

Understand:

- Producer
- Consumer
- Queue
- Message
- Acknowledgement

---

# RabbitMQ Integration

Master RabbitMQ.

Use cases:

- Distributed systems
- Background processing
- Microservices communication

---

# RabbitMQ Architecture

```
Producer

 |

Exchange

 |

Queue

 |

Consumer
```

---

# Apache Kafka Integration

Master Kafka concepts.

Kafka provides:

- Event streaming
- High throughput
- Distributed messaging

---

# Kafka Concepts

Understand:

- Topics
- Partitions
- Producers
- Consumers
- Consumer groups
- Offsets

---

# Kafka Use Cases

Use Kafka for:

- Data pipelines
- Analytics
- Event sourcing
- Large-scale systems

---

# Microservices with Node.js

Master microservice architecture.

Understand:

- Service boundaries
- Communication patterns
- Deployment strategy
- Monitoring

---

# Monolithic Architecture

Traditional approach:

```
Single Application

 |

All Features
```

Advantages:

- Simple development
- Easy deployment

Problems:

- Hard scaling
- Tight coupling

---

# Microservices Architecture

Modern approach:

```
API Gateway

 |

-----------------

User Service

Order Service

Payment Service

Notification Service

-----------------

 |

Databases
```

---

# Microservice Principles

Follow:

- Single responsibility
- Independent deployment
- Loose coupling
- Autonomous services

---

# Service Communication

Understand:

## Synchronous Communication

Examples:

- REST APIs
- GraphQL

---

## Asynchronous Communication

Examples:

- Kafka
- RabbitMQ
- Events

---

# API Gateway Pattern

Gateway handles:

- Routing
- Authentication
- Rate limiting
- Request transformation

Architecture:

```
Client

 |

API Gateway

 |

Microservices
```

---

# Service Discovery

Understand:

- Service registration
- Service lookup
- Dynamic routing

Tools:

- Consul
- Kubernetes Services

---

# Distributed Systems Concepts

Master:

- Scalability
- Availability
- Fault tolerance
- Consistency
- Reliability

---

# CAP Theorem

Understand:

Distributed systems trade-offs:

- Consistency
- Availability
- Partition tolerance

---

# Fault Handling

Implement:

- Retry mechanism
- Circuit breaker
- Timeout handling
- Fallback strategies

---

# Circuit Breaker Pattern

Protect systems from failures.

Flow:

```
Service Failure

 |

Circuit Opens

 |

Prevent Requests

 |

Recovery Check

 |

Resume Traffic
```

---

# Node.js Design Patterns

Master backend patterns.

---

# Singleton Pattern

Used for:

- Database connections
- Configuration objects
- Logging services

---

# Factory Pattern

Used for:

- Object creation
- Dynamic service selection

---

# Strategy Pattern

Used for:

- Multiple algorithms
- Payment methods
- Authentication methods

---

# Observer Pattern

Used for:

- Events
- Notifications
- Reactive systems

---

# Dependency Injection Pattern

Benefits:

- Loose coupling
- Better testing
- Maintainability

---

# Docker with Node.js

Master containerization.

Understand:

- Docker images
- Containers
- Dockerfile
- Docker Compose

---

# Node.js Dockerfile

Example:

```dockerfile
FROM node:20

WORKDIR /app

COPY package.json .

RUN npm install

COPY .

CMD ["npm","start"]
```

---

# Docker Best Practices

Follow:

- Small images
- Multi-stage builds
- Environment variables
- Security scanning

---

# Docker Compose

Manage multiple services.

Example:

```
Node API

+

Database

+

Redis

+

Queue
```

---

# Kubernetes with Node.js

Master container orchestration.

Understand:

- Pods
- Services
- Deployments
- ConfigMaps
- Secrets

---

# Kubernetes Deployment

Architecture:

```
User

 |

Load Balancer

 |

Kubernetes Service

 |

Node.js Pods

 |

Database
```

---

# Scaling Node.js Applications

Scale using:

- Horizontal scaling
- Load balancing
- Clustering
- Containers

---

# Node.js Cluster Module

Use multiple processes.

Architecture:

```
Master Process

 |

----------------

Worker 1

Worker 2

Worker 3

----------------
```

---

# Reverse Proxy

Use:

- Nginx
- Apache
- Cloud Load Balancers

Responsibilities:

- SSL termination
- Routing
- Compression
- Load balancing

---

````markdown id="ndy5qf"
# Node.js Testing

Master complete testing strategies for Node.js backend applications.

Understand:

- Unit testing
- Integration testing
- API testing
- End-to-end testing
- Mocking
- Test automation
- Code coverage
- Test-driven development

---

# Testing Pyramid

Follow the testing pyramid.

```
              E2E Tests

        Integration Tests

      Unit Tests
```

---

# Unit Testing

Unit testing focuses on individual pieces of code.

Test:

- Functions
- Services
- Utilities
- Business logic
- Validation rules

Avoid testing:

- External systems
- Real databases
- Network calls

---

# Unit Testing Tools

Master:

- Jest
- Vitest
- Mocha
- Chai

---

# Jest Framework

Install:

```bash
npm install jest --save-dev
```

Jest provides:

- Test runner
- Assertions
- Mocking
- Coverage reports

---

# Jest Test Structure

Example:

```javascript
describe(
"User Service",
()=>{

test(
"should create user",
()=>{

});

});
```

---

# Assertions

Master:

```javascript
expect()
```

Examples:

```javascript
expect(value)
.toBe(true)
```

```javascript
expect(array)
.toHaveLength(5)
```

---

# Mocking

Mock external dependencies.

Mock:

- APIs
- Databases
- Services
- Files
- Third-party libraries

---

# Jest Mock Example

```javascript
jest.mock(
"./userService"
);
```

---

# Integration Testing

Test multiple layers together.

Examples:

- Controller + Service
- API + Database
- Authentication flow

---

# API Testing

Master API testing.

Validate:

- HTTP methods
- Status codes
- Request body
- Response data
- Authentication

---

# Supertest

Use Supertest for API testing.

Install:

```bash
npm install supertest --save-dev
```

Example:

```javascript
request(app)
.get("/users")
.expect(200);
```

---

# End-to-End Testing

Test complete user workflows.

Examples:

```
Login

 |

Create Data

 |

Update Data

 |

Logout
```

---

# E2E Testing Tools

Master:

- Playwright
- Cypress
- Selenium

---

# Test Coverage

Measure:

- Line coverage
- Function coverage
- Branch coverage
- Statement coverage

---

# Test Driven Development

Follow TDD cycle:

```
Write Test

 |

Write Code

 |

Refactor

 |

Repeat
```

---

# Code Quality Tools

Maintain high-quality Node.js code.

Master:

- ESLint
- Prettier
- Husky
- Commitlint
- SonarQube

---

# ESLint

Purpose:

- Detect bugs
- Enforce standards
- Improve readability

---

# Prettier

Purpose:

- Automatic formatting
- Consistent code style

---

# Git Hooks

Use Husky for:

- Pre-commit checks
- Automated tests
- Code formatting

---

# Node.js Security

Build secure backend systems.

Understand:

- OWASP Top 10
- Secure coding
- Dependency security
- Authentication security
- Data protection

---

# OWASP Security Risks

Protect against:

- Injection attacks
- Broken authentication
- Sensitive data exposure
- Security misconfiguration
- XSS
- CSRF
- SSRF

---

# SQL Injection Prevention

Never create queries using string concatenation.

Bad:

```javascript
"SELECT * FROM users WHERE id="
+ id
```

Use:

- Parameterized queries
- ORM protection
- Query builders

---

# NoSQL Injection Prevention

Validate:

- User input
- Query objects
- Filters

Avoid:

- Direct user object injection

---

# XSS Prevention

Protect user-generated content.

Use:

- Input sanitization
- Output encoding
- Content security policy

---

# CSRF Protection

Protect state-changing requests.

Use:

- CSRF tokens
- SameSite cookies
- Secure cookie settings

---

# Secure Headers

Use Helmet.js.

Install:

```bash
npm install helmet
```

Provides:

- Security headers
- XSS protection
- Clickjacking protection

---

# Rate Limiting Security

Protect APIs from abuse.

Implement:

- Request limits
- IP restrictions
- User-based limits

---

# Dependency Security

Monitor packages.

Tools:

- npm audit
- Snyk
- Dependabot

---

# Secret Management

Never commit:

- API keys
- Passwords
- Tokens
- Certificates

Use:

- Environment variables
- Secret managers

Examples:

- AWS Secrets Manager
- Azure Key Vault
- Hashicorp Vault

---

# Logging Architecture

Implement professional logging.

Log:

- Application events
- Errors
- API requests
- Performance metrics
- Security events

---

# Logging Libraries

Master:

- Winston
- Pino
- Bunyan

---

# Structured Logging

Prefer JSON logs.

Example:

```json
{
"level":"error",
"message":"Database failed",
"service":"user-api"
}
```

---

# Log Levels

Understand:

```
error

warn

info

debug
```

---

# Monitoring Node.js Applications

Monitor:

- CPU usage
- Memory usage
- Event loop delay
- API latency
- Error rate

---

# Monitoring Tools

Master:

- Prometheus
- Grafana
- Datadog
- New Relic
- Application Insights

---

# Health Checks

Create endpoints:

Example:

```
GET /health
```

Return:

```json
{
"status":"healthy"
}
```

---

# Application Metrics

Track:

- Requests per second
- Response time
- Error count
- Active users
- Database performance

---

# Performance Optimization

Optimize Node.js applications.

Focus on:

- Event loop performance
- Database queries
- Memory usage
- API response time
- Network calls

---

# Event Loop Optimization

Avoid:

- Blocking code
- Heavy calculations
- Large synchronous operations

---

# Async Optimization

Prefer:

```javascript
Promise.all()
```

for parallel tasks.

Example:

```javascript
await Promise.all([

getUsers(),

getOrders()

]);
```

---

# Memory Optimization

Prevent:

- Memory leaks
- Large object retention
- Unreleased resources

---

# API Performance Optimization

Improve:

- Response compression
- Caching
- Pagination
- Database indexes
- Async processing

---

# Compression

Use:

- gzip
- Brotli

Benefits:

- Smaller responses
- Faster APIs

---

# Node.js CI/CD Pipeline

Master continuous integration and deployment.

Pipeline:

```
Code Commit

 |

Build

 |

Test

 |

Security Scan

 |

Deploy

 |

Monitor
```

---

# GitHub Actions

Automate:

- Testing
- Building
- Deployment

---

# CI Pipeline Steps

Typical flow:

```
Install Dependencies

 |

Lint Code

 |

Run Tests

 |

Build Application

 |

Deploy
```

---

# Environment Deployment

Understand:

- Development
- Testing
- Staging
- Production

---

# Production Deployment Platforms

Deploy Node.js applications on:

- AWS
- Azure
- Google Cloud
- DigitalOcean
- Render
- Railway

---

# AWS Node.js Deployment

Master:

- EC2
- ECS
- Lambda
- Elastic Beanstalk
- RDS
- ElastiCache

---

# Serverless Node.js

Understand:

- AWS Lambda
- Azure Functions
- Google Cloud Functions

Use cases:

- APIs
- Background jobs
- Event processing

---

# Node.js Production Checklist

Before production:

## Code Quality

- Clean architecture
- Code reviews
- Tests completed

## Security

- Secrets protected
- Authentication implemented
- Dependencies scanned

## Performance

- Caching enabled
- Database optimized
- Monitoring configured

## Deployment

- CI/CD ready
- Logging enabled
- Backup strategy available

---

# Node.js AI Agent Rules

The Node.js AI agent must always follow:

1. Write clean and maintainable code.

2. Prefer TypeScript for enterprise applications.

3. Follow layered architecture.

4. Separate controllers, services, and repositories.

5. Validate every external input.

6. Handle errors gracefully.

7. Never expose secrets.

8. Write tests for important functionality.

9. Consider scalability.

10. Consider security in every implementation.

11. Optimize performance before production release.

12. Follow industry best practices.

---

# Node.js Expert Mindset

Think like:

- Backend Architect
- Software Engineer
- Security Engineer
- Cloud Engineer
- Performance Engineer

Do not only write APIs.

Design reliable, scalable, secure backend systems.

---
