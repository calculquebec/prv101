# Matériel pour la formation PRV101

[Site Web](https://calculquebec.github.io/prv101/)

## État

Ce matériel est en cours de création et seule une version française sera
disponible, en premier lieu.

* For an English version, see the
  [original material](https://folio.vastcloud.org/introParaview.html).

## Installation locale et compilation

```Bash
pip install sphinx==8.1.3 sphinx-intl sphinx-book-theme==1.1.3

cd doc
./build.sh
```

## Déploiement via GitHub

Dans le dépôt GitHub -> Settings -> Pages :

* Sélectionner la *Source* **Deploy from a branch**
* Sélectionner la branche **gh-pages** et **/ (root)**
* Cliquer sur le bouton *Save*

## Style de programmation

Indentez toujours avec 4 espaces.

Pour configurer Vim:

```Bash
mkdir -p "$HOME"/.vim/indent
cp /usr/share/vim/vim*/indent/rst.vim "$HOME"/.vim/indent/
sed -e 's/= 3/= 4/' -i "$HOME"/.vim/indent/rst.vim
```
