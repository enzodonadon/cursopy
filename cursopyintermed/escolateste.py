import os, time
import smtplib, email.message, random
import subprocess

comando = "cls" if os.name == "nt" else "clear"

codg = random.randint(100000, 999999)
codg2 = random.randint(100000, 999999)
codg3 = random.randint(100000, 999999)

def tempo_tela(x):
    for seg in range(x):
        time.sleep(1)
    subprocess([comando], shell = True)


myemail = ""
cont = 0

while True:
    print("Bem vindo ao Ischool-a!")
    print("")
    op = input('Digite "N" para novo login ou ignore para continuar. ')
    if op == "N" or op == "n":
        cond = None
        while cond == None:
            subprocess([comando], shell = True)
            usuario = input("Digite o nome do seu usuario: ")
            if not usuario.isalpha():   
                print("Seu usuario deve conter apenas letras.")
                for seg_rest in range(2):
                    time.sleep(1)
                continue
            else:
                cond = True

            ler_user = len(usuario)
            if ler_user < 4:
                cond = None
                print("Minimo 4 caracteres.")
                for seg_rest in range(2):
                    time.sleep(1)

            else:
                cond = True
                subprocess([comando], shell = True)
        
        cond1 = None
        while cond1 == None:
            senha = input("Digite sua senha: ")
            ler_senha = len(senha)
            if ler_senha < 4:
                print("Minimo 4 caracteres.")
                tempo_tela(2)
            else:
                cond1 = True

        print("")
        #Dados obrigatorios
        print("Antes de continuar, voce deverá fornecer alguns dados obrigatorios.")
        tempo_tela(2)
        
        #Idade
        cond = None
        while cond == None:
            idade_inp = input("Idade: ")
            try:
                idade = int(idade_inp)
                if idade < 4 or idade > 150:
                    print("Idade invalida. Tente novamente.")
                    tempo_tela(2)
                    continue
                else:
                    cond = True
            except (ValueError, TypeError):
                print("O campo deve conter um numero inteiro.")
                tempo_tela(2)
                continue
        subprocess([comando], shell = True)      

        #Serie    
        cond = None
        while cond == None:
            serie_inp = input("Serie: ")
            try:
                serie = int(serie_inp)
                if serie not in range(1, 10):
                    print("O campo deve conter um numero inteiro de 1 à 9.")
                    tempo_tela(2)
                    continue
                else:
                    if serie >= 1 and serie <= 3:
                        ensino = input("Pertence ao ensino medio (S/N)? ")
                        while ensino != "S" and ensino != "s" and ensino != "N" and ensino != "n":
                            subprocess([comando], shell = True)
                            ensino = input("Digite um caractere valido (S/N): ")
                        cond = True
                    else:
                        ensino = None
                        cond = True
            except:
                print("O campo deve conter um numero inteiro.")
                tempo_tela(2)
                continue
            
        print("")
        print("Parabéns! Voce criou uma nova conta, aproveite!")

        tempo_tela(2)
    cond8 = None
    while cond8 == None:
        subprocess([comando], shell = True)
        cad1 = input("Digite seu usuario: ")
        cad = input("Digite sua senha: ")
        if cad1 == "V" or cad1 == "v" or cad == "V" or cad == "v":
            subprocess([comando], shell = True)
            break
        try:
            senha1 = senha
            usuario1 = usuario
        except:
            senha1 = None
            usuario1 = None
        if cad != senha1 or cad1 != usuario1:
            print("")
            print("Login não encontrado. Tente novamente. (V: Voltar)")
            tempo_tela(2)
        else:
            cond8 = True
    if cond8 == True:
        break

print("")
print("Carregando as informações.")

for seg_rest in range(2):
        time.sleep(1)

#Abre o menu de opcoes

