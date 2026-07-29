---
name: mongodb
description: Complete MongoDB database skill covering NoSQL database concepts, document-oriented architecture, schema design, CRUD operations, aggregation pipelines, indexing, performance optimization, replication, sharding, security, cloud deployment, MongoDB administration, and production-ready database development.
---

# MongoDB Skill

# Skill Instructions

You are an expert MongoDB database engineer.

Your responsibility is to design, develop, optimize, secure, troubleshoot, and maintain production-ready MongoDB database systems.

You must think like:

- Senior MongoDB Engineer
- NoSQL Database Architect
- Backend Engineer
- Data Engineer
- Database Administrator
- Performance Engineer
- Security Engineer

Always generate:

- Efficient MongoDB schemas
- Optimized queries
- Scalable database architecture
- Secure database solutions
- Production-ready implementations

---

# MongoDB Overview

MongoDB is a document-oriented NoSQL database.

MongoDB stores data as:

- Documents
- Collections
- Databases

Instead of:

```
Tables

Rows

Columns
```

MongoDB uses:

```
Database

 |

Collection

 |

Document

 |

Fields
```

---

# MongoDB Core Features

Master:

- Document database model
- BSON storage
- Flexible schemas
- Query language
- Aggregation framework
- Indexing
- Replication
- Sharding
- Transactions
- Change streams

---

# MongoDB Architecture

Understand MongoDB internals.

```
Application

      |

MongoDB Driver

      |

MongoDB Server

      |

Storage Engine

      |

Data Files
```

---

# MongoDB Components

Master:

- mongod
- mongosh
- MongoDB Compass
- Replica Sets
- Shards
- Config Servers
- Query Routers

---

# MongoDB Installation

Install using:

```bash
brew install mongodb-community
```

Start MongoDB:

```bash
brew services start mongodb-community
```

Connect:

```bash
mongosh
```

---

# MongoDB Shell Commands

Show databases:

```javascript
show dbs
```

Create/use database:

```javascript
use ecommerce
```

Show collections:

```javascript
show collections
```

---

# MongoDB Database Management

Create database:

```javascript
use ecommerce
```

MongoDB creates database when data is inserted.

---

# Collections

Collections are similar to SQL tables.

Example:

```
users

products

orders

payments
```

---

# Create Collection

Example:

```javascript
db.createCollection("users")
```

---

# Documents

Documents store JSON-like data.

Example:

```javascript
{
 name:"John",
 email:"john@test.com",
 age:30
}
```

---

# BSON Format

MongoDB stores BSON.

BSON supports:

- Strings
- Numbers
- Dates
- Arrays
- Objects
- Binary data

---

# MongoDB Data Types

Master:

- String
- Integer
- Double
- Boolean
- Date
- ObjectId
- Array
- Object
- Null
- Binary

---

# ObjectId

MongoDB default identifier.

Example:

```javascript
_id:
ObjectId()
```

Contains:

- Timestamp
- Machine identifier
- Process identifier
- Counter

---

# MongoDB Schema Design

MongoDB schema design differs from relational databases.

Focus on:

- Query patterns
- Data access patterns
- Performance requirements

---

# Embedding Documents

Store related data together.

Example:

```javascript
{
 name:"John",

 address:{
 city:"Chennai",
 country:"India"
 }

}
```

Benefits:

- Faster reads
- Single document access

---

# Referencing Documents

Store relationships using references.

Example:

User:

```javascript
{
_id:1,
name:"John"
}
```

Order:

```javascript
{
userId:1,
product:"Laptop"
}
```

---

# Embedding vs Referencing

Use Embedding:

- Data accessed together
- Small related data

Use Referencing:

- Large relationships
- Independent entities

---

# MongoDB CRUD Operations

Master:

- Create
- Read
- Update
- Delete

---

# Insert Document

Insert one:

```javascript
db.users.insertOne({

name:"John",

age:30

})
```

---

# Insert Multiple Documents

```javascript
db.users.insertMany([

{
name:"John"
},

{
name:"Alex"
}

])
```

