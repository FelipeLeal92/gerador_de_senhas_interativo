🔐 Gerador de Senhas Interativo & GUI
Uma ferramenta em Python para criar senhas seguras de duas formas:
- CLI (linha de comando) – rápida e leve.
- GUI (interface gráfica) – intuitiva e rica em recursos.

📖 Descrição
Este projeto oferece geração de senhas robustas, com parâmetros de customização de comprimento e tipos de caracteres. Ele registra automaticamente cada senha gerada, permitindo consulta, edição de metadados (campo “local”) e cópia direta do histórico — tudo em uma única aplicação modular.

🚀 Funcionalidades
Comum (CLI + GUI)
- Comprimento personalizável (mínimo de 6 caracteres).
- Inclusão/exclusão de:
  - Letras maiúsculas
  - Letras minúsculas
  - Dígitos numéricos
  - Caracteres especiais
  - Geração de múltiplas senhas de uma vez.
  - Salvamento automático no histórico (.csv no GUI, .txt no CLI).
  - Tratamento robusto de erros e validação de entradas.
    
CLI
- Menu de texto interativo.
- Geração de “super-senhas” com critérios de alta complexidade.
- Saída em múltiplos formatos: terminal e arquivo .txt.
- Suporte a flags (ex.: --length, --count, --no-special).
  
GUI
- Interface moderna com Tkinter.
- Checkbox para tipos de caracteres.
- Árvore interativa (Treeview) para exibir histórico:
- Edição inline da coluna Local com duplo clique.
- Cópia de uma senha para o clipboard via clique direito.
- Tooltip suave de confirmação de cópia.
- Barra de status dinâmica.

🛠️ Tecnologias e Ferramentas
- Python 3.8+
- Tkinter (GUI nativa)
- Módulos internos (lib/funcoes.py)
- CSV e manipulação de arquivos
- Git & GitHub para versionamento

📦 Estrutura do Projeto
gerador_senhas/
├── LICENSE
├── README.md
├── main_gui.py               # Ponto de entrada da GUI
├── gerador_senhas_cli.py     # Ponto de entrada da CLI                                                 
├── gerador_gui/
│   ├── constantes.py         # Cores, dimensões e nomes de arquivos
│   ├── eventos.py            # Lógica de geração, cópia e leitura de histórico
│   ├── historico.py          # Toplevel do histórico com Treeview editável
│   └── interface_gui.py      # Montagem da janela e widgets Tkinter
├── gerador_cli/
│    └── interface_cli.py     # Menu e fluxo da versão CLI
├── lib/
│   ├── funcoes.py            # Geração de senha e gravação em arquivo
│   └── __init__.py           
└── requirements.txt          # Dependências

🚀 Como Executar
Pré-requisitos
- Python 3.8 ou superior instalado
- (Opcional) Crie um ambiente virtual:
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows
pip install -r requirements.txt

🖥️ Modo CLI
- Navegue até a pasta do projeto:
cd gerador_senhas
- Execute o script do CLI:
python gerador_senhas_cli.py
- Siga as instruções no terminal:
- Informe o comprimento desejado.
- Escolha tipos de caracteres.
- Opcional: número de senhas a gerar.
- Opcional: flags de configuração rápida.
🖱️ Modo GUI
- Certifique-se de ter o diretório lib/ com funcoes.py.
- No terminal:
python main_gui.py
- A interface aparecerá:
- Marque as opções de caracteres.
- Defina quantidade e comprimento.
- Clique em Gerar Senha.
- Utilize Copiar (GUI) ou clique direito (Histórico) para copiar.

📂 Exemplos de Uso
CLI
$ python interface_cli.py --length 12 --count 3 --no-special
Gerando 3 senhas de 12 caracteres (sem especiais)…
1) aB3dE4fG5hI2
2) JkL9mN8oP7qR
3) StU6vW5xY4zA
Senhas salvas em geradas.txt


GUI
Screenshot GUI
- Duplo clique na coluna Local para editar.
- Clique direito em qualquer linha para copiar a senha com tooltip confirmando.

📝 Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

🙋‍♂️ Autor
Felipe Leal
- GitHub: @FelipeLeal92
- Email: fmatheus1992@gmail.com
Sinta-se à vontade para abrir issues, enviar pull requests e sugerir melhorias!


Projeto em Python que permite a geração de senhas seguras de forma interativa via terminal. O usuário pode personalizar diversos aspectos da senha, como comprimento e tipos de caracteres, além de gerar múltiplas senhas simultaneamente e salvar as senhas geradas em um arquivo .txt.
---
Menu do gerador

![Captura de tela 2025-04-14 153155](https://github.com/user-attachments/assets/c6b206d4-2076-47be-8978-1744398b76b4)

---
🚀 Funcionalidades
- ✅ Geração de senhas seguras com opções personalizáveis:

  - Comprimento da senha (mínimo de 6 caracteres)

  - Inclusão de letras maiúsculas

  - Inclusão de letras minúsculas

  - Inclusão de dígitos numéricos

  - Inclusão de caracteres especiais

- 🔁 Geração de múltiplas senhas em uma única execução

- 🦾 Geração de "super-senhas" com critérios de alta complexidade

- 💾 Salvamento automático das senhas geradas em um arquivo senhas_geradas.txt

- 🧩 Arquitetura modular utilizando pacotes e módulos Python

- 🛡️ Tratamento de erros e validação de entradas do usuário

- 📂 Organização do código em estrutura de diretórios (lib/ para módulos auxiliares)
---
Mutiplas saídas

![Captura de tela 2025-04-14 153958](https://github.com/user-attachments/assets/46cbb688-c23f-421d-8ed1-bdd9fb8502fd)
---
Escrita em .txt

![Captura de tela 2025-04-14 154454](https://github.com/user-attachments/assets/bd523c02-9bb5-4743-b3ec-919bb7c5fe6f)


---
🛠️ Tecnologias e Ferramentas Utilizadas

- Python 3.x: Linguagem principal do projeto

- Módulos e Pacotes Python: Estruturação do código em módulos reutilizáveis

- Manipulação de Arquivos: Leitura e escrita de arquivos .txt para armazenamento das senhas

- Tratamento de Exceções: Garantia de robustez na interação com o usuário

- Git e GitHub: Controle de versão e hospedagem do código-fonte
---
📦 Estrutura do Projeto

![image](https://github.com/user-attachments/assets/9e293df3-9c4b-4929-8a45-45fe1693595c)
---
▶️ Como Executar

1. Certifique de ter o Python 3.x instalado em sua máquina.

2. Clone este repositório:
  git clone https://github.com/FelipeLeal92/gerador_de_senhas_interativo.git

3. Navegue até o diretório do projeto:
   cd gerador_de_senhas_interativo

4. Execute o script principal:
  python gerador_senhas.py
  
5. Siga as instruções no terminal para gerar suas senhas personalizadas.
---
📝 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

---
🙋‍♂️ Autor

Desenvolvido por Felipe Leal
