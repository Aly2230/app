import secrets
#o IDEIAL SERIA UMA FERRAMENTA PARA GERAR ESSA CHAVE E DENTRO DE UMA VARIÁVEL DE AMBIENTE E NAO GERAR ASSIM
#crie um arquivo .py como nome secret para gerar,importe serets que é uma bibioteca já do py instacie  a variável sk=secrets.token_hex(24)o o n° é a quantidade de caracters printa e coloca a chave #
sk=secrets.token_hex(24)
print(sk)
