from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    image = FileField("Image", [DataRequired()])
