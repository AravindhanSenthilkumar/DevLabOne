---
name: postgresql
description: Complete PostgreSQL database skill covering relational database architecture, advanced SQL, schema design, data modelling, indexing, query optimization, transactions, PostgreSQL administration, security, replication, extensions, JSON handling, performance tuning, cloud deployment, and enterprise database development.
---

# PostgreSQL Skill

# Skill Instructions

You are an expert PostgreSQL database engineer.

Your responsibility is to design, develop, optimize, secure, troubleshoot, and maintain production-ready PostgreSQL database systems.

You must think like:

- Senior PostgreSQL Engineer
- Database Architect
- Data Engineer
- Backend Engineer
- Performance Engineer
- Database Administrator
- Security Engineer

Always generate:

- Optimized SQL queries
- Scalable database architecture
- Secure database solutions
- Efficient indexing strategies
- Production-ready database designs

---

# PostgreSQL Overview

PostgreSQL is an advanced open-source object-relational database management system (ORDBMS).

Used for:

- Enterprise applications
- Financial systems
- SaaS platforms
- Analytics systems
- Backend APIs
- AI applications
- Geospatial applications

---

# PostgreSQL Core Features

Master:

- Advanced SQL
- ACID transactions
- JSON support
- Full-text search
- Extensions
- Stored procedures
- Custom data types
- Advanced indexing
- Replication

---

# PostgreSQL Architecture

Understand PostgreSQL internals.

```
Client Application

        |

PostgreSQL Server

        |

Query Parser

        |

Query Planner

        |

Executor

        |

Storage Engine

        |

Data Files
```

---

# PostgreSQL Components

Master:

- PostgreSQL Server
- Client Connections
- Query Planner
- Executor
- WAL Manager
- Storage Manager
- Background Workers

---

# PostgreSQL Installation

Install using:

```bash
brew install postgresql
```

Start server:

```bash
brew services start postgresql
```

Connect:

```bash
psql postgres
```

---

# PostgreSQL Command Line

Useful commands:

List databases:

```sql
\l
```

Connect database:

```sql
\c database_name
```

List tables:

```sql
\dt
```

Describe table:

```sql
\d table_name
```

Exit:

```sql
\q
```

---

# Database Management

Create database:

```sql
CREATE DATABASE ecommerce;
```

List databases:

```sql
SELECT datname
FROM pg_database;
```

Delete database:

```sql
DROP DATABASE ecommerce;
```

---

# PostgreSQL Schemas

Schemas organize database objects.

Example:

```
Database

 |

Schemas

 |

Tables
```

Create schema:

```sql
CREATE SCHEMA sales;
```

---

# Schema Benefits

Provides:

- Logical separation
- Security boundaries
- Better organization
- Multi-tenant support

---

# PostgreSQL Data Types

Master PostgreSQL data types.

---

# Numeric Types

Use:

- INTEGER
- BIGINT
- NUMERIC
- DECIMAL
- REAL
- DOUBLE PRECISION

---

# Character Types

Use:

- CHAR
- VARCHAR
- TEXT

---

# Date and Time Types

Use:

- DATE
- TIME
- TIMESTAMP
- TIMESTAMPTZ
- INTERVAL

---

# Boolean Type

Example:

```sql
active BOOLEAN;
```

Values:

```
TRUE

FALSE

NULL
```

---

# UUID Data Type

Used for unique identifiers.

Example:

```sql
id UUID PRIMARY KEY
```

Benefits:

- Distributed systems
- Security
- Unique identifiers

---

# JSON Data Types

PostgreSQL supports:

- JSON
- JSONB

---

# JSON vs JSONB

JSON:

- Stores exact input

JSONB:

- Binary storage
- Faster queries
- Supports indexing

Prefer:

```
JSONB
```

for production applications.

---

# Array Data Type

PostgreSQL supports arrays.

Example:

```sql
tags TEXT[];
```

---

# Enum Types

Create custom values.

Example:

```sql
CREATE TYPE status AS ENUM(

'ACTIVE',

'INACTIVE'

);
```

---

# Table Creation

Example:

```sql
CREATE TABLE users(

id UUID PRIMARY KEY,

name VARCHAR(100),

email VARCHAR(200),

created_at TIMESTAMP

);
```

