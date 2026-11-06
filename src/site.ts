// Dados fixos do site e utilidades usadas pelas páginas.
import { getCollection } from "astro:content";

export const SITE = {
  nome: "Matheus Dalmolin",
  url: "https://dalmolin.dev",
  // Bio do X do usuário (06/11/2026), escolhida por ele para o site.
  bio: "Construo ferramentas com IA e faço análises com dados públicos. Agentes, mapas, simulações e o que mais der vontade de entender.",
  contatos: [
    { nome: "contato@dalmolin.dev", url: "mailto:contato@dalmolin.dev" },
    { nome: "X", url: "https://x.com/MatheusDalmolin" },
    { nome: "LinkedIn", url: "https://www.linkedin.com/in/matheus-dalmolin/" },
    { nome: "Threads", url: "https://www.threads.com/@dalmolinmatheuss" },
    { nome: "GitHub", url: "https://github.com/MatheusGSD" },
  ],
};

const MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];
export const dataCurta = (d: Date) => `${d.getUTCDate()} ${MESES[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
export const dataIso = (d: Date) => d.toISOString().slice(0, 10);

export type Item = {
  k: "projeto" | "texto";
  id: string;
  titulo: string;
  resumo: string;
  data: Date;
  url: string;
  rotulo: string;
  dominio: string;
  print?: string; // projeto: nome base do print claro/escuro
  imagem?: string; // texto: imagem única
  registro?: boolean;
};

export async function itens(filtro: "tudo" | "projeto" | "texto" = "tudo"): Promise<Item[]> {
  const projetos = (await getCollection("projetos", (p) => !p.data.rascunho)).map((p) => ({
    k: "projeto" as const,
    id: p.id,
    titulo: p.data.titulo,
    resumo: p.data.resumo,
    data: p.data.data,
    url: p.data.url,
    rotulo: `projeto · ${p.data.tema.toLowerCase()}`,
    dominio: p.data.dominio,
    print: p.data.print,
    registro: p.data.registro,
  }));
  const textos = (await getCollection("textos", (t) => !t.data.rascunho)).map((t) => ({
    k: "texto" as const,
    id: t.id,
    titulo: t.data.titulo,
    resumo: t.data.lede,
    data: t.data.data,
    url: t.data.url ?? `/textos/${t.id}/`,
    rotulo: t.data.tipo,
    dominio: `dalmolin.dev/textos/${t.id}`,
    imagem: t.data.imagem,
  }));
  return [...projetos, ...textos]
    .filter((i) => filtro === "tudo" || i.k === filtro)
    .sort((a, b) => b.data.getTime() - a.data.getTime() || (a.k === "texto" ? -1 : 1));
}

export async function contagens() {
  const [p, t] = await Promise.all([itens("projeto"), itens("texto")]);
  return { projetos: p.length, textos: t.length };
}
