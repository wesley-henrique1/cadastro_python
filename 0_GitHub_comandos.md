
#### configura projetos 

git = 
    O git no início é o comando principal, a "porta de entrada" para todas as operações do Git.
    Ele funciona como um "executável" que você chama, e os comandos que vêm depois (como init, add, commit, push, etc.) são as instruções que você dá a ele.


git init = 
    Este comando cria um novo repositório local do Git no diretório em que você está. Ele inicializa o controle de versão para o seu projeto, criando uma pasta oculta chamada .git. É nessa pasta que o Git armazena todo o histórico de alterações do seu projeto.

git branch = 
    Este comando é usado para gerenciar branches no seu repositório local. Uma branch é como um "caminho" separado para desenvolver novas funcionalidades ou corrigir bugs sem alterar a branch principal do projeto.
    Quando usado sem argumentos, ele lista todas as branches existentes e mostra qual delas é a atual (com um asterisco *).

    Quando usado com um nome, ele cria uma nova branch que aponta para o mesmo commit da sua branch atual.
    " git branch <nome_do_branch> "

    git branch -m <novo_nome> = 
        Este comando renomeia uma branch localmente. A flag -m serve para mover ou renomear. É um comando rápido e fácil para ajustar o nome de uma branch antes de enviá-la para um repositório remoto.

    git branch -d <nome-da-branch-para-apagar> =
        Este comando apaga a branch localmente, mas com uma proteção. Ele só funcionará se a branch que você quer apagar já tiver sido mesclada (ou seja, se todos os commits dela já estiverem na branch principal).

    git branch -D <nome-da-branch-para-apagar> = 
        Este comando apaga a branch localmente, mesmo que ela não tenha sido mesclada. Ele ignora o aviso de segurança e é usado quando você tem certeza de que quer apagar a branch e todos os commits dela.

git config = 
    é a ferramenta principal no Git para visualizar, definir e modificar as configurações de como o Git opera, tanto no seu repositório atual quanto globalmente na sua máquina.

        git config <escopos> user.name "Seu Nome Completo": Seu nome, anexado a todos os seus commits.
        git config <escopos> user.email "seu.email@exemplo.com": Seu e-mail, usado para identificar sua autoria.
        OBS: Se ja estiver um usario cadastrado os comando ira subistituir o atual 

    O git config pode salvar as configurações em três escopos diferentes, afetando a prioridade e o alcance:

    Local: git config user.name ...	
        *Onde é Salvo*= no arquivo.git/config dentro do repositório.	
        *Alcance*= Apenas no repositório atual.
    
    Global:	git config --global user.name ...	
        *Onde é Salvo*= No seu diretório de usuário (ex: ~/.gitconfig).	
        *Alcance*= Todos os seus repositórios na sua máquina.
    
    Sistema	git config --system user.name ...	
        *Onde é Salvo*= Arquivos de configuração globais do sistema. 
        *Alcance*= Todos os usuários da máquina (menos comum).



git remote add <apelido>  <URL_do_repositório_remoto> = 
    Este comando cria uma "conexão" nomeada para um repositório remoto. Ele pega a URL do repositório remoto e a associa a um apelido (o nome que você quiser dar).

        remote: indica que você está trabalhando com repositórios externos.

        add: é a ação de adicionar uma nova conexão.

        origin: é o apelido mais comum e padrão para o repositório principal do projeto. É uma convenção.

        <URL_do_repositório_remoto>: é o endereço do seu repositório no GitHub, GitLab, etc.

    git remote -v = 
        Este comando lista todas as conexões remotas (apelidos) que foram configuradas no seu repositório local, mostrando também a URL de cada uma. O -v significa "verbose" (detalhado). Sem ele, o comando git remote listaria apenas o nome dos apelidos (ex: origin).
            

.gitignore = 
    É um arquivo de texto simples que lista arquivos e diretórios que o Git deve ignorar, ou seja, não rastrear. Isso é fundamental para evitar que arquivos desnecessários, como chaves de API, arquivos de cache, pastas de módulos (node_modules), arquivos de log ou executáveis, sejam adicionados ao seu repositório. 


#### FLUXO PROJETO 

git add <arquivo> = 
    Este comando adiciona um arquivo específico do seu diretório de trabalho para a área de preparação (também conhecida como staging area ou index). A área de preparação é um local intermediário onde o Git "prepara" as mudanças que você quer incluir no próximo commit.
    Sintaxes adicionais e úteis:
    git add . =
        Adiciona todos os arquivos do diretório atual e subdiretórios para a área de preparação. É muito útil quando você quer adicionar todas as suas alterações de uma vez.

    git add -A =
        Adiciona todos os arquivos modificados e excluídos em todo o repositório. É uma alternativa segura para adicionar todas as alterações.

    git add -u =
        Adiciona apenas os arquivos modificados e excluídos, ignorando os novos arquivos que ainda não foram rastreados.


git status = 
    Este comando exibe o estado do seu diretório de trabalho e da área de preparação (staging area). Ele te mostra quais arquivos foram modificados, quais estão prontos para o commit, quais foram excluídos e quais ainda não estão sendo rastreados pelo Git.
    Changes to be committed:
        Mostra os arquivos que você adicionou com git add e que estão prontos para serem salvos no próximo commit.

    Changes not staged for commit: 
        Mostra os arquivos que foram modificados, mas que você ainda não adicionou com git add.

    Untracked files: 
        Lista os arquivos que são novos no diretório e que o Git ainda não está rastreando.


