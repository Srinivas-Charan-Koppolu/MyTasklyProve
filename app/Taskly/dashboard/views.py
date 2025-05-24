from flask import Blueprint, render_template, session, redirect, url_for, flash
from utils import isLoggedIn


def dashboard_disabled():
    return render_template('dashboard_disabled.html')

@isLoggedIn
def dashboard():
    return render_template('dashboard.html', username=session.get('username'))
