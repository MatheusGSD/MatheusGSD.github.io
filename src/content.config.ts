import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

// Um arquivo por projeto. O print fica em public/img/projetos/<print>-claro.webp e <print>-escuro.webp.
const projetos = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projetos" }),
  schema: z.object({
    titulo: z.string(),
    resumo: z.string(),
    tema: z.string(),
    data: z.coerce.date(),
    url: z.string().url(),
    dominio: z.string(),
    print: z.string(),
    registro: z.boolean().default(false), // página de um dia só (ex.: checagem de debate)
    rascunho: z.boolean().default(false),
  }),
});

// Textos: artigos e ideias. Com `url`, o texto é HTML pronto gerado no repo do projeto
// (em public/textos/<slug>/). Sem `url`, o corpo Markdown vira a página /textos/<slug>/.
const textos = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/textos" }),
  schema: z.object({
    titulo: z.string(),
    lede: z.string(),
    tipo: z.enum(["artigo", "ideia"]),
    data: z.coerce.date(),
    url: z.string().optional(),
    imagem: z.string().optional(),
    rascunho: z.boolean().default(false),
  }),
});

export const collections = { projetos, textos };