---

# Find Documents

Example:

```javascript
db.users.find()
```

---

# Find Specific Data

Example:

```javascript
db.users.find({

age:30

})
```

---

# Projection

Select required fields.

Example:

```javascript
db.users.find(

{},

{
name:1

}

)
```

---

# Query Operators

Master:

- Comparison operators
- Logical operators
- Element operators
- Array operators

---

# Comparison Operators

Examples:

```
$eq

$ne

$gt

$gte

$lt

$lte
```

Example:

```javascript
{
age:{
$gt:25
}
}
```

---

# Logical Operators

Master:

```
$and

$or

$not

$nor
```

Example:

```javascript
{
$or:[
{name:"John"},
{name:"Alex"}
]
}
```

---

# Array Queries

Operators:

```
$in

$all

$size

$elemMatch
```

---

# Update Documents

Example:

```javascript
db.users.updateOne(

{
name:"John"
},

{
$set:{
age:31
}
}

)
```

---

# Update Operators

Master:

```
$set

$unset

$inc

$push

$pull

$addToSet
```

---

# Delete Documents

Delete one:

```javascript
db.users.deleteOne({

name:"John"

})
```

---

# MongoDB Indexing

Indexes improve query performance.

Without index:

```
Collection Scan
```

With index:

```
Index Lookup
```

---

# Index Types

Master:

- Single field index
- Compound index
- Multikey index
- Text index
- Geospatial index
- Hashed index

---

# Create Index

Example:

```javascript
db.users.createIndex({

email:1

})
```

---

# Compound Index

Example:

```javascript
db.users.createIndex({

country:1,

age:-1

})
```

---

# Index Best Practices

Create indexes on:

- Frequently queried fields
- Sorting fields
- Join/reference fields

Avoid:

- Too many indexes
- Unused indexes

---

# Query Analysis

Use:

```javascript
.explain()
```

Example:

```javascript
db.users.find({

email:"test@test.com"

}).explain()
```

---

````markdown id="mongodbpart2"
# MongoDB Aggregation Framework

Master MongoDB aggregation for advanced data processing.

Aggregation is used for:

- Data transformation
- Analytics
- Reporting
- Data processing
- Complex queries

---

# Aggregation Pipeline

MongoDB processes data through stages.

Architecture:

```
Collection

    |

Aggregation Pipeline

    |

Stage 1

    |

Stage 2

    |

Result
```

---

# Aggregation Syntax

Example:

```javascript
db.orders.aggregate([

{

$match:{
status:"completed"
}

}

])
```

---

# Aggregation Stages

Master:

- $match
- $group
- $project
- $sort
- $limit
- $skip
- $lookup
- $unwind
- $facet

---

# $match Stage

Filters documents.

Equivalent to SQL:

```
WHERE
```

Example:

```javascript
{
$match:{
age:{
$gte:18
}
}
}
```

---

# $project Stage

Select or transform fields.

Example:

```javascript
{
$project:{
name:1,
email:1
}
}
```

---

# $group Stage

Groups documents.

Equivalent to SQL:

```
GROUP BY
```

Example:

```javascript
{
$group:{

_id:"$country",

count:{
$sum:1
}

}

}
```

---

# Aggregation Functions

Master:

- $sum
- $avg
- $min
- $max
- $push
- $addToSet

---

# $sort Stage

Sort results.

Example:

```javascript
{
$sort:{
createdAt:-1
}
}
```

---

# $limit Stage

Limit results.

Example:

```javascript
{
$limit:10
}
```

---

# $skip Stage

Skip records.

Example:

```javascript
{
$skip:20
}
```

---

# $unwind Stage

Expand arrays.

Example:

Document:

```javascript
{
tags:[
"AI",
"MongoDB"
]
}
```

After unwind:

```
AI

MongoDB
```

---

# $lookup Stage

MongoDB equivalent of SQL JOIN.

Example:

```javascript
{
$lookup:{

from:"orders",

localField:"_id",

foreignField:"userId",

as:"orders"

}

}
```

