from flask import Blueprint, render_template, request, redirect, url_for, flash

Taskly = Blueprint('Taskly', __name__)


@Taskly.route('/')
def index():
    return redirect(url_for('Taskly.dashboard.index'))
