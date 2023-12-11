import pygame
import sys
from data_base_handler import db_handler

# Definir dificultades
FACIL = 1
MEDIO = 2
DIFICIL = 3

# Definir colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

class Menu:

    def __init__(self):
        # Inicializar la variable de dificultad_seleccionada
        self.dificultad_seleccionada = None
        self.usuario = "Invitado"
        self.data_base = db_handler()

    def run_main_menu(self):
        # Inicializar Pygame
        pygame.init()

        # Configuración de la pantalla
        ANCHO, ALTO = 800, 600
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("./assets/Buscaminas Perrón")

        # Cargar la imagen de fondo
        fondo = pygame.image.load("./assets/wallpaper.jpg")  # Reemplaza con la ruta de tu imagen

        # Cargar la imagen del título
        titulo_imagen = pygame.image.load("./assets/titulo.png")  # Reemplaza con la ruta de tu imagen
        titulo_imagen = pygame.transform.scale(titulo_imagen, (430, 166))  # Ajusta el tamaño según sea necesario

        # Crear rectángulos para los botones
        iniciar_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 50, 200, 50)
        tutorial_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 20, 200, 50)
        salir_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 90, 200, 50)

        facil_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 50, 200, 50)
        intermedia_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 20, 200, 50)
        dificil_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 90, 200, 50)

        # Nuevo rectángulo para el botón "Volver al Menú Principal"
        volver_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 160, 200, 50)

        # Función para mostrar el menú
        def mostrar_menu():
            pantalla.blit(fondo, (0, 0))  # Dibujar el fondo

            # Dibujar la imagen del título
            pantalla.blit(titulo_imagen, (ANCHO // 2 - titulo_imagen.get_width() // 2, ALTO // 4 - titulo_imagen.get_height() // 2))

            if self.dificultad_seleccionada is None:
                # Botón de iniciar partida
                pygame.draw.rect(pantalla, AZUL, iniciar_rect)
                mostrar_texto("Iniciar Partida", 30, ANCHO // 2, ALTO // 2 - 25, BLANCO)

                # Botón de ver tutorial
                pygame.draw.rect(pantalla, AZUL, tutorial_rect)
                mostrar_texto("Ver Tutorial", 30, ANCHO // 2, ALTO // 2 + 45, BLANCO)

                # Botón de salir (rojo al ser presionado)
                pygame.draw.rect(pantalla, ROJO, salir_rect)
                mostrar_texto("Salir", 30, ANCHO // 2, ALTO // 2 + 115, BLANCO)
            else:
                # Mostrar botones de selección de dificultad
                pygame.draw.rect(pantalla, AZUL, facil_rect)
                mostrar_texto("Facil", 30, ANCHO // 2, ALTO // 2 - 25, BLANCO)

                pygame.draw.rect(pantalla, AZUL, intermedia_rect)
                mostrar_texto("Intermedia", 30, ANCHO // 2, ALTO // 2 + 45, BLANCO)

                pygame.draw.rect(pantalla, AZUL, dificil_rect)
                mostrar_texto("Dificil", 30, ANCHO // 2, ALTO // 2 + 115, BLANCO)

                # Botón para volver al Menú Principal
                pygame.draw.rect(pantalla, AZUL, volver_rect)
                mostrar_texto("Volver al Menú Principal", 20, ANCHO // 2, ALTO // 2 + 190, BLANCO)

        # Función para mostrar texto en la pantalla
        def mostrar_texto(texto, tamanio, x, y, color):
            fuente = pygame.font.Font(None, tamanio)
            texto_superficie = fuente.render(texto, True, color)
            texto_rect = texto_superficie.get_rect(center=(x, y))
            pantalla.blit(texto_superficie, texto_rect)

        # Bucle principal
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    # Verificar si se hizo clic en algún botón
                    if self.dificultad_seleccionada is None:
                        if iniciar_rect.collidepoint(x, y):
                            print("Iniciar Partida")
                            self.dificultad_seleccionada = "seleccion_dificultad"
                        elif tutorial_rect.collidepoint(x, y):
                            print("Ver Tutorial")
                            # Agregar aquí el código para mostrar el tutorial
                        elif salir_rect.collidepoint(x, y):
                            pygame.quit()
                            sys.exit()
                    else:
                        if facil_rect.collidepoint(x, y):
                            print("Seleccionada dificultad: Fácil")
                            self.dificultad_seleccionada = FACIL
                            pygame.quit()
                            return
                            
                        elif intermedia_rect.collidepoint(x, y):
                            print("Seleccionada dificultad: Intermedia")
                            self.dificultad_seleccionada = MEDIO
                            pygame.quit()
                            return
                            
                        elif dificil_rect.collidepoint(x, y):
                            print("Seleccionada dificultad: Difícil")
                            self.dificultad_seleccionada = DIFICIL
                            pygame.quit()
                            return
                            
                        elif volver_rect.collidepoint(x, y):
                            self.dificultad_seleccionada = None  # Volver al menú principal
            mostrar_menu()
            pygame.display.flip()

    def run_victory_screen(self, victoria, tiempo):

        # Inicializar Pygame
        pygame.init()

        # Configuración de la pantalla
        ANCHO, ALTO = 800, 600
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pantalla.fill((255,255,255))

        fuente = pygame.font.SysFont('unispacebold', 32)
        if victoria:
            pygame.display.set_caption("Victoria")
        else:
            pygame.display.set_caption("Derrota")

        i = 0
        for data in self.data_base.leer_csv(5):
            if data[1]:
                aux = "WIN"
            else :
                aux = "LOSE"
            db_str = fuente.render(f"{data[0]} | {aux} | {data[2]} | {data[3]}% | {data[4]} segs.", True, (0,0,0))
            pantalla.blit(db_str, (10, 10 + i))
            i += 20
        if victoria:
            aux = "WIN"
        else:
            aux = "LOSE"
        str_data = fuente.render(f"Your game data: \n {self.usuario} | {aux} | Dificultad | porcentaje | {tiempo:.0f}segs.",True, (0,0,0))
        pantalla.blit(str_data, (10, 10 + 2*i))

        salir_rect = pygame.Rect(ANCHO // 2 + 100, ALTO - 100 , 200, 50)
        play_again_rect = pygame.Rect(ANCHO // 2 - 300, ALTO - 100, 200, 50)
        pygame.draw.rect(pantalla, ROJO, salir_rect)
        pygame.draw.rect(pantalla, AZUL, play_again_rect)
        
        pygame.display.update()
        
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if salir_rect.collidepoint(x, y):
                        print("Salir")
                        pygame.quit()
                        sys.exit()
                    elif play_again_rect.collidepoint(x, y):
                        print("Jugar otra vez")
                        return True

    def get_user(self):
        pygame.init()

        # Configuración de la ventana
        width, height = 400, 100
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Ingrese Usuario')

        # Configuración de fuentes y texto
        font = pygame.font.Font(None, 36)
        text = ""
        text_color = (255, 255, 255)

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("Usuario ingresado:", text)
                        self.usuario = text
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            screen.fill((0, 0, 0))

            # Renderizar y mostrar el texto actual
            input_text = font.render(text, True, text_color)
            screen.blit(input_text, (10, 10))
            pygame.display.flip()
            clock.tick(30)



    def get_params_from_dificulty(self):
        if self.dificultad_seleccionada == FACIL:
            return (10, 10, 10)
        if self.dificultad_seleccionada == DIFICIL:
            return (30, 20, 40)
        return (20, 15, 25)
        
