# RFIDJuke

Le RFID JukeBox est un projet open-source de la FABrique du Loch.

## Matériel
- Raspberry Py

## Logiciel
On privilégie comme IDE (environnement de développement), VSCode.

### Installer vscode

#### Pour Linux
Rendez-vous sur le site de [Visual Studio Code](https://code.visualstudio.com)
Et installez-le pour votre machine (Windowd, Mac, Linux)

##### installer git

Si `git` `--``help` ne donne rien,
Installez git avec : `sudo apt install git`

#### Clonez le repository

Mettez vous dans un répertoire sur votre machine (ex: `dev`) et tapez

    git clone https://github.com/fabloch/rfid_juke.git
    cd rfid_juke

##### Installez pip et les librairies nécessaires au projet

    sudo apt install python3-pip
    pip3 install -r config/requirements_dev.txt


#### Ouvrez le projet dans VSCode
Dans le terminal, tapez `code`

Un fois VSCode lancé, tapez (anglais ou français):
- `Fichier` ou `File` en anglais
- `Ouvrir l'espace de travail à partir du fichier` ou `Open Workspace From File` en anglais
- Choisissez le fichier `config/rfid_juke.code-workspace`

VSCode va vous proposer d’installer les extensions pour notamment la magique extension `Python`
Sinon vous pouvez [l'installer depuis cette adresse](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
Une fois installée, 
- cliquez sur la roue crantée
- puis `Paramètres d'extension`
- puis `Espace de travail` ou `Workspace` en anglais
- vérifiez que le menu déroulant `Python › Formatting: Provider` est bien sur `black` (cela vous offrira un formattage automatique du code à la sauvegarde des fichiers)

Optionnel : coloriser par paires les parenthèses, crochets, accolades est très pratique pour la lecture du code. Pour cela, installez l'extension [bracket pair colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)

#### Pour lancer les tests
Depuis le terminal, tapez:

    python3 -m unittest



#### Ecrire un test

#### Ecrire une fonctionnalité
