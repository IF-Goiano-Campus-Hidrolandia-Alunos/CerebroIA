---
tags: [cheat-sheet, command-line, developer, nextjs, drizzle, tauri, vercel]
updated: 2026-06-21
---

## Definição

Guia de comandos rápidos e cheat sheet técnico para as tecnologias usadas nos projetos (Next.js, Drizzle ORM, Tauri, Vercel e ESP32). Evita pesquisas web externas redundantes e erros de sintaxe CLI.

---

## 1. Drizzle ORM & Neon (Banco de Dados)
Executar dentro do diretório do projeto web (`/web`):

- **Gerar migrations** baseadas em mudanças no `schema.ts`:
  ```bash
  npx drizzle-kit generate
  ```
- **Aplicar migrations** no Neon Postgres de produção/dev:
  ```bash
  npx drizzle-kit migrate
  ```
- **Fazer Push direto** das alterações do schema para o banco (para desenvolvimento rápido, sem gerar arquivos de migration):
  ```bash
  npx drizzle-kit push
  ```
- **Abrir Drizzle Studio** (interface gráfica local do banco de dados):
  ```bash
  npx drizzle-kit studio
  ```

---

## 2. Next.js & Node (Frontend/API)
Executar dentro do diretório `/web`:

- **Iniciar servidor de desenvolvimento local** (porta padrão 3000):
  ```bash
  npm run dev
  ```
- **Gerar build de produção** (valida tipos TypeScript e compila):
  ```bash
  npm run build
  ```
- **Iniciar servidor de produção local** (após rodar build):
  ```bash
  npm run start
  ```
- **Executar Linter** para validar código:
  ```bash
  npm run lint
  ```

---

## 3. Tauri 2 (Desktop App)
Executar dentro do diretório `/desktop`:

- **Iniciar ambiente de desenvolvimento local** (roda o Rust backend + React frontend):
  ```bash
  npm run tauri dev
  ```
- **Build de produção** (gera o instalador `.msi` ou executável standalone):
  ```bash
  npm run tauri build
  ```
- **Limpar cache do compilador Rust** (resolução de erros estranhos de compilação):
  ```bash
  cargo clean
  ```

---

## 4. Vercel CLI
Executar na raiz do projeto ou em `/web`:

- **Login no console Vercel**:
  ```bash
  npx vercel login
  ```
- **Iniciar deploy de teste (Development/Staging)**:
  ```bash
  npx vercel
  ```
- **Deploy de Produção**:
  ```bash
  npx vercel --prod
  ```
- **Puxar variáveis de ambiente da nuvem para o local** (`.env.local`):
  ```bash
  npx vercel env pull .env.local
  ```

---

## 5. ESP32 & Arduino CLI (Firmware)
Executar na pasta `/firmware`:

- **Compilar código da ESP32**:
  ```bash
  arduino-cli compile --fqbn esp32:esp32:esp32 esp32_plantium/
  ```
- **Gravar código na ESP32** (substituir `COM3` pela porta correta):
  ```bash
  arduino-cli upload -p COM3 --fqbn esp32:esp32:esp32 esp32_plantium/
  ```

---

## Links

- [[10_projects/Colaborador1/general/plataforma-web-arquitetura]]
- [[30_libraries/general/protocolo-esp32]]
- [[20_workflows/deploy-plataforma-web-vercel-neon]]
