import React, { useState, useEffect } from 'react';
import './App.css';

export default function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [statusData, setStatusData] = useState(null);
  const [pipelineTasks, setPipelineTasks] = useState([]);
  const [projectsList, setProjectsList] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);
  const [dsmHistory, setDsmHistory] = useState([]);
  const [selectedStandupIdx, setSelectedStandupIdx] = useState(0);
  const [loading, setLoading] = useState(true);
  const [selectedRosterAgent, setSelectedRosterAgent] = useState(null);
  const [rosterModalLoading, setRosterModalLoading] = useState(false);

  // API Base URL
  const baseUrl = 'http://localhost:8000/api';

  const handleAgentClick = async (role, currentStatus, currentTask, currentBlockers) => {
    setRosterModalLoading(true);
    try {
      const res = await fetch(`${baseUrl}/workspace/agent/details/?agent=${encodeURIComponent(role)}`);
      if (res.ok) {
        const details = await res.json();
        setSelectedRosterAgent({
          ...details,
          status: currentStatus,
          task: currentTask,
          blockers: currentBlockers
        });
      } else {
        setSelectedRosterAgent({
          role,
          status: currentStatus,
          task: currentTask,
          blockers: currentBlockers,
          purpose: 'Detailed profile document not configured or empty.',
          responsibilities: [],
          outputs: [],
          extreme_skills: []
        });
      }
    } catch (e) {
      console.error('Error fetching agent details:', e);
      setSelectedRosterAgent({
        role,
        status: currentStatus,
        task: currentTask,
        blockers: currentBlockers,
        purpose: 'Could not fetch detailed profile from server.',
        responsibilities: [],
        outputs: [],
        extreme_skills: []
      });
    }
    setRosterModalLoading(false);
  };

  // Fetch status data
  const fetchStatus = async () => {
    try {
      const res = await fetch(`${baseUrl}/workspace/status/`);
      const data = await res.json();
      setStatusData(data);
    } catch (e) {
      console.error('Error fetching workspace status:', e);
    }
  };

  // Fetch pipeline tasks
  const fetchPipeline = async () => {
    try {
      const res = await fetch(`${baseUrl}/workspace/pipeline/`);
      const data = await res.json();
      setPipelineTasks(data);
    } catch (e) {
      console.error('Error fetching pipeline:', e);
    }
  };

  // Fetch all projects
  const fetchProjects = async () => {
    try {
      const res = await fetch(`${baseUrl}/workspace/projects/`);
      const data = await res.json();
      setProjectsList(data);
    } catch (e) {
      console.error('Error fetching projects:', e);
    }
  };

  // Fetch standup history logs
  const fetchDsmHistory = async () => {
    try {
      const res = await fetch(`${baseUrl}/workspace/dsm/history/`);
      const data = await res.json();
      setDsmHistory(data);
    } catch (e) {
      console.error('Error fetching DSM history:', e);
    }
  };

  const loadAllData = async () => {
    setLoading(true);
    await Promise.all([
      fetchStatus(),
      fetchPipeline(),
      fetchProjects(),
      fetchDsmHistory()
    ]);
    setLoading(false);
  };

  useEffect(() => {
    loadAllData();
  }, []);

  // Move pipeline task status
  const moveTask = async (taskId, newStatus) => {
    try {
      const res = await fetch(`${baseUrl}/workspace/pipeline/move/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ storyId: taskId, status: newStatus })
      });
      if (res.ok) {
        await fetchPipeline();
        await fetchStatus();
      }
    } catch (e) {
      console.error('Error moving task:', e);
    }
  };

  const getStatusColor = (status) => {
    if (status === 'Green') return 'green';
    if (status === 'Yellow') return 'yellow';
    return 'red';
  };

  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="nav-icon">
        <path strokeLinecap="round" strokeLinejoin="round" d="M7.5 14.25v2.25m3-4.5v4.5m3-6.75v6.75m3-9v9M6 20.25h12A2.25 2.25 0 0 0 20.25 18V6A2.25 2.25 0 0 0 18 3.75H6A2.25 2.25 0 0 0 3.75 6v12A2.25 2.25 0 0 0 6 20.25Z" />
      </svg>
    )},
    { id: 'projects', label: 'Projects', icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="nav-icon">
        <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 12.75V12A2.25 2.25 0 0 1 4.5 9.75h15A2.25 2.25 0 0 1 21.75 12v.75m-8.69-6.44-2.12-2.12a1.5 1.5 0 0 0-1.061-.44H4.5A2.25 2.25 0 0 0 2.25 6v12a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9a2.25 2.25 0 0 0-2.25-2.25h-5.379a1.5 1.5 0 0 1-1.06-.44Z" />
      </svg>
    )},
    { id: 'pipeline', label: 'Sprints', icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="nav-icon">
        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 0 0 2.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 0 0-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75 2.25 2.25 0 0 0-.1-.664m-5.8 0A2.251 2.251 0 0 1 13.5 2.25H15c1.03 0 1.9.693 2.166 1.638m-7.377 12.408-.007-.007H3.75a2.25 2.25 0 0 1-2.25-2.25V6.108c0-1.135.845-2.098 1.976-2.192a48.424 48.424 0 0 1 1.123-.08" />
      </svg>
    )},
    { id: 'agents', label: 'AI Agent Status', icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="nav-icon">
        <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
      </svg>
    )},
    { id: 'dsm', label: 'Daily Standup', icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="nav-icon">
        <path strokeLinecap="round" strokeLinejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
      </svg>
    )}
  ];

  const currentStandup = dsmHistory[selectedStandupIdx];

  return (
    <div className="portal-container">
      {/* Sidebar Navigation */}
      <aside className="portal-sidebar">
        <div>
          <div className="brand-section">
            <div className="brand-logo">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 1.5c2.9 0 5.25 2.35 5.25 5.25v10.5c0 2.9-2.35 5.25-5.25 5.25H6c-2.9 0-5.25-2.35-5.25-5.25V6.75C.75 3.85 3.1 1.5 6 1.5h12Zm-1.8 15v-6.75L12 13.5l-4.2 3.75v6.75h-2.4V5.25h2.4l4.2 3.75 4.2-3.75h2.4v11.25h-2.4Z"/>
              </svg>
            </div>
            <span className="brand-title">DevLab-One</span>
          </div>

          <nav>
            <ul className="nav-list">
              {navItems.map((item) => (
                <li
                  key={item.id}
                  className={`nav-item ${activeTab === item.id ? 'active' : ''}`}
                  onClick={() => setActiveTab(item.id)}
                >
                  {item.icon}
                  <span>{item.label}</span>
                </li>
              ))}
            </ul>
          </nav>
        </div>
      </aside>

      {/* Main Workspace Frame */}
      <main className="portal-main">
        {loading ? (
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '80vh' }}>
            <span style={{ fontSize: '18px', color: 'var(--text-muted)' }}>Synching workspace status...</span>
          </div>
        ) : (
          <>
            {/* Dashboard Tab */}
            {activeTab === 'dashboard' && (
              <>
                <div className="page-header">
                  <h1 className="page-title">Workspace <span className="gradient-text">Dashboard</span></h1>
                  <button onClick={loadAllData} className="send-btn" style={{ padding: '8px 16px', borderRadius: '20px', fontSize: '13px' }}>Sync Portal</button>
                </div>

                {statusData && (
                  <div className="status-cards-grid">
                    <div className="status-card glass-panel glow-indigo clickable" onClick={() => setActiveTab('projects')}>
                      <div className="status-card-header">Projects</div>
                      <div className="status-value" style={{ fontSize: '24px', fontWeight: '800', margin: '6px 0' }}>
                        {projectsList.filter(p => p.released).length} / {projectsList.length}
                      </div>
                      <span className="status-badge green" style={{ alignSelf: 'flex-start' }}>Completed</span>
                    </div>

                    <div className="status-card glass-panel clickable" onClick={() => setActiveTab('pipeline')}>
                      <div className="status-card-header">Active Sprint</div>
                      <div className="status-value" style={{ fontSize: '15px', lineHeight: '1.4', margin: '6px 0' }}>{statusData.sprintName || "DevLabOne-sprint-01"}</div>
                      
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%', marginTop: '4px' }}>
                        <span className="status-badge" style={{ background: 'rgba(99, 102, 241, 0.15)', color: '#a5b4fc', margin: 0 }}>
                          {statusData.sprintDay || "Day 1"} of {statusData.sprintDuration || "10 days"}
                        </span>
                        <span className={`status-badge ${getStatusColor(statusData.status)}`} style={{ margin: 0 }}>
                          {statusData.status === 'Green' ? 'Healthy' : 'Blocked'}
                        </span>
                      </div>
                      
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%', marginTop: '6px', fontSize: '12px' }}>
                        <span style={{ color: 'var(--text-muted)' }}>Progress</span>
                        <strong style={{ color: 'var(--emerald-success)' }}>{statusData.progress}%</strong>
                      </div>
                      
                      <div className="progress-bar-container" style={{ width: '100%', marginTop: '4px' }}>
                        <div className="progress-bar-fill" style={{ width: `${statusData.progress}%` }}></div>
                      </div>
                    </div>
                  </div>
                )}

                <div className="dashboard-grid">
                  {/* Left Column: Active Agents Grid */}
                  <div className="dashboard-panel glass-panel">
                    <h2 className="panel-title">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" style={{ width: '20px', height: '20px' }}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.109A11.386 11.386 0 0 1 10.089 21c-2.243 0-4.32-.647-6.08-1.764a3 3 0 0 1-1.002-4.015 11.378 11.378 0 0 1 12.083-4.283c.273.08.54.175.801.285M15 8.25a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM19.5 8.25a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Z" />
                      </svg>
                      Active AI Agent Status
                    </h2>
                    {statusData && (
                      <div className="agent-grid">
                        {statusData.agents.slice(0, 6).map((agent) => (
                          <div key={agent.role} className="agent-card clickable" style={{ cursor: 'pointer' }} onClick={() => handleAgentClick(agent.role, agent.status, agent.task, agent.blockers)}>
                            <div className="agent-header">
                              <div className="agent-info">
                                <div className="agent-avatar">{agent.role.slice(0, 2).toUpperCase()}</div>
                                <span className="agent-name">{agent.role}</span>
                              </div>
                              <span className={`agent-status-badge ${agent.status.toLowerCase()}`}>
                                {agent.status}
                              </span>
                            </div>
                            <p className="agent-task"><strong>Next Task:</strong> {agent.task}</p>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>

                  {/* Right Column: Quick Stats / DSM reminder */}
                  <div className="dashboard-panel glass-panel">
                    <h2 className="panel-title">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" style={{ width: '20px', height: '20px' }}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
                      </svg>
                      Sprint Checklist Summary
                    </h2>
                    {pipelineTasks && (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px' }}>
                          <span style={{ color: 'var(--text-muted)' }}>Stories Finished</span>
                          <strong>{pipelineTasks.filter(t => t.status === 'DONE').length} / {pipelineTasks.length}</strong>
                        </div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px' }}>
                          <span style={{ color: 'var(--text-muted)' }}>Active In Development</span>
                          <strong>{pipelineTasks.filter(t => t.status === 'IN_PROGRESS').length}</strong>
                        </div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px' }}>
                          <span style={{ color: 'var(--text-muted)' }}>Ready for QA Review</span>
                          <strong>{pipelineTasks.filter(t => t.status === 'READY_FOR_REVIEW').length}</strong>
                        </div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px' }}>
                          <span style={{ color: 'var(--text-muted)' }}>Blocked Tasks</span>
                          <strong style={{ color: 'var(--red-danger)' }}>{pipelineTasks.filter(t => t.status === 'BLOCKER').length}</strong>
                        </div>
                        
                        <div style={{ marginTop: '16px', borderTop: '1px solid rgba(255, 255, 255, 0.08)', paddingTop: '16px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                          <p style={{ fontSize: '12px', color: 'var(--text-muted)', lineHeight: '1.4' }}>
                            View tasks and milestones in standard project views or trigger daily DSM standup synthesis.
                          </p>
                          <button onClick={() => setActiveTab('dsm')} className="send-btn" style={{ padding: '8px', fontSize: '12px', borderRadius: '8px', width: '100%' }}>
                            Open DSM Room
                          </button>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </>
            )}

            {/* Projects Tab */}
            {activeTab === 'projects' && (
              <>
                <div className="page-header">
                  <h1 className="page-title">Workspace <span className="gradient-text">Projects Portfolio</span></h1>
                  <span style={{ color: 'var(--text-muted)', fontSize: '14px' }}>Overview of all sub-projects and release statuses</span>
                </div>

                <div className="glass-panel" style={{ padding: '24px' }}>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '20px' }}>
                    {projectsList.map((project) => (
                      <div
                        key={project.id}
                        className="agent-card clickable"
                        style={{ padding: '20px', background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.06)', cursor: 'pointer' }}
                        onClick={() => setSelectedProject(project)}
                      >
                        <div className="agent-header" style={{ marginBottom: '12px' }}>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                            <span style={{ fontSize: '16px', fontWeight: '700', color: 'var(--text-primary)' }}>{project.name}</span>
                            <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Location: {project.folder}</span>
                          </div>
                        </div>
                        <p style={{ fontSize: '13px', color: 'var(--text-muted)', lineHeight: '1.4', margin: '0 0 16px 0', height: '54px', overflow: 'hidden', textOverflow: 'ellipsis', display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical' }}>
                          {project.description}
                        </p>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <div style={{ display: 'flex', gap: '4px' }}>
                            {project.tech.slice(0, 3).map((t, idx) => (
                              <span key={idx} style={{ fontSize: '10px', background: 'rgba(255,255,255,0.04)', padding: '2px 6px', borderRadius: '4px', color: 'var(--text-muted)' }}>{t}</span>
                            ))}
                          </div>
                          <span className={`agent-status-badge ${project.released ? 'active' : 'idle'}`}>
                            {project.released ? 'Released' : project.status}
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </>
            )}

            {/* Pipeline Kanban Tab */}
            {activeTab === 'pipeline' && (
              <>
                <div className="page-header">
                  <h1 className="page-title">Sprint <span className="gradient-text">Kanban Board</span></h1>
                  <span style={{ color: 'var(--text-muted)', fontSize: '14px' }}>Active Sprint: DevLabOne-sprint-01 (Day 1/10)</span>
                </div>

                <div className="kanban-board">
                  {['TO_DO', 'IN_PROGRESS', 'READY_FOR_REVIEW', 'DONE', 'BLOCKER'].map((colStatus) => {
                    const tasksInCol = pipelineTasks.filter(t => t.status === colStatus);
                    return (
                      <div key={colStatus} className="kanban-column">
                        <div className="column-header">
                          <span>{colStatus.replace('_', ' ')}</span>
                          <span className="card-count">{tasksInCol.length}</span>
                        </div>
                        
                        {tasksInCol.map((task) => (
                          <div key={task.id} className="kanban-card">
                            <div className="card-id">{task.id}</div>
                            <div className="card-title">{task.title}</div>
                            <div className="card-description">{task.description}</div>
                            <div className="card-footer">
                              <span className="card-role">{task.role}</span>
                            </div>
                            
                            <div className="card-actions">
                              {colStatus !== 'TO_DO' && (
                                <button onClick={() => moveTask(task.id, 'TO_DO')} className="card-move-btn">Todo</button>
                              )}
                              {colStatus !== 'IN_PROGRESS' && (
                                <button onClick={() => moveTask(task.id, 'IN_PROGRESS')} className="card-move-btn">Dev</button>
                              )}
                              {colStatus !== 'READY_FOR_REVIEW' && (
                                <button onClick={() => moveTask(task.id, 'READY_FOR_REVIEW')} className="card-move-btn">Review</button>
                              )}
                              {colStatus !== 'DONE' && (
                                <button onClick={() => moveTask(task.id, 'DONE')} className="card-move-btn">Done</button>
                              )}
                            </div>
                          </div>
                        ))}
                      </div>
                    );
                  })}
                </div>
              </>
            )}

            {/* AI Agent Status Tab */}
            {activeTab === 'agents' && statusData && (
              <>
                <div className="page-header">
                  <h1 className="page-title">AI Agent <span className="gradient-text">Roster</span></h1>
                  <span style={{ color: 'var(--text-muted)', fontSize: '14px' }}>Status of DevLab-One Roster</span>
                </div>

                <div className="glass-panel" style={{ padding: '24px' }}>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '20px' }}>
                    {statusData.agents.map((agent) => (
                      <div key={agent.role} className="agent-card clickable" style={{ padding: '20px', background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.06)', cursor: 'pointer' }} onClick={() => handleAgentClick(agent.role, agent.status, agent.task, agent.blockers)}>
                        <div className="agent-header">
                          <div className="agent-info">
                            <div className="agent-avatar" style={{ width: '40px', height: '40px', fontSize: '14px' }}>
                              {agent.role.slice(0, 2).toUpperCase()}
                            </div>
                            <div>
                              <div className="agent-name" style={{ fontSize: '15px' }}>{agent.role}</div>
                              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Specialist</div>
                            </div>
                          </div>
                          <span className={`agent-status-badge ${agent.status.toLowerCase()}`}>
                            {agent.status}
                          </span>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '12px' }}>
                          <p className="agent-task" style={{ fontSize: '13px' }}><strong>Ongoing Task:</strong> {agent.task}</p>
                          <p className="agent-task" style={{ fontSize: '12px', color: 'var(--text-muted)' }}><strong>Blockers:</strong> {agent.blockers}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </>
            )}

            {/* Daily Standup (DSM) Tab */}
            {activeTab === 'dsm' && (
              <>
                <div className="page-header">
                  <h1 className="page-title">Daily <span className="gradient-text">Standups Archive</span></h1>
                  <span style={{ color: 'var(--text-muted)', fontSize: '14px' }}>Historical list of daily standups and individual roles status</span>
                </div>

                <div className="glass-panel chat-container" style={{ height: '70vh' }}>
                  {/* Left Pane: Standups History List */}
                  <div className="chat-sidebar" style={{ width: '280px', borderRight: '1px solid rgba(255,255,255,0.08)' }}>
                    <h3 style={{ fontSize: '12px', textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: '12px', letterSpacing: '0.5px' }}>Conducted Logs</h3>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', overflowY: 'auto' }}>
                      {dsmHistory.map((standup, idx) => (
                        <div
                          key={idx}
                          className={`chat-agent-item ${selectedStandupIdx === idx ? 'selected' : ''}`}
                          style={{ padding: '12px 14px', borderRadius: '8px', cursor: 'pointer' }}
                          onClick={() => setSelectedStandupIdx(idx)}
                        >
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                            <span style={{ fontSize: '14px', fontWeight: '700', color: 'var(--text-primary)' }}>{standup.title}</span>
                            <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Sprint: {standup.sprint}</span>
                            <span style={{ fontSize: '10px', color: '#a5b4fc', marginTop: '4px' }}>Facilitator: {standup.facilitator}</span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Right Pane: Selected Standup updates list */}
                  <div className="chat-area">
                    {currentStandup ? (
                      <>
                        <div className="chat-header">
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                            <div style={{ fontWeight: '800', fontSize: '18px', color: 'var(--text-primary)' }}>{currentStandup.title} Details</div>
                            <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Sprint: {currentStandup.sprint} | Facilitated by: {currentStandup.facilitator}</div>
                          </div>
                        </div>

                        <div className="chat-messages" style={{ padding: '24px', overflowY: 'auto' }}>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                            {currentStandup.updates.map((update, idx) => (
                              <div key={idx} className="detail-block" style={{ display: 'flex', gap: '16px', padding: '18px', background: 'rgba(255, 255, 255, 0.01)' }}>
                                <div className="agent-avatar" style={{ width: '42px', height: '42px', fontSize: '13px', background: 'rgba(99, 102, 241, 0.15)', color: '#c7d2fe', flexShrink: 0 }}>
                                  {update.role.slice(0, 2).toUpperCase()}
                                </div>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', flex: 1 }}>
                                  <span style={{ fontSize: '15px', fontWeight: '700', color: 'var(--text-primary)' }}>{update.role}</span>
                                  
                                  <div style={{ fontSize: '13px', lineHeight: '1.4' }}>
                                    <strong style={{ color: '#a5b4fc', fontSize: '11px', textTransform: 'uppercase', display: 'block', marginBottom: '2px' }}>Completed Work:</strong>
                                    <span style={{ color: 'var(--text-primary)' }}>{update.workDone}</span>
                                  </div>

                                  <div style={{ fontSize: '13px', lineHeight: '1.4' }}>
                                    <strong style={{ color: '#a5b4fc', fontSize: '11px', textTransform: 'uppercase', display: 'block', marginBottom: '2px' }}>Next Steps:</strong>
                                    <span style={{ color: 'var(--text-muted)' }}>{update.nextSteps}</span>
                                  </div>

                                  <div style={{ fontSize: '13px', lineHeight: '1.4' }}>
                                    <strong style={{ color: update.blockers !== "None" ? 'var(--red-danger)' : '#a5b4fc', fontSize: '11px', textTransform: 'uppercase', display: 'block', marginBottom: '2px' }}>Blockers:</strong>
                                    <span style={{ color: update.blockers !== "None" ? 'var(--red-danger)' : 'var(--text-muted)', fontWeight: update.blockers !== "None" ? '600' : 'normal' }}>{update.blockers}</span>
                                  </div>
                                </div>
                              </div>
                            ))}
                          </div>
                        </div>
                      </>
                    ) : (
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%', color: 'var(--text-muted)' }}>
                        No standup details loaded.
                      </div>
                    )}
                  </div>
                </div>
              </>
            )}
          </>
        )}
      </main>

      {/* Roster Agent Details Modal Overlay */}
      {selectedRosterAgent && (
        <div className="modal-overlay" onClick={() => setSelectedRosterAgent(null)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <div>
                <h2 style={{ fontSize: '20px', fontWeight: '700', color: 'var(--text-primary)' }}>
                  {selectedRosterAgent.role}
                </h2>
                <div className="agent-detail-badge-row">
                  <span className={`agent-status-badge ${selectedRosterAgent.status.toLowerCase()}`}>
                    {selectedRosterAgent.status}
                  </span>
                  <span className="status-badge" style={{ background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-muted)' }}>
                    Specialist
                  </span>
                </div>
              </div>
              <button className="modal-close-btn" onClick={() => setSelectedRosterAgent(null)}>
                ✕
              </button>
            </div>

            <div className="modal-body">
              {/* Ongoing Task */}
              <div>
                <h4 className="detail-section-title">Current Sprint Task</h4>
                <div className="detail-block">
                  <p style={{ fontSize: '13px', color: 'var(--text-primary)', margin: 0, lineHeight: '1.4' }}>
                    {selectedRosterAgent.task}
                  </p>
                </div>
              </div>

              {/* Blockers */}
              {selectedRosterAgent.blockers && selectedRosterAgent.blockers !== "None" && (
                <div>
                  <h4 className="detail-section-title" style={{ color: 'var(--red-danger)' }}>Active Blockers</h4>
                  <div className="detail-block" style={{ borderLeft: '3px solid var(--red-danger)' }}>
                    <p style={{ fontSize: '13px', color: 'var(--text-primary)', margin: 0, lineHeight: '1.4' }}>
                      {selectedRosterAgent.blockers}
                    </p>
                  </div>
                </div>
              )}

              {/* Purpose */}
              {selectedRosterAgent.purpose && (
                <div>
                  <h4 className="detail-section-title">Role Purpose & Objective</h4>
                  <div className="detail-block">
                    <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0, lineHeight: '1.5' }}>
                      {selectedRosterAgent.purpose}
                    </p>
                  </div>
                </div>
              )}

              {/* Responsibilities */}
              {selectedRosterAgent.responsibilities && selectedRosterAgent.responsibilities.length > 0 && (
                <div>
                  <h4 className="detail-section-title">Core Responsibilities</h4>
                  <ul className="detail-list">
                    {selectedRosterAgent.responsibilities.map((resp, i) => (
                      <li key={i} className="detail-list-item">{resp}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Expected Outputs */}
              {selectedRosterAgent.outputs && selectedRosterAgent.outputs.length > 0 && (
                <div>
                  <h4 className="detail-section-title">Expected Deliverables</h4>
                  <ul className="detail-list">
                    {selectedRosterAgent.outputs.map((out, i) => (
                      <li key={i} className="detail-list-item">{out}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Extreme Skills */}
              {selectedRosterAgent.extreme_skills && selectedRosterAgent.extreme_skills.length > 0 && (
                <div>
                  <h4 className="detail-section-title">Extreme Skills</h4>
                  <div className="detail-block" style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', padding: '12px' }}>
                    {selectedRosterAgent.extreme_skills.map((skill, i) => (
                      <span key={i} className="status-badge" style={{ background: 'rgba(99, 102, 241, 0.12)', color: '#c7d2fe', border: '1px solid rgba(99, 102, 241, 0.2)', fontSize: '11px', margin: 0 }}>
                        {skill}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Project Details Modal Overlay */}
      {selectedProject && (
        <div className="modal-overlay" onClick={() => setSelectedProject(null)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <div>
                <h2 style={{ fontSize: '20px', fontWeight: '700', color: 'var(--text-primary)' }}>
                  {selectedProject.name}
                </h2>
                <div className="agent-detail-badge-row">
                  <span className={`agent-status-badge ${selectedProject.released ? 'active' : 'idle'}`}>
                    {selectedProject.released ? 'Released' : selectedProject.status}
                  </span>
                  <span className="status-badge" style={{ background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-muted)' }}>
                    Target: {selectedProject.releaseDate}
                  </span>
                </div>
              </div>
              <button className="modal-close-btn" onClick={() => setSelectedProject(null)}>
                ✕
              </button>
            </div>

            <div className="modal-body">
              {/* Folder Location */}
              <div>
                <h4 className="detail-section-title">Project Directory Folder</h4>
                <div className="detail-block">
                  <code style={{ fontSize: '12px', color: '#a5b4fc', fontFamily: 'monospace' }}>
                    {selectedProject.folder}
                  </code>
                </div>
              </div>

              {/* Description */}
              <div>
                <h4 className="detail-section-title">Project Summary & Objective</h4>
                <div className="detail-block">
                  <p style={{ fontSize: '13px', color: 'var(--text-primary)', margin: 0, lineHeight: '1.5' }}>
                    {selectedProject.description}
                  </p>
                </div>
              </div>

              {/* Technology Stack */}
              <div>
                <h4 className="detail-section-title">Technology Stack</h4>
                <div className="detail-block" style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', padding: '12px' }}>
                  {selectedProject.tech.map((t, idx) => (
                    <span key={idx} className="status-badge" style={{ background: 'rgba(99, 102, 241, 0.12)', color: '#c7d2fe', border: '1px solid rgba(99, 102, 241, 0.2)', fontSize: '11px', margin: 0 }}>
                      {t}
                    </span>
                  ))}
                </div>
              </div>

              {/* Sprint Status */}
              <div>
                <h4 className="detail-section-title">Active Milestone / Sprint Run</h4>
                <div className="detail-block">
                  <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0, lineHeight: '1.4' }}>
                    {selectedProject.sprint}
                  </p>
                </div>
              </div>

              {/* Custom Action (e.g. redirect to Sprint Kanban if active) */}
              {selectedProject.id === 'car-detection' && (
                <div style={{ marginTop: '10px' }}>
                  <button
                    className="send-btn"
                    style={{ width: '100%', padding: '12px', borderRadius: '10px', fontSize: '13px' }}
                    onClick={() => {
                      setActiveTab('pipeline');
                      setSelectedProject(null);
                    }}
                  >
                    Open Active Sprint Kanban Board
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Roster Loading Overlay */}
      {rosterModalLoading && (
        <div className="modal-overlay">
          <div style={{ color: 'var(--text-primary)', fontSize: '16px' }}>Loading agent specifications...</div>
        </div>
      )}
    </div>
  );
}
