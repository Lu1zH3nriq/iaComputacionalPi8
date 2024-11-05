import cv2
import os

def capturar_imagem():
    # Cria a pasta _data/images/train se não existir
    if not os.path.exists('_data/images/train'):
        os.makedirs('_data/images/train')

    # Captura a imagem da webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if ret:
        # Salva a imagem na pasta _data/images/train
        image_path = '_data/images/train/captured_image.jpg'
        cv2.imwrite(image_path, frame)
        print(f"Imagem capturada e salva em {image_path}")

        # Gera o arquivo de anotação
        criar_anotacao(image_path, (100, 150, 300, 400))  # Substitua pelas coordenadas reais da caixa delimitadora
    else:
        print("Falha ao capturar a imagem")

    cap.release()
    cv2.destroyAllWindows()

def criar_anotacao(imagem_path, bbox, classe=0):
    # Extrai o nome do arquivo sem extensão
    nome_arquivo = os.path.splitext(os.path.basename(imagem_path))[0]
    anotacao_path = os.path.join(os.path.dirname(imagem_path), f"{nome_arquivo}.txt")

    # Dimensões da imagem
    img_width = 640  # Substitua pela largura real da imagem
    img_height = 480  # Substitua pela altura real da imagem

    # Coordenadas da caixa delimitadora
    x_min, y_min, x_max, y_max = bbox

    # Calcular o centro e as dimensões normalizadas
    x_center = (x_min + x_max) / 2 / img_width
    y_center = (y_min + y_max) / 2 / img_height
    width = (x_max - x_min) / img_width
    height = (y_max - y_min) / img_height

    # Escrever a anotação no arquivo
    with open(anotacao_path, 'w') as f:
        f.write(f"{classe} {x_center} {y_center} {width} {height}\n")

    print(f"Anotação criada e salva em {anotacao_path}")

if __name__ == "__main__":
    capturar_imagem()
