# Falhas

| data | o que quebrou | menor correção | prompt / infra |
|---|---|---|---|
| 2026-09-21 | CSS claro impedia fundo sépia e JS antigo ficava em cache no navegador | Reduzir seletor claro e versionar asset alterado | prompt |
| 2026-09-21 | Camada v2 descartava campos extras no export e não retomava entre páginas | Persistir extras, validar import e resolver tópico pelo manifesto; não gravar checkpoint em índices | infra |
| 2026-09-21 | Extração do anti-FOUC capturou menção a script em comentário do template | Extrair a tag real no início da linha e validar JS no navegador | prompt |
| 2026-09-21 | Painel de aparência usava hidden, incompatível com toggle data-open da camada v2 | Controlar visibilidade por data-open | prompt |
| 2026-09-21 | Slot textual do medidor não correspondia ao contrato da camada v2 | Usar data-inema-meter-frac | prompt |
