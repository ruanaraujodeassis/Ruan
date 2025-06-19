#projeto oraculo
import pygame
import random
import time
import pyttsx3

voz = pyttsx3.init()
voz.setProperty('rate',200)
voz.setProperty('volume',3.0)




pygame.mixer.init()


def tocar_som_mistico():
    pygame.mixer.music.load("mystical-music-54294.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.30)

    





respostas = [ "Com certeza!",
    "Nem em um milhão de anos.",
    "Melhor você nem saber...",
    "Sinais apontam que sim.",
    "Pfff, tenta outra vez!",
    "AHHMM? Só se chover ouro no céu.",
    "Lógico!, mas só se você dançar antes.",
    "A resposta está dentro de você jovem padawan.",
    "Eu acho que você já tem ideia da resposta né.",
    "99% de chance... de você se arrepender.",
    "A resposta é não, mas se você tiver fé, talvez",
    "você já conseguiu, mas não sabe."
]



print("🎇🧙‍♂️Bem vindo ao oráculo da força misteriosa!🔮🎇")
print("Faça a sua pergunta, e eu responderei com a força misteriosa...🌠")
tocar_som_mistico()
voz.say("Bem vindo ao oráculo da força misteriosa! Faça a sua pergunta, e eu responderei com a força misteriosa.")
voz.runAndWait()

while True:
    pergunta = input("\n ❓Faça sua pergunta:")

   
   
    if pergunta.strip() == "":
        print("O oráculo não reponde perguntas vazias! Faça a sua pergunta mística!")
        voz.say("O oráculo não reponde perguntas vazias! Faça a sua pergunta mística!")
        voz.runAndWait()
   
   
    else:
       
        print("O oráculo está pensando...")
        time.sleep(2)
        voz.stop()
        voz.say("O oráculo está pensando...")

        
        
        resposta = random.choice(respostas)
        print(f"✨Resposta do oráculo: {resposta}✨")
        voz.stop()
        voz.say(f"Resposta: {resposta}")
        voz.runAndWait()
        
        
        repetir = input("\n Deseja fazer outra pergunta? (s/n):").lower().strip()
        if repetir != 's':
            print("Obrigado por usar o oráculo da força misteriosa! Até a próxima! 🌌")
           
        
           
            break
