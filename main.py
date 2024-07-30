import pygame, sys
from Oreo import *
from Menu_Screen import *
from Shop import *

pygame.init()
pygame.display.set_caption("Oreo Clicker")
Clock = pygame.time.Clock()
Timer = pygame.USEREVENT + 1
pygame.time.set_timer(Timer, 1000)
CPS_Timer = pygame.USEREVENT + 2
pygame.time.set_timer(CPS_Timer, 1000)
cookie = Cookie()
Menu = MiddleScreen()
shop = Upgrades()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == Timer:
            Menu.Time(OC['Time'])
        if e.type == CPS_Timer:
            shop.AMFunc()
            shop.GrandmaFunc()
            shop.FarmFunc()
            shop.MineFunc()
            shop.FactoryFunc()
            shop.BankFunc()
            shop.TempleFunc()
            shop.WTFunc()
            shop.ShipmentFunc()
            shop.ALFunc()
            shop.PortalFunc()
            shop.TMFunc()
            shop.ACFunc()
            shop.PrismFunc()
            shop.ChanceMakerFunc()
            shop.FEFunc()
            shop.PCFunc()
            shop.IVFunc()
            shop.CBFunc()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LSHIFT or e.key == pygame.K_RSHIFT:
                shop.Upgrades = not (shop.Upgrades)
                print(OC)
        if e.type == pygame.MOUSEBUTTONDOWN:print(e.pos)
    SCREEN.blit(BG1, BG1_Rect)
    SCREEN.blit(BG2, BG2_rect)
    SCREEN.blit(BG3, BG3_rect)
    Menu.Draw()
    cookie.Draw()
    shop.Draw()
    pygame.display.update()
    Clock.tick(10_000)
