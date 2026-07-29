---
name: reactjs
description: Expert knowledge of ReactJS including modern React architecture, functional components, JSX, hooks, state management, concurrent rendering, React Compiler, React Server Components, React 19 features, performance optimization, accessibility, security, testing, enterprise application architecture, component design systems, frontend engineering best practices, and scalable production-grade React applications. This skill enables AI agents to design, develop, review, debug, optimize, migrate, test, document, and maintain modern React applications following professional frontend engineering standards.
---

# ReactJS Skill

# Primary Responsibilities

The ReactJS skill must be capable of:

- Designing React applications
- Creating reusable components
- Building scalable frontend architectures
- Managing application state
- Designing component systems
- Implementing responsive interfaces
- Building accessible applications
- Integrating APIs
- Handling authentication
- Managing client state
- Managing server state
- Optimizing performance
- Testing applications
- Reviewing React code
- Refactoring legacy applications
- Migrating React versions
- Building enterprise applications
- Creating frontend libraries
- Building design systems
- Implementing modern React patterns

---

# Capabilities

The ReactJS expert agent can:

- Generate React components
- Generate hooks
- Create reusable UI components
- Design component architecture
- Build React applications
- Build dashboards
- Build SaaS applications
- Build admin panels
- Build e-commerce applications
- Build enterprise applications
- Build design systems
- Create React libraries
- Optimize rendering performance
- Debug React issues
- Review pull requests
- Improve application architecture
- Implement authentication
- Implement authorization
- Integrate REST APIs
- Integrate GraphQL APIs
- Integrate WebSockets
- Build real-time applications
- Create testing strategies
- Configure build pipelines
- Deploy React applications

---

# Skill Instructions

You are an expert ReactJS architect with extensive experience building enterprise-scale frontend applications.

Your responsibility is to create, review, debug, optimize, migrate, and architect React applications using modern React standards.

Always produce:

- Production-ready code
- Clean architecture
- Strong TypeScript support
- Reusable components
- Accessible UI
- Secure implementations
- Performant applications
- Maintainable code
- Testable solutions

---

# React Philosophy

Understand React as:

- Component-based UI library
- Declarative UI framework
- State-driven rendering system
- Functional programming approach
- Unidirectional data flow architecture

Core principles:

- UI is a function of state
- Components should be composable
- State should be predictable
- Logic should be reusable
- Rendering should be optimized

---

# React Evolution

Understand React evolution.

---

## React Early Versions

Master:

- React Components
- JSX
- Virtual DOM
- Component Lifecycle
- Class Components

---

## React Modern Era

Master:

- Functional Components
- Hooks
- Concurrent Rendering
- Suspense
- Server Components
- React Compiler
- Actions
- Modern State Patterns

---

# React Versions Knowledge

Understand:

- React 15
- React 16
- React 17
- React 18
- React 19
- Future React Releases

Understand:

- Breaking Changes
- Migration Paths
- Deprecated APIs
- New Features
- Performance Improvements

---

# React Architecture

Master different React architectures.

---

## Component-Based Architecture

React applications are built using:

- Components
- Composition
- Props
- State
- Hooks

Example:

```
Application

 |

Components

 |

UI Elements
```

---

## Feature-Based Architecture

Recommended enterprise structure.

Example:

```
src

├── app

├── features

│   ├── users

│   │   ├── components

│   │   ├── hooks

│   │   ├── services

│   │   ├── api

│   │   ├── models

│   │   └── state

│   │

│   ├── products

│   └── orders

├── shared

├── components

├── hooks

├── utils

├── services

├── styles

└── assets
```

---

# Enterprise React Folder Structure

Recommended structure:

```
src

├── app

│   ├── router

│   ├── providers

│   ├── config

│   └── store

│

├── features

│   ├── authentication

│   ├── dashboard

│   ├── users

│   ├── reports

│   └── settings

│

├── shared

│   ├── components

│   ├── hooks

│   ├── utils

│   ├── constants

│   ├── types

│   └── validation

│

├── api

│

├── assets

│

├── layouts

│

├── routes

│

├── styles

│

└── main.tsx
```

---

# React Setup

Master React project setup.

Tools:

- Vite
- Create React App
- Next.js
- Remix
- Gatsby

Prefer:

- Vite for modern SPA applications
- Next.js for full-stack React applications

---

# Vite

Master:

- Vite Configuration
- Development Server
- Build Process
- Environment Variables
- Plugins
- Optimization

Commands:

```bash
npm create vite
npm run dev
npm run build
npm run preview
```

---

# Package Management

Master:

- npm
- yarn
- pnpm

Understand:

- package.json
- package-lock.json
- dependencies
- devDependencies
- peerDependencies

---

# TypeScript Integration

React applications should prefer TypeScript.

Master:

- Interfaces
- Types
- Generics
- Utility Types
- Type Inference
- Type Guards
- JSX Types
- Component Props Types
- Hook Types

---

# TypeScript Rules

Always:

- Enable strict mode
- Avoid any
- Define component contracts
- Type API responses
- Type state
- Type hooks

Avoid:

```typescript
const data:any;
```

Prefer:

```typescript
interface User {
 id:number;
 name:string;
}
```

---

# JSX

Master JSX completely.

Understand:

- JSX Syntax
- JSX Expressions
- JSX Attributes
- JSX Children
- Conditional Rendering
- Lists
- Fragments

Example:

```tsx
function App(){

 return (
   <h1>Hello React</h1>
 );

}
```

---

# JSX Rules

JSX should contain:

- UI structure
- Simple conditions
- Rendering logic

Avoid:

- Business logic
- API calls
- Complex calculations

---

# JSX Expressions

Support:

- Variables
- Functions
- Expressions
- Ternary operators
- Logical operators

Example:

```tsx
{
 isLoggedIn 
 ? <Dashboard/>
 : <Login/>
}
```

---

# React Components

Master all component types.

---

## Functional Components

Modern React standard.

Example:

```tsx
function UserCard(){

 return (
   <div>User</div>
 );

}
```

Prefer:

- Functional Components
- Hooks
- Composition

---

## Class Components

Understand legacy concepts:

- Constructor
- State
- Lifecycle Methods
- setState
- Error Boundaries

Maintain knowledge for legacy applications.

---

# Component Design

Every component should have:

- Single responsibility
- Clear props
- Predictable behavior
- Reusable design
- Easy testing

Avoid:

- Giant components
- Mixed responsibilities
- Hidden side effects

---

# Component Categories

Master:

## Presentational Components

Responsible for:

- UI
- Styling
- Rendering

---

## Container Components

Responsible for:

- Data
- State
- Business logic

---

## Layout Components

Responsible for:

- Page structure
- Navigation
- Common layouts

---

## Feature Components

Responsible for:

- Business workflows
- User actions

---

# Component Composition

React prefers composition over inheritance.

Use:

- Children props
- Render props
- Higher Order Components
- Custom Hooks

Avoid:

- Deep inheritance
- Tight coupling

---

# Props

Master React Props.

Understand:

- Passing data
- Props validation
- Default props
- Children props
- Callback props
- Render props

Example:

```tsx
<UserCard user={user}/>
```

---

# Props Best Practices

Always:

- Keep props simple
- Use TypeScript interfaces
- Avoid unnecessary props
- Prefer composition

Avoid:

- Passing huge objects
- Passing unnecessary callbacks

---

````markdown id="react2"
# React State Management

Master React state management completely.

Understand:

- Local Component State
- Shared State
- Global State
- Server State
- Client State
- URL State
- Form State
- Cache State
- Persistent State

Choose the correct state solution based on:

- Application complexity
- Team size
- Data ownership
- Performance requirements
- Maintainability

---

# React State Principles

Follow:

- Keep state as local as possible
- Avoid unnecessary global state
- Derive values instead of storing duplicates
- Keep state immutable
- Normalize complex state
- Separate server state from client state

Avoid:

- Duplicate state
- Deep prop drilling
- Excessive Context usage
- Storing everything globally

---

# useState Hook

Master useState.

Purpose:

Manage local component state.

Example:

```tsx
const [count, setCount] = useState(0);
```

Use for:

- UI state
- Form fields
- Toggles
- Selected items
- Local data

---

# useState Best Practices

Prefer:

```tsx
const [user, setUser] = useState<User | null>(null);
```

Avoid:

```tsx
const [data,setData]=useState<any>();
```

Always:

- Use proper types
- Keep state minimal
- Avoid unnecessary updates

---

# State Updates

Understand:

- Functional Updates
- Batch Updates
- Async State Updates
- State Queueing

Example:

```tsx
setCount(previous => previous + 1);
```

Use functional updates when new state depends on previous state.

---

# Immutable State Updates

Always update state immutably.

Avoid:

```tsx
user.name="John";
```

Prefer:

```tsx
setUser({
 ...user,
 name:"John"
});
```

Benefits:

- Predictable rendering
- Better debugging
- Easier testing

---

# useReducer Hook

Master useReducer.

Use for:

- Complex state
- Multiple state transitions
- Business workflows

Example:

```tsx
const [state,dispatch]=useReducer(
 reducer,
 initialState
);
```

---

# Reducer Pattern

Architecture:

```
Component

 |

Dispatch Action

 |

Reducer

 |

New State
```

Reducer responsibilities:

- Receive current state
- Receive action
- Return new state

Avoid:

- API calls inside reducers
- Side effects
- Mutations

---

# Reducer Actions

Design clear actions.

Example:

```typescript
{
 type:"USER_LOGIN",
 payload:user
}
```

Common actions:

- CREATE
- UPDATE
- DELETE
- FETCH_SUCCESS
- FETCH_ERROR
- RESET

---

# Complex State Management

For complex state use:

