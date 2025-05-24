from flask import render_template, request, redirect, url_for, flash, session
from app import db
from .models import User
from config import Config

def index():
    return render_template('index.html')

def about():
    return render_template('about.html')

def see_users():
    users = User.query.all()
    return render_template('see_users.html', users=users, database_url=Config.SQLALCHEMY_DATABASE_URI)
