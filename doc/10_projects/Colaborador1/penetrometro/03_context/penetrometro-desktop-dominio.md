---
tags: [penetrometro, dominio, ifgoiano, javafx, solo]
updated: 2026-06-13
---

## Definição

Regras de negócio do sistema desktop Penetrometer Project (IF Goiano, JavaFX), base fiel para a migração mobile. Mede compactacao do solo via penetrometro de impacto e de pressao.

## Contexto

Engenharia reversa de github.com/Colaborador1/penetrometre. Vale o CODIGO, nao o README (3 divergencias abaixo).

## Calculos (fiel ao codigo)

- Impacto (Equacao de Stolf): R = 5.6 + 6.89 * N (kgf/cm2). Profundidade NAO entra na formula. N<=0 => 0.0.
- Pressao: coef = MPa * 10.1972. Profundidades padrao {5,10,15,20,40} cm.
- Quirk pressao: persiste impactsQuantity = (int)(MPa*100). Recuperar: MPa = impactsQuantity/100.

## Diagnostico (controllers, impacto e pressao)

- <10 adequado | <=20 moderada | <=30 alta | <=40 compactado | >40 extremamente compactado.

## Interpretacao no PDF (faixas por tipo)

- Impacto: <10 / <25 / <40 / else. Pressao: <5 / <15 / <30 / else.

## Modelo (tabela MEDICOES)

- id, impactsQuantity, deep, coefficient, FloorResistance(diagnostico), MeteringDate, SystemDate, SystemInfo, latitude, longitude, place, nameCollector, meteringType(IMPACT/PRESSURE).
- NAO existe CPF (apesar do README citar). Banco do snapshot vazio (sem dados legados).

## Divergencias README x codigo

- README diz R=(5.6+6.89N)/P; codigo nao divide por P.
- README tabela de diagnostico 0-2.5/2.5-5; codigo usa <10/<=20/<=30/<=40.
- README cita campo CPF; nao existe no codigo.

## Links

- [[10_projects/Colaborador1/penetrometro/03_context/penetrometro-mobile]]