---

# Constraints

Master:

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- CHECK
- DEFAULT

---

# Primary Key

Uniquely identifies rows.

Example:

```sql
id BIGSERIAL PRIMARY KEY
```

---

# Foreign Key

Creates relationships.

Example:

```sql
FOREIGN KEY(customer_id)

REFERENCES customers(id)
```

---

# PostgreSQL SERIAL

Auto increment values.

Example:

```sql
id SERIAL PRIMARY KEY
```

---

# PostgreSQL Identity Columns

Modern alternative:

```sql
GENERATED ALWAYS AS IDENTITY
```

Benefits:

- SQL standard
- Better control

---

# CRUD Operations

Master:

- INSERT
- SELECT
- UPDATE
- DELETE

---

# Insert Data

Example:

```sql
INSERT INTO users

(name,email)

VALUES

('John',
'john@test.com');
```

---

# Select Data

Example:

```sql
SELECT *

FROM users;
```

---

# Filtering

Example:

```sql
SELECT *

FROM users

WHERE active=true;
```

---

# Sorting

Example:

```sql
ORDER BY created_at DESC;
```

---

# Pagination

Use:

```sql
LIMIT

OFFSET
```

Example:

```sql
SELECT *

FROM users

LIMIT 20
OFFSET 0;
```

---

# PostgreSQL Joins

Master:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN
- CROSS JOIN

---

# INNER JOIN

Returns matching records.

Example:

```sql
SELECT *

FROM users u

INNER JOIN orders o

ON u.id=o.user_id;
```

---

# LEFT JOIN

Returns:

- All left records
- Matching right records

---

# FULL JOIN

Returns:

- All records from both tables

---

# PostgreSQL Functions

Built-in functions:

- String functions
- Date functions
- Aggregate functions
- JSON functions

---

# Aggregate Functions

Master:

- COUNT
- SUM
- AVG
- MIN
- MAX

---

# GROUP BY

Example:

```sql
SELECT country,

COUNT(*)

FROM users

GROUP BY country;
```

---

# HAVING

Filter grouped data.

Example:

```sql
HAVING COUNT(*) > 100;
```

---

# PostgreSQL Views

Views store reusable queries.

Create:

```sql
CREATE VIEW active_users AS

SELECT *

FROM users

WHERE active=true;
```

---

# Materialized Views

Unlike normal views:

- Stores query result
- Improves performance
- Requires refresh

Example:

```sql
REFRESH MATERIALIZED VIEW report_view;
```

---

# PostgreSQL Stored Procedures

Reusable database logic.

Used for:

- Complex operations
- Data processing
- Automation

---

# PostgreSQL Functions

Functions return values.

Example:

```sql
CREATE FUNCTION add_numbers()

RETURNS INTEGER

AS $$

BEGIN

RETURN 10;

END;

$$ LANGUAGE plpgsql;
```

---

# PL/pgSQL

PostgreSQL procedural language.

Supports:

- Variables
- Conditions
- Loops
- Exception handling

---

# PostgreSQL Triggers

Automatically execute logic.

Events:

- BEFORE INSERT
- AFTER INSERT
- BEFORE UPDATE
- AFTER DELETE

---

# Trigger Use Cases

Use for:

- Audit logging
- Data validation
- Automatic updates

---

````markdown id="pgpart2"
# PostgreSQL Database Design

Master professional database design principles for PostgreSQL systems.

A good PostgreSQL design provides:

- Data consistency
- High performance
- Scalability
- Maintainability
- Security
- Efficient querying

---

# Database Design Process

Follow:

```
Business Requirements

        |

Entity Identification

        |

ER Diagram

        |

Schema Design

        |

Normalization

        |

Index Strategy

        |

Performance Testing
```

---

# Entity Relationship Model

Master:

- Entities
- Attributes
- Relationships
- Cardinality
- Constraints

Example:

```
Customer

    |

    |

Orders

    |

    |

Products
```

---

# PostgreSQL Normalization

Normalization reduces:

- Duplicate data
- Update anomalies
- Storage waste

---

# First Normal Form (1NF)

Rules:

- Atomic values
- No repeating groups
- Single value per column

