from django.urls import path
from . import views

urlpatterns = [
    path('detect/image/', views.DetectImageView.as_view(), name='detect_image'),
    path('detect/frame/', views.DetectFrameView.as_view(), name='detect_frame'),
    path('model/info/', views.ModelInfoView.as_view(), name='model_info'),
    path('health/', views.HealthView.as_view(), name='health'),
    
    # Workspace Status Portal Endpoints
    path('workspace/status/', views.WorkspaceStatusView.as_view(), name='workspace_status'),
    path('workspace/pipeline/', views.WorkspacePipelineView.as_view(), name='workspace_pipeline'),
    path('workspace/pipeline/move/', views.WorkspacePipelineMoveView.as_view(), name='workspace_pipeline_move'),
    path('workspace/docs/', views.WorkspaceDocsView.as_view(), name='workspace_docs'),
    path('workspace/chat/', views.WorkspaceChatView.as_view(), name='workspace_chat'),
    path('workspace/dsm/', views.WorkspaceDSMView.as_view(), name='workspace_dsm'),
    path('workspace/logs/', views.WorkspaceLogsView.as_view(), name='workspace_logs'),
    path('workspace/approvals/', views.WorkspaceApprovalsView.as_view(), name='workspace_approvals'),
    path('workspace/approvals/act/', views.WorkspaceApprovalsActView.as_view(), name='workspace_approvals_act'),
    path('workspace/agent/run/', views.WorkspaceAgentRunView.as_view(), name='workspace_agent_run'),
    path('workspace/agent/details/', views.WorkspaceAgentDetailsView.as_view(), name='workspace_agent_details'),
    path('workspace/projects/', views.WorkspaceProjectsView.as_view(), name='workspace_projects'),
    path('workspace/dsm/history/', views.WorkspaceDSMHistoryView.as_view(), name='workspace_dsm_history'),
]