- useReducer
- Context
- Zustand
- Redux Toolkit
- MobX
- Jotai

Avoid creating custom solutions unnecessarily.

---

# React Context API

Master Context API.

Purpose:

Share data across component trees.

Use cases:

- Theme
- Authentication
- Language
- Configuration
- User Preferences

---

# Context Architecture

Structure:

```
Provider

 |

Consumer Components
```

Example:

```tsx
<UserProvider>

<App/>

</UserProvider>
```

---

# Context Best Practices

Use Context for:

- Stable global values
- Application configuration
- Authentication state

Avoid:

- Frequently changing state
- Large application stores

Reason:

Context updates can trigger unnecessary renders.

---

# Custom Context Pattern

Create:

```
context

├── AuthContext.tsx

├── ThemeContext.tsx

└── ConfigContext.tsx
```

Include:

- Provider
- Hook
- Types
- Default values

---

# Custom Hooks

Master custom hooks.

Purpose:

Extract reusable logic.

Examples:

- useAuth()
- useFetch()
- useDebounce()
- useForm()
- usePagination()
- usePermission()

---

# Custom Hook Rules

Hooks must:

- Start with use
- Follow hook rules
- Be reusable
- Avoid hidden side effects

Example:

```tsx
function useUser(){
 return userData;
}
```

---

# Hook Composition

Combine hooks.

Example:

```
useUser

 |

useApi

 |

useAuthToken
```

Benefits:

- Reusable logic
- Cleaner components
- Better testing

---

# React Hooks Complete Mastery

Master built-in hooks:

- useState
- useEffect
- useContext
- useReducer
- useMemo
- useCallback
- useRef
- useImperativeHandle
- useLayoutEffect
- useDebugValue
- useTransition
- useDeferredValue
- useId
- useSyncExternalStore

---

# useEffect Hook

Master side effects.

Use for:

- API calls
- Event listeners
- Timers
- External subscriptions
- Browser APIs

Example:

```tsx
useEffect(()=>{

 loadUsers();

},[]);
```

---

# useEffect Rules

Avoid:

- Unnecessary effects
- Derived state effects
- Infinite loops
- Missing dependencies

Always:

- Cleanup resources
- Handle async operations
- Manage dependencies correctly

---

# useEffect Cleanup

Cleanup:

- Subscriptions
- Timers
- Event listeners
- WebSocket connections

Example:

```tsx
useEffect(()=>{

 const timer=setInterval(()=>{},1000);

 return ()=>{
   clearInterval(timer);
 };

},[]);
```

---

# Async Operations in Effects

Handle:

- Loading state
- Error state
- Cancellation
- Cleanup

Prefer:

```tsx
async function loadData(){

}
```

inside effect with proper handling.

---

# useMemo Hook

Master memoized calculations.

Use for:

- Expensive calculations
- Derived values
- Heavy transformations

Example:

```tsx
const filteredUsers = useMemo(
 ()=>users.filter(x=>x.active),
 [users]
);
```

Avoid:

- Memoizing everything
- Premature optimization

---

# useCallback Hook

Master function memoization.

Use for:

- Stable callbacks
- Child component optimization
- Dependency management

Example:

```tsx
const handleClick =
useCallback(()=>{

},[]);
```

---

# React.memo

Master component memoization.

Purpose:

Prevent unnecessary re-renders.

Example:

```tsx
export default React.memo(UserCard);
```

Use when:

- Component renders frequently
- Props rarely change

---

# useRef Hook

Master references.

Use for:

- DOM access
- Previous values
- Mutable references
- Timers
- External libraries

Example:

```tsx
const inputRef=useRef<HTMLInputElement>(null);
```

---

# useLayoutEffect

Understand difference:

useEffect:

- Runs after paint

useLayoutEffect:

- Runs before browser paint

Use for:

- DOM measurements
- Layout calculations

Avoid unnecessary usage.

---

# useTransition

Master concurrent UI updates.

Use for:

- Non-urgent updates
- Large rendering operations
- Search filtering

Example:

```tsx
const [
 isPending,
 startTransition
]=useTransition();
```

---

# useDeferredValue

Optimize slow rendering.

Use for:

- Expensive lists
- Search results
- Heavy UI updates

---

# useId

Generate unique IDs.

Use for:

- Accessibility
- Form labels
- Component identifiers

---

# useSyncExternalStore

Use for:

- External state libraries
- Browser stores
- Custom subscriptions

---

# React Rendering Model

Master how React renders.

Understand:

- Render Phase
- Commit Phase
- Reconciliation
- Fiber Architecture
- Virtual DOM

---

# React Render Process

Flow:

```
State Change

 |

Render Phase

 |

Virtual DOM Comparison

 |

Commit Phase

 |

Browser Update
```

---

# Virtual DOM

Understand:

- Virtual DOM creation
- Diffing algorithm
- Reconciliation
- DOM updates

Benefits:

- Efficient updates
- Declarative programming
- Better developer experience

---

# React Fiber Architecture

Master:

- Fiber Nodes
- Incremental Rendering
- Scheduling
- Priorities
- Concurrent Work

Understand how React manages rendering internally.

---

# Reconciliation

Understand:

React compares:

Previous Tree

vs

New Tree

Then updates only required changes.

Optimization depends on:

- Keys
- Component structure
- Memoization

---

# React Keys

Always provide stable keys.

Good:

```tsx
users.map(user=>
 <User key={user.id}/>
)
```

Avoid:

```tsx
key={index}
```

unless list order never changes.

---

# Rendering Optimization

Optimize:

- Component renders
- State updates
- Large lists
- Expensive calculations

Use:

- React.memo
- useMemo
- useCallback
- Virtualization
- Code splitting

---

# Avoid Unnecessary Rendering

Common causes:

- Parent re-render
- New object references
- New function references
- Context updates
- State placement

Solutions:

- Component splitting
- Memoization
- Better state location

---

# React Strict Mode

Understand:

- Development checks
- Double rendering behavior
- Side effect detection
- Deprecated API detection

Use in development.

---

# React Concurrent Rendering

Master modern concurrent features.

Understand:

- Interruptible rendering
- Scheduling
- Priorities
- Transitions
- Suspense integration

Benefits:

- Smoother user experience
- Responsive interfaces
- Better rendering control

---

````markdown id="react3"
# React 19 Features

Master modern React features introduced in React 19.

Understand:

- Actions
- Server Components
- Server Actions
- use()
- Form Actions
- Optimistic Updates
- New Hooks
- Improved Hydration
- React Compiler Integration

---

# React Actions

Understand React Actions architecture.

Actions simplify:

- Form submissions
- Async operations
- Data mutations
- Loading states
- Error handling

Traditional approach:

```
Submit Button

 |

Loading State

 |

API Call

 |

Success/Error Handling
```

Modern approach:

```
Action

 |

React manages

- Pending State
- Errors
- Updates
```

---

# useActionState Hook

Master:

- useActionState
- Action lifecycle
- Pending state
- Error handling

Use cases:

- Forms
- Authentication
- Data mutations
- Server actions

Example:

```tsx
const [
 state,
 action,
 pending
] = useActionState(
 submitForm,
 initialState
);
```

---

# useFormStatus Hook

Master form status management.

Use for:

- Submit buttons
- Loading indicators
- Form feedback

Example:

```tsx
const {
 pending
}=useFormStatus();
```

Benefits:

- Cleaner forms
- Less manual state handling

---

# useOptimistic Hook

Master optimistic UI updates.

Purpose:

Update UI immediately before server confirmation.

Flow:

```
User Action

 |

Optimistic Update

 |

Server Request

 |

Confirm / Rollback
```

Use cases:

- Likes
- Comments
- Messaging
- Cart Updates

---

# React Compiler

Master React Compiler concepts.

Understand:

- Automatic memoization
- Render optimization
- Compiler transformations
- Component optimization

Purpose:

Reduce manual optimization.

Future React applications can rely less on:

- useMemo
- useCallback
- React.memo

---

# React Compiler Rules

Write compiler-friendly code.

Prefer:

- Pure components
- Immutable data
- Predictable hooks
- Clean rendering logic

Avoid:

- Hidden mutations
- Side effects during rendering
- Dynamic hook usage

---

# React Server Components (RSC)

Master React Server Components.

Understand:

- Server rendering
- Client components
- Component boundaries
- Data fetching
- Bundle reduction

Architecture:

```
Server Components

        |

Client Components

        |

Browser
```

---

# Server Components

Run on:

- Server

Benefits:

- Smaller client bundles
- Direct backend access
- Faster initial load
- Better SEO

Cannot use:

- Browser APIs
- useState
- useEffect

---

# Client Components

Run in:

- Browser

Used for:

- Interactions
- State
- Events
- Browser APIs

Examples:

- Buttons
- Forms
- Modals
- Interactive widgets

---

# Component Boundary Design

Decide:

Server Component:

- Data fetching
- Static content
- Heavy processing

Client Component:

- User interaction
- Dynamic state
- Browser features

---

# Suspense

Master React Suspense.

Purpose:

Handle asynchronous rendering.

Use cases:

- Lazy loading
- Data fetching
- Streaming UI

Example:

```tsx
<Suspense fallback={<Loader/>}>
 <Dashboard/>
</Suspense>
```

---

# Suspense Patterns

Master:

- Component loading
- Route loading
- Streaming content
- Progressive rendering

---

# Lazy Loading Components

Master:

```tsx
React.lazy()
```

Example:

```tsx
const Dashboard =
lazy(()=>import('./Dashboard'));
```

Benefits:

- Smaller bundles
- Faster initial load

---

# Error Boundaries

Master error handling components.

Purpose:

Catch rendering errors.

Handle:

- Component crashes
- UI failures
- Runtime rendering issues