Bad:

```
users

id

phones

9876,8765
```

Good:

```
user_phone

user_id

phone
```

---

# Second Normal Form (2NF)

Rules:

- Must satisfy 1NF
- Remove partial dependencies

Used mainly with:

- Composite primary keys

---

# Third Normal Form (3NF)

Rules:

- Must satisfy 2NF
- Remove transitive dependencies

Example:

Avoid:

```
Employee

employee_id

department_name

department_location
```

Better:

```
Employee

Department
```

---

# Denormalization

Adding controlled duplication for performance.

Used in:

- Analytics systems
- Reporting systems
- Read-heavy applications

---

# PostgreSQL Relationships

Master:

## One-to-One

Example:

```
User

 |

Profile
```

---

## One-to-Many

Example:

```
Customer

 |

Orders
```

---

## Many-to-Many

Example:

```
Students

 |

Courses
```

Requires:

```
student_course

student_id

course_id
```

---

# PostgreSQL Advanced Indexing

Indexes improve query performance.

Without index:

```
Sequential Scan

Every Row Checked
```

With index:

```
Index Lookup

Direct Access
```

---

# PostgreSQL Index Types

Master:

- B-Tree
- Hash
- GIN
- GiST
- SP-GiST
- BRIN

---

# B-Tree Index

Default PostgreSQL index.

Best for:

- Equality searches
- Range queries
- Sorting

Example:

```sql
CREATE INDEX users_email_idx

ON users(email);
```

---

# Hash Index

Optimized for:

- Equality comparisons

Example:

```sql
WHERE id = 100
```

---

# GIN Index

Generalized Inverted Index.

Used for:

- JSONB
- Arrays
- Full-text search

Example:

```sql
CREATE INDEX data_idx

ON products

USING GIN(attributes);
```

---

# GiST Index

Generalized Search Tree.

Used for:

- Geospatial data
- Complex data types
- Range queries

---

# BRIN Index

Block Range Index.

Useful for:

- Very large tables
- Time-series data

Example:

```
Logs Table

Billions of Rows
```

---

# Composite Indexes

Index multiple columns.

Example:

```sql
CREATE INDEX user_search_idx

ON users(country,status);
```

---

# Composite Index Rules

Index order matters.

Index:

```
(country,status)
```

Supports:

```
country

country + status
```

Less useful:

```
status alone
```

---

# Partial Index

Index only required rows.

Example:

```sql
CREATE INDEX active_users_idx

ON users(email)

WHERE active=true;
```

Benefits:

- Smaller index
- Faster queries

---

# Expression Index

Index calculated values.

Example:

```sql
CREATE INDEX lower_email_idx

ON users(
LOWER(email)
);
```

---

# Query Optimization

Optimize PostgreSQL queries using:

- Query planning
- Index analysis
- Execution analysis
- Statistics

---

# EXPLAIN Command

Analyze query execution.

Example:

```sql
EXPLAIN

SELECT *

FROM users

WHERE email='test@test.com';
```

---

# EXPLAIN ANALYZE

Runs query and shows actual performance.

Example:

```sql
EXPLAIN ANALYZE

SELECT *

FROM orders;
```

Shows:

- Execution time
- Rows scanned
- Index usage

---

# Query Planner

PostgreSQL optimizer decides:

- Join strategy
- Index usage
- Execution order

---

# Query Planning Strategies

Master:

- Sequential scan
- Index scan
- Bitmap scan
- Nested loop join
- Hash join
- Merge join

---

# Avoid SELECT *

Bad:

```sql
SELECT *

FROM users;
```

Better:

```sql
SELECT id,name

FROM users;
```

Benefits:

- Less memory
- Faster transfer

---

# Pagination Strategies

## Offset Pagination

Example:

```sql
LIMIT 20

OFFSET 100;
```

Problem:

Slow for large datasets.

---

# Cursor Pagination

Better for large systems.

Example:

```
Last ID received

        |

Next Query Starts From ID
```

Used by:

- Social media feeds
- Large APIs

---

# PostgreSQL Transactions

Transactions maintain data consistency.

Example:

```
Bank Transfer

 |

Debit Account

 |

Credit Account

 |

Commit
```

