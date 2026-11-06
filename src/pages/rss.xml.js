import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import { SITE } from "../site";

export async function GET(context) {
  const textos = (await getCollection("textos", (t) => !t.data.rascunho)).sort((a, b) => b.data.data - a.data.data);
  return rss({
    title: `Textos · ${SITE.nome}`,
    description: "Artigos e ideias sobre dados, eleições e o método por trás dos números.",
    site: context.site,
    customData: "<language>pt-BR</language>",
    items: textos.map((t) => ({
      title: t.data.titulo,
      description: t.data.lede,
      pubDate: t.data.data,
      link: t.data.url ?? `/textos/${t.id}/`,
    })),
  });
}
