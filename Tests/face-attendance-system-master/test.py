# Arquivo temporário para resolver dependência ausente
# Este é um mock da função test para anti-spoofing
# Por enquanto sempre retorna 1 (pessoa real)

def test(image, model_dir, device_id):
    """
    Função temporária que simula detecção anti-spoofing
    Sempre retorna 1 (pessoa real) para permitir teste básico
    
    Args:
        image: imagem capturada da webcam
        model_dir: diretório dos modelos (não usado neste mock)
        device_id: ID do dispositivo (não usado neste mock)
    
    Returns:
        1: pessoa real (sempre por enquanto)
        0: seria spoof/fake
    """
    print("⚠️  Usando detecção anti-spoofing simulada - sempre aprovando como pessoa real")
    return 1