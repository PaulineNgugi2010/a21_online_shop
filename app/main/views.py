from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import main
from .. import db

@main.route('/')
def home():
    return render_template('index.html', title="Welcome to Couture Boutique")

# @main.route('/dashboard')
# @login_required
# def dashboard():
#     issue_count = Issue.query.filter(Issue.user_id == current_user.id).count()
#     resolved_issues = (Issue.query
#         .filter(Issue.user_id == current_user.id)
#         .filter(Issue.is_resolved == True)
#         ).count()
#     issues_in_progress = (Issue.query
#         .filter(Issue.user_id == current_user.id)
#         .filter(Issue.is_assigned == True)
#         ).count()

#     counts = dict(issue_count=issue_count, resolved_issues=resolved_issues, issues_in_progress=issues_in_progress)
#     return render_template('dashboard.html', counts=counts, title="Dashboard")

# @main.route('/admin/dashboard')
# @login_required
# def admin_dashboard():
#     issue_count = Issue.query.count()
#     resolved_issues = Issue.query.filter(Issue.is_resolved == True).count()
#     issues_in_progress = Issue.query.filter(Issue.is_assigned == True).count()

#     counts = dict(issue_count=issue_count, resolved_issues=resolved_issues, issues_in_progress=issues_in_progress)
#     return render_template('admin_dashboard.html', counts=counts, title="Dashboard")