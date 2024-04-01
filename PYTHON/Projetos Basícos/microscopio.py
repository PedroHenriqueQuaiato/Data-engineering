import cv2
import mediapipe as mp

def detect_hand_landmarks(frame):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        return results.multi_hand_landmarks[0]
    return None

def is_hand_open(hand_landmarks):
    if hand_landmarks is not None:
        fingers_up = [False] * 5
        for idx, landmark in enumerate(hand_landmarks.landmark):
            if idx in [4, 8, 12, 16, 20]:
                if landmark.y < hand_landmarks.landmark[idx - 2].y:
                    fingers_up[idx // 4] = True
        return sum(fingers_up) >= 3
    return False

def main():
    # Inicialize a câmera
    cap = cv2.VideoCapture(0)
    
    # Verifique se a câmera foi inicializada corretamente
    if not cap.isOpened():
        print("Erro ao acessar a câmera")
        return
    
    camera_on = False
    
    while True:
        # Capture um quadro da câmera
        ret, frame = cap.read()
        
        if ret:
            # Detecta landmarks da mão
            hand_landmarks = detect_hand_landmarks(frame)
            
            if hand_landmarks is not None:
                
                if is_hand_open(hand_landmarks):
                    camera_on = True
                    print("Câmera ligada")
                else:
                    camera_on = False
                    print("Câmera desligada")
            
            # Se a câmera estiver ligada, exibe o quadro capturado
            if camera_on:
                cv2.imshow("Microscópio Digital", frame)
            
            # Aguarde por uma tecla para sair
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Erro ao capturar quadro")
            break
    
    # Libere os recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
