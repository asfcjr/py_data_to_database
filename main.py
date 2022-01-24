from tkinter import *
import mysql.connector


# realizando a conexao entre o Python e MySQL
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_login"
)

# executando a funcao de armazenar dados
def impDados():

# transcrevendo as variaveis do comando .Entry() do Tkinter, adicionando .get()
# caso nao transcreva o valor que sera adicionado na tabela sera .entry1!
    user = in_user.get()
    email = in_email.get()
    password = in_password.get()

# comando MySQL para inserir na tabela Cadastros nos campos user,email,password, com valor vazio, atribuindo em strings
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cadastros (user,email,password) VALUES (%s,%s,%s)"
    dados = (str(user), str(email), str(password))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    print(user)
    print(email)
    print(password)


# funcoes para text placeholder, quando usuario clicar sumira o textholder, voltara pro state=NORMAL
def click(event):
    in_user.config(state=NORMAL)
    in_user.delete(0, END)

def click2(event2):
    in_email.config(state=NORMAL)
    in_email.delete(0, END)

def click3(event3):
    in_password.config(state=NORMAL, textvariable=hide_password, show="•")
    in_password.delete(0, END)


# definindo as dimensoes da interface e adicionando icone
interface = Tk()
interface.title("Create Account")
interface.geometry("490x560+610+153")
interface.iconbitmap(default="icones\\ico.ico")
interface.resizable(width= 1, height=1)

# mascarar a senha
hide_password = StringVar()

# importando imagens e salvando em variaveis
img_bg = PhotoImage(file="images\\fundo.png")
img_button = PhotoImage(file="images\\bt-img.png")

# definindo imagem de fundo com comando Label(image=)
lab_fundo = Label(interface, image=img_bg)
lab_fundo.pack()


# adicionando entrada de texto com comando Entry()
# local onde sera colocado
in_user = Entry(interface, bd=2, font=("Calibri", 15))
in_user.place(width=392, height=45, x=49, y=150)

# inserindo um texholder em User
in_user.insert(0, " Type a user")
in_user.config(state=DISABLED)
in_user.bind("<Button-1>", click)


# adicionando entrada de texto com comando Entry()
# local da tela onde sera colocado
in_email = Entry(interface, bd=2, font=("Calibri", 15))
in_email.place(width=392, height=45, x=49, y=248)

# inserindo um texholder em E-mail
in_email.insert(0, " Type a e-mail")
in_email.config(state=DISABLED)
in_email.bind("<Button-1>", click2)


# adicionando entrada de texto com comando Entry()
# local da tela onde sera colocado
in_password = Entry(interface, bd=2, font=("Calibri", 15))
in_password.place(width=392, height=45, x=49, y=348)

# inserindo um texholder em Password
in_password.insert(0, " Type a password")
in_password.config(state=DISABLED)
in_password.bind("<Button-1>", click3)


# adicionando botao na interface, importando img e adicionando comando na funcao de armazenar dados
# local da tela onde sera colocado
bt_create = Button(interface, bd=0, image=img_button, command=impDados)
bt_create.place(width=118, height=64, x=186, y=448)

interface.mainloop()