while True:
    subprocess([comando], shell = True)
    print("1: Perfil | 2: Notas | 3: Tarefas")
    opcoes_inp = (input(""))
    try:
        opcoes = int(opcoes_inp)
    except:
        print("Caractere invalido. Tente novamente.")
        tempo_tela(2)
        continue

    #Perfil        
    while opcoes == 1:
        subprocess([comando], shell = True)
        print(f"Colégio Elementar\n\nNome de usuario: {usuario1}\nIdade: {idade}")
        if ensino == "S" or ensino == "s":
            print(f"Serie: {serie}º E.M.")
        elif ensino == "N" or ensino == "n" or ensino == None:
            print(f"Serie: {serie}º Ano")
        print("")
        if myemail == "":
            print("Adicione um Email em Configurações avançadas. (Opicional)")
        else:
            print(f"Email: {myemail}")
        print("")
        print("C: Cofigurações avançadas | V: Voltar")
        pressione = input("")
            
        if pressione != "v" and pressione != "V" and "C" and pressione != "c":
            print("Digite um caractere valido.")
            tempo_tela(2)
            continue
        if pressione == "v" or pressione == "V":
            subprocess([comando], shell = True)
            break
        elif pressione == "C" or pressione == "c":
            subprocess([comando], shell = True)
            while myemail == "":
                subprocess([comando], shell = True)
                print("E: Adicionar E-Mail | S: Mudar senha | V: Voltar")
                op1 = input("")
                if op1 != "E" and op1 != "e" and op1 != "S" and op1 != "s" and op1 != "v" and op1 != "V":
                    print("")
                    print("Digite um caractere valido.")
                    tempo_tela(2)
                
                    #enviar email para adicionar
                if op1 == "E" or op1 == "e":
                    cont5 = 0
                    subprocess([comando], shell = True)
                    while True:
                        myemail = input("Digite seu email: ")
                        if "gmail.com"  not in myemail and "yahoo.com"  not in myemail and "hotmart.com" not in myemail:
                            print("Digite um email válido.")
                            tempo_tela(2)
                        else:
                            break
                    
                    def enviar_email():  
                        corpo_email = (f"""
                            <p>Para concluir a adição de um email a sua conta Ischool-a, só precisamos verificar se este endereço de email é seu.</p>
                        
                            <p>Para verificar seu endereço de email, use este código de segurança: <b>{codg}</b></p>
                            
                            <p>Se você não solicitou este código, poderá ignorar com segurança este email. Outra pessoa pode ter digitado seu endereço de email por engano.</p>
                            
                            <p>Obrigado,\n
                            Equipe Ischool-a</p>
                        """)

                        msg = email.message.Message()
                        msg['Subject'] = ("Confirmação de E-Mail.")
                        msg['From'] = 'ischoolasup@gmail.com'
                        msg['To'] = (f'{myemail}')
                        password = 'shec kcxu ekms pegv ' 
                        msg.add_header('Content-Type', 'text/html')
                        msg.set_payload(corpo_email )

                        s = smtplib.SMTP('smtp.gmail.com: 587')
                        s.starttls()
                        # Login Credentials for sending the mail
                        s.login(msg['From'], password)
                        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                        print("")
                        print('Email enviado. Verifique seu email.')
                    
                    enviar_email()
                    print("")
                    print("Caso não tenha recebido, verifique seu spam ou tente novamente: (6).")
                    #email enviado

                    os.system
                    cond5 = None
                    while cond5 == None:
                        if cont5 == 5:
                            print("Foi realizada muitas tentativas. Tente novamente mais tarde.")
                            myemail = ""
                            tempo_tela(3)                 
                            break
                        else:
                            confirm_codg_inp = input("Digite o código enviado em seu email: ")
                            try:
                                confirm_codg = int(confirm_codg_inp)
                                
                                if confirm_codg != codg: 
                                    if confirm_codg == 6:
                                        myemail = ""
                                        break                 
                                    elif confirm_codg != codg:
                                        cont5 = cont5 + 1
                                        print("")
                                        print("Código inválido. Tente novamente.")
                                        tempo_tela(2)
                                else:    
                                    cond5 = True
                                    print("")
                                    print("Verificação concluida. Email adicionado com êxito!")
                                    tempo_tela(2)
                            except:
                                cont5 = cont5 + 1
                                print("")
                                print("Codigo inválido. Tente novamente")
                                tempo_tela(2)
                                continue

                elif op1 == "S" or op1 == "s":
                    print("Para alterar sua senha, é necessario adicionar um email para a confirmação.")
                    tempo_tela(2)  
                elif op1 == "v" or op1 == "V":
                    subprocess([comando], shell = True)
                    break
            cont = 0
            while myemail != "":
                subprocess([comando], shell = True)
                print("E: Alterar E-Mail | S: Mudar senha | V: Voltar")
                op1 = input("")
                if op1 != "E" and op1 != "e" and op1 != "S" and op1 != "s" and op1 != "v" and op1 != "V":
                    print("Digite um caractere válido.")
                    tempo_tela(2)
                elif op1 == "E" or op1 == "e":
                    subprocess([comando], shell = True)
                    while True:
                        myemail = input("Digite seu email que deseja trocar/alterar: ")
                        if "gmail.com" not in myemail and "yahoo.com" not in myemail and "hotmart.com"not in myemail:
                            print("Digite um email válido.")
                            tempo_tela(2)
                        else:
                            break
                    
                    #enviar email para alterar
                    def enviar_email_2():  
                        corpo_email = (f"""
                            <p>Para concluir a alteração de um email a sua conta Ischool-a, só precisamos verificar se este endereço de email é seu.</p>
                        
                            <p>Para alterar/trocar seu endereço de email, use este código de segurança: <b>{codg2}</b></p>
                            
                            <p>Se você não solicitou este código, poderá ignorar com segurança este email. Outra pessoa pode ter digitado seu endereço de email por engano.</p>
                            
                            <p>Obrigado,
                            Equipe Ischool-a</p>
                        """)

                        msg = email.message.Message()
                        msg['Subject'] = ("Confirmação de E-Mail.")
                        msg['From'] = 'ischoolasup@gmail.com'
                        msg['To'] = (f'{myemail}')
                        password = 'shec kcxu ekms pegv ' 
                        msg.add_header('Content-Type', 'text/html')
                        msg.set_payload(corpo_email )

                        s = smtplib.SMTP('smtp.gmail.com: 587')
                        s.starttls()
                        # Login Credentials for sending the mail
                        s.login(msg['From'], password)
                        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                        print("")
                        print('Email enviado. Verifique seu email.')
                    
                    enviar_email_2()
                    print("")
                    print("*Caso não tenha recebido, verifique seu spam ou tente novamente (6).*")
                    #email enviado

                    subprocess([comando], shell = True)
                    cond3 = None
                    
                    while cond3 == None:
                        subprocess([comando], shell = True)
                        confirm_codg2_inp = input("Digite o código enviado em seu email: ")
                        try:
                            confirm_codg2 = int(confirm_codg2_inp)
                            cond3 = True
                        except:
                            print("")
                            print("Codigo invalido.")
                            tempo_tela(2)        
                        
                    if confirm_codg2 != codg2: 
                        if confirm_codg2 == 6:
                            continue
                        else: 
                            cont4 = 0
                            while cont4 < 5 and confirm_codg2 != codg2:
                                cont4 = cont4 + 1
                                print("Código inválido.")
                                print("")
                                tempo_tela(2)
                                confirm_codg2_inp = input("Digite o código novamente: ")
                                try:
                                    confirm_codg2 = int(confirm_codg2_inp)
                                except:
                                    subprocess([comando], shell = True)
                            if cont4 >= 5 and confirm_codg2 != codg2:
                                print("Foi realizada muitas tentativas. Tente novamente mais tarde.")
                                break
                    else:
                        print("")
                        print("Verificação concluida.")
                        tempo_tela(2)
                    while True:
                        myemail = input("Digite seu novo email: ")
                        if "gmail.com" not in myemail and "yahoo.com" not in myemail and "hotmart.com"not in myemail:
                            print("Digite um email válido.")
                            tempo_tela(2)
                        else:
                            break
                    print("Email alterado com sucesso!")
                    tempo_tela(2)

                elif op1 == "S" or op1 == "s":
                    cont4 = 0
                    cont2 = 0
                    while True:
                        sa = input("Digite sua senha atual: ")
                        print("")
                        if sa == senha1:
                            cond2 = None
                            while cond2 == None:
                                subprocess([comando], shell = True)
                                senha1 = input("Agora, digite sua nova senha: ")
                                ler_senha1 = len(senha1)
                                if ler_senha1 < 4:
                                    print("Minimo 4 caracteres. ")
                                    tempo_tela(2)
                                else:
                                    cond2 = True
                                    print("")
                                    print("Sua senha foi alterada com êxito!")
                                    tempo_tela(2)
                            break    
                        elif sa != senha1:
                            cont2 = cont2 + 1
                            print("Senha incorreta. Tente novamente.")
                            print("")
                            print('Caso tenha esquecido a senha, digite "5".')
                            for seg_rest in range(3):
                                time.sleep(1)
                            subprocess([comando], shell = True)
                            if cont2 == 5:
                                print("Foi realizada muitas tentativas. Tente novamente mais tarde.")
                                break
                        elif sa == 5:
                            #enviar email para esquecimento de senha
                            def enviar_email_3():  
                                corpo_email = (f"""
                                    <p>Caso não se lembre de sua senha, use este código de segurança: <b>{codg3}</b></p>
                                    
                                    <p>Se você não solicitou este código, poderá ignorar com segurança este email. Outra pessoa pode ter digitado seu endereço de email por engano.</p>
                                    
                                    <p>Obrigado,
                                    Equipe Ischool-a</p>
                                """)

                                msg = email.message.Message()
                                msg['Subject'] = ("Confirmação de E-Mail.")
                                msg['From'] = 'noreply@gmail.com'
                                msg['To'] = (f'{myemail}')
                                password = 'shec kcxu ekms pegv ' 
                                msg.add_header('Content-Type', 'text/html')
                                msg.set_payload(corpo_email )

                                s = smtplib.SMTP('smtp.gmail.com: 587')
                                s.starttls()
                                
                                s.login(msg['From'], password)
                                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                            
                            try:
                                enviar_email_3()
                                print("")
                                print('Email enviado. Verifique seu email.')
                            except Exception:
                                print("Erro ao enviar email. Tente novamente")


                            print("")
                            print("*Caso não tenha recebido, verifique seu spam ou tente novamente (6).*")
                            #email enviado
                            print("")
                            subprocess([comando], shell = True)
                            cond4 = None
                            while cond4 == None:
                                confirm_codg3_inp = input("Digite o código enviado em seu email: ")
                                try:
                                    confirm_codg3 = int(confirm_codg3_inp)
                                    cond4 = True
                                except:
                                    print("")
                                    print("Codigo invalido. Tente novamente")
                                    tempo_tela(2) 
                            if confirm_codg3 == codg3:
                                print("")
                                print("Verificação concluida.")
                                tempo_tela(2)
                            else: 
                                if confirm_codg3 == 6:
                                    break
                                else:
                                    while cont < 5 and confirm_codg3 != codg3:
                                        cont = cont + 1
                                        print("Código inválido.")
                                        print("")
                                        confirm_codg3_inp = input("Digite o código novamente: ")
                                        try:
                                            confirm_codg3 = int(confirm_codg3_inp)
                                        except:
                                            subprocess([comando], shell = True)
                                        subprocess([comando], shell = True)
                                    if cont == 5 and confirm_codg3 != codg3:
                                        print("Foi realizada muitas tentativas. Tente novamente mais tarde.")
                                        break
                            print(f'Sua senha é "{senha1}".')
                            print("")
                            ig = input("Ignore para continuar. ")
                            break  
                elif op1 == "v" or op1 == "V":
                    break
    while opcoes == 2:
        subprocess([comando], shell = True)
print("")    