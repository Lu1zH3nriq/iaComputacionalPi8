import cv2
import torch

def detectar_pessoa():
    # Carrega o modelo treinado
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/custom_model/weights/best.pt')

    # Captura da webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Faz a detecção
        results = model(frame)

        # Renderiza os resultados na imagem
        results.render()

        # Mostra a imagem com as detecções
        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_pessoa()