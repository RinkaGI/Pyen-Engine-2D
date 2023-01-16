from sdl2 import *

class PyenEngine:
    def __init__(self, title: str, width: int, height: int) -> None:
        # Setting up variables
        self.title = title.encode()
        self.width = width
        self.height = height

        # Making the window with SDL2 (window manager)
        SDL_Init(SDL_INIT_EVERYTHING)
        
        self.window = SDL_CreateWindow(
            self.title,
            SDL_WINDOWPOS_CENTERED,
            SDL_WINDOWPOS_CENTERED,
            self.width,
            self.height,
            SDL_WINDOW_SHOWN
        )

        self.renderer = SDL_CreateRenderer(
            self.window,
            -1,
            0
        )

        SDL_ShowWindow(self.window)

        SDL_RenderClear(self.renderer)
        SDL_RenderPresent(self.renderer)

        SDL_Delay(5000)

if __name__ == '__main__':
    PyenEngine('Window test', 800, 600)