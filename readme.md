Merci d'utiliser MachinePingu.

MachinePingu est un programme qui a pour objectifs d'avoir une vision de l'état de son réseau

Il est composé d'un tableau de connexion qui propose chacun deux moyens d'accéder à un réseau (par Internet et par Lan)

Fonctionnement du programme : Au démmarage puis toutes les 30 sec le programme fait un ping sur chaque réseau, puis selon le résultat affiche la case concernés en VERT pour réponse et ROUGE pour absence de réponse. Pour faire manuellement un ping, il est possible de cliquer sur la case directement.

Ajouter/Modifier un réseau :

Pour Ajoutez un Réseau :

Voir ligne 9 : BoxP = Box("Box Principale")
Cette ligne créé la grande case, elle demande un seul paramètre
Pour créer une nouvel box copier la ligne modifier le nom de la case (ci-dessus Frame1)
et modifier le nom de la box (ci-dessus Box1)

Voir ligne 10 : ReseauInt = Reseau(BoxP,"Internet", "172.1.1.1")
Cette ligne créé la case verte ou rouge avec l'ip, elle demande 3 paramètres
Pour créer un nouveau réseau copier la ligne modifier le nom du réseau (ci-dessus FrameInternet),
Frame1 represente la box sous laquelle le réseau apparaitra, "Internet" represente le nom du réseau, 
"192.1.1.1" represente l'ip qui sera ping

Modification de fonctionnement :

Pour modifier le temps de rechargement :
	
	Allez dans Classe puis dans le fichier Reseau à la ligne 25 et modifiez le temps de rechargement (de base 30000)
		self.frameParent.fenetre.fenetre.after(30000, self.reload)

Pour modifier le nombre de paquet à envoyez et le temps d'attente de réponse :

	Allez dans Classe puis dans le fichier Reseau
	Allez à la ligne 35 et le chiffre aprés le -n répresente le nombre de paquet 
	et le chiffre aprés le -w répresente le temps d'attente de réponse (en sec)
		    p=subprocess.Popen(["ping","-n","2", "-w", "2", ip], stdout=limbo, stderr=limbo).wait()
	/!\ Laissez les guillemets

Programme conçu en Python par Woodlutins
