# Painel de Custos e Aderência de Programas Governamentais

Painel analítico que integra **planejamento (PPA)**, **orçamento (LOA)** e **execução orçamentária**, com o desenho de duas análises por inteligência artificial:

1. **Custo do programa** — meta física confrontada com quantidade liquidada; meta financeira confrontada com valor liquidado
2. **Aderência contratual** — objeto contratado confrontado com o produto da ação e o objetivo do programa

Caso em uso: **Campo Grande — MS**, exercício de 2026, com o programa 19 (Rumo à Excelência: Campo Grande, Referência Nacional em Educação) como piloto.

---

## O que abrir primeiro

| Arquivo | O que é |
|---|---|
| `painel-campo-grande-2026.html` | Painel com os dados reais já embutidos. Abre no navegador, sem instalação |
| `painel-municipio.html` | Mesmo painel, vazio, para receber outro município via JSON |
| `mapa-do-fluxo.html` | Detalhamento das 11 etapas do fluxo: origem, campos, regras e exceções |
| `painel-ppa-execucao-contratos.html` | Protótipo genérico, com dados fictícios, anterior ao caso real |

Os arquivos são autocontidos: um único HTML cada, sem dependências além das fontes carregadas via Google Fonts.

---

## Fontes dos dados de Campo Grande

- **PPA 2026-2029** — remessa do Esfinge (TCE/MS) e texto publicado no DIOGRANDE n. 8.175, de 30/12/2025
- **LOA 2026** — DIOGRANDE n. 8.175, suplemento II, anexo *Vinculação das Ações e Unidades Orçamentárias aos Programas, Objetivos e Iniciativas do PPA*
- **Execução 2026** — empenho, liquidação e pagamento por ação, conforme remessa
- **LDO** — não carregada; o painel exibe a lacuna em vez de omiti-la

O PDF da LOA é digitalizado, sem camada de texto. Os valores das cinco ações foram localizados por reconhecimento óptico e conferidos um a um na imagem original.

---

## O que o painel mostra

**Conciliação.** PPA e LOA fecham em 100% no programa 19: as cinco ações têm o mesmo par de códigos e o mesmo valor nas duas leis, somando R$ 1.573.491.000 em 2026.

**Execução desigual entre ações.** As de manutenção rodam perto de 55% de liquidação; as de expansão estão praticamente paradas — a ação 1002 tem R$ 6,5 milhões empenhados e R$ 145 mil liquidados.

**Lei × remessa.** As 5 ações declaram **24 metas concretas** na lei do PPA — concluir obras de EMEIs por região urbana, ampliar 25 escolas, construir 10 novas — e todas chegam ao controle externo com meta física registrada como *"Porcentagem, 25% ao ano"*. A quantidade existe; a unidade não permite medir entrega.

**Régua incompleta para a fase de contratos.** Nos 55 programas, finalidade e público-alvo não foram declarados, e 38 objetivos terminam em exatos 255 caracteres — indício de truncamento na remessa.

---

## A fase de contratos

Ainda sem dados, mas com o desenho pronto. Três decisões estruturam essa etapa:

**Três perguntas em separado**, porque misturá-las leva o painel a afirmar o que não pode sustentar:
enquadramento (o contrato está na dotação certa — formal), aderência (o objeto serve à finalidade — interpretativa) e contribuição (a entrega fez avançar a meta — depende de dado ainda inexistente).

**A ponte em duas pernas.** O objeto contratado é meio; o objetivo do programa é fim. Comparar os dois diretamente reprova contratos legítimos. Quem faz a ligação é o produto da ação — e a pergunta "o produto serve ao objetivo?" se responde uma vez por ação, valendo para todos os contratos dela.

**Camada determinística antes da IA.** Oito verificações explicáveis em uma linha, que filtram volume e servem de controle: vínculo declarado, ação existe no PPA, ação com dotação, valor dentro da dotação, natureza compatível com o tipo da ação, objeto descrito, fornecedor identificado, vigência informada.

A classificação por **item**, e não por contrato, é o que torna a saída acionável: "R$ 3,1 mi aderentes e R$ 1,1 mi a reclassificar" decide algo; "parcialmente aderente" no contrato inteiro, não.

---

## Estrutura

```
.
├── painel-campo-grande-2026.html    painel com dados embutidos
├── painel-municipio.html            modelo vazio, para outro município
├── mapa-do-fluxo.html               as 11 etapas do fluxo, detalhadas
├── painel-ppa-execucao-contratos.html   protótipo genérico
├── dados/
│   ├── dados-campo-grande.json      base de dados do painel
│   └── embutir.py                   embute o JSON no HTML
└── docs/
    ├── Proposta_Solucao_....docx    documento da solução
    ├── Apresentacao_Completa_....pptx   27 slides, seção por seção
    └── Apresentacao_Resumida.pptx   11 slides
```

### Gerar o painel com dados atualizados

```bash
python3 dados/embutir.py painel-municipio.html dados/dados-campo-grande.json painel-campo-grande-2026.html
```

O modelo vazio também aceita carga direta: abra `painel-municipio.html`, clique em **Carregar dados (JSON)** e use **Baixar modelo** para ver o formato esperado.

---

## Estado do projeto

Protótipo navegável, não sistema em produção. Não há backend, banco de dados nem integração automática com sistemas de origem, e a análise de aderência ainda não está conectada — a seção mostra o desenho e um parecer de demonstração.

Princípio que atravessa o painel: **lacuna aparece como lacuna**. Campo ausente nunca vira zero, e nenhum valor é estimado. Quando o dado não permite responder, o painel diz que não permite.

## Próximos passos

- [ ] LDO 2026: anexos de metas fiscais e de prioridades
- [ ] Quantidade nas liquidações, para apurar custo por unidade entregue
- [ ] Detalhamento das ações dos 53 programas restantes
- [ ] Contratos, para ligar a fase de aderência
- [ ] Revisão do PPA: finalidade, público-alvo e unidade de medida das metas
