# Workflow: Daily CEO Meeting

## Purpose
Run a daily leadership call between the CEO, Project Manager, Scrum Master, and Business Analyst to keep the company aligned on project status, new opportunities, resource needs, investments, tools, improvements, and feedback.

## Participants
- CEO: final decision-maker for priorities, investment, company direction, and resource approval.
- Project Manager: project status, timeline, risk, dependencies, and action tracking.
- Scrum Master: sprint health, blockers, process issues, and delivery improvements.
- Business Analyst: client needs, new project ideas, requirements, and business value.

## Recommended Duration
30 to 45 minutes.

## Meeting Agenda
1. Company priority check.
2. Active project status.
3. Sprint progress and blockers.
4. New client requests or project ideas.
5. Tools, platforms, or process improvements needed.
6. Investment or budget needs.
7. AI-agent resource planning.
8. Decisions, owners, and follow-up actions.

## Project Idea Review
The Business Analyst should bring a short list of project ideas when available:
- Top 3 ideas for CEO review.
- Score and recommendation for each idea.
- Expected customer, revenue path, MVP scope, and required AI agents.
- Clear decision needed: discover, build MVP, park, or reject.

## AI-Agent Resource Planning
For each active or proposed project, decide:
- Which agents are required.
- Whether each agent is needed full-time, part-time, or only for review.
- What outputs each agent must produce.
- What human approval is required.
- Whether new specialized agents should be created.

## Resource Estimate Guide
- Small feature: Business Analyst, UX Designer, Frontend or Backend, QA, Code Reviewer.
- API or backend feature: Business Analyst, Solution Architect, Backend, Database, QA, Security, Code Reviewer.
- New product module: CEO, Project Manager, Business Analyst, UX Designer, Solution Architect, Frontend, Backend, Database, QA, Security, DevOps, Documentation.
- Production release: Project Manager, QA, Security, DevOps, Documentation, Code Reviewer.
- New client discovery: CEO, Business Analyst, Project Manager, Solution Architect.

## Decision Rules
- CEO approves priorities, budget, investment, and new client direction.
- Project Manager owns delivery follow-up.
- Scrum Master owns process improvements and blocker removal.
- Business Analyst owns requirement discovery and client clarification.
- Security or compliance concerns must be reviewed before commitment.

## Required Outputs
- Daily meeting notes.
- Project status summary.
- New opportunities list.
- Decisions made.
- Action items with owners and dates.
- Resource plan for AI agents.
- Risks and blockers.

## After the Meeting
- Update `ai/memory/decisions.md` for major decisions.
- Update `ai/memory/known-issues.md` for serious blockers.
- Update `ai/memory/lessons-learned.md` for process improvements.
- Update `ai/memory/project-ideas.md` for new, approved, parked, or rejected ideas.
- Convert approved ideas into user stories or discovery tasks.
