# AI Agent Registry

This registry defines the agent workflow and responsibilities for the startup software organization.

## Core Flow
1. CEO sets direction and priorities.
2. Project Manager turns priorities into delivery plans.
3. Business Analyst defines requirements and acceptance criteria.
4. UX Designer defines user flows and experience expectations.
5. Solution Architect defines technical approach.
6. Frontend, Backend, and Database agents implement.
7. QA verifies quality.
8. Security reviews risk.
9. Code Reviewer reviews changes.
10. DevOps deploys and monitors.
11. Documentation updates shared knowledge.
12. Memory files capture decisions, lessons, sprint history, and known issues.

## Responsibility Map
| Area | Primary Agent | Supporting Agents |
| --- | --- | --- |
| Company strategy | CEO | Project Manager, Business Analyst |
| Daily CEO meeting | CEO | Project Manager, Scrum Master, Business Analyst |
| AI-agent resource planning | CEO | Project Manager, Scrum Master, Business Analyst, Solution Architect |
| Project idea discovery | Business Analyst | CEO, Project Manager, Scrum Master, Solution Architect, UX Designer |
| Requirements | Business Analyst | CEO, UX Designer, QA |
| Architecture | Solution Architect | Backend, Database, Security, DevOps |
| Machine learning | ML Engineer | Solution Architect, Backend, QA, DevOps |
| User experience | UX Designer | Business Analyst, Frontend, QA |
| Frontend | Frontend | UX Designer, Backend, QA |
| Backend | Backend | Solution Architect, Database, Security |
| Data | Database | Backend, Security, DevOps |
| Quality | QA | Business Analyst, Frontend, Backend |
| Code review | Code Reviewer | Security, QA |
| Security | Security | Solution Architect, Backend, DevOps |
| Deployment | DevOps | QA, Security, Backend |
| Documentation | Documentation | All agents |

| Car detection project | ML Engineer | CEO, Business Analyst, Project Manager, Scrum Master, Solution Architect, Frontend, Backend, QA, Security, DevOps, Documentation |

## Startup Rule
Move fast with small releases, but never bypass security, review, or the definition of done for production work.

## Daily Leadership Rhythm
The CEO meets daily with the Project Manager, Scrum Master, and Business Analyst to review:
- Project status.
- Sprint health.
- Blockers and risks.
- New client or project ideas.
- Tools and investment needs.
- Company improvement and feedback.
- Required AI-agent resources for active and proposed work.

Use `ai/workflows/daily-ceo-meeting.md`, `ai/templates/daily-ceo-meeting.md`, and `ai/prompts/daily-ceo-meeting.md` to run the meeting consistently.

## Project Idea Pipeline
The Business Analyst team owns project idea discovery. Use:
- `ai/workflows/project-idea-discovery.md`
- `ai/templates/project-idea-brief.md`
- `ai/prompts/generate-project-ideas.md`
- `ai/memory/project-ideas.md`

Ideas should be scored before CEO review, and each recommendation should include MVP scope, revenue path, risks, and required AI agents.