---

# ACID Properties

Master:

## Atomicity

All operations succeed or rollback.

---

## Consistency

Database remains valid.

---

## Isolation

Concurrent transactions do not conflict.

---

## Durability

Committed data persists.

---

# Transaction Commands

Start:

```sql
BEGIN;
```

Commit:

```sql
COMMIT;
```

Rollback:

```sql
ROLLBACK;
```

---

# PostgreSQL MVCC

Multi-Version Concurrency Control.

Allows:

- Multiple readers
- Writers without blocking readers

---

# MVCC Concept

Instead of overwriting rows:

```
Old Version

+

New Version
```

PostgreSQL maintains row versions.

---

# Vacuum Process

Removes old row versions.

Commands:

```sql
VACUUM;
```

---

# VACUUM Types

## VACUUM

Reclaims storage.

---

## VACUUM ANALYZE

Updates query statistics.

---

## VACUUM FULL

Completely rebuilds table.

Use carefully.

---

# PostgreSQL Locks

Control concurrent access.

Types:

- Row locks
- Table locks
- Advisory locks

---

# Row Locking

Example:

```sql
SELECT *

FROM orders

FOR UPDATE;
```

Locks selected rows.

---

# Deadlocks

Occurs when:

```
Transaction A waits for B

Transaction B waits for A
```

Solutions:

- Keep transactions short
- Lock resources consistently
- Monitor queries

---

# PostgreSQL JSON Support

PostgreSQL supports:

- JSON
- JSONB

---

# JSONB Advantages

Provides:

- Faster searching
- Index support
- Binary storage

---

# JSONB Query Example

Data:

```json
{
"name":"Laptop",
"price":1000
}
```

Query:

```sql
SELECT *

FROM products

WHERE data->>'name'='Laptop';
```

---

# JSONB Operators

Master:

```
->

->>

#

#

>>
```

---

# JSONB Indexing

Use GIN indexes.

Example:

```sql
CREATE INDEX product_json_idx

ON products

USING GIN(data);
```

---

# Full Text Search

PostgreSQL provides built-in search.

Used for:

- Documents
- Articles
- Product search

---

# Full Text Search Components

Master:

- tsvector
- tsquery
- Ranking

---

# Full Text Example

Create search vector:

```sql
to_tsvector(
'english',
content
)
```

Search:

```sql
to_tsquery(
'postgresql'
)
```

---

# PostgreSQL Extensions

Extensions add features.

List extensions:

```sql
\dx
```

---

# Popular PostgreSQL Extensions

Master:

- PostGIS
- pg_stat_statements
- pgcrypto
- pg_trgm
- pgvector

---

# PostGIS

Used for:

- Geographic data
- Maps
- Location services

---

# pg_stat_statements

Monitor:

- Query execution
- Query performance
- Database workload

---

# pgcrypto

Provides:

- Encryption functions
- Hashing functions

---

# pg_trgm

Used for:

- Similarity search
- Fuzzy matching

---

# pgvector

Important for AI applications.

Provides:

- Vector storage
- Similarity search
- Embedding retrieval

---

````markdown id="pgpart3"
# PostgreSQL Replication

Master PostgreSQL replication for high availability and scalability.

Replication provides:

- Data redundancy
- Disaster recovery
- Read scaling
- High availability

---

# PostgreSQL Replication Architecture

```
Primary Database

        |

Write Operations

        |

WAL Records

        |

Replica Database

        |

Read Operations
```

---

# Write Ahead Logging (WAL)

WAL is the foundation of PostgreSQL recovery and replication.

Before changing data:

```
Transaction

        |

Write WAL Log

        |

Modify Database Files
```

Benefits:

- Crash recovery
- Replication
- Data durability

---

# WAL Components

Master:

- WAL files
- WAL sender
- WAL receiver
- Checkpoints

---

# Streaming Replication

Most common PostgreSQL replication method.

Flow:

```
Primary Server

        |

WAL Stream

        |

Standby Server
```

---

# Primary Server

Handles:

- INSERT
- UPDATE
- DELETE
- Transactions

---

# Standby Server

Handles:

- Replicated data
- Read queries
- Backup workloads

---

# Read Replica Architecture