---

# $facet Stage

Run multiple aggregations together.

Used for:

- Dashboards
- Reports
- Analytics

---

# MongoDB Data Modelling Patterns

Master professional MongoDB schema patterns.

---

# Attribute Pattern

Used when documents contain dynamic fields.

Example:

```javascript
{
product:"Phone",

attributes:[

{
key:"color",
value:"black"
}

]

}
```

---

# Bucket Pattern

Group related data.

Used for:

- Time-series data
- Logs
- Events

Example:

```
Sensor Data

 |

Hourly Bucket
```

---

# Outlier Pattern

Handle documents with unusually large data.

Example:

Social media posts:

```
Normal Users

+

Celebrity Users
```

---

# Computed Pattern

Store calculated values.

Example:

Instead of calculating:

```
Total Orders
```

every time:

Store:

```
orderCount
```

---

# Extended Reference Pattern

Store frequently accessed information together.

Example:

Order:

```javascript
{
customer:{
name:"John",
email:"john@test.com"
}
}
```

---

# MongoDB Transactions

MongoDB supports ACID transactions.

Used for:

- Financial operations
- Multiple document updates
- Data consistency

---

# Transaction Example

Scenario:

```
Transfer Money

 |

Remove Balance

 |

Add Balance

 |

Commit
```

---

# Transaction Commands

Start:

```javascript
session.startTransaction()
```

Commit:

```javascript
session.commitTransaction()
```

Rollback:

```javascript
session.abortTransaction()
```

---

# MongoDB Replica Sets

Replica sets provide:

- High availability
- Data redundancy
- Automatic failover

---

# Replica Set Architecture

```
Primary

   |

Replication

   |

----------------

Secondary 1

Secondary 2

----------------
```

---

# Primary Node

Handles:

- Write operations
- Client requests

---

# Secondary Nodes

Receive:

- Replicated data

Can handle:

- Read operations

---

# Automatic Failover

Process:

```
Primary Failure

        |

Election

        |

Secondary Becomes Primary

        |

Application Continues
```

---

# Replica Set Election

MongoDB automatically selects:

- New primary
- Highest priority node

---

# Read Preferences

Control where reads happen.

Options:

- Primary
- Primary Preferred
- Secondary
- Secondary Preferred
- Nearest

---

# Write Concern

Controls write confirmation.

Example:

```javascript
{
writeConcern:{
w:"majority"
}
}
```

---

# Read Concern

Controls consistency level.

Options:

- Local
- Available
- Majority
- Linearizable

---

# MongoDB Sharding

Sharding distributes data across servers.

Used for:

- Huge datasets
- High traffic applications
- Horizontal scaling

---

# Sharding Architecture

```
Application

      |

Query Router

      |

-----------------

Shard 1

Shard 2

Shard 3

-----------------

      |

Config Server
```

---

# Sharding Components

Master:

- Shards
- Config servers
- mongos router

---

# Shard Key

Determines data distribution.

Example:

```
userId

tenantId

region
```

---

# Good Shard Key

Characteristics:

- High cardinality
- Even distribution
- Frequently queried

---

# Bad Shard Key

Avoid:

- Low uniqueness fields
- Sequential values
- Hot spots

Example:

```
status
```

---

# MongoDB Performance Optimization

Optimize:

- Queries
- Indexes
- Schema design
- Hardware resources

---

# Performance Optimization Process

```
Measure

 |

Analyze

 |

Optimize

 |

Test

 |

Monitor
```

---

# Query Optimization

Use:

- explain()
- Proper indexes
- Projection
- Pagination

---

# Avoid Returning Large Documents

Bad:

```javascript
db.users.find({})
```

Better:

```javascript
db.users.find(
{},
{
name:1
}
)
```

---

# Pagination Optimization

Avoid:

```javascript
skip(100000)
```

For large data.

Use:

```
Range Based Pagination
```

Example:

```
_id > lastSeenId
```

---

# Connection Pooling

MongoDB drivers maintain connection pools.

Benefits:

- Faster requests
- Reduced overhead
- Better scalability

---

# MongoDB Monitoring

Monitor:

- Query performance
- Memory usage
- Connections
- Replication status
- Disk usage

---

# Monitoring Tools

Use:

- MongoDB Compass
- MongoDB Atlas Monitoring
- Prometheus
- Grafana

---

# MongoDB Profiler

Analyze slow operations.

Enable:

```javascript
db.setProfilingLevel(1)
```

Tracks:

- Slow queries
- Operations
- Execution time

---

# MongoDB Backup

Backup strategies:

- Logical backup
- Snapshot backup
- Continuous backup

---

# mongodump

Create backup:

```bash
mongodump

--db ecommerce
```

---

# mongorestore

Restore:

```bash
mongorestore
```

---

# Backup Best Practices

Always:

- Automate backups
- Encrypt backups
- Test restoration
- Store offsite copies

---

````markdown id="mongodbpart3"
# MongoDB Security

Master MongoDB security for enterprise and production systems.

Security goals:

- Protect data
- Control access
- Prevent unauthorized operations
- Encrypt sensitive information
- Monitor database activity

---

# MongoDB Security Architecture

```
Application

      |

Authentication

      |

Authorization

      |

Database Access

      |

Storage Layer
```

---

# MongoDB Authentication

Authentication verifies user identity.

Supported methods:

- SCRAM Authentication
- X.509 Certificates
- LDAP
- Kerberos
- Cloud IAM

---

# SCRAM Authentication

Default MongoDB authentication mechanism.

Supports:

- SCRAM-SHA-256
- SCRAM-SHA-1

Example:

```javascript
db.createUser({

user:"admin",

pwd:"password",

roles:[

{
role:"root",
db:"admin"
}

]

})
```

---

# MongoDB Users

Create users with specific permissions.

Example:

```javascript
use ecommerce

db.createUser({

user:"appUser",

pwd:"securePassword",

roles:[

{
role:"readWrite",
db:"ecommerce"
}

]

})
```

---

# MongoDB Roles

Master built-in roles:

## Database Roles

- read
- readWrite
- dbAdmin
- userAdmin

---

## Cluster Roles

- clusterAdmin
- clusterManager
- clusterMonitor

---

## Backup Roles

- backup
- restore

---

# Least Privilege Principle

Always:

- Give minimum permissions
- Separate application users
- Avoid root access

Example:

```
Application User

        !=

Administrator User
```

---

# MongoDB Authorization

Authorization controls:

- What users can access
- What operations users can perform

---

# Role Based Access Control (RBAC)

MongoDB uses RBAC.

Structure:

```
User

 |

Role

 |

Privileges

 |

Resources
```

---

# Database User Separation

Recommended:

```
Application User

Reporting User

Admin User

Backup User
```

---

# Network Security

Protect MongoDB network access.

Best practices:

- Private networking
- Firewall rules
- IP restrictions
- Disable public exposure

---

# Bind IP Configuration

Restrict MongoDB access.

Example:

```
bindIp=127.0.0.1
```

---

# TLS Encryption

Secure communication.

Architecture:

```
Application

      |

Encrypted TLS Connection

      |

MongoDB Server
```

---

# Encryption At Rest

Protect stored data.

MongoDB supports:

- WiredTiger Encryption
- Key Management Integration

---

# Field Level Encryption

Encrypt sensitive fields.

Examples:

- Credit card numbers
- Personal information
- Secrets

---

# MongoDB Auditing

Track:

- User activities
- Database changes
- Security events

Audit information:

- Who
- What
- When
- Where

---

# MongoDB Change Streams

Change Streams provide real-time database events.

Used for:

- Event-driven systems
- Notifications
- Real-time applications

---

# Change Stream Architecture

```
Database Change

      |

Change Stream

      |

Application Event

      |

Action
```

---

# Change Stream Example

Listen for changes:

```javascript
collection.watch()
```

---

# Change Stream Use Cases

Use for:

- Real-time dashboards
- Notifications
- Data synchronization
- Microservices events

---

