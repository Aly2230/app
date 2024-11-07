from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email, EqualTo, ValidationError

from app import db,bcrypt
from app.models import Contato ,User,Post
#baixar o pacote flask_wtf e wtforms para poder utilizar  StringField,SubmitField,
#DataRequired,Email
#criar a lista

#Formulário para o controle de login padrão
class UserForm(FlaskForm):
     nome=StringField('Nome:',validators=[DataRequired()])
     sobrenome=StringField('Sobrenome:',validators=[DataRequired()])
     email=StringField('E-Mail:',validators=[DataRequired(),Email()])
     senha=PasswordField('Senha:',validators=[DataRequired()])
     confirmacao_senha=PasswordField('Senha:',validators=[DataRequired(),EqualTo('senha')])
     btnSubmit=SubmitField('Cadastrar')
     #função para verificar se o mail já existe no banco de dados
     def validade_email(self,email):
         if User.query.filter(email=email.data).first():
             return ValidationError('Usuário já cadastrado com esse E-mail!!!')
         #aqui é para salvar no banco de dados
     def save(self):
         senha=bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
         user = User(
                nome=self.nome.data,
                 sobrenome=self.sobrenome.data,
                 email=self.email.data,
                 senha=senha    
             )
         
         db.session.add(user)
         db.session.commit()
         return user
     
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
        
class LoginForm(FlaskForm):
   email=StringField('E-Mail:',validators=[DataRequired(),Email()])
   senha=PasswordField('Senha:',validators=[DataRequired()])
   btnSubmit=SubmitField('Login')
   def login(self):
       #Recperar o usuário do e-mail
       user=User.query.filter_by(email=self.email.data).first()
       
       #Verificar se a senha é válida
       if user:
            if bcrypt.check_password_hash(user.senha,self.senha.data.encode('utf-8')):
                 # retornar o usuario 
               return user
            else:
                raise Exception('Senha incorreta!!')
       else:
           raise Exception('Usuário não encontrado!!!')
       
       
class PostForm(FlaskForm):
        mensagem=StringField('Mensagem',validators=[DataRequired()])
        btnSubmit=SubmitField('Enviar')
         
        def save(self,user_id):
            post= Post(
                  mensagem=self.mensagem.data,
                  user_id=user_id
             )
            db.session.add(post)
            db.session.commit()



