# Análise Crítica do Formulário de Solicitação de Direitos — Casas Bahia (Securiti/PrivacyCentral)

**URL analisada:** `https://privacy-central.securiti.ai/#/dsr/c2729d94-118b-4567-b93b-29c57fd9b2ff`

---

## 1. Encontrabilidade do Canal

**Problemas identificados:**

- O formulário está hospedado em um **domínio de terceiro** (`privacy-central.securiti.ai`), não no domínio principal da Casas Bahia (`casasbahia.com.br`). Isso dificulta que um usuário comum o encontre via busca orgânica ou navegação intuitiva no site.
- A URL utiliza um **UUID** (`c2729d94-118b-4567-b93b-29c57fd9b2ff`), o que torna impossível lembrar, compartilhar oralmente ou digitar manualmente.
- Não há evidência de que o canal esteja visível na página inicial, no rodapé ou em seção de fácil acesso do site principal. O usuário depende de saber que o canal existe previamente.

**Dispositivos LGPD relevantes:** Art. 18 (direitos do titular devem ser exercidos mediante requerimento ao controlador) e Art. 41, §1º (o encarregado deve ter identidade e contato divulgados **publicamente, de forma clara e objetiva**).

---

## 2. Clareza e Linguagem (Heurística de Nielsen: Correspondência entre o sistema e o mundo real)

**Problemas identificados:**

- O texto de abertura mistura **explicação legal** com **instrução prática** em um único bloco. Exemplo: *"Este documento é utilizado para possibilitar as requisições previstas na Lei nº: 13.709/2018 - Lei Geral de Proteção de Dados (LGPD)"* — o usuário comum não sabe o que é a Lei 13.709/2018.
- O trecho sobre base legal e retenção de dados para auditoria pela ANPD é **denso e jurídico**: *"A base legal para o presente tratamento refere-se ao cumprimento de obrigação legal, tendo em vista a necessidade de estabelecimento de meios de contato entre o titular e o controlador..."* — isso é linguagem de advogado, não de interface.
- Não há separação visual entre "o que você precisa saber" e "o que você precisa fazer".

**Conclusão:** Alta carga cognitiva. O formulário falha na heurística de **falar a linguagem do usuário**.

---

## 3. Visibilidade do Status do Sistema (Heurística de Nielsen)

**Problemas identificados:**

- A única informação sobre o andamento é: *"O prazo para processamento da requisição é de até 15 dias"*.
- **Não há:**
  - Indicação de etapas do processo (ex: "Recebido → Em análise → Concluído").
  - Canal ou link para acompanhamento posterior.
  - Número de protocolo mencionado.
- O usuário envia a solicitação e fica "no escuro" — sem saber se foi recebida, se está em análise, ou se será respondida.

**Dispositivo LGPD relevante:** Art. 19 — a confirmação de existência ou o acesso a dados devem ser providenciados em até 15 dias, mas o titular precisa ter meios de acompanhar.

---

## 4. Feedback do Sistema (Heurística de Nielsen)

**Problemas identificados:**

- O formulário menciona que *"encaminharemos uma mensagem no e-mail informado para confirmar a sua solicitação"*, mas:
  - Não há indicação de **confirmação visual imediata** após o envio (ex: tela de sucesso, número de protocolo).
  - A confirmação depende exclusivamente de um e-mail — se cair em spam ou não chegar, o usuário não tem como saber se a solicitação foi registrada.
- Não há feedback em tempo real nos campos (validação inline).

---

## 5. Consistência e Padronização (Heurística de Nielsen)

**Problemas identificados:**

- O campo de **Data de Nascimento** utiliza o formato `yyyy-MM-dd`, que é o padrão ISO, mas **completamente estranho ao usuário brasileiro**, habituado a `dd/MM/yyyy`. Isso induz erros de preenchimento.
- Mistura de campos com e sem máscara (CPF aparentemente sem formatação guiada, telefone sem indicação de formato esperado).
- O botão é "Enviar solicitação" — aceitável, mas não esclarece se há etapa de revisão antes.

---

## 6. Prevenção de Erros (Heurística de Nielsen)

**Problemas identificados:**

- **Não há orientação preventiva nos campos:**
  - CPF: sem máscara (XXX.XXX.XXX-XX), sem validação aparente em tempo real.
  - Telefone: sem indicação se deve incluir DDD, código do país, etc.
  - Data de nascimento: formato não intuitivo sem explicação auxiliar.
