# Perfil de commits deste vault (compartilhado entre usuários)

Este vault é compartilhado por **mais de um usuário**. Cada PC define o seu próprio
perfil de autor para os commits — e esse perfil **não é versionado** (cada máquina
escolhe o seu).

## Perfis disponíveis

| Perfil | Nome do commit | E-mail |
|---|---|---|
| ThyagoToledo | `ThyagoToledo` | `thyago10a2007@gmail.com` |
| FeronZerbana | `FeronZerbana` | `ddrive221@gmail.com` |

## Como configurar (faça UMA vez ao baixar/clonar o vault)

Rode, na raiz do vault, o `.bat` correspondente ao **seu** perfil (duplo-clique ou no terminal):

- **ThyagoToledo** → `perfil-thyago.bat`
- **FeronZerbana** → `perfil-feron.bat`

Cada script:
1. Configura `git config user.name` e `user.email` **deste repositório** para o seu perfil (config local, que não vai para o repositório remoto);
2. Cria o arquivo **`IDENTIDADE-LOCAL.md`** na raiz, registrando quem é este PC.

## Antes de commitar (para o usuário ou para uma IA assistente)

1. **Leia o arquivo [`IDENTIDADE-LOCAL.md`](IDENTIDADE-LOCAL.md)** na raiz do vault para saber qual é o perfil deste PC.
2. Use exatamente o nome/e-mail indicados ali nos commits.
3. Se `IDENTIDADE-LOCAL.md` **não existir**, nenhum perfil foi definido neste PC ainda — rode o `.bat` do seu perfil primeiro e não commite até definir.

> `IDENTIDADE-LOCAL.md` está no `.gitignore`: ao baixar o vault ele **não vem junto**.
> Assim, ninguém herda o perfil de outra pessoa por engano — cada PC define o seu.
