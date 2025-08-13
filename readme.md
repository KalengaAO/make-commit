Evitar que o script apita com qualquer mudança irrelevante (como uma quebra de linha temporária ou um espaço que logo será removido). Para isso, o truque foi detectar alterações realmente novas comparando o estado do último commit com o estado atual — só acionar quando houver diferença real no conteúdo.
Abordagem: Tirar um snapshot (hash) do repositório no início.
Monitorar mudanças usando git diff HEAD (com --ignore-blank-lines e --ignore-space-change para ignorar quebras de linha ou espaços).

    Quando detectar diferença relevante:

        Fazer git add .

        Fazer git commit -m "mensagem"

        Fazer git push

    Atualizar o snapshot para o commit mais recente e continuar monitorando.
    Poderias adiconar mais comando, mas deixo ao criteiro do usuário segundo a complexidade
    do projecto!
    
    Alterações relevantes – o script só considera mudanças que afetam o conteúdo real do código ou arquivos do projeto. Espaços extras, indentação ajustada ou linhas em branco não contam como alteração relevante.

	Quantidade mínima de impacto – o commit só é feito se o número total de linhas modificadas (adições + remoções) for maior que 5. Isso evita que pequenas edições, como correção de um caractere ou um comentário, disparem um commit automático.
    