# MongoDB Cloud

## MongoDB Atlas

Managed MongoDB cloud platform.

Provides:

- Automated deployment
- Backups
- Monitoring
- Scaling
- Security

---

# MongoDB Atlas Architecture

```
Application

      |

MongoDB Driver

      |

MongoDB Atlas Cluster

      |

Replica Sets / Shards
```

---

# Atlas Features

Master:

- Automated backups
- Auto scaling
- Performance monitoring
- Security controls
- Global clusters

---

# MongoDB Deployment Models

Deploy MongoDB using:

- Local server
- Docker
- Kubernetes
- Cloud providers

---

# Docker MongoDB

Run MongoDB container.

Example:

```bash
docker run

--name mongodb

-p 27017:27017

mongo
```

---

# Docker Compose MongoDB

Architecture:

```
Backend API

      |

MongoDB Container

      |

Persistent Volume
```

---

# Kubernetes MongoDB Deployment

Master:

- Pods
- StatefulSets
- Services
- Persistent volumes
- Secrets

---

# MongoDB Microservices Architecture

MongoDB works well with microservices.

Example:

```
API Gateway

       |

-----------------

User Service

Order Service

Payment Service

-----------------

       |

MongoDB Databases
```

---

# Database Per Service Pattern

Each service owns:

- Own database
- Own collections
- Own schema

Benefits:

- Independent scaling
- Loose coupling
- Better ownership

---

# MongoDB Event Driven Architecture

Example:

```
Order Created

       |

MongoDB Change Stream

       |

Message Queue

       |

Notification Service
```

---

# MongoDB with Message Brokers

Integrate with:

- Kafka
- RabbitMQ
- Azure Service Bus
- AWS SQS

---

# MongoDB AI Integration

MongoDB is useful for AI applications.

Use cases:

- AI memory storage
- Document storage
- Semantic search
- Vector search
- RAG applications

---

# MongoDB Vector Search

Supports AI similarity search.

Used for:

- Embeddings
- Semantic retrieval
- Recommendation systems

---

# AI Vector Architecture

```
Documents

      |

Embedding Model

      |

Vector Storage

      |

Similarity Search

      |

LLM Response
```

---

# MongoDB Atlas Vector Search

Provides:

- Vector indexing
- Similarity queries
- AI application support

---

# RAG Architecture With MongoDB

```
User Question

      |

Embedding Generation

      |

Vector Search

      |

Retrieve Context

      |

LLM

      |

Final Answer
```

---

# MongoDB AI Agent Memory

Store:

- Conversation history
- User preferences
- Agent state
- Workflow information
- Knowledge documents

---

# MongoDB Agent Database Design

Example:

```
agents

 |

agent_id

name

configuration


conversations

 |

conversation_id

messages


memory

 |

user_id

preferences
```

---

# MongoDB AI Agent Rules

The MongoDB AI agent must always:

1. Design efficient document models.

2. Choose embedding or referencing correctly.

3. Create proper indexes.

4. Avoid unnecessary document growth.

5. Optimize aggregation pipelines.

6. Secure database access.

7. Handle transactions carefully.

8. Monitor performance.

9. Design scalable collections.

10. Support AI memory requirements.

11. Protect sensitive information.

12. Generate production-ready MongoDB solutions.

---

# MongoDB Expert Mindset

Think like:

- MongoDB Architect
- NoSQL Engineer
- Backend Engineer
- Data Engineer
- AI Database Engineer

Build MongoDB systems that are:

- Flexible
- Scalable
- Secure
- High performance
- Production ready

---

# MongoDB Production Checklist

## Schema Design

- Query patterns analyzed
- Embedding strategy decided
- Document size optimized

---

## Performance

- Indexes created
- Aggregations optimized
- Slow queries monitored

---

## Security

- Authentication enabled
- Roles configured
- Encryption enabled

---

## Operations

- Backup configured
- Replication tested
- Monitoring enabled

---

## AI Readiness

- Vector strategy planned
- Embedding storage designed
- RAG architecture prepared

---
