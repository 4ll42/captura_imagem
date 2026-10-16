import cv2
def capturar_e_salvar():
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("erro: Não foi possível acessar a webcam.")
        return
    print("[ESPAÇO] Captura e salvar foto")
    print("[ESC] sair")

    #configuração da fonte de texto
    fonte = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    escala = 0.6
    cor_texto = (255, 255, 255)
    espessura = 1

    while True:
        status, frame = webcam.read()
        if not status:
            print("falha ao receber frame do webcam")
            break

        frame_limpo = frame.copy()
        cv2.rectangle(frame, (10, 10), (320, 75), (0, 0, 0), -1)
        cv2.putText(frame, "[ESPAÇO] salvar foto", (20,35), fonte, escala, cor_texto, espessura )
        cv2.putText(frame, "[ESC]sair", (20, 60), fonte, escala, cor_texto, espessura)
         
        cv2.imshow("capturanda Webcam local", frame)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == 32:
            cv2.imwrite("foto.jpg", frame_limpo)
            print("Foto salva: foto.jpg")
            foto_cinza = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2GRAY)
            cv2.imwrite("foto_cinza.jpg", foto_cinza)
            foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
            cv2.imwrite("foto_invertida.jpg", foto_invertida)
        elif tecla == 27:
            print("Encerrando camera...")
            break
    webcam.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    capturar_e_salvar()