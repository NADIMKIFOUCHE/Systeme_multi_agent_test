# Système Multi-Agents Test

Première expérience avec un système d'agents intelligents basé sur des modèles de langage.

## Description du Projet

Ce projet implémente un système multi-agents utilisant le modèle Qwen/Qwen2.5-1.5B-Instruct pour effectuer des tâches séquentielles. Le système démontre comment plusieurs agents spécialisés peuvent collaborer pour traiter une requête utilisateur et évaluer la qualité des réponses.

## Structure du Projet

```
Systeme_multi_agent_test/
├── src/
│   ├── main.py          # Point d'entrée principal
│   ├── agent.py         # Classe Agent de base
│   └── llm.py           # Interface avec le modèle de langage
├── bin/
│   └── interface_agent.py # Interface expérimentale avec agent humoristique
└── README.md
```

## Fonctionnement

Le système utilise trois agents spécialisés :

1. **Agent Calculateur** : Répond aux questions mathématiques avec seulement le résultat numérique
2. **Agent Culturèle** : Fournit des informations culturelles liées à la réponse numérique
3. **Agent Évaluateur** : Note la réponse sur 10 avec des critères précis

### Exemple de flux

1. L'utilisateur pose une question mathématique
2. L'agent calculateur résout le problème
3. L'agent culturalise enrichit la réponse avec des faits pertinents
4. L'agent évaluateur attribue une note à la réponse complète

## Technologies Utilisées

- **Python** : Langage principal du projet
- **Transformers (Hugging Face)** : Pour le chargement et l'utilisation du modèle Qwen
- **PyTorch** : Backend pour l'exécution du modèle

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel : `python -m venv venv`
3. Activer l'environnement : `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Installer les dépendances : `pip install transformers torch`

## Utilisation

Exécuter le script principal :
```bash
python src/main.py
```

Suivre les instructions à l'écran pour poser une question.

## Composants Clés

### LLM (Large Language Model)
Utilise le modèle Qwen/Qwen2.5-1.5B-Instruct avec chargement automatique et mise en cache.

### Agent
Classe représentant un agent spécialisé avec :
- Un prompt système définissant son rôle
- Une mémoire des interactions
- Une méthode `run()` pour exécuter une tâche

## Développement Futur = objectifs d’expérimentation


Ce projet n’a pas pour objectif de devenir un produit final, mais une base d’expérimentation autour des systèmes multi-agents et des modèles de langage locaux.

Les axes explorés sont :

- Première expérience avec une architecture multi-agents
- Compréhension du fonctionnement des LLM locaux et de leurs limites
- Analyse de l’impact du nombre de paramètres des modèles sur :
    - la qualité des réponses
    - la latence d’exécution
    - la stabilité des résultats
- Étude de la spécialisation des agents :
    - séparation des rôles (calcul, culture, évaluation)
    - impact sur la qualité globale des réponses
    - réduction partielle des hallucinations par structuration des tâches
- Analyse de l’impact du prompting :
    - importance de la formulation des instructions
    - sensibilité des modèles aux consignes système
    - variation des résultats selon la structure des prompts
- Expérimentation sur la collaboration entre agents :
    - enchaînement de tâches séquentielles
    - propagation d’erreurs entre agents
    - importance du format des sorties intermédiaires

Compréhensions issues du projet :

- La performance d’un modèle ne dépend pas uniquement de sa taille, mais aussi du cas d’usage
- La structuration en agents améliore la lisibilité du pipeline de traitement
- La spécialisation des agents permet de mieux contrôler les réponses, mais introduit des dépendances entre étapes
- Les modèles locaux sont fortement sensibles au prompting et à la formulation des instructions
- La qualité du format de sortie est aussi importante que le contenu généré
- Les hallucinations ne disparaissent pas avec la structure multi-agents, mais peuvent être mieux contenues