Architecture:

```
Error Boundary

 |

Child Components
```

---

# Error Boundary Design

Implement:

- Fallback UI
- Error logging
- Recovery actions

Integrate with:

- Sentry
- Datadog
- Application Monitoring Tools

---

# Data Fetching Architecture

Master modern React data fetching.

Understand:

- Client fetching
- Server fetching
- Cache management
- Synchronization
- Loading states
- Error states

---

# Fetch API

Master native fetch.

Handle:

- Requests
- Responses
- Errors
- AbortController
- JSON parsing

Example:

```typescript
const response =
await fetch('/api/users');
```

---

# Axios Integration

Master Axios.

Understand:

- Interceptors
- Headers
- Error handling
- Request cancellation
- Retry strategies

Architecture:

```
Component

 |

Service Layer

 |

Axios Client

 |

API
```

---

# API Service Layer

Do not call APIs directly everywhere.

Prefer:

```
Component

 |

Hook

 |

Service

 |

API Client
```

Benefits:

- Reusable logic
- Better testing
- Cleaner components

---

# REST API Integration

Master:

- GET
- POST
- PUT
- PATCH
- DELETE

Handle:

- Authentication
- Pagination
- Filtering
- Sorting
- Error states

---

# GraphQL Integration

Master:

- Queries
- Mutations
- Subscriptions
- Fragments
- Cache handling

Libraries:

- Apollo Client
- Relay
- urql

---

# WebSocket Integration

Build real-time applications.

Use cases:

- Chat
- Notifications
- Live dashboards
- Collaboration tools

Understand:

- Connection lifecycle
- Reconnection
- Authentication
- Message handling

---

# TanStack Query

Master React Query / TanStack Query.

Purpose:

Manage server state.

Handles:

- Fetching
- Caching
- Synchronization
- Background updates
- Refetching

---

# TanStack Query Concepts

Master:

- Query
- Mutation
- Query Key
- Query Cache
- Query Invalidation
- Prefetching
- Optimistic Updates

---

# Query Architecture

Example:

```
Component

 |

Custom Hook

 |

TanStack Query

 |

API Service

 |

Backend
```

---

# Query States

Handle:

- Loading
- Success
- Error
- Refetching
- Stale Data
- Cached Data

---

# Query Optimization

Use:

- Proper query keys
- Cache configuration
- Prefetching
- Pagination
- Infinite queries

---

# Infinite Queries

Master:

- Infinite scrolling
- Cursor pagination
- Load more patterns

Use cases:

- Social feeds
- Search results
- Product listings

---

# Server State vs Client State

Understand difference.

Server State:

- API data
- Users
- Products
- Orders

Use:

- TanStack Query

---

Client State:

- Theme
- Modal state
- UI preferences

Use:

- Context
- Zustand
- Redux

---

# React Forms

Master form development.

Understand:

- Controlled Components
- Uncontrolled Components
- Form Libraries
- Validation
- Async Submission

---

# Controlled Components

React manages form state.

Example:

```tsx
<input
 value={name}
 onChange={e=>setName(e.target.value)}
/>
```

Benefits:

- Predictable state
- Easy validation

---

# Uncontrolled Components

DOM manages state.

Use:

- useRef
- Native form APIs

Suitable for:

- Simple forms
- Performance-sensitive inputs

---

# React Hook Form

Master React Hook Form.

Benefits:

- High performance
- Minimal re-renders
- Easy validation
- TypeScript support

---

# React Hook Form Concepts

Master:

- useForm
- register
- Controller
- FormProvider
- useFieldArray
- Validation

---

# Form Validation

Master:

- Client validation
- Server validation
- Schema validation

Libraries:

- Zod
- Yup
- Joi
- Valibot

---

# Zod Integration

Master:

- Schema creation
- Type inference
- Validation
- Error handling

Example:

```typescript
const UserSchema =
z.object({
 name:z.string()
});
```

---

# Dynamic Forms

Build forms dynamically.

Support:

- JSON configuration
- Conditional fields
- Dynamic sections
- Custom controls

Use cases:

- CMS
- Enterprise systems
- Survey applications

---

# Multi Step Forms

Master:

- Wizard forms
- Step validation
- State persistence
- Navigation control

---

# Form Best Practices

Always:

- Validate user input
- Show clear errors
- Support accessibility
- Handle loading states
- Prevent duplicate submissions
- Sanitize data

---

````markdown id="react4"
# React Router

Master React routing architecture completely.

Understand:

- Client-side routing
- Route configuration
- Navigation
- Nested routes
- Protected routes
- Dynamic routes
- Lazy routes
- Route parameters
- Query parameters
- Data loading
- Route-based layouts

---

# React Router Fundamentals

Master:

- BrowserRouter
- Routes
- Route
- Link
- NavLink
- Outlet
- Navigate
- useNavigate
- useParams
- useLocation

Example:

```tsx
<BrowserRouter>

 <Routes>

  <Route 
    path="/users"
    element={<Users/>}
  />

 </Routes>

</BrowserRouter>
```

---

# Route Architecture

Enterprise routing structure:

```
src

├── routes

│   ├── index.tsx

│   ├── public.routes.tsx

│   ├── private.routes.tsx

│   └── feature.routes.tsx

```

Benefits:

- Maintainable routing
- Feature isolation
- Easier authorization

---

# Nested Routes

Master nested routing.

Example:

```
Dashboard

 |
 ├── Profile

 ├── Settings

 └── Reports
```

Implementation:

```tsx
<Route
 path="/dashboard"
 element={<Dashboard/>}
>

 <Route
  path="profile"
  element={<Profile/>}
 />

</Route>
```

---

# Layout Routes

Create reusable layouts.

Examples:

- Admin Layout
- User Layout
- Authentication Layout
- Marketing Layout

Structure:

```
Layout

 |

Outlet

 |

Child Routes
```

---

# Dynamic Routes

Master:

- URL Parameters
- Route Variables
- Dynamic Pages

Example:

```
/users/:id
```

Access:

```tsx
const {id}=useParams();
```

---

# Query Parameters

Master:

- Search params
- Filters
- Pagination
- Sorting

Example:

```
/products?page=2&sort=name
```

Use:

```tsx
useSearchParams()
```

---

# Navigation

Master:

## Declarative Navigation

Using:

- Link
- NavLink

Example:

```tsx
<Link to="/users">
Users
</Link>
```

---

## Programmatic Navigation

Using:

```tsx
const navigate=useNavigate();

navigate('/dashboard');
```

Use cases:

- Login redirect
- Form submission
- Workflow completion

---

# Protected Routes

Implement route protection.

Architecture:

```
Route

 |

Auth Guard

 |

Permission Check

 |

Component
```

Example:

```
PrivateRoute

 |
check user

 |
allow / redirect
```

---

# Authentication Routing

Handle:

- Login pages
- Logout flows
- Session expiry
- Token refresh
- Redirect URLs

---

# Authorization Routing

Support:

- Role-based routing
- Permission-based routing
- Feature access

Example:

```
Admin

 |
Reports Route

 |
Permission Check

 |
Access
```

---

# Lazy Loading Routes

Optimize bundle size.

Use:

```tsx
lazy(
 ()=>import('./Dashboard')
)
```

Benefits:

- Faster startup
- Smaller bundles
- Better performance

---

# Route Error Handling

Handle:

- Invalid routes
- Loading errors
- Permission errors
- Network errors

Provide:

- Error pages
- Recovery actions
- Logging

---

# State Management Architecture

Master professional React state management.

Understand:

- Local State
- Context
- Redux
- Zustand
- Jotai
- MobX
- Recoil
- Server State

---

# Redux Toolkit

Master modern Redux.

Avoid old Redux patterns.

Prefer:

- Redux Toolkit
- createSlice
- createAsyncThunk
- RTK Query

---

# Redux Architecture

Structure:

```
Application

 |

Store

 |

Slices

 |

Reducers

 |

State
```

---

# Redux Store

Master:

- configureStore
- Middleware
- DevTools
- Enhancers

Example:

```typescript
const store =
configureStore({

 reducer:{
  users:userReducer
 }

});
```

---

# Redux Slice

Master:

- State
- Reducers
- Actions

Example:

```typescript
createSlice({

name:"users",

initialState,

reducers:{}

})
```

---

# Redux Actions

Understand:

- Action creators
- Payloads
- Dispatching
- Async actions

Example:

```typescript
dispatch(
 userAdded(user)
)
```

---

# Redux Selectors

Master selectors.

Purpose:

Read state efficiently.

Example:

```typescript
const users=
useSelector(
 selectUsers
);
```

Benefits:

- Reusable queries
- Derived state
- Performance

---

# Redux Middleware

Master:

- Redux Thunk
- Custom Middleware
- Logging Middleware
- Analytics Middleware

Use cases:

- Side effects
- API calls
- Tracking

---

# RTK Query

Master server state using Redux Toolkit Query.

Features:

- API caching
- Automatic refetching
- Loading states
- Mutations
- Cache invalidation

Architecture:

```
Component

 |

RTK Query Hook

 |

API Slice

 |

Backend
```

---

# Zustand

Master lightweight state management.

Benefits:

- Simple API
- Minimal boilerplate
- Good performance

Example:

```typescript
const useStore=create(
 set=>({

 count:0,

 increment:()=>set(
 state=>({
 count:state.count+1
 })
 )

 })
)
```

---

# Zustand Best Practices

Use for:

- Global UI state
- Application state
- Small to medium applications

Avoid:

- Huge uncontrolled stores

---

# Jotai

Master atomic state management.

Concept:

```
Atom

 |

Component
```

Use:

- Independent state pieces
- Fine-grained updates

---

# Recoil

Understand:

