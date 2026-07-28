# Notion via MCP — Guide d'utilisation

Toutes les interactions Notion passent par le MCP Notion connecté.
URL du MCP : `https://mcp.notion.com/mcp`

Déclaré dans `.gemini/settings.json` (clé `mcpServers.notion`).
Vérifier la connexion : `/mcp list` — autoriser : `/mcp auth notion`.
Si les outils `notion-*` sont absents, produire les livrables en Markdown local
et signaler le blocage au pilote (VOIX 1).

---

## Trouver la database "Projets de recherche"

```
notion-search : query="Projets de recherche", filter="database"
```

Garder l'ID de la database dans uxr-state.json une fois trouvé.

---

## Créer une carte projet

```
notion-create-pages :
  parent: { database_id: "[ID database Projets de recherche]" }
  properties:
    Nom: "[Nom du projet] · [date]"
    Statut: "Cadrage"
    Objectif: "[1 phrase]"
    "Nb entretiens prévus": [N]
    "Nb entretiens réalisés": 0
    "Date début": "[date ISO]"
```

---

## Créer une sous-page dans une carte

```
notion-create-pages :
  parent: { page_id: "[ID de la carte projet]" }
  properties:
    title: "📋 Préparation entretien"
```

Répéter pour :
- "📝 Notes brutes"
- "🧠 Synthèse & insights"
- "📊 Rapport final"

---

## Écrire du contenu dans une page

Utiliser `notion-update-page` avec des blocs de contenu.

Structure des blocs :
```json
{
  "heading_2": { "rich_text": [{ "text": { "content": "Titre de section" } }] }
}
{
  "paragraph": { "rich_text": [{ "text": { "content": "Contenu..." } }] }
}
```

---

## Mettre à jour le statut d'une carte

```
notion-update-page :
  page_id: "[ID de la carte]"
  properties:
    Statut: "Terrain"  // ou "Analyse" ou "Terminé"
    "Nb entretiens réalisés": [N]
```

---

## Lire le contenu d'une page

```
notion-fetch : url="[URL de la page Notion]"
```

Ou par ID :
```
notion-fetch : url="https://notion.so/[page-id]"
```

---

## Créer une sous-page dans "Notes brutes"

Après avoir trouvé l'ID de la page "📝 Notes brutes" :

```
notion-create-pages :
  parent: { page_id: "[ID Notes brutes]" }
  properties:
    title: "🎙 Entretien #[N] · [Prénom] · [date]"
```

Puis écrire les notes avec `notion-update-page`.

---

## Erreurs courantes

- **Page introuvable** → vérifier l'ID dans uxr-state.json, refaire un `notion-search`
- **Propriété non trouvée** → la database a peut-être un nom de propriété différent → faire `notion-fetch` sur la database pour vérifier le schéma
- **Permission refusée** → le workspace Notion doit avoir l'intégration activée
