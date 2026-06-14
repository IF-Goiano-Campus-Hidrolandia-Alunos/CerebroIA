---
tags: [ignisengine, decisoes, arquitetura, adr]
updated: 2026-06-14
---

## Definição

Registro de decisões arquiteturais do IgnisEngine (evidenciadas no código/histórico).

## Decisões

- Java 17 LTS puro; dependência única org.json. Ver [[concepts/ignisengine-java-17]].
- Modelo de entidade por herança (GameObject abstrato) + scripts (IgnisScript), não ECS.
- Serialização JSON .ignis via loadProperties/saveProperties + @Serialize (reflexão).
- Render via java.awt.Canvas + BufferStrategy + Graphics2D (loop em thread própria).
- UI in-game própria (core/ui) desenhada em canvas, separada do Swing do editor.
- Builder com estratégias (BuildStrategy/BuildTarget): Java (JVM) e C++ (consoles).
- IA via AIServiceProvider (Gemini hoje; multi-provedor futuro).
- Marketplace: backend só URLs Git; Next.js+Neon na Vercel; auth GitHub OAuth; editor publica via token. Ver [[concepts/ignisengine-marketplace]].
- Branches: Legado = Swing estável + marketplace; main = migração JavaFX. Ver [[concepts/ignisengine-javafx-migracao]].
- Migração JavaFX: incremental com ponte de render (BufferedImage -> SwingFXUtils -> Canvas FX); big-bang rejeitado.
- Commits do projeto: usuário ThyagoToledo (exceto auditorias commitadas com o usuário do Vault, FeronZerbana, quando solicitado).

## Links

- [[concepts/ignisengine-roadmap-mestre]]
- [[concepts/ignisengine-auditoria-arquitetural]]