git restore --staged <nome_do_arquivo> = 
    Este comando move um arquivo que já foi adicionado à área de preparação (staging area) de volta para o seu diretório de trabalho. Ele "desfaz" o efeito do git add em um arquivo específico, sem apagar nenhuma alteração.

    git restore --staged . = 
        Este comando remove todos os arquivos da área de preparação (staging area). Ele desfaz o efeito de um git add . completo, movendo todas as alterações de volta para o diretório de trabalho.


git commit -m "Sua mensagem de commit" = 
    Este é o comando que salva permanentemente as alterações que estão na área de preparação (staging area) no histórico do seu repositório local. Cada commit é como um ponto de salvamento ou uma "foto" do seu projeto em um momento específico. A flag -m permite que você adicione uma mensagem curta e descritiva diretamente no comando.

    A mensagem é a parte mais importante. Ela deve ser um resumo claro e conciso das alterações. Use o tempo verbal no imperativo ("Adiciona funcionalidade", "Corrige bug", "Atualiza documentação").

    Sintaxe alternativa:
        Se você usar apenas git commit, o Git abrirá um editor de texto (como VIM, Nano ou VS Code) para que você escreva uma mensagem de commit mais longa e detalhada. Isso é útil para commits mais complexos.


git revert <hash_do_commit> =
    Este comando cria um novo commit que desfaz as alterações de um commit anterior. Em vez de apagar o histórico, ele adiciona um novo "capítulo" que reverte o que foi feito.

    O git revert é a forma mais segura e recomendada de desfazer alterações que já foram enviadas para um repositório remoto, pois ele não apaga ou reescreve o histórico do projeto.

    git revert -m 1 HEAD =
        Este comando cria um novo commit que reverte as alterações do commit de merge mais recente. É a maneira mais segura e recomendada de desfazer um git pull que deu errado, especialmente em projetos colaborativos.

git push <repositório-remoto> <nome-da-branch> = 
    Este comando envia os commits do seu repositório local para o repositório remoto (geralmente, o GitHub). Ele é o responsável por "publicar" o seu trabalho, tornando-o visível para outras pessoas e salvando-o na nuvem.

    git push -u <repositório-remoto> <nome-da-branch> = 
        A flag -u (ou --set-upstream) é usada apenas na primeira vez que você envia uma nova branch para o repositório remoto. Ela cria um link de rastreamento entre a sua branch local e a branch remota. Após usá-la, você pode usar apenas git push sem argumentos, e o Git saberá para onde enviar as suas alterações.

git merge <nome-da-branch-que-voce-quer-mesclar> =
    Este comando integra o histórico e as alterações de uma branch em outra. Em termos simples, ele pega todo o trabalho que foi feito em uma branch separada (como nova-funcionalidade) e o adiciona à branch em que você está no momento (geralmente, a main).

    Importante: Para que o git merge funcione, você deve estar na branch de destino. Ou seja, se você quer mesclar a nova-funcionalidade na main, você precisa estar na main.

git pull <repositório-remoto> <nome-da-branch> =
    Este comando é uma combinação de duas ações:

    Ele baixa os commits mais recentes do repositório remoto (como um git fetch).

    Ele mescla esses commits na sua branch local atual (como um git merge).

    Em resumo, o git pull atualiza o seu repositório local com tudo o que há de novo no repositório remoto. É o comando que você usa para pegar as alterações de outros colaboradores.

#### movimentação 

git checkout <nome-da-branch> =
    Este é o uso mais comum. Ele te leva para a branch que você especificar, atualizando todos os arquivos no seu diretório de trabalho para refletir o estado daquela branch.

    git checkout -b <nome_da_nova_branch> = 
        Este é um comando combinado que executa duas ações de uma só vez:
        Ele cria uma nova branch com o nome que você especificou (assim como git branch).
        Ele muda imediatamente para essa nova branch (assim como git checkout).
        A flag -b significa "branch" e indica ao Git que a sua intenção é criar uma nova branch e começar a trabalhar nela.

    git checkout -- <nome-do-arquivo> = 
        Este comando reverte um arquivo para o seu último estado salvo. Ele apaga todas as alterações que você fez desde o último commit ou git add. O comando git restore é a alternativa moderna e recomendada para essa função.


git switch <nome-da-branch> = 
    Muda o seu diretório de trabalho para a branch especificada. É uma alternativa mais moderna e intuitiva ao git checkout quando você quer apenas alternar entre branches.


#### CORINGAS

git clone <URL_do_repositório_remoto> = 
    Este comando cria uma cópia exata e completa de um repositório Git, incluindo todos os arquivos, pastas, branches e todo o histórico de commits. A cópia é salva em uma nova pasta na sua máquina.

git log = 
     Este comando exibe uma lista de todos os commits já feitos no repositório. Cada entrada do log mostra informações essenciais, como:
        Hash do commit: O identificador único e irremovível do commit.
        Autor: O nome da pessoa que fez o commit.
        Data: Quando o commit foi feito.
        Mensagem: O texto descritivo que resume as alterações.
    O git log é essencial para entender a evolução do projeto, rastrear mudanças e encontrar o ponto de onde você precisa reverter algo.

    git log --oneline = 
        Mostra cada commit em uma única linha, facilitando a visualização rápida do histórico.

    git log --oneline --graph = 
        Adiciona uma visualização gráfica que mostra como as branches e os merges aconteceram.