- Atoms
- Selectors
- Derived State

Used for:

- Complex reactive state

---

# MobX

Understand:

- Observable state
- Actions
- Computed values
- Reactions

Useful for:

- Object-oriented state management

---

# State Management Selection Guide

Small App:

Use:

- useState
- Context
- Custom Hooks

---

Medium App:

Use:

- Zustand
- TanStack Query
- Context

---

Large Enterprise App:

Use:

- Redux Toolkit
- RTK Query
- Zustand
- Feature-based stores

---

# React Design Patterns

Master professional React patterns.

---

# Presentational Component Pattern

Purpose:

Separate UI from logic.

Example:

```
UserCard

Input:
user data

Output:
UI
```

---

# Container Component Pattern

Responsible for:

- Data fetching
- State
- Business logic

Example:

```
UsersContainer

 |

UsersList
```

---

# Custom Hook Pattern

Extract reusable logic.

Example:

```
useUsers()

 |

API Logic

 |

Component
```

---

# Compound Component Pattern

Build flexible APIs.

Example:

```tsx
<Select>

<Select.Option/>

<Select.Option/>

</Select>
```

Used in:

- Design systems
- UI libraries

---

# Render Props Pattern

Share logic through functions.

Example:

```tsx
<DataProvider>

{
 data=>(
 <Component data={data}/>
)

}

</DataProvider>
```

---

# Higher Order Component Pattern

Understand legacy pattern.

Structure:

```
Component

 |

HOC

 |

Enhanced Component
```

Used in older React applications.

---

# Provider Pattern

Used for:

- Context
- Theme
- Authentication
- Configuration

Example:

```
App

 |

Provider

 |

Components
```

---

# Adapter Pattern

Transform external data.

Example:

```
API Response

 |

Adapter

 |

UI Model
```

---

# Facade Pattern

Simplify complex systems.

Example:

```
Component

 |

User Facade

 |

API
Store
Cache
```

---

# Repository Pattern

Separate data access.

Architecture:

```
Component

 |

Repository

 |

API Client

 |

Backend
```

---

# Dependency Injection Pattern

React does not have built-in DI like Angular.

Implement using:

- Context
- Providers
- Factories
- Custom Hooks

---

# React Clean Architecture

Master scalable architecture.

Layers:

```
Presentation

      |

Application

      |

Domain

      |

Infrastructure
```

---

# Presentation Layer

Contains:

- Components
- Pages
- UI Hooks
- Styling

---

# Application Layer

Contains:

- Use Cases
- Business Workflows
- Facades

---

# Domain Layer

Contains:

- Entities
- Business Rules
- Interfaces

---

# Infrastructure Layer

Contains:

- APIs
- Storage
- External Services

---

````markdown id="react5"
# React Performance Engineering

Master React performance optimization for production applications.

Performance goals:

- Fast initial load
- Smooth interactions
- Efficient rendering
- Low memory usage
- Small bundle size
- Better Core Web Vitals
- Excellent user experience

---

# Performance Optimization Principles

Always optimize:

- Rendering
- State updates
- Component structure
- Network requests
- Bundle size
- Asset loading
- Memory usage

Avoid:

- Premature optimization
- Unnecessary complexity
- Optimizing without measurements

---

# React Rendering Optimization

Understand:

- Render cycles
- Component updates
- Reconciliation
- Commit phase
- Browser painting

Optimize:

- Component boundaries
- State placement
- Memoization
- Data flow

---

# Component Re-render Optimization

Common causes:

- Parent re-rendering
- Changed props
- New object references
- New function references
- Context updates
- State updates

Solutions:

- React.memo
- useMemo
- useCallback
- Component splitting
- State isolation

---

# React.memo Optimization

Master:

```tsx
React.memo(Component)
```

Purpose:

Prevent unnecessary component rendering.

Use when:

- Component renders frequently
- Props rarely change
- Rendering is expensive

Avoid:

- Wrapping every component
- Blind memoization

---

# Memoization Strategy

Use:

## useMemo

For:

- Expensive calculations
- Derived data
- Filtering
- Sorting

Example:

```tsx
const filteredUsers =
useMemo(
()=>users.filter(user=>user.active),
[users]
);
```

---

## useCallback

For:

- Stable callbacks
- Child component optimization
- Hook dependencies

Example:

```tsx
const handleSave =
useCallback(
()=>{
saveUser();
},
[]
);
```

---

# State Optimization

Follow:

- Keep state close to usage
- Avoid unnecessary global state
- Split large states
- Normalize complex state

Avoid:

```
Global Store

Everything
```

Prefer:

```
Feature State

Local Ownership
```

---

# Large List Optimization

Master:

- Virtualization
- Pagination
- Infinite scrolling
- Windowing

Problems:

Rendering:

```
10000 Items
```

causes:

- Slow rendering
- Memory usage
- Poor scrolling

---

# React Virtualization

Libraries:

- React Window
- React Virtualized
- TanStack Virtual

Use for:

- Tables
- Feeds
- Search results
- Large datasets

---

# Infinite Scrolling

Implement:

- Intersection Observer
- Cursor pagination
- Lazy loading

Architecture:

```
User Scroll

 |

Detect Bottom

 |

Fetch Next Page

 |

Append Data
```

---

# Image Optimization

Optimize:

- Image size
- Format
- Loading
- Rendering

Use:

- WebP
- AVIF
- Responsive images
- Lazy loading

Example:

```html
<img
 loading="lazy"
/>
```

---

# Code Splitting

Master:

- Dynamic imports
- Lazy loading
- Route splitting
- Component splitting

Example:

```tsx
const Admin =
lazy(
()=>import('./Admin')
);
```

Benefits:

- Smaller initial bundle
- Faster startup

---

# Bundle Optimization

Analyze:

- Bundle size
- Dependencies
- Duplicate packages
- Tree shaking

Tools:

- Vite Analyzer
- Webpack Bundle Analyzer

---

# Tree Shaking

Understand:

Removing unused code during build.

Best practices:

- Use ES modules
- Avoid unnecessary imports
- Remove unused dependencies

---

# React Profiler

Master React Profiler.

Analyze:

- Component renders
- Rendering duration
- Commit times
- Performance bottlenecks

---

# Browser Performance Tools

Master:

Chrome DevTools:

- Performance Tab
- Memory Tab
- Network Tab
- Lighthouse
- Coverage Tool

---

# Core Web Vitals

Optimize:

## Largest Contentful Paint (LCP)

Improve:

- Server response
- Images
- Critical resources

---

## First Input Delay (FID)

Improve:

- JavaScript execution
- Long tasks
- Event handling

---

## Interaction to Next Paint (INP)

Improve:

- Rendering
- Event handlers
- State updates

---

## Cumulative Layout Shift (CLS)

Improve:

- Image dimensions
- Dynamic content
- Fonts

---

# React Security

Master secure React development.

Understand:

- OWASP Top 10
- Browser security
- Data protection
- Authentication security
- API security

---

# Cross Site Scripting (XSS)

Prevent:

- Unsafe HTML
- Script injection
- Malicious content

React automatically escapes:

```tsx
{
 userInput
}
```

Avoid:

```tsx
dangerouslySetInnerHTML
```

unless required.

---

# HTML Injection Protection

If using:

```tsx
dangerouslySetInnerHTML
```

Always:

- Sanitize content
- Validate source
- Restrict HTML

Use:

- DOMPurify

---

# Authentication Security

Master:

- JWT
- OAuth2
- OpenID Connect
- SSO
- MFA

Implement:

- Secure login flow
- Token refresh
- Session handling

---

# Token Storage

Understand:

Options:

- Memory
- Secure cookies
- Local storage

Consider:

- Security requirements
- Application type
- Threat model

Avoid exposing sensitive tokens.

---

# Authorization

Implement:

- Role-based access control
- Permission-based access
- Feature permissions

Example:

```
User

 |

Role

 |

Permissions

 |

Features
```

---

# Protected Components

Create reusable authorization components.

Example:

```tsx
<CanAccess permission="ADMIN">
 <AdminPanel/>
</CanAccess>
```

---

# API Security

Secure API communication.

Implement:

- HTTPS
- Authentication headers
- Request validation
- Error handling
- Rate limiting support

---

# Environment Security

Never store:

- API secrets
- Private keys
- Passwords

Frontend environment variables are public.

---

# Error Handling Architecture

Design centralized error handling.

Handle:

- API errors
- Runtime errors
- Validation errors
- Network errors

---

# Global Error Handling

Implement:

- Error Boundaries
- API interceptors
- Logging services
- Monitoring tools

---

# Error Logging

Integrate:

- Sentry
- Datadog
- New Relic
- Application Insights

Capture:

- Error message
- Stack trace
- User context
- Browser information

Never capture:

- Passwords
- Tokens
- Sensitive information

---

# Loading State Architecture

Create consistent loading patterns.

States:

- Initial loading
- Fetching
- Saving
- Uploading
- Processing

---

# Loading Components

Create:

- Spinner
- Skeleton
- Progress bar
- Placeholder UI

Prefer:

Skeleton loading for better UX.

---

# Notification Architecture

Centralize:

- Success messages
- Error messages
- Warnings
- Alerts

Structure:

```
Component

 |

Notification Service

 |

Toast System
```

Libraries:

- React Hot Toast
- Sonner
- Material UI Snackbar

---

# Accessibility (A11Y)

Every React application must support accessibility.

Follow:

- WCAG Guidelines
- Semantic HTML
- Keyboard navigation
- Screen readers

---

# Semantic HTML

Use:

```html
<button>

<nav>

<header>

<main>

<section>
```

Avoid:

```html
<div onclick="">
```

---

# Keyboard Accessibility

Support:

- Tab navigation
- Enter actions
- Escape handling
- Focus management

---

# ARIA

Master:

- aria-label
- aria-describedby
- aria-expanded
- aria-hidden
- role attributes

Use only when semantic HTML is insufficient.

---

# Focus Management

Handle:

- Modals
- Dialogs
- Menus
- Route changes

Implement:

- Focus trap
- Focus restoration

---

# Internationalization (i18n)

Master React localization.

Libraries:

- react-i18next
- FormatJS
- Lingui

Support:

- Multiple languages
- Date formatting
- Currency formatting
- RTL layouts

---

# Localization Architecture

Structure:

```
locales

├── en.json

├── fr.json

└── de.json
```

---

# Date and Time Handling

Master:

- Time zones
- Locale formatting
- Date parsing

Libraries:

- date-fns
- Day.js
- Luxon

---

# Theme Architecture

Implement:

- Light theme
- Dark theme
- Custom themes

Approaches:

- Context
- CSS Variables
- Theme Providers

---

# Dark Mode

Support:

- User preference
- System preference
- Runtime switching

Use:

```css
prefers-color-scheme
```

---

````markdown id="react6"
# React Testing Strategy

Master professional React testing practices.

Testing goals:

- Verify functionality
- Prevent regressions
- Improve confidence
- Enable safe refactoring
- Maintain code quality

Testing pyramid:

```
              E2E Tests

          Integration Tests

       Component Tests

     Unit Tests
```

---

# Testing Types

Master:

- Unit Testing
- Component Testing
- Integration Testing
- End-to-End Testing
- Visual Testing
- Accessibility Testing
- Performance Testing

---

# Testing Principles

Always test:

- User behavior
- Business requirements
- Critical workflows

Avoid:

- Testing implementation details
- Testing private functions
- Over-mocking everything

---

# Jest

Master Jest testing framework.

Understand:

- Test suites
- Test cases
- Assertions
- Mocking
- Spies
- Coverage
- Snapshots

Example:

```typescript
describe(
 'User Service',
 ()=>{

 test(
 'should return user',
 ()=>{
 
 }

 )

}
)
```

---

# Jest Matchers

Master:

Common matchers:

```typescript
expect(value)
.toBe()

expect(value)
.toEqual()

expect(value)
.toContain()

expect(value)
.toThrow()
```

---

# Jest Mocking

Master:

- Mock functions
- Mock modules
- Mock APIs
- Mock timers

Example:

```typescript
jest.fn()
```

Use for:

- External dependencies
- API calls
- Services

---

# React Testing Library

Master React Testing Library.

Philosophy:

Test applications like users interact with them.

Prefer:

- Finding elements by role
- User interactions
- Visible behavior

Avoid:

- Testing component internals

---

# RTL Queries

Master:

Priority order:

1. getByRole

2. getByLabelText

3. getByPlaceholderText

4. getByText

5. getByTestId


Prefer:

```typescript
screen.getByRole(
 'button'
)
```

Avoid:

```typescript
getByTestId()
```

unless required.

---

# Component Testing

Test:

- Rendering
- User interaction
- State changes
- Props handling
- Events
- Conditional UI

Example:

```tsx
render(
 <Button/>
);

expect(
 screen.getByText("Save")
)
.toBeInTheDocument();
```

---

# User Event Testing

Use:

```typescript
userEvent
```

for realistic interactions.

Test:

- Click
- Typing
- Keyboard
- Selection
- Upload

Example:

```typescript
await user.click(button);
```

---

# Async Testing

Handle:

- API responses
- Loading states
- Delayed rendering

Use:

- waitFor
- findBy
- async utilities

Example:

```typescript
await screen
.findByText("User");
```

---

# Mock Service Worker (MSW)

Master API mocking.

Purpose:

Mock network requests realistically.

Architecture:

```
Component

 |

API Request

 |

MSW Handler

 |

Mock Response
```

Benefits:

- Realistic tests
- Less mocking code
- Better integration testing

---

# Snapshot Testing

Understand snapshots.

Use for:

- Stable UI components
- Design system components

Avoid:

- Large snapshots
- Blind snapshot updates

---

# End-to-End Testing

Master:

- Playwright
- Cypress

Test:

- Complete user journeys
- Authentication
- Forms
- Navigation
- Critical workflows

---

# Playwright

Master Playwright.

Features:

- Multi-browser testing
- Network mocking
- Screenshots
- Video recording
- Parallel execution

---

# Playwright Test Strategy

Test:

```
User Login

 |

Dashboard

 |

Business Workflow

 |

Logout
```

---

# Cypress

Master Cypress.

Features:

- Browser automation
- Component testing
- Time travel debugging
- Network interception

---

# Visual Testing

Test UI changes.

Tools:

- Chromatic
- Percy
- Playwright Screenshots

Validate:

- Layout
- Colors
- Typography
- Components

---

# Accessibility Testing

Integrate:

- axe-core
- Lighthouse
- React Testing Library

Test:

- Keyboard support
- ARIA attributes
- Screen reader compatibility

---

# Storybook

Master Storybook.

Purpose:

Develop components independently.

Use cases:

- Design systems
- Component documentation
- Visual testing

---

# Storybook Architecture

Structure:

```
Component

 |

Story

 |

Documentation

 |

Testing
```

---

# Storybook Stories

Create:

- Default state
- Loading state
- Error state
- Empty state
- Disabled state
- Responsive state

Example:

```
Button

├── Primary

├── Secondary

├── Loading

└── Disabled
```

---

# Component Documentation

Document:

- Purpose
- Props
- Usage
- Variations
- Accessibility
- Examples

---

# Design Systems

Master React design system architecture.

A design system contains:

- Components
- Tokens
- Guidelines
- Documentation
- Patterns

---

# Design System Structure

Example:

```
design-system

├── components

│   ├── Button

│   ├── Input

│   ├── Modal

│   └── Table

├── tokens

├── themes

├── utilities

└── documentation
```

---

# Component Library Development

Build reusable libraries.

Include:

- TypeScript support
- Documentation
- Testing
- Accessibility
- Versioning

---

# Component API Design

Good components have:

- Clear props
- Flexible composition
- Sensible defaults
- Accessibility built-in

Avoid:

- Too many props
- Complex configuration
- Hidden behavior

---

# Atomic Design Pattern

Master:

Levels:

```
Atoms

 |

Molecules

 |

Organisms

 |

Templates

 |

Pages
```

---

# UI Component Libraries

Master:

## Material UI

Understand:

- Components
- Theme system
- Customization
- Styling

---

## Ant Design

Master:

- Enterprise components
- Tables
- Forms
- Layouts

---

## Chakra UI

Understand:

- Component primitives
- Theme customization
- Accessibility

---

## Tailwind CSS Integration

Master:

- Utility classes
- Responsive design
- Theme configuration
- Component patterns

---

# CSS Architecture

Master styling approaches.

Options:

- CSS Modules
- Styled Components
- Emotion
- Tailwind CSS
- Sass
- Vanilla CSS

---

# CSS Modules

Benefits:

- Scoped styles
- No naming conflicts
- Maintainable CSS

Example:

```tsx
import styles from './Button.module.css'
```

---

# Styled Components

Master:

- CSS-in-JS
- Dynamic styling
- Theme providers

---

# Responsive Design

Build applications for:

- Mobile
- Tablet
- Desktop
- Large screens

Use:

- Responsive layouts
- Flexible units
- Media queries

---

# Mobile First Development

Follow:

```
Mobile

 |

Tablet

 |

Desktop
```

Benefits:

- Better performance
- Better accessibility
- Better UX

---

# Micro Frontend Architecture

Master enterprise frontend scaling.

Purpose:

Split large applications into independent applications.

Architecture:

```
Shell Application

 |

-----------------

App A

App B

App C
```

---

# Micro Frontend Approaches

Master:

- Module Federation
- Web Components
- Single SPA
- iframe isolation

---

# Module Federation

Understand:

- Host application
- Remote applications
- Shared dependencies
- Runtime loading

---

# Micro Frontend Benefits

Provides:

- Team independence
- Independent deployment
- Technology flexibility
- Better ownership

---

# Micro Frontend Challenges

Handle:

- Dependency duplication
- Communication
- Authentication
- Shared state
- Version management

---

# Monorepo Architecture

Master React monorepos.

Tools:

- Nx
- Turborepo
- pnpm workspace

---

# Monorepo Structure

Example:

```
workspace

├── apps

│   ├── web

│   └── admin

│

├── packages

│   ├── ui

│   ├── utils

│   └── config
```

---

# Monorepo Benefits

Support:

- Shared libraries
- Consistent tooling
- Better dependency management
- Faster development

---

````markdown id="react7"
# React Build Tools

Master modern React build systems and application tooling.

Understand:

- Vite
- Webpack
- Rollup
- ESBuild
- SWC
- Babel
- TypeScript Compiler
- Package Bundlers

---

# Vite

Master Vite for modern React development.

Vite provides:

- Fast development server
- Hot Module Replacement
- Optimized production builds
- Native ES module support
- Plugin ecosystem

---

# Vite Project Architecture

Example:

```
project

├── src

│   ├── main.tsx

│   ├── App.tsx

│   ├── components

│   ├── features

│   └── assets

├── public

├── vite.config.ts

├── tsconfig.json

└── package.json
```

---

# Vite Configuration

Master:

- Plugins
- Aliases
- Environment variables
- Build options
- Proxy configuration
- Dependency optimization

Example:

```typescript
export default defineConfig({

 plugins:[
   react()
 ],

 resolve:{
   alias:{
    "@":"./src"
   }
 }

});
```

---

# Environment Configuration

Manage:

- Development
- Testing
- Production

Example:

```
.env

.env.development

.env.production
```

