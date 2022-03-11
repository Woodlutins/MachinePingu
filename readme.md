Merci d'utiliser MachinePingu.

MachinePingu est un programme qui a pour objectifs d'avoir une vision de l'état de son réseau.

Il est composé d'un tableau de connexion.

Fonctionnement du programme : Au démmarage puis toutes les 30 sec (modifiable) le programme fait un ping sur chaque réseau, puis selon le résultat affiche la case concernés en VERT pour si réponse et ROUGE pour si absence de réponse. Pour faire manuellement un ping, il est possible de cliquer sur la case directement.

Ajouter/Modifier un réseau :

Pour Ajoutez un Réseau :

Voir ligne 59 : BoxP = Box("Box Principale")
Cette ligne créé la grande case, elle demande un seul paramètre
Pour créer une nouvel box copier la ligne modifier le nom de la case (ci-dessus Frame1)
et modifier le nom de la box (ci-dessus Box1)

Voir ligne 60 : ReseauInt = Reseau(BoxP,"Internet", "172.1.1.1")
Cette ligne créé la case verte ou rouge avec l'ip, elle demande 3 paramètres
Pour créer un nouveau réseau copier la ligne modifier le nom du réseau (ci-dessus FrameInternet),
Frame1 represente la box sous laquelle le réseau apparaitra, "Internet" represente le nom du réseau,
"192.1.1.1" represente l'ip qui sera ping

Modifier l'interface Graphique :

Options>Colors

	Cliquer sur une couleur puis sélectionner la couleur que vous voulez.

	FondFenetre : le fond de base noir
	FondBox : le fond des boites de base Gris foncé
	FondNom : le fond du titre des box de base Gris
	CouleurTexte : la couleur du texte de base Gris Clair
	CouleurUp : la couleur quand les pings répondent de base Vert
	CouleurDown : la couleur quand les pings ne répondent pas de base Rouge
	CouleurTest : la couleur quand les pings sont en train d'être fait

Si aprés modification vous voulez retournez au couleur de base allez dans le fichier config.txt dans Classe et remplacer le texte par ceci

		black
		darkslategray
		slategray
		lightgray
		green
		red
		orange

Modification de fonctionnement :

Pour modifier le temps de rechargement :

Allez à la ligne 38 et modifiez le temps de rechargement (de base 30000)
		fenetre.after(30000, self.reload)

Pour modifier le nombre de paquet à envoyez et le temps d'attente de réponse :

Allez à la ligne 9 et le chiffre aprés le -n répresente le nombre de paquet
et le chiffre aprés le -w répresente le temps d'attente de réponse (en sec)
		    p=subprocess.Popen(["ping","-n","2", "-w", "2", ip], stdout=limbo, stderr=limbo).wait()
/!\ Laissez les guillemets

Programme conçu en Python par Woodlutins
