---
titulo: "A enchente de 2024 mudou o voto na Grande Porto Alegre?"
lede: "Cruzei 1.252 locais de votação com a mancha da enchente. Do 1º turno de 2022 para o de 2026, o voto andou para o PL quase igual dentro e fora da área alagada."
tipo: artigo
# Data da 1ª publicação, no LinkedIn. Texto de C:\dev\enchente-votos\rascunhos\artigo_linkedin.md, com o endereço novo do mapa
# e as correções de 06/11/2026 (registradas na nota do fim).
# Figuras em public/textos/enchente-e-voto/: mudanca-2022-2026 e tres-eleicoes vêm de scripts/12_figuras_artigo.py
# (fig3 e fig2); mapa-interativo é captura do mapa (docs/ servido localmente, #passo=4, 1440×709, painel recolhido e
# um clique de zoom); artigo_og.png sai de scripts/15_capa_linkedin.py --og.
data: 2026-10-20
imagem: /textos/enchente-e-voto/artigo_og.png
---

Em maio de 2024, a água cobriu bairros inteiros de Porto Alegre, Canoas, São Leopoldo, Eldorado do Sul e de outras cidades da região. No estado, a Defesa Civil contou [2,4 milhões de pessoas afetadas em 478 municípios](https://estado.rs.gov.br/defesa-civil-atualiza-balanco-das-enchentes-no-rs-24-4) e [185 mortes](https://defesacivil.rs.gov.br/defesa-civil-atualiza-lista-de-obitos-e-desaparecidos-decorrentes-da-inundacao-de-2024).

No dia 4 de outubro de 2026, no 1º turno, quem vota nesses bairros voltou às urnas para escolher presidente. Muita gente perguntou se a tragédia mudaria o voto, para um lado ou para o outro.

Eu queria saber algo mais concreto. Os locais de votação que ficaram embaixo d'água votaram diferente do resto da região?

Pelos dados do TSE, não. Do 1º turno de 2022 para o de 2026, a Grande Porto Alegre inteira andou cerca de 8 pontos na direção do PL, e a área alagada andou junto: 8,6 pontos dentro dela, 7,9 fora. A diferença entre as duas é menor que a margem de acaso. No caminho, montei um mapa interativo aberto, com cada local de votação nas três últimas eleições.

## O que eu fiz

Cruzei arquivos públicos de duas fontes. Do TSE, a votação por seção e o cadastro de locais de votação do 1º turno de 2018, 2022 e 2026. Da UFRGS, o mapa da área diretamente afetada pela enchente, feito principalmente com imagens de satélite de 6 e 8 de maio de 2024. O recorte tem 42 municípios, 1.252 locais de votação e 3 milhões de eleitores.

A primeira decisão foi o que conta como "alagado". O TSE diz onde a pessoa vota, não onde mora, então a unidade é o local de votação. E um local pode contar como alagado de três jeitos:

- o ponto do local cai dentro da mancha da enchente;
- o local fica a até 500 m da mancha;
- cada local pesa conforme a população atingida em volta dele, pelo Censo 2022.

Usei o primeiro como principal: são 153 locais, com 376 mil eleitores. Os outros dois servem para conferir se a conclusão depende dessa escolha. Também refiz a conta com outra mancha, a da Secretaria de Planejamento do governo do RS (SPGG), feita com imagens de 23 de maio de 2024.

A segunda decisão foi acompanhar as mesmas seções no tempo. Cada seção eleitoral é pareada pelo código (município, zona e número) e conta no local onde funcionou em 2026. Assim a conta não se perde quando uma escola deixa de ser local de votação. Na comparação de 2022 para 2026, as seções criadas em 2026, com 1% do eleitorado, entram só no voto de 2026. A que olha as três eleições usa só as seções que existem em todas, que somam 94% dos votos de 2026.

## O mapa

Em vez de publicar só um gráfico, montei uma página com todos os locais de votação da região. Ela está em [dalmolin.dev/enchente-votos](https://dalmolin.dev/enchente-votos/).

<figure>
  <a href="https://dalmolin.dev/enchente-votos/"><img src="/textos/enchente-e-voto/mapa-interativo.webp" width="1440" height="709" loading="lazy" decoding="async" alt="Mapa interativo da Grande Porto Alegre no passo 2026. Cada local de votação é um círculo, do vermelho (Lula à frente) ao azul (Flávio Bolsonaro à frente): vermelho no centro e no sul de Porto Alegre, azul em Canoas, Novo Hamburgo, Gravataí e no resto da região. A área alagada aparece em cinza, ao longo do Guaíba e dos rios. À direita, um cartão com o gráfico dentro × fora da área alagada."></a>
  <figcaption>Mapa interativo no passo 2026. Os locais com contorno escuro ficaram dentro da área alagada; o cartão à direita compara os dois grupos.</figcaption>
</figure>

O mapa avança numa linha do tempo de cinco passos: 2018, 2022, a enchente, 2026 e a mudança de 2022 para 2026. Dá para ligar a mancha da enchente, destacar os locais que ficaram dentro dela, ir direto a um município e, em Porto Alegre, ver a simulação do Guaíba a 5,30 m. Ao clicar num local, aparece o voto nas três eleições. Um cartão ao lado compara os locais dentro e fora da área alagada.

## O que os dados mostram

Para medir o voto, uso a vantagem do PT sobre o PL: a diferença entre os dois, em pontos percentuais dos votos válidos do 1º turno. Em 2022, Lula × Jair Bolsonaro; em 2026, Lula × Flávio Bolsonaro. Um número negativo quer dizer que o PL ficou à frente.

- **O voto andou quase igual dentro e fora da água.** Nos locais dentro da área alagada, a vantagem do PT foi de +1,9 em 2022 para −6,7 em 2026: caiu 8,6 pontos. Fora dela, foi de −2,0 para −9,9: caiu 7,9.
- **A diferença entre as duas mudanças cabe na margem de acaso.** Dentro da área alagada, o voto andou 0,8 ponto a mais para o PL. Refiz a conta 2.000 vezes, sorteando zonas eleitorais inteiras, e em 95% das vezes essa diferença ficou entre 2,3 pontos a mais para o PL e 1,5 a menos. O zero está dentro desse intervalo.
- **A conclusão não depende da definição de alagado.** Com 500 m de folga, com o peso da população atingida ou com a mancha do governo do RS, a diferença vai de 0,7 ponto a mais para o PL dentro da área alagada (com o peso da população) a 1,1 a menos (com a mancha do governo e 500 m de folga).
- **Cidade a cidade, não há padrão.** Em Canoas e São Leopoldo, os locais dentro da área alagada andaram cerca de 2 pontos a mais para o PL que os de fora. Em Porto Alegre e Guaíba, foi o contrário: os de dentro andaram menos para o PL, 0,8 e 2,3 pontos a menos que os de fora.

<figure>
  <a href="/textos/enchente-e-voto/mudanca-2022-2026.webp"><img src="/textos/enchente-e-voto/mudanca-2022-2026.webp" width="1456" height="1408" loading="lazy" decoding="async" alt="Mapa da Grande Porto Alegre com uma seta por local de votação. Quase todas são azuis e apontam para a direita, para o PL, dentro e fora da área alagada, que aparece hachurada. As poucas setas vermelhas, para o PT, se concentram no centro de Porto Alegre."></a>
  <figcaption>Cada seta é um local de votação e mostra para onde o voto andou de 2022 para 2026: em azul, para a direita, para o PL; em vermelho, para a esquerda, para o PT. O tamanho da seta mostra quanto: até 4 pontos, de 4 a 10, ou mais de 10. As setas fortes ficaram dentro da área alagada, hachurada; as apagadas, fora dela. Fontes: TSE; UFRGS; IBGE.</figcaption>
</figure>

As setas vermelhas ficam quase todas no centro de Porto Alegre. Dos 75 locais que andaram para o PT, 64 ficam na capital e 12 dentro da área alagada.

## Antes da água

Os locais dentro da área alagada votam um pouco mais no PT que os de fora. Olhando só 2026, daria para ler isso como efeito da enchente. Mas a distância já existia antes da água. Nas seções que existem nas três eleições, ela foi de 3,3 pontos em 2018, quando Fernando Haddad (PT) enfrentou Jair Bolsonaro, então no PSL, e de 3,7 em 2022. Em 2026, ficou em 2,9.

A mesma conta feita entre 2018 e 2022, quando ainda não havia enchente, também não separa os grupos. Os locais que depois alagariam andaram 0,5 ponto a mais para o PT que os outros, com intervalo de 95% entre 2,3 pontos a menos e 3,4 a mais. Os dois grupos andam juntos há três eleições.

<figure>
  <a href="/textos/enchente-e-voto/tres-eleicoes.webp"><img src="/textos/enchente-e-voto/tres-eleicoes.webp" width="1456" height="936" loading="lazy" decoding="async" alt="Gráfico de linhas da vantagem do PT sobre o PSL/PL em 2018, 2022 e 2026. A linha dos locais dentro da área alagada fica sempre um pouco acima da dos de fora: 3,3 pontos em 2018, 3,7 em 2022 e 2,9 em 2026. As duas sobem juntas de 2018 para 2022 e descem juntas de 2022 para 2026."></a>
  <figcaption>Vantagem do PT sobre o PSL/PL, em pontos percentuais dos votos válidos do 1º turno, nos locais dentro da área alagada (linha preta) e fora dela (tracejada), nas seções que existem nas três eleições. O fundo mostra quem venceu; embaixo, a distância entre as duas linhas. Fonte: TSE.</figcaption>
</figure>

## O que os dados não dizem

- **O efeito sobre cada pessoa.** A comparação é por local de votação. Quem se mudou depois da enchente vota em outro lugar e sai da conta. O número de eleitores nos locais dentro da área alagada caiu um pouco mais que nos de fora, mas o cadastro não diz por quê.
- **O peso da enchente na eleição como um todo.** A região inteira sentiu a tragédia, em preços, serviços e notícias. Uma comparação entre dentro e fora da área alagada não capta isso.
- **Onde a água chegou em cada rua.** As manchas não concordam entre si. Em Porto Alegre, a da UFRGS cobre 39% da Cidade Baixa e 41% do Menino Deus; a simulação do Guaíba a 5,30 m cobre 61% de cada um. Por isso conferi o resultado com 500 m de folga e com a mancha do governo.
- **O 2º turno e as outras eleições.** Olhei só o voto para presidente no 1º turno. O 2º turno, de 25 de outubro, e o voto para governador, prefeito ou deputado ficaram de fora.
- **A causa.** É uma comparação descritiva. Mostra onde o voto mudou diferente, não prova por quê.

Deixo esses limites por escrito para que quem discordar possa discutir com os números na mão.

## O que eu aprendi

- **Comparar mudanças, não níveis.** Candidatos e clima mudam de uma eleição para outra. O que diz alguma coisa é a distância entre os grupos antes e depois do evento.
- **Olhar para trás antes de apontar causa.** A distância de cerca de 3 pontos em 2026 parecia efeito da água, mas já estava lá em 2018.
- **Trocar a definição e ver se a conclusão fica de pé.** Se a resposta mudasse com 500 m a mais de mancha, ela não valeria muito.

O mapa com cada local de votação e as três eleições está em [dalmolin.dev/enchente-votos](https://dalmolin.dev/enchente-votos/). O resumo saiu [no X](https://x.com/MatheusDalmolin/status/2111824181453000772).

O código está aberto no [GitHub](https://github.com/MatheusGSD/enchente-votos), sob licença MIT, e as figuras e os dados derivados, sob CC BY 4.0. Se achar algum erro, me avise por e-mail, em [contato@dalmolin.dev](mailto:contato@dalmolin.dev), ou no [X](https://x.com/MatheusDalmolin). Eu corrijo e deixo a correção registrada.

<div class="notas">
<p>Publicado primeiro no <a href="https://www.linkedin.com/pulse/enchente-de-2024-mudou-o-voto-na-grande-porto-alegre-dentro-dalmolin-8oblf/">LinkedIn</a>, em 20 de outubro de 2026, antes do 2º turno.</p>
<p>Correções em 6 de novembro de 2026, em relação à versão do LinkedIn. A distância de 2022 entre os dois grupos é de 3,7 pontos, não 3,8, e o intervalo de 95% começa em 2,3 pontos a mais para o PL, não 2,4: nos dois casos, o número tinha sido arredondado duas vezes. Com as outras definições de alagado, a diferença começa em 0,7 ponto a mais para o PL; o 0,8 era o da definição principal. E a mancha da UFRGS cobre de 39% a 48% do Centro Histórico, da Cidade Baixa e do Menino Deus; a versão anterior dizia que ela quase não pegava esses três bairros. O resumo publicado no X antes desta correção ainda traz 3,8.</p>
<p>Fontes: TSE, <a href="https://dadosabertos.tse.jus.br/">dados abertos</a> (votação por seção eleitoral e eleitorado por local de votação, 1º turno de 2018, 2022 e 2026). UFRGS, Possantti et al., <a href="https://doi.org/10.5281/zenodo.14617475">Banco de dados das cheias na Região Hidrográfica do Lago Guaíba em Maio de 2024</a>, v1.4 (CC BY 4.0): área diretamente afetada e simulação do Guaíba a 5,30 m em Porto Alegre. Governo do RS/SPGG, área inundada em 23 de maio de 2024. IBGE, <a href="https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html">malha municipal 2025</a> e <a href="https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios/">Censo 2022, agregados por setores censitários</a>. SEMA-RS, base cartográfica do RS 1:25.000 (BCRS25), dos insumos do banco da UFRGS. Defesa Civil do RS, balanços de <a href="https://estado.rs.gov.br/defesa-civil-atualiza-balanco-das-enchentes-no-rs-24-4">24 de abril de 2025</a> (pessoas e municípios afetados) e de <a href="https://defesacivil.rs.gov.br/defesa-civil-atualiza-lista-de-obitos-e-desaparecidos-decorrentes-da-inundacao-de-2024">19 de agosto de 2025</a> (mortes).</p>
</div>
