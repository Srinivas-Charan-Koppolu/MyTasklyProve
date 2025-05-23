from flask import render_template, request, redirect, url_for, flash, session
from app import db
from app.models import User

def auth_disabled_index():
    return render_template('auth_disabled.html')

def register():
    if 'user_id' in session:
        flash('You are already logged in.', 'info')
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if user exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already taken. Please choose another.', 'error')
            return redirect(url_for('modules.auth.register'))

        # Create new user
        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('modules.auth.login'))

    return render_template('register.html')

def login():
    if 'user_id' in session:
        flash('You are already logged in.', 'info')
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('modules.dashboard.index'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('modules.auth.login'))

    return render_template('login.html')

def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('modules.auth.login'))