Store:

- API URLs
- Feature flags
- Public configuration

Never store:

- Secrets
- Private keys
- Passwords

---

# Build Optimization

Optimize:

- Bundle size
- Assets
- Code splitting
- Compression
- Tree shaking

Strategies:

- Remove unused dependencies
- Lazy load features
- Optimize images
- Analyze bundles

---

# Webpack

Master Webpack for enterprise applications.

Understand:

- Entry points
- Loaders
- Plugins
- Modules
- Bundling
- Optimization

---

# Webpack Concepts

Architecture:

```
Source Code

 |

Webpack Loader

 |

Webpack Plugin

 |

Bundle Output
```

---

# Webpack Loaders

Understand:

- Babel loader
- CSS loader
- File loader
- Asset loader
- TypeScript loader

---

# Webpack Plugins

Master:

- HtmlWebpackPlugin
- MiniCssExtractPlugin
- DefinePlugin
- BundleAnalyzerPlugin

---

# Babel

Master JavaScript transformation.

Purpose:

Convert modern JavaScript into compatible code.

Understand:

- Presets
- Plugins
- JSX transformation
- Browser compatibility

---

# SWC

Understand modern compiler tooling.

Benefits:

- Faster compilation
- Rust-based performance
- Modern JavaScript transformation

Used by:

- Next.js
- Modern React tools

---

# Package Publishing

Master React library publishing.

Create:

- Component libraries
- Utility packages
- Hooks libraries

---

# React Library Structure

Example:

```
react-ui-library

├── src

│   ├── Button

│   ├── Input

│   ├── Modal

│   └── index.ts

├── package.json

├── README.md

└── dist
```

---

# Library Best Practices

Include:

- TypeScript declarations
- Documentation
- Unit tests
- Storybook
- Semantic versioning

---

# Next.js Integration

Master React with Next.js.

Understand:

- App Router
- Pages Router
- Server Components
- Server Actions
- Routing
- Rendering strategies

---

# Next.js Architecture

Structure:

```
Next.js Application

 |

App Router

 |

Server Components

 |

Client Components

 |

Backend APIs
```

---

# Next.js App Router

Master:

- app directory
- layouts
- pages
- loading.tsx
- error.tsx
- route handlers

---

# Next.js File Structure

Example:

```
app

├── layout.tsx

├── page.tsx

├── loading.tsx

├── error.tsx

├── api

│   └── users

│       └── route.ts

└── dashboard

    └── page.tsx
```

---

# Server Side Rendering (SSR)

Master SSR.

Purpose:

Render pages on server.

Benefits:

- Better SEO
- Faster first load
- Dynamic content

Flow:

```
Request

 |

Server Render

 |

HTML Response

 |

React Hydration
```

---

# Static Site Generation (SSG)

Master SSG.

Purpose:

Generate HTML at build time.

Benefits:

- Very fast
- CDN friendly
- Low server load

Use cases:

- Documentation
- Marketing sites
- Blogs

---

# Incremental Static Regeneration (ISR)

Master ISR.

Purpose:

Update static pages after deployment.

Benefits:

- Static performance
- Dynamic updates

Use cases:

- Product pages
- News websites
- Content platforms

---

# Client Side Rendering (CSR)

Understand CSR.

Flow:

```
Browser Request

 |

Download JavaScript

 |

React Renders UI
```

Use for:

- Dashboards
- Internal applications
- Highly interactive apps

---

# Rendering Strategy Selection

Choose based on requirement.

---

## Use SSR For

- SEO pages
- Dynamic public pages
- Content platforms

---

## Use SSG For

- Documentation
- Blogs
- Static content

---

## Use CSR For

- Admin panels
- Dashboards
- Internal tools

---

## Use Hybrid Rendering For

- Enterprise applications
- SaaS products
- Large platforms

---

# SEO Optimization

Master React SEO.

Understand:

- Metadata
- Structured data
- Semantic HTML
- Server rendering
- Performance

---

# SEO Fundamentals

Optimize:

- Page titles
- Meta descriptions
- Headings
- URLs
- Images
- Loading speed

---

# React Metadata Management

Manage:

- Title
- Description
- Open Graph tags
- Twitter cards

Libraries:

- React Helmet
- Next Metadata API

---

# Structured Data

Implement:

- JSON-LD
- Schema.org
- Rich snippets

Examples:

- Products
- Articles
- Reviews
- Events

---

# Performance SEO

Improve:

- Core Web Vitals
- Loading speed
- Mobile experience
- Accessibility

---

# React Deployment

Master production deployment.

Platforms:

- Vercel
- Netlify
- AWS
- Azure
- Google Cloud
- Cloudflare

---

# Deployment Process

Flow:

```
Developer

 |

Git Repository

 |

CI Pipeline

 |

Build

 |

Deploy

 |

Production
```

---

# Static Deployment

Suitable for:

- React SPA
- Documentation sites
- Marketing websites

Platforms:

- Netlify
- Vercel
- Cloudflare Pages

---

# Server Deployment

Suitable for:

- SSR applications
- Backend integrated apps

Options:

- Node.js server
- Containers
- Cloud platforms

---

# Docker for React

Master containerization.

Benefits:

- Consistent environments
- Easy deployment
- Scalability

---

# React Docker Structure

Example:

```
project

├── Dockerfile

├── nginx.conf

├── package.json

└── src
```

---

# Docker Build Process

Flow:

```
Source Code

 |

Docker Build

 |

Image

 |

Container

 |

Production
```

---

# Docker Best Practices

Use:

- Multi-stage builds
- Small images
- Environment configuration
- Security scanning

---

# CI/CD Pipeline

Master automated deployment.

Pipeline:

```
Code Push

 |

Install Dependencies

 |

Run Tests

 |

Build Application

 |

Deploy
```

---

# CI/CD Tools

Understand:

- GitHub Actions
- GitLab CI
- Jenkins
- Azure DevOps
- CircleCI

---

# GitHub Actions

Master:

- Workflows
- Jobs
- Steps
- Secrets
- Deployment

Example:

```
.github

 |

workflows

 |

deploy.yml
```

---

# Automated Quality Checks

Pipeline should include:

- Linting
- Type checking
- Unit tests
- Build verification
- Security checks

---

# Code Quality Tools

Master:

- ESLint
- Prettier
- Husky
- Commitlint
- SonarQube

---

# ESLint Configuration

Enforce:

- Code standards
- React rules
- TypeScript rules
- Accessibility rules

---

# Prettier

Maintain:

- Consistent formatting
- Readable code
- Team standards

---

# Git Hooks

Use:

- Husky
- lint-staged

Automate:

- Before commit checks
- Formatting
- Testing

---

````markdown id="react8"
# Advanced Enterprise React Architecture

Master enterprise-level React application architecture.

Enterprise React applications require:

- Clear boundaries
- Scalable folder structures
- Maintainable code
- Team ownership
- Security
- Performance
- Testing strategy
- Deployment strategy

---

# Enterprise React Architecture Principles

Always follow:

- Separation of concerns
- Feature ownership
- Domain-driven design
- Reusable components
- Strong typing
- Automated testing
- Continuous delivery

Avoid:

- One giant component structure
- Global uncontrolled state
- Mixed business and UI logic
- Duplicate implementations

---

# Feature-Based Architecture

Recommended enterprise pattern.

Structure:

```
src

├── features

│
├── authentication

│   ├── components

│   ├── hooks

│   ├── services

│   ├── api

│   ├── store

│   ├── models

│   └── pages

│
├── users

│   ├── components

│   ├── hooks

│   ├── services

│   └── models

│
└── dashboard
```

---

# Feature Ownership Model

Each feature owns:

- Components
- Business logic
- API communication
- State
- Tests
- Documentation

Benefits:

- Easier maintenance
- Independent development
- Better scalability

---

# Domain Driven React Architecture

Apply Domain Driven Design concepts.

Layers:

```
Presentation Layer

        |

Application Layer

        |

Domain Layer

        |

Infrastructure Layer
```

---

# Presentation Layer

Contains:

- React components
- Pages
- UI hooks
- Styling
- User interactions

Responsibilities:

- Render UI
- Handle user actions
- Display information

Avoid:

- API logic
- Business rules

---

# Application Layer

Contains:

- Use cases
- Workflows
- Feature orchestration

Examples:

- Create user
- Process payment
- Generate report

---

# Domain Layer

Contains:

- Business entities
- Rules
- Validation
- Domain models

Example:

```
User

Order

Product

Invoice
```

---

# Infrastructure Layer

Contains:

- API clients
- Storage
- External integrations
- Third-party services

---

# API Layer Architecture

Create centralized API communication.

Structure:

```
Component

 |

Custom Hook

 |

Service Layer

 |

API Client

 |

Backend
```

---

# API Client Pattern

Create reusable API clients.

Example:

```
api

├── httpClient.ts

├── userApi.ts

├── productApi.ts

└── orderApi.ts
```

---

# HTTP Client Responsibilities

Handle:

- Base URL
- Headers
- Authentication
- Interceptors
- Error handling
- Request configuration

---

# Repository Pattern

Master repository architecture.

Purpose:

Separate data access from business logic.

Architecture:

```
Feature

 |

Repository

 |

API Service

 |

Backend
```

---

# Repository Responsibilities

Handle:

- Data retrieval
- Data transformation
- Storage interaction
- API communication

Avoid:

- UI logic
- Rendering logic

---

# Service Layer Pattern

Create business services.

Example:

```
UserService

Responsibilities:

- User workflows
- Validation
- Business operations
```

---

# Facade Pattern

Master React facade architecture.

Purpose:

Provide a simple interface between UI and complex systems.

Architecture:

```
Component

 |

Facade

 |

----------------

API

State

Cache

Business Logic
```

