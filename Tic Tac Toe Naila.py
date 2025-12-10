# Tic Tac Toe (perbaikan)
import pygame as pg
import sys
import time
from pygame.locals import *

# -------------------------
# konfigurasi / variabel
# -------------------------
XO = 'x'                # giliran sekarang ('x' atau 'o')
winner = None           # pemenang saat ini
draw = False            # apakah seri
width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None]*3, [None]*3, [None]*3]

# -------------------------
# inisialisasi pygame
# -------------------------
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("My Tic Tac Toe")

# -------------------------
# load gambar (dengan fallback)
# -------------------------
def safe_load_image(path, size=None, fallback_text=None):
    try:
        img = pg.image.load(path)
        if size:
            img = pg.transform.scale(img, size)
        return img
    except Exception as e:
        # buat surface fallback dengan teks
        surf = pg.Surface(size if size else (80, 80))
        surf.fill((200, 200, 200))
        if fallback_text:
            try:
                font = pg.font.Font(None, 48)
                txt = font.render(fallback_text, True, (20, 20, 20))
                txt_rect = txt.get_rect(center=(surf.get_width()//2, surf.get_height()//2))
                surf.blit(txt, txt_rect)
            except:
                pass
        return surf

initiating_window = safe_load_image("modified_cover.png", (width, height + 100), None)
x_img = safe_load_image("X_modified.png", (80, 80), "X")
o_img = safe_load_image("o_modified.png", (80, 80), "O")

# -------------------------
# fungsi tampilan & logika
# -------------------------
def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(1)   # singkat saja
    screen.fill(white)

    # garis pembagi (gunakan integer)
    third_w = width // 3
    third_h = height // 3
    pg.draw.line(screen, line_color, (third_w, 0), (third_w, height), 7)
    pg.draw.line(screen, line_color, (third_w * 2, 0), (third_w * 2, height), 7)
    pg.draw.line(screen, line_color, (0, third_h), (width, third_h), 7)
    pg.draw.line(screen, line_color, (0, third_h * 2), (width, third_h * 2), 7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"

    font = pg.font.Font(None, 30)
    text = font.render(message, True, (255, 255, 255))

    # buat area status di bawah
    screen.fill((0, 0, 0), (0, height, width, 100))
    text_rect = text.get_rect(center=(width // 2, height + 50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global board, winner, draw

    # rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner = board[row][0]
            y = (row + 1) * (height // 3) - (height // 6)
            pg.draw.line(screen, (250, 0, 0), (0, y), (width, y), 4)
            break

    # cols
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            x = (col + 1) * (width // 3) - (width // 6)
            pg.draw.line(screen, (250, 0, 0), (x, 0), (x, height), 4)
            break

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (10, 10), (width-10, height-10), 4)

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (width-10, 10), (10, height-10), 4)

    # draw: semua tidak None dan tidak ada winner
    if all(all(cell is not None for cell in row) for row in board) and winner is None:
        draw = True

    draw_status()

def drawXO(row, col):
    global board, XO

    # hitung pos berdasarkan baris/kolom (pusat gambar agak di-offset)
    # gunakan integer coordinates
    third_w = width // 3
    third_h = height // 3

    # default None check (shouldn't happen jika dipanggil benar)
    if row not in (1,2,3) or col not in (1,2,3):
        return

    posx = (row - 1) * third_w + 30
    posy = (col - 1) * third_h + 30

    # set board
    board[row-1][col-1] = XO

    if XO == 'x':
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()

def user_click():
    x, y = pg.mouse.get_pos()

    # kolom
    if x < width // 3:
        col = 1
    elif x < (width // 3) * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None

    # baris
    if y < height // 3:
        row = 1
    elif y < (height // 3) * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None

    if row and col and board[row-1][col-1] is None:
        drawXO(row, col)
        check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(1)
    XO = 'x'
    draw = False
    winner = None
    board = [[None]*3, [None]*3, [None]*3]
    screen.fill(white)
    game_initiating_window()

# -------------------------
# main loop
# -------------------------
game_initiating_window()

running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)

pg.quit()
sys.exit()