- **Não há tooltips, placeholders explicativos ou textos de ajuda** visíveis que orientem o preenchimento correto.
- O upload de documento com foto é obrigatório (`*`), mas não especifica formatos aceitos, tamanho máximo, ou o que fazer se o documento não tiver frente e verso em arquivo separado.

---

## 7. Controle e Liberdade do Usuário (Heurística de Nielsen)

**Problemas identificados:**

- **Não há tela de revisão** antes do envio. O usuário preenche tudo e clica "Enviar solicitação" sem poder conferir um resumo dos dados inseridos.
- Não há opção de **salvar rascunho** ou continuar depois.
- Não há menção sobre como **editar ou cancelar** uma solicitação já enviada.
- O CAPTCHA (hCaptcha) no final adiciona uma barreira e pode falhar, sem orientação de recuperação.

---

## 8. Eficiência e Esforço (Atrito do Formulário)

**Problemas identificados:**

- O formulário exige preenchimento de **múltiplos campos obrigatórios**: tipo de usuário, tipo de requisição, detalhes da solicitação, nome, sobrenome, data de nascimento, CPF, e-mail, telefone.
- **Além disso, exige upload de documento de identificação com foto (frente e verso)** — isso representa uma barreira significativa, especialmente para:
  - Usuários em dispositivos móveis.
  - Pessoas que não possuem scanner ou não sabem digitalizar documentos.
  - Idosos ou pessoas com baixa alfabetização digital.
- O esforço exigido é **desproporcional** para solicitações simples como "quero saber quais dados vocês têm sobre mim".

**Dispositivo LGPD relevante:** Art. 18, §5º — os direitos devem ser exercidos mediante requerimento ao controlador, mas o Art. 6º, X exige que o tratamento observe a **facilitação** do exercício de direitos pelo titular.

---

## 9. Transparência do Processo (LGPD)

**Problemas identificados:**

- O texto informa a base legal (cumprimento de obrigação legal) e menciona retenção para auditoria pela ANPD, mas:
  - **Não explica o fluxo prático**: quem vai analisar, quais áreas internas serão acionadas, como será a resposta.
  - **Não informa se haverá contato intermediário** ou se a resposta será apenas ao final dos 15 dias.
  - **Não esclarece o que acontece se a solicitação for negada** ou se forem necessários dados adicionais.
- A informação sobre retenção de dados para auditoria é vaga: *"seus dados poderão permanecer retidos"* — por quanto tempo? Com base em qual política?

**Dispositivos LGPD relevantes:** Art. 9º (direito de acesso facilitado às informações sobre o tratamento), Art. 6º, VI (princípio da transparência).

---

## 10. Conformidade Formal com a LGPD

| Requisito LGPD | Atendido? | Observação |
|---|---|---|
| Canal para exercício de direitos (Art. 18) | Parcialmente | Existe, mas com barreiras de acesso e usabilidade |
| Prazo de resposta (Art. 19) | Sim | Informa 15 dias |
| Identificação do encarregado (Art. 41) | Parcialmente | Menciona "encarregado" mas sem nome/contato direto visível no formulário |
| Facilitação do exercício de direitos (Art. 6º, X) | Não | Alto atrito, linguagem complexa, documento obrigatório |
| Transparência sobre o tratamento (Art. 9º) | Parcialmente | Informa base legal, mas omite fluxo e prazos de retenção |
| Confirmação de existência de tratamento (Art. 19, II) | Não verificável | Depende da resposta pós-envio |

---

## Conclusão: Dark Patterns ou Negligência?

Os elementos identificados **não configuram dark patterns intencionais clássicos** (como misdirection ou confirmshaming), mas apresentam um padrão de **friction by design negligente** — ou seja, o formulário cumpre a obrigação formal da LGPD de existir, mas impõe tantas barreiras práticas que **desestimula o exercício efetivo dos direitos do titular**. Isso pode ser resultado de:

- Uso de plataforma terceirizada (Securiti) sem customização para o público brasileiro.
- Falta de testes de usabilidade com usuários reais.
- Priorização do compliance formal ("o canal existe") sobre o compliance substancial ("o canal funciona para o titular").
