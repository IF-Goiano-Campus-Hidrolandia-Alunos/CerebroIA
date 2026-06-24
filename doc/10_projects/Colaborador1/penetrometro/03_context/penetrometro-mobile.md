---
tags: [penetrometro, mobile, flutter, riverpod, drift, clean-architecture]
updated: 2026-06-13
---

## Definição

App Android (Flutter) que migra o desktop Penetrometer Project, offline-first, integrado ao Google Drive, pronto para Play Store. Local: C:\Users\thyag\OneDrive\Desktop\penetrometreMobile (app/ = projeto Flutter, docs/ = entregaveis).

## Stack

- Flutter 3.27+ / Dart 3.6+, Riverpod (estado/DI), go_router.
- Drift (SQLite) + SQLCipher (cripto em F7), path_provider.
- Google Drive: googleapis + google_sign_in (F6).
- pdf/printing, excel, csv, archive (relatorios F4). fl_chart (graficos F5).
- geolocator, connectivity_plus, workmanager, flutter_secure_storage.

## Arquitetura

- Clean Architecture por feature: presentation -> application -> domain <- data.
- domain puro Dart (calculadoras, entidades, contratos). Repository Pattern + DI Riverpod.
- Banco: tabelas Measurements, Projects, AuditLogs (Drift). Soft-delete + version + syncStatus para sync.

## Plano por fases

- F0 fundacao (feito). F1 dominio cientifico + testes (feito). F2 persistencia Drift + entidade Projeto (feito).
- F3 GPS/UI, F4 relatorios, F5 graficos, F6 Drive, F7 seguranca, F8 testes, F9 Play Store (concluidos).

## Build

- Flutter SDK nao instalado na maquina de geracao; cliente builda no Android Studio.
- Passos: flutter create . --platforms=android --org br.edu.ifgoiano; flutter pub get; dart run build_runner build; dart run flutter_launcher_icons; flutter run.
- Icone do cliente em app/assets/icon/app_icon.png.

## Bloqueios externos

- Credenciais OAuth Google (F6), keystore de release (F9).

## Links

- [[10_projects/Colaborador1/penetrometro/03_context/penetrometro-desktop-dominio]]
