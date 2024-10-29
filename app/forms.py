from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email

from app import db
from app.models import Contato 
#baixar o pacote flask_wtf e wtforms para poder utilizar  StringField,SubmitField,
#DataRequired,Email
#criar a lista
class ContatoForm(FlaskForm):
    nome=StringField('Nome:',validators=[DataRequired()])
    email=StringField('E-Mail:',validators=[DataRequired(),Email()])
    assunto=StringField('Assunto:',validators=[DataRequired()])  
    mensagem=StringField('Mensagem:',validators=[DataRequired()])
    btnSubmit=SubmitField('Enviar')
    #construir uma função para salvar os dados do formulário no banco de dados
    def save(self):
        contato=Contato(
             nome=self.nome.data,
             email=self.email.data,
             assunto=self.assunto.data,
             mensagem=self.mensagem.data
        )
        db.session.add(contato)
        db.session.commit()