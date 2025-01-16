from flask import Blueprint, render_template
from .models import Article

main = Blueprint('main', __name__)

@main.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html')
