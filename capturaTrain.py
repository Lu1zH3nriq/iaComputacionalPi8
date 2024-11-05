import os
import subprocess

def verificar_torch_distributed():
    try:
        import torch.distributed as dist
        print("torch.distributed importado com sucesso!")
    except ImportError:
        print("Erro ao importar torch.distributed")
        raise

def treinar_modelo():
    # Verifica se o módulo torch.distributed está disponível
    verificar_torch_distributed()

    # Caminho para os dados de treinamento
    data_path = '_data'

    # Comando para treinar o modelo
    comando = [
        'python', 'train.py',
        '--img', '640',
        '--batch', '16',
        '--epochs', '10',
        '--data', 'C:/Users/luiz.mendes/Desktop/ia computacional/yolov5/data/custom_data.yaml',  # Ajuste conforme necessário
        '--weights', 'yolov5s.pt',
        '--name', 'custom_model'
    ]

    # Executa o comando de treinamento
    subprocess.run(comando, check=True)

if __name__ == "__main__":
    treinar_modelo()
