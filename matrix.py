import time
import sys


def digitar(texto, delay=0.03):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def pausa(segundos=2):
    time.sleep(segundos)


def apresentacao():
    """Introdução e coleta do nome do jogador."""
    print("\n" + "=" * 50)
    digitar("        BEM VINDO À MATRIX", delay=0.05)
    print("=" * 50 + "\n")
    pausa(1)

    while True:
        nome = input("Qual o seu nome? ").strip()
        if nome:
            return nome
        print("Por favor, insira um nome válido.\n")


def conversa_morpheus(nome):
    """Primeira conversa com Morpheus sobre a realidade."""
    pausa(1)
    digitar(f"\nMe chamo Morpheus, e tenho uma escolha pra você, {nome}.")
    pausa(2)
    digitar("Você realmente acha que vive em um mundo real?")
    pausa(1)

    while True:
        escolha = input("\n(s) Sim / (n) Não: ").lower().strip()

        if escolha == "s":
            digitar("\nTenho uma notícia ruim pra você...")
            pausa(1)
            digitar("Você nunca vai descobrir a verdade. Fim de jogo.")
            sys.exit()

        elif escolha == "n":
            digitar("\nBoa escolha. Venha comigo e eu vou te mostrar até onde vai a toca do coelho.")
            pausa(2)
            break

        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def escolha_pilula(nome):
    """Cena clássica da escolha das pílulas."""
    pausa(1)
    print()
    digitar(
        f"Tenho duas pílulas, {nome}.\n\n"
        "  [AZUL]     → Fim da história. Você acorda na sua cama\n"
        "               e acredita no que quiser acreditar.\n\n"
        "  [VERMELHA] → Eu te mostro até onde vai a toca do coelho.\n"
    )

    while True:
        pilula = input("Escolha sua pílula (azul/vermelha): ").lower().strip()

        if pilula == "azul":
            pausa(1)
            digitar("\nVocê tomou a pílula azul...")
            pausa(2)
            digitar("Você continuou na Matrix. Fim de jogo.")
            sys.exit()

        elif pilula == "vermelha":
            pausa(1)
            digitar("\nVocê tomou a pílula vermelha...")
            pausa(2)
            digitar("Bem-vindo ao mundo real.")
            pausa(2)
            break

        else:
            print(f"Escolha inválida, {nome}. Digite 'azul' ou 'vermelha'.")


def fuga(nome):
    """Sequência de fuga com sistema de força e saúde."""
    pausa(1)
    print()
    digitar("Agora que você já sabe a verdade, temos que fugir daqui!")
    pausa(2)

    forca = 4
    saude = 5
    agente_apareceu = False

    while forca > 0 and saude > 0:
        print(f"\n{'─' * 30}")
        print(f"  Força: {'█' * forca}{'░' * (4 - forca)}  ({forca}/4)")
        print(f"  Saúde: {'█' * saude}{'░' * (5 - saude)}  ({saude}/5)")
        print(f"{'─' * 30}")

        acao = input("\nO que você faz? (correr/lutar): ").lower().strip()

        if acao == "correr":
            forca -= 1
            digitar("Você correu desesperadamente pelos corredores...")

        elif acao == "lutar":
            saude -= 1
            digitar("Você enfrentou um agente e saiu machucado...")
            pausa(1)

        else:
            print("Ação inválida. Escolha 'correr' ou 'lutar'.")
            continue

        if not agente_apareceu:
            pausa(1)
            digitar(f"\nAgente Smith: Senhor {nome}... você pertence a este sistema.")
            agente_apareceu = True

        if forca <= 2 or saude <= 2:
            pausa(1)
            digitar(f"\nMorpheus: Melhor sairmos daqui, {nome}! Agora!")
            break

    if forca == 0 or saude == 0:
        digitar("\nVocê não teve forças para escapar. Os agentes te capturaram.")
        digitar("Fim de jogo.")
        sys.exit()


def descoberta_escolhido(nome):
    """Morpheus revela que o jogador pode ser o Escolhido."""
    pausa(3)
    print()
    digitar(f"Morpheus: Você lutou bem, {nome}...")
    pausa(2)
    digitar("Morpheus: Acho que você é o Escolhido.")
    pausa(2)
    digitar("Morpheus: Mas antes precisamos confirmar com o Oráculo...")
    pausa(2)


def visita_oraculo(nome):
    """Segunda missão — encontro com o Oráculo."""
    print()
    continuar = input("Você quer continuar sua jornada? (s/n): ").lower().strip()

    if continuar != "s":
        digitar("\nVocê decidiu não continuar. Talvez em outro momento...")
        sys.exit()

    pausa(2)
    digitar(
        "\nMorpheus: Durante toda a sua vida você procurou respostas.\n"
        "Hoje, talvez encontre perguntas ainda maiores.\n"
        "O Oráculo não está aqui para lhe mostrar um destino pronto,\n"
        "mas para revelar aquilo que você ainda não consegue enxergar em si mesmo."
    )
    pausa(3)
    print()
    digitar("Você entra em uma casa antiga junto a Morpheus...")
    pausa(2)
    digitar("Uma mulher misteriosa já está te esperando.")
    pausa(2)
    digitar(f"Oráculo: Então você é o {nome}.")
    pausa(2)

    input("\nVocê acena com a cabeça. [Pressione ENTER para continuar] ")

    pausa(1)
    digitar(f"\nOráculo: Você sabe quem você é, {nome}?")
    pausa(2)
    digitar("Oráculo: Você merece entender tudo isso...")
    pausa(2)
    digitar(
        "\nOráculo: A humanidade criou as máquinas, mas elas evoluíram além do controle.\n"
        "Agora, os humanos vivem presos em uma simulação chamada Matrix,\n"
        "enquanto seus corpos são usados como fonte de energia."
    )
    pausa(3)
    print()
    digitar(f"Você: Sem volta, como vamos sair dessa distopia?")
    pausa(2)
    print()
    digitar(
        f"Oráculo: Temos uma última esperança, e essa esperança é você, {nome}.\n"
        "Você é o Escolhido. Vai guiar a humanidade para a luz novamente."
    )
    pausa(3)
    print()
    print("=" * 50)
    digitar("         FIM DO CAPÍTULO 1", delay=0.05)
    print("=" * 50 + "\n")


def main():
    nome = apresentacao()
    conversa_morpheus(nome)
    escolha_pilula(nome)
    fuga(nome)
    descoberta_escolhido(nome)
    visita_oraculo(nome)


if __name__ == "__main__":
    main()
