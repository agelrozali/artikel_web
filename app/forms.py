from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ArticlesForm(FlaskForm):
    judul = StringField('Judul', validators=[DataRequired()], render_kw={'class': 'form-control'})
    konten = TextAreaField('Konten', validators=[DataRequired()], render_kw={'class': 'form-control'})
    penulis = StringField('Penulis', validators=[DataRequired()], render_kw={'class': 'form-control'})
    kategori = SelectField('Kategori', choices=[], validators=[DataRequired()], render_kw={'class': 'form-control'})