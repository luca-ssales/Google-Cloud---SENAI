def chatbot_suporte():
  print("=" * 50)
  print("🤖 BEM-VINDO AO SUPORTE DE TI - ATENDIMENTO RÁPIDO")
  print("=" * 50)

  # --- ETAPA 1: COLETAGEM DE DADOS BÁSICOS ---
  print("\n📋 Por favor, preencha seus dados para iniciarmos:")
  nome = input("Nome Completo: ").strip()
  email = input("E-mail corporativo: ").strip()
  area = input("Área / Departamento: ").strip()

  print(f"\nObrigado, {nome} ({area})! Conexão estabelecida.")
  print("-" * 50)
  print(
      "Dica: Sou especializado em problemas simples como 'impressora não liga'"
      " ou 'papel preso'."
  )
  print(
      "Digite o seu problema ou escreva 'sair' / 'chamado' a qualquer momento."
  )
  print("-" * 50)

  # --- ETAPA 2: LOOP DE ATENDIMENTO (CHAT) ---
  while True:
    try:
      prompt = input(f"\n{nome}> ").strip()
    except (KeyboardInterrupt, EOFError):
      print("\nAtendimento encerrado.")
      break

    if not prompt:
      continue

    prompt_lower = prompt.lower()

    # Condição de saída ou encerramento
    if prompt_lower in ["sair", "exit", "tchau"]:
      print(f"\nBot: Até logo, {nome}! Fechando o atendimento.")
      break

    # Respostas baseadas em problemas comuns
    if (
        "papel" in prompt_lower
        or "atolamento" in prompt_lower
        or "preso" in prompt_lower
    ):
      print("\nBot: [📄 Como resolver Papel Preso na Impressora]")
      print("1. Desligue a impressora da tomada por segurança.")
      print("2. Abra as tampas traseira e frontal com cuidado.")
      print("3. Puxe o papel no sentido do fluxo de impressão, sem rasgar.")
      print("4. Verifique se restaram pedacinhos nos roletes.")
      print("5. Feche tudo, religue e faça um teste.")
      print("\nO problema foi resolvido? (Se não, digite 'abrir chamado')")

    elif "liga" in prompt_lower or "energia" in prompt_lower:
      print("\nBot: [🔌 Impressora não liga]")
      print(
          "1. Verifique se o cabo de energia está firme na tomada e na"
          " impressora."
      )
      print("2. Teste ligar em outra tomada ou troque o cabo, se possível.")
      print("3. Certifique-se de que o filtro de linha/estabilizador está ligado.")
      print("\nAinda continua sem sinal de energia?")

    elif "chamado" in prompt_lower or "nao funcionou" in prompt_lower or "não funcionou" in prompt_lower:
      print(
          f"\nBot: Entendi, {nome}. Como os passos básicos não resolveram,"
          f" registrei um chamado técnico para o e-mail: {email}."
      )
      print("Um analista entrará em contato em breve. Encerrando atendimento.")
      break

    else:
      print(
          "\nBot: Compreendi. No momento, consigo te ajudar com"
          " **impressoras** (não ligam ou papel preso). Se for o caso, detalhe"
          " melhor ou digite **'abrir chamado'** para falar com um humano."
      )


if __name__ == "__main__":
  chatbot_suporte()
