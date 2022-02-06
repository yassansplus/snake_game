import sys, random
import pygame


class Game:
    # contenir toutes les variables ainsi que les fonctions utiles pour le bon deroulement du jeu

    def __init__(self):

        self.display = pygame.display.set_mode(
            (800, 600))  # defini la resoultion de la fenetre ,tuple(longueur,largeur)

        pygame.display.set_caption('Jeu Snake')  # attribue un titre a la fenetre
        self.is_launched = True

        self.name = ''
        # creer les variables de position et de direction du serpent
        self.snake_pos_x = 300
        self.snake_pos_y = 300
        self.snake_direction_x = 0
        self.snake_direction_y = 0
        self.snake_body = 10

        # cree la position pour la pomme

        self.apple_pos_x = random.randrange(110, 690, 10)
        self.apple_pos_y = random.randrange(110, 590, 10)
        self.apple = 10
        # fixer les fps
        self.clock = pygame.time.Clock()

        # creer une liste qui rescence toutes les positions du serpent
        self.snake_pos = []

        # creer la variable en rapport avec la taille du serpent
        self.snake_size = 1

        self.beginning_screen = True

        self.head_snake = pygame.image.load('steve.png')

        # Charger l'image

        self.image = pygame.image.load('presentation.jpeg')
        # retrecir l'image
        self.image_title = pygame.transform.scale(self.image, (100, 100))

        # creer la variable score

        self.score = 0

    def main(self):

        self.introduction()

        self.game()

    def game_limit(self):
        # afficher les limites du jeu

        pygame.draw.rect(self.display, (255, 255, 255), (100, 100, 600, 500), 3)

    def snake_movement(self):

        # faire bouger le serpent

        self.snake_pos_x += self.snake_direction_x  # faire bouger le serpent a gauche ou a droite
        self.snake_pos_y += self.snake_direction_y  # faire bouger le serpent en haut ou en bas

        # print(self.serpent_position_x,self.serpent_position_y)

    def display_element(self):

        self.display.fill((0, 0, 0))  # attriubue la couleur noir a l'ecran

        self.display.blit(self.head_snake, (self.snake_pos_x, self.snake_pos_y,
                                            self.snake_body, self.snake_body))

        # afficher la pomme
        pygame.draw.rect(self.display, (255, 0, 0),
                         (self.apple_pos_x, self.apple_pos_y, self.apple, self.apple))

        self.display_snake()

    def display_snake(self):
        # afficher les autres parties du serpent

        for partie_du_serpent in self.snake_pos[:-1]:
            pygame.draw.rect(self.display, (0, 255, 0),
                             (partie_du_serpent[0], partie_du_serpent[1], self.snake_body, self.snake_body))

    def bite_himself(self, snake_head):

        # le serpent se mord

        for snake_parts in self.snake_pos[:-1]:
            if snake_parts == snake_head:
                sys.exit()

    # creer une fonction qui permet d'afficher des messages

    def create_messsage(self, font, message, message_rectangle, couleur):

        if font == 's':
            font = pygame.font.SysFont('Minecraft', 15, False)

        elif font == 'm':
            font = pygame.font.SysFont('Minecraft', 25, False)

        elif font == 'l':
            font = pygame.font.SysFont('Minecrat', 35, True)

        message = font.render(message, True, couleur)

        self.display.blit(message, message_rectangle)

    # Créer une fonction permettant d'enregistrer les score dans un CSV
    def saveScore(self):
        print('Score enregistré')

    # Ecran de démarrage
    def introduction(self):
        # permet de gerer les evenements , d'afficher certains composants du jeu grace au while loop

        while self.beginning_screen:

            for event in pygame.event.get():  # verifier les evenements lorsque le jeu est en cours
                # print(evenement)
                if event.type == pygame.QUIT:
                    sys.exit()

                # Saisie du nom et check avant la partie
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.beginning_screen = False
                    if event.unicode.isalpha():
                        self.name += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                elif event.type == pygame.QUIT:
                    sys.exit()

                self.display.fill((0, 0, 0))

                self.display.blit(self.image_title, (350, 50, 100, 50))

                self.create_messsage('s', 'Bon, on vous appelle comment dans le comte? '
                                     , (200, 300, 200, 5), (240, 240, 240))
                self.create_messsage('s', self.name
                                     , (250, 330, 200, 5), (240, 240, 240))

                self.create_messsage('s', 'Le but du jeu est un wok a volonté faut se bousiller sans boire d\'eau '
                                     , (200, 200, 200, 5), (240, 240, 240))
                self.create_messsage('s', 'Aide steve se ramasser le plus d\'assiette possible',
                                     (250, 220, 200, 5), (240, 240, 240))
                self.create_messsage('m', 'Appuyer sur Enter pour commencer', (200, 450, 200, 5),
                                     (200, 255, 255))

                pygame.display.flip()

    def game(self):
        while self.is_launched:

            # creer un while loop pour creer l'ecran de debut /events /afficher l'image ...

            for event in pygame.event.get():  # verifier les evenements lorsque le jeu est en cours
                # print(evenement)
                if event.type == pygame.QUIT:
                    sys.exit()

                # creer les evenements qui permettent de bouger le serpent

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        # lorsque l'on presse la touche 'fleche droite'
                        self.snake_direction_x = 10
                        self.snake_direction_y = 0
                        # print('Droite')

                    if event.key == pygame.K_LEFT:
                        # lorsque l'on presse la touche 'fleche gauche'

                        self.snake_direction_x = -10
                        self.snake_direction_y = 0
                        # print('LEFT')

                    if event.key == pygame.K_DOWN:
                        # lorsque l'on presse la touche 'fleche vers le  bas'

                        self.snake_direction_y = 10
                        self.snake_direction_x = 0
                        # print('En bas')

                    if event.key == pygame.K_UP:
                        # lorsque l'on presse la touche 'fleche vers le haut'

                        self.snake_direction_y = -10
                        self.snake_direction_x = 0
                        # print('En haut ')

            # faire bouger le serpent si il se trouve dans les limites du jeu

            if self.snake_pos_x <= 100 or self.snake_pos_x >= 700 \
                    or self.snake_pos_y <= 100 or self.snake_pos_y >= 600:
                # si la position du serpent depasse les limites alors le jeu s'arrete
                sys.exit()

            self.snake_movement()

            # cree la cond si le serpent mange la pomme

            if self.apple_pos_y == self.snake_pos_y and self.snake_pos_x == self.apple_pos_x:
                print('Miam miam this shit feels good')

                self.apple_pos_x = random.randrange(110, 690, 10)
                self.apple_pos_y = random.randrange(110, 590, 10)

                # augmenter la taille du serpent

                self.snake_size += 1
                # augmenter le score
                self.score += 1

            # creer une liste pour les qui stocke la position de la tete du serpent
            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.snake_pos_x)
            la_tete_du_serpent.append(self.snake_pos_y)

            # append dans la liste des positions du serpent

            self.snake_pos.append(la_tete_du_serpent)

            # cond pour resoudre le probleme des positions du serpent avec la taille du serpent
            if len(self.snake_pos) > self.snake_size:
                self.snake_pos.pop(0)
                print(self.snake_pos)

            self.display_element()
            self.bite_himself(la_tete_du_serpent)

            self.create_messsage('l', 'Snake Game', (300, 10, 100, 50), (255, 255, 255), )
            self.create_messsage('l', 'score de ' + self.name + ': {}'.format(str(self.score)), (290, 50, 50, 50),
                                 (255, 255, 255), )

            # afficher les limites
            self.game_limit()
            self.clock.tick(15)

            pygame.display.flip()  # mettre a jour l'ecran


if __name__ == '__main__':
    pygame.init()  # initie pygame
    Game().main()
    pygame.quit()  # quitte pygame
