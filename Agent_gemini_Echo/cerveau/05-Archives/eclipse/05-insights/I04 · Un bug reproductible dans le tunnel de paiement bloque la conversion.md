---
type: insight
projet: "[[Eclipse]]"
priorite: P1
confiance: moyenne
occurrences: 1
participants:
  - "#013"
tags:
  - uxr
  - insight
  - defaut-technique
---

# I04 · Un bug reproductible dans le tunnel de paiement bloque la conversion

## Énoncé

Le sélecteur de pays du formulaire Stripe échoue lorsque l'utilisateur recourt à
l'autocomplétion de son navigateur. La page se rafraîchit sans confirmation ni
message d'erreur.

## Preuves

> « C'est frustrant. Je veux vous donner mon argent car l'outil me fait gagner
> 2h par jour, mais votre tunnel de vente est moins stable que votre outil
> gratuit. » — [[E05 · #013]]

Trois tentatives de paiement consécutives échouées, cause identifiée et
documentée par le participant lui-même.

## Portée

1 participant sur 8 — mais **probablement sous-déclaré** : #013 est développeur
et a su diagnostiquer la cause. Un utilisateur non technique aurait conclu à une
erreur de sa part, comme l'a fait #002 dans un autre contexte.

Impact business : conversions directement perdues, invisibles dans les
analytics produit actuels.

## Ce que cet insight ne dit pas

Il ne permet pas d'estimer la part de ce défaut dans les 45 % d'abandons.
Seule une analyse des logs de checkout le permettrait.

## HMW

Comment pourrait-on garantir que le formulaire de paiement fonctionne avec les
comportements de navigation standard — autocomplétion, retour arrière ?

## Non distillé — et c'est volontaire

Un défaut technique corrigible n'est pas une connaissance durable sur les
utilisateurs : il disparaîtra avec le correctif. Ce qui pourrait le devenir,
après confirmation sur d'autres études, c'est le fait que les utilisateurs
recourent massivement à l'autocomplétion dans les tunnels de paiement.
Pas assez de preuves aujourd'hui pour créer une connaissance.
