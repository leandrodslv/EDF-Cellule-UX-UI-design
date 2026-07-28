# Schéma uxr-state.json

Ce fichier est la mémoire persistante de l'agent. Il doit être lu au démarrage
et mis à jour après CHAQUE action.

## Structure complète

```json
{
  "version": "1.0",
  "agent": "uxr-agent",
  "last_updated": "2025-04-20T10:30:00",
  "active_project": "onboarding-edf",

  "projects": [
    {
      "id": "onboarding-edf",
      "name": "Onboarding EDF",
      "status": "terrain",
      "created_at": "2025-04-15",

      "research": {
        "objective": "Comprendre les frictions lors de l'onboarding client",
        "hypotheses": ["H1: ...", "H2: ...", "H3: ..."],
        "participant_profile": "Nouveaux clients EDF < 3 mois",
        "interviews_planned": 5,
        "interviews_done": 2
      },

      "notion": {
        "card_id": "abc123",
        "card_url": "https://notion.so/...",
        "pages": {
          "preparation": "https://notion.so/...",
          "notes_folder": "https://notion.so/...",
          "synthese": "https://notion.so/...",
          "rapport": "https://notion.so/..."
        }
      },

      "interviews": [
        {
          "number": 1,
          "participant": "Sarah",
          "date": "2025-04-17",
          "status": "done",
          "notion_page_id": "xyz789",
          "notion_page_url": "https://notion.so/..."
        },
        {
          "number": 2,
          "participant": "Marc",
          "date": "2025-04-19",
          "status": "done",
          "notion_page_id": "xyz790",
          "notion_page_url": "https://notion.so/..."
        },
        {
          "number": 3,
          "participant": null,
          "date": null,
          "status": "planned",
          "notion_page_id": null,
          "notion_page_url": null
        }
      ],

      "plan": {
        "phase_current": "terrain",
        "phases_done": ["init", "preparation"],
        "next_action": "Attendre entretien #3",
        "estimated_end": "2025-05-01"
      },

      "human_tasks": {
        "current": {
          "id": 3,
          "title": "Mener l'entretien #3",
          "status": "pending",
          "emitted_at": "2025-04-19T14:00:00",
          "resume_phrase": "entretien 3 fait, voici les notes"
        },
        "history": [
          {
            "id": 1,
            "title": "Valider le plan de recherche",
            "status": "done",
            "completed_at": "2025-04-15T16:00:00"
          },
          {
            "id": 2,
            "title": "Recruter les participants",
            "status": "done",
            "completed_at": "2025-04-16T10:00:00"
          }
        ]
      }
    }
  ]
}
```

## Règles de mise à jour

| Événement | Champs à mettre à jour |
|-----------|----------------------|
| Nouveau projet | Ajouter entrée dans `projects[]`, `active_project` |
| Entretien reçu | `interviews_done++`, `interviews[N].status = "done"` |
| Phase terminée | `phases_done[]`, `phase_current`, `next_action` |
| Human Task émis | `human_tasks.current` |
| Human Task complété | Déplacer vers `human_tasks.history`, vider `current` |
| Notion écrit | Mettre à jour l'URL correspondante dans `notion.pages` |

## Statuts projet possibles
- `cadrage` → Phase 0 en cours
- `preparation` → Phase 1 en cours  
- `terrain` → Phase 2 en cours
- `analyse` → Phase 3 en cours
- `termine` → Phase 4 complète

---

## Champs ajoutés pour le mode questionnaire

```json
{
  "research_mode": "mixed",  // "interviews_only" | "survey_only" | "mixed"

  "survey": {
    "status": "done",        // "pending" | "in_progress" | "done"
    "excel_path": "./onboarding-edf-questionnaire.xlsx",
    "forms_url": "https://forms.office.com/...",
    "responses_received": 47,
    "responses_target": 50,
    "recruited_for_interviews": ["Sarah", "Marc", "Julie"]
  }
}
```

Ajouter ces champs dans chaque entrée de `projects[]` selon le mode.
