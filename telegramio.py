#!/usr/bin/env python3

import os

def envio_mensaje(TOKEN, ID, Mensaje):
    """
    Codigo mòdulo parar envio de mensajes a telegram se requiere tener instalado curl en el sistema operativo GNU Linux

    Args:
        TOKEN (string): token del bot
        ID (string): Id del chat a enviar mensaje
        mensaje (string): mensaje a enviar

    #/usr/bin/curl -s -X POST $URL -d chat_id=$IDJN -d text="$MENSAJE"  > /dev/null

    #URL="https://api.telegram.org/bot$TOKEN/sendMessage"

    """
    URL_part1 = "https://api.telegram.org/bot"
    URL_part2 = "/sendMessage"
    URL = URL_part1 + TOKEN + URL_part2
    #print(URL)
    comando_part0 = "/usr/bin/curl"
    comando_part1 = " -s -X POST "
    comando_part2 = " -d chat_id="
    comando_part3 = " -d text=\""
    comando_part4 = "\"  > /dev/null"
    comando = comando_part0 + comando_part1 + URL + comando_part2 + ID + comando_part3 + Mensaje + comando_part4
    #print(comando)
    os.system(comando)
    return


#em = envio_mensaje(TOKEN, ID, Mensaje)