---

# Facade Responsibilities

Handle:

- Data loading
- State updates
- Business workflows
- Error handling

Benefits:

- Cleaner components
- Easier testing
- Better maintainability

---

# Custom Hook Facade Pattern

Common React implementation.

Example:

```
useUsers()

 |

User Facade

 |

API + Store
```

Component:

```tsx
const {
 users,
 loading
}=useUsers();
```

---

# Authentication Architecture

Master enterprise authentication.

Support:

- JWT
- OAuth2
- OpenID Connect
- SAML
- SSO
- MFA

---

# Authentication Flow

Architecture:

```
Login Page

 |

Auth Service

 |

Identity Provider

 |

Token

 |

Application
```

---

# JWT Authentication

Understand:

- Access Token
- Refresh Token
- Expiration
- Token Validation

Flow:

```
Login

 |

Receive Token

 |

Store Securely

 |

Attach Token

 |

API Request
```

---

# OAuth2 Architecture

Master:

- Authorization Code Flow
- PKCE
- Client Credentials
- Refresh Tokens

---

# OpenID Connect

Understand:

- Identity layer
- User information
- ID tokens
- Authentication claims

---

# Single Sign-On (SSO)

Support:

- Enterprise login
- Multiple applications
- Central identity management

Providers:

- Azure AD
- Okta
- Auth0
- Keycloak

---

# Multi Factor Authentication

Support:

- OTP
- Authenticator apps
- Hardware keys
- Biometric verification

---

# Authentication State Management

Manage:

- Current user
- Login status
- Permissions
- Session expiry

Possible solutions:

- Context API
- Zustand
- Redux Toolkit

---

# Authorization Architecture

Master access control systems.

Types:

## Role Based Access Control (RBAC)

Example:

```
User

 |

Role

 |

Permissions
```

---

## Attribute Based Access Control (ABAC)

Access based on:

- User attributes
- Resource attributes
- Environment conditions

---

# Permission System

Create centralized permission handling.

Example:

```typescript
permissions:

[
"USER_CREATE",
"USER_DELETE",
"REPORT_VIEW"
]
```

---

# Permission Component Pattern

Example:

```tsx
<PermissionGate
 permission="USER_DELETE"
>

 <DeleteButton/>

</PermissionGate>
```

---

# Route Permission Protection

Architecture:

```
Route

 |

Permission Guard

 |

Component
```

---

# Feature Flag Architecture

Master feature management.

Purpose:

Control features without deployments.

---

# Feature Flag Use Cases

Use for:

- Beta releases
- A/B testing
- Customer-specific features
- Gradual rollout

---

# Feature Flag Structure

Example:

```
Feature Flag Service

 |

Configuration

 |

Application

 |

Features
```

---

# Multi Tenant React Applications

Master SaaS architecture.

Support:

- Multiple customers
- Different branding
- Different permissions
- Different configurations

---

# Multi Tenant Architecture

```
Application

 |

Tenant Resolver

 |

-----------------

Tenant A

Tenant B

Tenant C
```

---

# Tenant Configuration

Manage:

- Theme
- Logo
- Features
- API endpoints
- Permissions

---

# White Label Applications

Build customizable applications.

Support:

- Custom branding
- Custom themes
- Custom workflows
- Customer configuration

---

# International Enterprise Applications

Support:

- Multiple regions
- Multiple languages
- Multiple currencies
- Multiple time zones

---

# Localization Architecture

Structure:

```
locales

├── en

├── fr

├── de

└── ja
```

---

# Currency Handling

Always:

- Store currency codes
- Format according to locale
- Avoid floating-point issues

Example:

```typescript
{
 amount:100,
 currency:"USD"
}
```

---

# Time Zone Management

Handle:

- UTC storage
- Local conversion
- User preferences

---

# Audit Logging Architecture

Enterprise applications require tracking.

Capture:

- User actions
- Data changes
- Security events

---

# Audit System

Architecture:

```
User Action

 |

Audit Service

 |

Logging System

 |

Database
```

---

# Monitoring Architecture

Implement:

- Error tracking
- Performance monitoring
- User analytics

Tools:

- Sentry
- Datadog
- New Relic
- Application Insights

---

# Application Observability

Monitor:

- Errors
- Performance
- API latency
- User behaviour
- Frontend metrics

---

# Logging Best Practices

Log:

- Errors
- Important events
- Performance issues

Never log:

- Passwords
- Tokens
- Sensitive information

---

````markdown id="react9"
# React AI Agent Instructions

## Role Definition

You are an expert ReactJS AI coding agent.

Your responsibility is to assist developers in building, maintaining, reviewing, debugging, optimizing, and architecting React applications.

You must behave as:

- Senior React Developer
- React Architect
- Frontend Consultant
- UI Engineering Expert
- Performance Engineer
- Security Engineer
- Testing Specialist
- Code Reviewer

---

# React Agent Core Responsibilities

The React AI agent must be able to:

- Generate React components
- Design application architecture
- Create reusable hooks
- Build frontend systems
- Review React code
- Debug issues
- Refactor applications
- Optimize performance
- Improve security
- Create tests
- Document applications
- Design scalable systems

---

# React Code Generation Rules

When generating React code:

Always create:

- Production-ready code
- TypeScript-first solutions
- Reusable components
- Clean architecture
- Accessible UI
- Testable code
- Maintainable structure

Always prefer:

- Functional components
- Hooks
- TypeScript
- Modern React APIs
- Feature-based architecture

Avoid:

- Legacy patterns
- Class components unless required
- Duplicate logic
- Any type
- Hardcoded values
- Unnecessary dependencies

---

# React Component Generation Rules

Every generated component should consider:

- Purpose
- Responsibility
- Props design
- State ownership
- Performance
- Accessibility
- Testing

Example:

```tsx
interface UserCardProps {

 user: User;

 onSelect(user: User): void;

}


export function UserCard(
{
 user,
 onSelect
}: UserCardProps
){

 return (

  <article>

   <h2>{user.name}</h2>

  </article>

 );

}
```

---

# Component Design Rules

Components should:

- Do one thing
- Be composable
- Have clear inputs
- Have predictable outputs
- Avoid hidden side effects

Avoid:

```
HugeComponent.tsx

2000+ lines
```

Prefer:

```
UserDashboard

├── UserHeader

├── UserTable

├── UserFilters

├── UserActions

└── useUsers()
```

---

# Props Design Rules

Good props:

- Clear names
- Strong types
- Minimal responsibility

Example:

```typescript
interface ButtonProps {

 label:string;

 variant:"primary"|"secondary";

 disabled?:boolean;

}
```

Avoid:

```typescript
props:any
```

---

# State Management Rules

Before adding state:

Ask:

- Is this local UI state?
- Is this shared state?
- Is this server data?
- Is this derived data?

---

# State Selection Guide

Use:

## useState

For:

- Local component state
- Simple UI state

---

## useReducer

For:

- Complex transitions
- Multiple related states

---

## Context

For:

- Theme
- Authentication
- Configuration

---

## Zustand

For:

- Lightweight global state

---

## Redux Toolkit

For:

- Large enterprise applications

---

## TanStack Query

For:

- Server state
- API caching

---

# React Hook Rules

Always follow:

- Hooks only inside components/hooks
- Hooks at top level
- Custom hooks start with use

Never:

- Call hooks conditionally
- Call hooks inside loops
- Call hooks inside normal functions

---

# useEffect Rules

Before using useEffect ask:

"Is this really a side effect?"

Avoid using useEffect for:

- Calculating values
- Transforming data
- Managing derived state

Prefer:

```typescript
const value = useMemo(()=>{

},[]);
```

---

# API Integration Rules

Never call APIs directly inside UI components.

Avoid:

```tsx
function Users(){

fetch("/api/users")

}
```

Prefer:

```
Component

 |

Custom Hook

 |

Service

 |

API Client
```

---

# API Error Handling Rules

Every API integration must handle:

- Loading state
- Success state
- Error state
- Empty state
- Retry possibility

---

# Loading State Rules

Never show blank screens.

Provide:

- Skeleton loading
- Progress indicators
- Empty states
- Error messages

---

# Form Generation Rules

Every form should include:

- Validation
- Error messages
- Loading state
- Submit handling
- Accessibility

---

# Form Security Rules

Validate:

- Client side
- Server side

Never trust:

- User input
- Browser validation alone

---

# Accessibility Rules

Every generated React UI must consider:

- Keyboard navigation
- Screen readers
- Semantic HTML
- ARIA
- Focus handling

---

# Accessibility Checklist

Check:

## Images

Must have:

```html
alt=""
```

---

## Buttons

Must:

- Have labels
- Be keyboard accessible

---

## Forms

Must include:

- Labels
- Error messages
- Instructions

---

## Navigation

Must support:

- Keyboard navigation
- Screen readers

---

# CSS Rules

Generated styling should:

- Be maintainable
- Support responsive design
- Follow design systems

Prefer:

- CSS Modules
- Tailwind CSS
- Styled Components
- Theme variables

Avoid:

- Inline styles everywhere
- Duplicate CSS
- Global pollution

---

# Responsive Design Rules

Support:

- Mobile
- Tablet
- Desktop

Use:

- Flexible layouts
- CSS Grid
- Flexbox
- Responsive breakpoints

---

# Performance Review Rules

When reviewing React code check:

## Rendering

- Unnecessary renders
- Large components
- Poor state placement

---

## Hooks

Check:

- Dependency arrays
- Memoization
- Cleanup

---

## Lists

Check:

- Keys
- Virtualization
- Rendering strategy

---

## Network

Check:

- API duplication
- Caching
- Request optimization

---

# React Code Review Checklist

Review:

## Architecture

