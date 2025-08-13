# Monitoramento Automático de Alterações no Projeto

Este projeto implementa um sistema para monitorar e versionar automaticamente mudanças em um repositório Git, evitando commits desnecessários causados por alterações irrelevantes como espaços ou linhas em branco.

---

## Objetivo

Evitar que o script acione commits automáticos para mudanças temporárias ou irrelevantes.
A detecção considera apenas modificações realmente relevantes no conteúdo do código ou arquivos do projeto.

---

## Abordagem Utilizada

Para evitar notificações por mudanças irrelevantes (como quebras de linha temporárias ou espaços removidos em seguida), a estratégia é detectar apenas alterações realmente novas comparando o estado do último commit com o estado atual.

1. Tirar um snapshot (hash) do repositório no início.
2. Monitorar mudanças usando:
   ```bash
   git diff HEAD --ignore-blank-lines --ignore-space-change
   ```
   - `--ignore-blank-lines`: ignora linhas em branco.
   - `--ignore-space-change`: ignora diferenças de espaços e indentação.
3. Quando detectar diferença relevante:
   - Executar `git add .`
   - Executar `git commit -m "mensagem"`
   - Executar `git push`
4. Atualizar o snapshot para o commit mais recente e continuar monitorando.

Observação: é possível adicionar etapas extras (build, testes, linting) conforme a complexidade do projeto.

---

## Critérios de Alterações Relevantes

- Inclusas: mudanças que afetam o conteúdo real do código ou arquivos rastreados.
- Ignoradas: ajustes de indentação, linhas em branco ou espaços extras.

---

## Quantidade Mínima de Impacto

- Commit automático somente se o número de linhas modificadas (adições + remoções) for maior que 5.
- Esse limite pode ser ajustado conforme a necessidade (por exemplo, exigir no mínimo 10 linhas modificadas).
- Também é possível ajustar o intervalo entre verificações para controlar a frequência de acionamento.

---

## Diferença entre Abordagens

- Snapshot: varre todos os arquivos no diretório, detectando qualquer modificação, mesmo fora do controle do Git.
- `git diff`: considera apenas arquivos rastreados no repositório e ignora mudanças irrelevantes como espaços ou linhas em branco.

---

## Como Usar

Guia rápido para instalar e executar o script a partir de qualquer lugar no terminal.

### 1. Colocar o Script no Local Correto
Escolha um diretório para guardar seus scripts pessoais:
```bash
mkdir -p ~/scripts
mv monitor_repo.py ~/scripts/
```

### 2. Criar um Atalho Global (Link Simbólico)
Permite rodar o script como um comando simples:
```bash
ln -s ~/scripts/monitor_repo.py ~/.local/bin/monitor_repo
```

### 3. Garantir que o Diretório esteja no PATH
Edite o arquivo de configuração do shell (`.zshrc`):
```bash
nano ~/.zshrc
```
Adicione a linha:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### 4. Recarregar as Configurações
```bash
source ~/.zshrc
```

### 5. Testar no Terminal
```bash
monitor_repo
```

Dica: é possível renomear o comando no passo do link simbólico para algo mais curto, como `mon` ou `pushauto`.
