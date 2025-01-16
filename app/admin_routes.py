from flask import Blueprint, render_template, redirect, url_for
from .models import db, Article
from .forms import ArticlesForm

admin = Blueprint('admin', __name__)

@admin.route('/add', methods=['GET', 'POST'])
def add_article():
    form = ArticlesForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data, content=form.content.data)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('admin/add_artikel.html', form=form)
