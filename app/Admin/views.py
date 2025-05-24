from flask import render_template, redirect, request, session, flash, url_for
from app.models import AdminUser

def has_admin_access(user_id):
    return AdminUser.isAdmin(user_id)


def adminPanel():
    if 'user_id' not in session:
        flash("Login to open admin panels", "error")
        return redirect(url_for("Taskly.auth.login"))
    if not has_admin_access(session['user_id']):
        flash("You don't have permissions for admin access", "error")
        return redirect(url_for("Taskly.dashboard.index"))
    return render_template('admin.html')

