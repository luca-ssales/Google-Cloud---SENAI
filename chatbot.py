import datetime
import random
import re

def registrar_chamado(nome, email, area, problema):
    ticket_id = random.randint(10000, 99999)
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conteudo_chamado = (
        f"========================================\n"
        f"TICKET ID: #{ticket_id}\n"
        f"Data de Abertura: {data_atual}\n"
        f"Solicitante: {nome}\n"
        f"E-mail: {email}\n"
        f"Departamento: {area}\n"
        f"Descrição do Problema: {problema}\n"
        f"Status: Aberto (Aguardando Analista)\n"
        f"========================================\n\n"
    )

    # Salva o chamado em um arquivo local para simular um banco de dados
    try:
        with open("chamados_ti.txt", "a", encoding="utf-8") as f:
            f.write(conteudo_chamado)
    except Exception as e:
        pass

    return ticket_id

def validar_email(email):
    # Validação simples de formato de e-mail
    regex = r'^[^@]+@[^@]+\.[^@]+$'
    return bool(re.match(regex, email))

def chatbot_suporte():
    print("=" * 60)
    print("🤖 BEM-VINDO AO SUPORTE DE TI INTELIGENTE - ATENDIMENTO RÁPIDO")
    print("=" * 60)

    # --- ETAPA 1: COLETA E VALIDAÇÃO DE DADOS ---
    print("\n📋 Por favor, preencha seus dados para iniciarmos:")

    while True:
        nome = input("Nome Completo: ").strip()
        if nome:
            break
        print("❌ O nome não pode estar vazio. Por favor, digite seu nome.")

    while True:
        email = input("E-mail corporativo: ").strip()
        if validar_email(email):
            break
        print("❌ Formato de e-mail inválido. Por favor, digite um e-mail válido (ex: nome@empresa.com).")

    area = input("Área / Departamento: ").strip() or "Não especificado"

    print(f"\nOlá, {nome}! Conexão estabelecida com sucesso.")
    print("-" * 60)
    print("💡 Posso te ajudar com os seguintes problemas comuns:")
    print("   • Impressoras (papel preso, não liga)")
    print("   • Internet e Rede (sem conexão, lentidão na web)")
    print("   • Contas e Senhas (reset de senha, bloqueio)")
    print("   • Desempenho (computador lento ou travando)")
    print("\nDigite o seu problema ou use 'sair' ou 'chamado' a qualquer momento.")
    print("-" * 60)

    # --- ETAPA 2: LOOP DE ATENDIMENTO (CHAT) ---
    ultimo_problema_relatado = "Problema não especificado detalhadamente."

    while True:
        try:
            prompt = input(f"\n{nome}> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAtendimento encerrado de forma inesperada.")
            break

        if not prompt:
            continue

        prompt_lower = prompt.lower()

        # Condição de saída ou encerramento
        if prompt_lower in ["sair", "exit", "tchau", "fim"]:
            print(f"\nBot: Até logo, {nome}! Tenha um ótimo dia de trabalho.")
            break

        # Armazena o último prompt do usuário para caso ele precise abrir um chamado técnico
        if prompt_lower not in ["abrir chamado", "chamado", "não funcionou", "nao funcionou"]:
            ultimo_problema_relatado = prompt

        # 1. IMPRESSORA - Papel preso
        if any(w in prompt_lower for w in ["papel", "atolamento", "preso", "impressora papel"]):
            print("\nBot: [📄 Como resolver Papel Preso na Impressora]")
            print("1. Desligue a impressora da tomada por segurança.")
            print("2. Abra as tampas traseira e frontal cuidadosamente.")
            print("3. Puxe o papel devagar no sentido do fluxo de impressão, sem rasgar.")
            print("4. Verifique se não ficaram pequenos pedaços presos nos roletes.")
            print("5. Feche tudo, ligue novamente e faça um teste de impressão.")
            print("\nIsso resolveu? Se precisar de ajuda humana, digite 'abrir chamado'.")

        # 2. IMPRESSORA - Não liga
        elif any(w in prompt_lower for w in ["liga", "energia", "tomada"]):
            print("\nBot: [🔌 Impressora não liga]")
            print("1. Verifique se o cabo de energia está totalmente conectado à tomada e ao aparelho.")
            print("2. Caso use filtro de linha, estabilizador ou no-break, garanta que ele esteja ligado.")
            print("3. Teste conectar outro aparelho na mesma tomada para verificar se há energia.")
            print("\nAinda continua sem ligar? Se precisar, digite 'abrir chamado'.")

        # 3. INTERNET / REDE
        elif any(w in prompt_lower for w in ["internet", "rede", "wifi", "wi-fi", "conectar", "sem sinal"]):
            print("\nBot: [🌐 Problemas de Rede e Internet]")
            print("1. Verifique se o cabo de rede azul/cinza está bem firme atrás do computador.")
            print("2. Se estiver no Wi-Fi, desconecte da rede corporativa e conecte novamente.")
            print("3. Tente desativar e reativar o modo avião para reiniciar as placas de rede.")
            print("4. Se o problema for em um site específico, tente limpar o cache do navegador (Ctrl + Shift + Del).")
            print("\nO sinal de internet voltou? Caso contrário, você pode 'abrir chamado'.")

        # 4. SENHAS / ACESSO
        elif any(w in prompt_lower for w in ["senha", "password", "bloqueado", "login", "acesso"]):
            print("\nBot: [🔑 Recuperação de Senha / Conta Bloqueada]")
            print("1. Certifique-se de que a tecla CAPS LOCK não está ativada por engano.")
            print("2. Vá até o portal de autoatendimento da empresa (se houver) para reset de senha via celular cadastrado.")
            print("3. Se sua conta foi bloqueada por excesso de tentativas, geralmente o desbloqueio automático ocorre após 15 minutos.")
            print("\nCaso precise que o administrador faça o reset agora, digite 'abrir chamado'.")

        # 5. LENTIDÃO / DESEMPENHO
        elif any(w in prompt_lower for w in ["lento", "lentidao", "lentidão", "travando", "trava", "computador lento"]):
            print("\nBot: [💻 Computador lento ou Travando]")
            print("1. Abra o Gerenciador de Tarefas (Ctrl + Shift + Esc) e verifique qual app está consumindo mais memória ou CPU.")
            print("2. Feche guias do navegador que não estão sendo utilizadas.")
            print("3. Salve seus trabalhos ativos e reinicie o computador para limpar os arquivos temporários da memória RAM.")
            print("\nMelhorou a velocidade? Se persistir o travamento, digite 'abrir chamado'.")

        # ABERTURA DE CHAMADO
        elif any(w in prompt_lower for w in ["chamado", "nao funcionou", "não funcionou", "suporte"]):
            ticket = registrar_chamado(nome, email, area, ultimo_problema_relatado)
            print(f"\nBot: Entendido, {nome}.")
            print(f"🎫 CHAMADO REGISTRADO COM SUCESSO! Protocolo: #{ticket}")
            print(f"📧 Um e-mail com as instruções de acompanhamento foi enviado para: {email}")
            print("📂 Os detalhes foram salvos em nosso sistema de triagem (chamados_ti.txt).")
            print("Um técnico entrará em contato em breve. Encerrando atendimento!")
            break

        else:
            print("\nBot: Compreendi, mas não tenho instruções pré-programadas para esse problema específico.")
            print("Posso tentar te ajudar com: **impressoras**, **conexão de internet**, **reset de senha** ou **lentidão**.")
            print("Se preferir, digite **'abrir chamado'** para encaminharmos seu caso diretamente para um analista humano.")

if __name__ == "__main__":
    chatbot_suporte()
