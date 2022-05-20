import speech_recognition as sr
import pyttsx3
import datetime
import cv2
import time

# Instancia o reconhecedor e sintetizador de voz
audio = sr.Recognizer()
maquina = pyttsx3.init()

# Instancia a câmera e o classificador de reconhecimento facial
video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Simula um banco de dados utilizando dicionários
cadastros = {}
pacientes = {'Bruno' :['Bruno', '19', '11122233344', '988887777', 'M']}


def identifica_face():
    qtd_frame_face = 0
    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        #Coloca um retângulo nas faces identificada
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('video', frame)

        #Conta se no frame tem um rosto
        if len(faces) != 0:
            qtd_frame_face += 1
        elif len(faces) == 0:
            qtd_frame_face = 0
                
        #Se o for identificado 30 frames seguidos com rosto
        if qtd_frame_face ==20:
            maquina.say('rosto identificado')
            maquina.runAndWait()
            break


        if cv2.waitKey(1) & 0xFF == ord('q'):
            maquina.say('rosto identificado')
            maquina.runAndWait()
            break

    cv2.destroyAllWindows()
    return True

def ouvindo():
    voz = audio.listen(source)        
    comando = audio.recognize_google(voz, language='pt')
    comando = comando.lower()
    print(comando)
    return comando

def cadastrar():
    maquina.say('Digite as informações necessárias.')
    maquina.runAndWait()
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    cpf = input('Digite seu CPF: ')
    telefone = input('Digite seu telefone: ')
    genero = input('Informe seu genero [M/F]: ')

    #coloca todas as informações em uma lista
    cadastro = [nome, idade, cpf, telefone, genero]
    return cadastro

def visita():
    #Recebe a hora do sistema
    hora = int(datetime.datetime.now().strftime('%H'))
    resposta = ''

    if 10 < hora < 16:
        maquina.say('Informe o nome do paciente.')
        maquina.runAndWait()
        nome_paciente = input('Informe o nome do paciente: ')
        
        #Verifica se o paciente existe no BD
        if nome_paciente in pacientes:
            resposta = 'Entrada autorizada'
        else:
            resposta = 'Paciente não encontrado'
    else:
        resposta = 'O horário de visita é das 10 ás 16 horas'

    return resposta

def consulta():
    maquina.say('Digite as informações necessárias.')
    maquina.runAndWait()
    temperatura = input('Digite a temperatura: ')
    pressao = input('Digite a pressão: ')
    batimentos = input('Digite os batimnetos: ')
    agendamento_consulta = ['Dr. Roberto', 'B', '14']
    return agendamento_consulta

def historico():
    consultas = [['Santa Cruz','12/04/2022', 'Dr. Roberto'], ['Santo Amaro', '15/04/2022', 'Dr. Breno']]
    return consultas

with sr.Microphone() as source:
                while True:
                    face = identifica_face()

                    while True:
                        if face == True:            #Se foi reconhecida alguma face
                            maquina.say('Posso ajudar?')
                            maquina.runAndWait()
                            comando = ouvindo()
                            if 'cadastro' in comando:
                                cadastro = cadastrar()
                                cadastros[cadastro[0]] = cadastro           #Pega a lista cadastro, utiliza o primerio termo(nome) como chave para o dicionario e a propria lista como valor
                                print(cadastros)
                                maquina.say('Cadastro finalizado')
                                maquina.runAndWait()
                            elif 'visita' in comando:
                                resposta = visita()
                                maquina.say(resposta)
                                maquina.runAndWait()
                            elif 'consulta' in comando:
                                agenda_consulta = consulta()
                                agenda = f'Você tem uma consulta marcada com {agenda_consulta[0]}, no setor {agenda_consulta[1]}, às {agenda_consulta[2]} horas'
                                print(agenda)
                                maquina.say(agenda)
                                maquina.runAndWait()
                            elif 'histórico' in comando:
                                historico = historico()
                                maquina.say('Exibindo seu histórico de triagem.')
                                maquina.runAndWait()
                                for c in historico:
                                    print(f'{c[0]}')
                                    print(f'{c[1]}')
                                    print(f'{c[2]}')
                                    print(10* '=')
                                time.sleep(3)
                            else: 
                                maquina.say('Desculpe, não entendi')
                                maquina.runAndWait()
                            
                        