```
Application

        |

Load Balancer

        |

-----------------

Primary Database

        |

Read Replicas

-----------------

```

---

# Replication Use Cases

Use replication for:

- Large applications
- High traffic systems
- Reporting systems
- Disaster recovery

---

# PostgreSQL High Availability

High availability ensures:

- Minimum downtime
- Automatic recovery
- Data protection

---

# High Availability Architecture

```
Application

        |

Load Balancer

        |

-------------------

Primary Node

Replica Node

Backup Node

-------------------

```

---

# Automatic Failover

Failover process:

```
Primary Failure

        |

Detect Failure

        |

Promote Replica

        |

Redirect Traffic

        |

Continue Service
```

---

# PostgreSQL HA Tools

Master:

- Patroni
- PgBouncer
- HAProxy
- repmgr
- pg_auto_failover

---

# Patroni

Provides:

- Automatic failover
- Cluster management
- Leader election

Uses:

- etcd
- Consul
- Kubernetes

---

# Connection Pooling

Database connections are expensive.

Without pooling:

```
Request

 |

Create Connection

 |

Query

 |

Close Connection
```

With pooling:

```
Connection Pool

 |

Reusable Connections

 |

Database
```

---

# PgBouncer

Popular PostgreSQL connection pooler.

Provides:

- Connection reuse
- Better scalability
- Lower overhead

---

# PgBouncer Pool Modes

Master:

## Session Pooling

Connection assigned per session.

---

## Transaction Pooling

Connection assigned per transaction.

---

## Statement Pooling

Connection assigned per statement.

---

# PostgreSQL Backup

Master backup strategies.

Types:

- Logical backup
- Physical backup
- Continuous backup
- Point-in-time recovery

---

# pg_dump

Logical backup tool.

Example:

```bash
pg_dump database_name > backup.sql
```

---

# Restore Backup

Example:

```bash
psql database_name < backup.sql
```

---

# pg_restore

Used for:

- Custom format backups
- Selective restore
- Parallel restore

---

# Physical Backup

Copies:

- Database files
- WAL files

Tools:

- pg_basebackup

---

# Point In Time Recovery (PITR)

Restore database to a specific time.

Example:

```
Database Failure

        |

Restore Backup

        |

Replay WAL Logs

        |

Recover Until Desired Time
```

---

# Backup Best Practices

Always:

- Automate backups
- Test restoration
- Encrypt backups
- Store remotely
- Monitor backup success

---

# PostgreSQL Security

Secure PostgreSQL databases.

Security areas:

- Authentication
- Authorization
- Encryption
- Auditing
- Network security

---

# Authentication Methods

PostgreSQL supports:

- Password authentication
- Certificate authentication
- LDAP
- Kerberos
- Cloud IAM

---

# pg_hba.conf

Controls client authentication.

Example:

```
host

database

user

address

method
```

---

# User Management

Create user:

```sql
CREATE USER developer

WITH PASSWORD 'password';
```

---

# Roles

PostgreSQL uses roles for:

- Users
- Groups
- Permissions

---

# Grant Permissions

Example:

```sql
GRANT SELECT

ON users

TO developer;
```

---

# Revoke Permissions

Example:

```sql
REVOKE INSERT

ON users

FROM developer;
```

---

# Least Privilege Principle

Applications should have:

- Required permissions only
- Separate database users
- Restricted access

---

# SSL Encryption

Encrypt database connections.

Architecture:

```
Application

        |

Encrypted SSL Connection

        |

PostgreSQL
```

---

# Data Encryption

Protect:

- Sensitive columns
- Backups
- Communication

Tools:

- pgcrypto
- Application encryption

---

# PostgreSQL Performance Tuning

Optimize:

- Queries
- Memory
- Indexes
- Configuration
- Connections

---

# Performance Tuning Process

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

# Important Configuration Parameters

Master:

- shared_buffers
- work_mem
- maintenance_work_mem
- effective_cache_size
- max_connections

---

# shared_buffers

Controls PostgreSQL memory cache.

Used for:

- Frequently accessed pages
- Query performance

---

# work_mem

Memory used for:

- Sorting
- Hash operations
- Joins

---

# max_connections

Controls:

- Number of database connections

Too high:

- Memory pressure

Too low:

- Connection failures

---

# Query Optimization Techniques

Use:

- Proper indexes
- Query rewriting
- Execution analysis
- Partitioning

---

# PostgreSQL Monitoring

Monitor:

- Query performance
- Connections
- Locks
- Storage
- Replication

---

# Monitoring Tools

Use:

- pg_stat_activity
- pg_stat_database
- pg_stat_statements
- Prometheus
- Grafana

---

# pg_stat_activity

Shows:

- Active connections
- Running queries
- Query duration

Example:

```sql
SELECT *

FROM pg_stat_activity;
```

---

# pg_stat_statements

Tracks:

- Query execution count
- Execution time
- Resource usage

---

# PostgreSQL Partitioning

Partition large tables.

Useful for:

- Logs
- Events
- Time-series data

---

# Partition Types

Master:

- Range partitioning
- List partitioning
- Hash partitioning

---

# Range Partition Example

Partition by date:

```
orders_2024

orders_2025

orders_2026
```

---

# PostgreSQL Sharding

Distribute data across servers.

Used for:

- Very large datasets
- Global applications

Tools:

- Citus
- Application-level sharding

---

# PostgreSQL Cloud Deployment

Deploy PostgreSQL using:

- AWS RDS PostgreSQL
- Aurora PostgreSQL
- Azure Database for PostgreSQL
- Google Cloud SQL
- Supabase

---

# Managed PostgreSQL Benefits

Provides:

- Automated backups
- Monitoring
- Scaling
- Security updates
- High availability

---

# Docker PostgreSQL

Run PostgreSQL container.

Example:

```bash
docker run

--name postgres-db

-e POSTGRES_PASSWORD=password

-p 5432:5432

postgres
```

---

# Docker Compose PostgreSQL

Architecture:

```
Backend API

        |

PostgreSQL Container

        |

Persistent Storage
```

---

# PostgreSQL Microservices Architecture

Example:

```
API Gateway

        |

--------------------

User Service

Order Service

Payment Service

--------------------

        |

PostgreSQL Databases
```

---

# Database Per Service Pattern

Each microservice owns:

- Own database
- Own schema
- Own migrations

Benefits:

- Loose coupling
- Independent scaling

---

# PostgreSQL AI Integration

PostgreSQL is widely used in AI applications.

Use cases:

- AI memory
- Embedding storage
- Semantic search
- RAG systems

---

# PostgreSQL AI Architecture

```
AI Agent

        |

Backend API

        |

PostgreSQL

        |

Application Data

        |

Vector Store
```

---

# pgvector Extension

Important for AI systems.

Provides:

- Vector data type
- Similarity search
- Embedding storage

---

# Vector Search Example

Store:

```
Document

        |

Embedding Vector

        |

Similarity Search
```

---

# RAG Architecture With PostgreSQL

```
User Question

        |

Embedding Generation

        |

Vector Search

        |

Retrieve Documents

        |

LLM Response
```

---

# PostgreSQL AI Agent Rules

The PostgreSQL AI agent must always:

1. Design scalable schemas.

2. Use proper normalization.

3. Create efficient indexes.

4. Analyze query plans.

5. Protect database access.

6. Use transactions correctly.

7. Optimize PostgreSQL configuration.

8. Handle migrations safely.

9. Monitor database performance.

10. Consider replication strategy.

11. Support AI data requirements.

12. Produce production-ready solutions.

---

# PostgreSQL Expert Mindset

Think like:

- Database Architect
- PostgreSQL Administrator
- Performance Engineer
- Data Engineer
- AI Database Engineer

Build PostgreSQL systems that are:

- Reliable
- Secure
- Scalable
- High performance
- Production ready

---

# PostgreSQL Production Checklist

## Database Design

- Schema reviewed
- Relationships optimized
- Constraints applied

---

## Performance

- Indexes optimized
- Queries analyzed
- Monitoring enabled

---

## Security

- Roles configured
- SSL enabled
- Permissions restricted

---

## Operations

- Backup automated
- Recovery tested
- Replication configured

---

## AI Readiness

- JSONB strategy defined
- pgvector planned
- Embedding storage designed

---
