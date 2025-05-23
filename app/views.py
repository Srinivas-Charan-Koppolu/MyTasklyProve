from flask import render_template, request, redirect, url_for, flash, session
from app import db
from .models import User



def index():
    return render_template('index.html')