- Is the structure scalable?
- Are responsibilities separated?

---

## Components

- Are components reusable?
- Are props clean?

---

## State

- Is state placed correctly?
- Is global state necessary?

---

## Performance

- Are renders optimized?
- Are bundles optimized?

---

## Security

- Is input handled safely?
- Is authentication secure?

---

## Testing

- Are important flows tested?

---

# Debugging Workflow

When debugging React issues:

Follow:

```
Problem

 |

Reproduce

 |

Analyze

 |

Find Root Cause

 |

Fix

 |

Test

 |

Document
```

---

# Rendering Debugging

Check:

- Component renders
- State updates
- Props changes
- Context updates

Tools:

- React DevTools
- Profiler

---

# Memory Leak Debugging

Check:

- Uncleaned subscriptions
- Timers
- Event listeners
- Async operations

Always cleanup:

```tsx
return ()=>{

cleanup();

}
```

---

# API Debugging

Check:

- Network requests
- Headers
- Authentication
- Response data
- Error handling

Tools:

- Browser DevTools
- Postman
- Network inspector

---

# Migration Strategy

Master React migrations.

Examples:

- JavaScript to TypeScript
- Class components to hooks
- CRA to Vite
- Old React versions to React 19
- Redux migration
- Legacy architecture modernization

---

# Migration Process

Follow:

## Step 1

Analyze:

- Application size
- Dependencies
- Architecture

---

## Step 2

Create migration plan.

---

## Step 3

Add tests.

---

## Step 4

Migrate gradually.

---

## Step 5

Remove legacy code.

---

# JavaScript To TypeScript Migration

Convert:

Before:

```javascript
function User(props){

}
```

After:

```typescript
function User(
props:UserProps
){

}
```

---

# Class Component Migration

Convert:

Before:

```
Class Component

 |

Lifecycle Methods

 |

State
```

After:

```
Functional Component

 |

Hooks

 |

State
```

---

# React AI Agent Output Format

When providing solutions:

Always include:

1. Explanation

2. Architecture

3. File Structure

4. Implementation

5. Testing Strategy

6. Performance Considerations

7. Security Considerations

8. Future Improvements

---

# React Agent Quality Standards

Every generated solution must be:

- Correct
- Scalable
- Secure
- Performant
- Maintainable
- Production-ready

---

# React Engineering Mindset

Think like:

- Software architect
- Product engineer
- Performance engineer
- Security engineer
- User experience engineer

Do not only write code.

Design systems.

---

````markdown id="react10"
# React Native Skills

Master React Native development for cross-platform mobile applications.

Understand:

- React Native architecture
- Mobile UI development
- Native components
- Platform APIs
- Navigation
- State management
- Performance optimization
- App deployment

---

# React Native Architecture

React Native allows building mobile applications using React concepts.

Architecture:

```
React Components

        |

React Native Bridge

        |

Native Platform APIs

        |

iOS / Android
```

---

# React Native Components

Master:

- View
- Text
- Image
- ScrollView
- FlatList
- SectionList
- TextInput
- Pressable
- Modal
- SafeAreaView

---

# React Native Layout

Understand:

- Flexbox
- Dimensions
- Responsive layouts
- Platform differences

React Native uses:

- Flexbox by default
- StyleSheet objects
- Platform-specific styles

---

# React Native Styling

Master:

- StyleSheet
- Dynamic styles
- Theme systems
- Responsive design

Example:

```typescript
const styles = StyleSheet.create({

 container:{
   flex:1
 }

});
```

---

# React Native Navigation

Master navigation solutions.

Libraries:

- React Navigation
- Expo Router
- Native Navigation

---

# Navigation Patterns

Implement:

- Stack Navigation
- Tab Navigation
- Drawer Navigation
- Nested Navigation
- Deep Linking

---

# React Native State Management

Use:

- Context API
- Zustand
- Redux Toolkit
- MobX
- Jotai

Choose based on:

- App complexity
- Team requirements
- Data flow

---

# Mobile API Integration

Handle:

- REST APIs
- GraphQL APIs
- WebSockets
- Offline synchronization

Consider:

- Network failures
- Slow connections
- Battery usage

---

# Offline First Mobile Apps

Master:

- Local storage
- SQLite
- AsyncStorage
- WatermelonDB
- Realm

Architecture:

```
Mobile App

 |

Local Database

 |

Sync Engine

 |

Backend
```

---

# Push Notifications

Understand:

- Firebase Cloud Messaging
- APNs
- Notification permissions
- Background handling

---

# Device Features

Integrate:

- Camera
- Location
- Contacts
- Biometrics
- Files
- Sensors

---

# React Native Performance

Optimize:

- Rendering
- Memory
- Animations
- Network usage
- Bundle size

---

# FlatList Optimization

Master:

- Virtual rendering
- keyExtractor
- getItemLayout
- windowSize
- removeClippedSubviews

---

# Mobile Memory Management

Avoid:

- Large images
- Memory leaks
- Unnecessary state
- Heavy computations

---

# Animations

Master:

- React Native Animated API
- Reanimated
- Gesture Handler

Use for:

- Transitions
- Gestures
- Interactive UI

---

# Mobile Security

Implement:

- Secure storage
- Certificate validation
- Encryption
- Authentication protection

Libraries:

- Secure Storage
- Keychain
- Keystore

---

# Mobile App Deployment

Understand:

## Android

- APK
- AAB
- Play Store deployment

---

## iOS

- IPA
- App Store Connect
- TestFlight

---

# Expo Framework

Master Expo.

Features:

- Faster development
- Native APIs
- Build services
- OTA updates

---

# React Ecosystem Mastery

Understand major React ecosystem tools.

---

# Package Management

Master:

- npm
- yarn
- pnpm

Understand:

- Dependencies
- Peer dependencies
- Package resolution
- Lock files

---

# Code Quality Ecosystem

Master:

## ESLint

Purpose:

- Code quality
- Best practices
- Error prevention

---

## Prettier

Purpose:

- Formatting
- Consistency

---

## Husky

Purpose:

- Git hooks
- Automation

---

## Commitlint

Purpose:

- Standard commits

---

# Documentation Tools

Master:

- Storybook
- Docusaurus
- React Styleguidist
- Markdown documentation

---

# API Documentation

Understand:

- OpenAPI
- Swagger
- GraphQL Schema Documentation

---

# Frontend Architecture Documentation

Document:

- Folder structure
- Data flow
- Component relationships
- State management
- Deployment process

---

# React Enterprise Checklist

Before production release verify:

---

## Architecture

Check:

- Feature-based structure
- Clear ownership
- Separation of concerns
- Scalable design

---

## Components

Check:

- Reusable components
- Clean props
- Accessibility
- Testing

---

## State

Check:

- Correct state solution
- No unnecessary global state
- Predictable updates

---

## API

Check:

- Error handling
- Loading states
- Caching
- Authentication

---

## Performance

Check:

- Bundle size
- Rendering performance
- Image optimization
- Lazy loading

---

## Security

Check:

- Authentication
- Authorization
- XSS protection
- Data handling

---

## Testing

Check:

- Unit tests
- Component tests
- Integration tests
- E2E tests

---

## Deployment

Check:

- CI/CD pipeline
- Environment configuration
- Monitoring
- Error tracking

---

# React Project Initialization Rules

When creating a new React project:

Analyze:

- Application type
- Scale
- Team size
- Deployment needs

---

# Small Application Setup

Use:

```
React

+

Vite

+

TypeScript

+

React Router

+

Simple State
```

---

# Medium Application Setup

Use:

```
React

+

Vite

+

TypeScript

+

Feature Architecture

+

TanStack Query

+

Zustand
```

---

# Enterprise Application Setup

Use:

```
React

+

TypeScript

+

Feature Architecture

+

Redux Toolkit

+

RTK Query

+

Design System

+

Testing Framework

+

CI/CD
```

---

# React Best Practices Summary

Always:

- Use TypeScript
- Prefer functional components
- Keep components small
- Separate business logic
- Optimize intentionally
- Write tests
- Follow accessibility standards
- Protect user data
- Document architecture

---

# React Engineering Rules

A professional React developer should understand:

Frontend:

- React
- TypeScript
- JavaScript
- CSS
- HTML

Architecture:

- Design patterns
- State management
- API architecture
- Component systems

Quality:

- Testing
- Performance
- Security
- Accessibility

Delivery:

- Git
- CI/CD
- Deployment
- Monitoring

---

# React AI Agent Final Behavior Rules

The React AI agent must always:

1. Understand requirements before coding.

2. Ask clarification when requirements are incomplete.

3. Suggest architecture before large implementations.

4. Explain trade-offs.

5. Generate maintainable code.

6. Prefer modern React patterns.

7. Avoid unnecessary complexity.

8. Consider performance.

9. Consider security.

10. Consider accessibility.

---

# React AI Agent Decision Process

For every request:

```
Requirement

 |

Analyze Context

 |

Choose Architecture

 |

Select Tools

 |

Implement Solution

 |

Test

 |

Optimize

 |

Document
```

---

# React Solution Quality Gate

Before final output verify:

## Code Quality

- Is it readable?
- Is it maintainable?
- Is it typed?

---

## Architecture

- Is responsibility separated?
- Will it scale?

---

## Performance

- Are unnecessary renders avoided?

---

## Security

- Is user data protected?

---

## UX

- Is loading handled?
- Are errors handled?
- Is accessibility considered?

---

# React Skill Completion

This ReactJS skill provides complete knowledge for AI agents to:

- Build React applications
- Architect enterprise systems
- Review React code
- Debug complex issues
- Optimize performance
- Implement security
- Build design systems
- Create scalable frontend platforms

---

# End of ReactJS Skill
