from flask import Blueprint, render_template, session, redirect, url_for, flash


def dashboard_disabled():
    return render_template('dashboard_disabled.html')

def dashboard():
    if 'user_id' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('Taskly.auth.login'))

    return render_template('dashboard.html', username=session.get('username'))
