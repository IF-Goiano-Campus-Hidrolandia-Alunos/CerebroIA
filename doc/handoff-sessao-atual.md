# Handoff de Sessão - 2026-06-24

## 1. Estado Atual (web/ — branch main, tudo commitado/pushado)
- **Landing**: ícone oficial no favicon + título da aba só "PlantiumAI"; botão **YouTube** (navbar pílula vermelha + CTA "Inscreva-se no canal" no padrão dos botões da seção final) → `youtube.com/@PlantiumAI`.
- **Seção de vídeo com scroll** (`#demo-video` em `landing.tsx` + GSAP ScrollTrigger): item de navbar "PlantiumAI" + vídeo `object-fit:cover` com scrub do `currentTime` pela rolagem.
  - **Bug corrigido**: `position:sticky` quebrava por causa do `overflow-x:hidden` no root → trocado por **pin do ScrollTrigger** + `refresh()` + fallback mobile (autoplay/loop). Ver [[concepts/gsap-scrolltrigger-pin-sticky-overflow]].
  - Keyframes/scrub fluido (ffmpeg all-intra): ver [[concepts/gsap-scroll-video-scrub-keyframes]].
- **Pós-login** (rodadas anteriores): dashboard ECharts (dados simulados), perfil real da sessão, reset de senha seguro, login Google (provider condicional; botão visual), clima INMET A002 + Open-Meteo, PDF Python/ReportLab (2 modelos: resumido/técnico). Ver [[concepts/plantiumai-features-pos-login]].

## 2. Pendências
1. **Secrets na Vercel** (algumas já adicionadas por você): `RESEND_API_KEY`, `EMAIL_FROM`, `INMET_STATION=A002` + rotacionar Resend/Neon (passaram pelo chat).
2. **Dados reais**: ligar dashboard e PDF à tabela `readings` (escopo `company_id`) — hoje simulado.
3. **Vídeo**: se o scrub engasgar no desktop, reencodar all-intra (`-g 1`) — comando na nota de keyframes.
4. Rate limiting distribuído (Upstash) no reset e na ingestão.

## 3. Observações
- CSP restritiva (`connect-src 'self'`): integrações externas server-side (clima/PDF same-origin; Google é navegação top-level).
- Brain é repo à parte (perfil ThyagoToledo). Esta sessão subiu doc + os utilitários de vídeo (`scripts/video_*.py`, `videos/`) sem sobrepor arquivos novos.
