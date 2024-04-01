import cv2
import pyautogui
import mediapipe as mp

# Inicializar o módulo de rastreamento de mãos do mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inicializar a câmera
cap = cv2.VideoCapture(0)

# Inicializar variáveis para controle de estado
volume_on = True

while True:
    # Ler o quadro da câmera
    ret, frame = cap.read()

    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar mãos no frame
    results = hands.process(gray)

    # Verificar se as mãos foram detectadas
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Obter as coordenadas da ponta dos dedos
            thumb_tip = landmarks.landmark[4]
            index_tip = landmarks.landmark[8]

            thumb_tip_x, thumb_tip_y = int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])
            index_tip_x, index_tip_y = int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])

            # Calcular a distância entre a ponta do polegar e a ponta do indicador
            distance = ((thumb_tip_x - index_tip_x)**2 + (thumb_tip_y - index_tip_y)**2)**0.5

            # Definir uma distância de referência para ativar/desativar o som
            reference_distance = 100

            # Verificar se a distância ultrapassa a referência
            if distance > reference_distance:
                if volume_on:
                    pyautogui.press("volumeup")  # Aumentar o volume
                    volume_on = False
            else:
                if not volume_on:
                    pyautogui.press("volumemute")  # Mudo o volume
                    volume_on = True

    # Exibir o frame
    cv2.imshow("Hand Tracking", frame)

    # Sair do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
