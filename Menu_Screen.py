import pygame, json, os
from Oreo import *
pygame.init()
BG2 = pygame.Surface((637, 615))
BG2.fill((159, 129, 112))
BG2_rect = BG2.get_rect(topleft = (405,0))

class MiddleScreen:
    def __init__(self):
        self.bar = pygame.Surface((637,101))
        self.bar.fill((165, 84, 42))
        self.bar_rect = self.bar.get_rect(topleft = (405,0))
        self.CountUp = 0
        
        #Options
        self.options = pygame.Surface((85,44))
        self.option = False
        self.options.fill((165, 84, 42))
        self.options_rect = self.options.get_rect(topleft = (405,0))
        self.options_text = Game_Font.render("Options", True, "White")
        self.options_text_rect = self.options_text.get_rect(center = self.options_rect.center)
        
        #Option info
        self.OptionButton1 = pygame.Surface((85,44))
        self.OptionButton1.fill((165, 84, 42))
        self.OptionButton1_rect = self.OptionButton1.get_rect(center = self.bar_rect.center)
        self.OptionButton1_text = Game_Font.render("Save", True, "White")
        self.OptionButton1_text_rect = self.OptionButton1_text.get_rect(center = (self.OptionButton1_rect.center))

        self.OptionButton2 = pygame.Surface((85,44))
        self.OptionButton2.fill("Red")
        x,y = self.bar_rect.center
        self.OptionButton2_rect = self.OptionButton2.get_rect(center = (x + 100,y))
        self.OptionButton2_text = Game_Font.render("Restart", True, "White")
        self.OptionButton2_text_rect = self.OptionButton2_text.get_rect(center = (self.OptionButton2_rect.center))
        
        # Stats
        self.Stats = pygame.Surface((85,44))
        self.Stat = False
        self.Stats.fill((165,84,42))
        self.Stats_rect = self.Stats.get_rect(topleft = self.bar_rect.midleft)
        self.Stats_text = Game_Font.render("Stats", True, "White")
        self.Stats_text_rect = self.Stats_text.get_rect(center = self.Stats_rect.center)
        
        #StatsScreen
        self.StatsScreen = pygame.Surface((640,520))
        self.StatsScreen.fill("chocolate4")
        
        #StatsInfo
        self.CC_Display,self.OC_Display,self.HM_Display,self.AC_Display = "","","",""
        self.OC_Display = self.NumberShrink(OC['AllClicks'],self.OC_Display)
        self.CC_Display = self.NumberShrink(OC['Clicks'],self.CC_Display)
        self.HM_Display = self.NumberShrink(OC['HandMade'], self.HM_Display)
        self.AC_Display = self.NumberShrink(OC['ShopClicks'], self.AC_Display)
        self.CurrentClicks = Game_Font.render(f"Oreos in Bank:{self.CC_Display}", True, "White")
        self.OverallClicks = Game_Font.render(f"Oreos made (all time): {self.OC_Display}", True, "White")
        self.TotalTime = Game_Font.render(f"PlayTime:{self.CountUp}", True, "White")
        self.Handmade = Game_Font.render(f"Hand-made Oreos:{self.HM_Display}", True, "White")
        self.AutoClicks = Game_Font.render(f"Auto Clicks: {self.AC_Display}", True, "White")
        self.ItemAmount = Game_Font.render(f"Items Purchased: {OC['ItemAmount']}", True, "White")
        self.UpgradeAmount = Game_Font.render(f'Upgrade Purchase: {OC["UpgradeAmount"]}', True, "White")
        self.Cursor_OPS_Display  = ""
        self.Cursor_OPS = Game_Font.render(f"Overall Mouse/Cursor OPS:{0.1*float(OC['AMX']) + (OC['AMADDER']*OC['AMADDERX'])}", True, "White")
        self.Grandma_OPS_Display = ""
        self.Grandma_OPS = Game_Font.render(f"Overall Grandma OPS:{1*float(OC['GrandX'])}", True, "White")
        self.Mine_OPS_Display = ""
        self.Farm_OPS_Display = ""
        self.Farm_OPS = Game_Font.render(f"Overall Farm OPS:{8*float(OC['FarmX'])* OC['FarmAmount']}", True, "White")
        self.Mine_OPS = Game_Font.render(f"Overall Mine OPS:{47*float(OC['MineX'])* OC['MineAmount']}", True, "White")
        self.Factory_OPS_Display = ''
        self.Factory_OPS = Game_Font.render(f"Overall Factory OPS:{260*float(OC['FactoryX'])*OC['FactoryAmount']}",True,"White")
        self.Bank_OPS_Diplay = ''
        self.Bank_OPS = Game_Font.render(f"Overall Bank OPS:{1400*float(OC['BankX']) * OC['BankAmount']}", True, "White")
        self.Temple_OPS_Display =""
        self.Temple_OPS = Game_Font.render(f"Overall Temple OPS:{7800*float(OC['TempleX']) *OC['TempleAmount']}", True, "White")
        self.WT_OPS_Dipsplay = ""
        self.WT_OPS = Game_Font.render(f"Overall Wizard Tower OPS:{44_000*float(OC['WizardTowerX'])*OC['WizardTowerAmount']}", True, "White")
        self.SM_OPS_Display = ""
        self.SM_OPS = Game_Font.render(f"Overall Shipment OPS:{260_000*float(OC['ShipmentX'])*OC['ShipmentAmount']}", True, "White")
        self.AL_OPS_Display = ""
        self.AL_OPS = Game_Font.render(f"Overall Alchemy Lab OPS:{(1_600_000*float(OC['ALX']))*OC['ALAmount']}", True, "White")
        self.Portal_OPS_display = ""
        self.Portal_OPS = Game_Font.render(f"Overall Portal OPS:{(10_000_000*float(OC['PortalX']))*OC['PortalAmount']}", True, "White")
        self.TM_OPS_Display = ""
        self.TM_OPS = Game_Font.render(f"Overall Time Machine OPS:{(65_000_000*float(OC['TMX']))*OC['TMAmount']}", True, "White")
        self.AC_OPS_Display = ""
        self.AC_OPS = Game_Font.render(f"Overall Antimatter Condenser OPS:{(430_000_000*float(OC['ACX']))*OC['ACAmount']}", True, "White")
        self.Prism_OPS_Display = ""
        self.Prism_OPS = Game_Font.render(f"Overall Prism OPS:{(2_900_000_000* OC['PrismX'])*OC['PrismAmount']}", True, "White")
        self.CM_OPS_Display = ""
        self.CM_OPS = Game_Font.render(f"Overall ChanceMaker OPS:{(21_000_000_000*OC['ChanceMakerX'])*OC['ChanceMakerAmount']}", True, "White")
        self.FE_OPS_Display = ""
        self.FE_OPS = Game_Font.render(f"Overall Fractal Engine OPS:{(150_000_000_000* OC['FEX'])*OC['FEAmount']}", True, "White")
        self.PC_OPS_Display = ""
        self.PC_OPS = Game_Font.render(f"Overall Python Terminal OPS:{(1_100_000_000_000*OC['PCX'])*OC['PCAmount']}", True, "White")
        self.IV_OPS_Display = ""
        self.IV_OPS = Game_Font.render(f"Overall Idleverse OPS:{(8_300_000_000_000*OC['IVX'])*OC['IVAmount']}", True, "White")
        self.CB_OPS_Display = ""
        self.CB_OPS = Game_Font.render(f"Overall Cortex Baker OPS:{(64_000_000_000_000*OC['CBX'])*OC['CBAmount']}", True, "White")

        #Info
        self.Info = pygame.Surface((85,44))
        self.info = False
        self.Info.fill((165,84,42))
        self.Info_rect = self.Info.get_rect(topright = self.bar_rect.topright)
        self.Info_text = Game_Font.render("Info", True, "White")
        self.Info_text_rect = self.Info_text.get_rect(center = self.Info_rect.center)
        
        #InfoScreen
        self.InfoScreen = pygame.Surface((640,520))
        self.InfoScreen.fill("chocolate4")
        
        #InfoInfo
        self.Language = Game_Font.render("This game was made entirely in python w/ pygame", True, "White")
        self.Made = Game_Font.render("Oreo Clicker was made in 1/10/2023", True, "White")
        self.Credits = Game_Font.render("Inspired by Cookie Clicker", True, "White")
        self.Button = Game_Font.render("Press Shift to toggle Upgrades and Items", True, 'White')
        self.Buy = Game_Font.render("Green = Purchaseable, Red = Too High", True, "White")

        #Legacy
        self.Legacy = pygame.Surface((85,44))
        self.legacy = False
        self.Legacy.fill((165,84,42))
        self.Legacy_rect = self.Legacy.get_rect(bottomright = self.bar_rect.bottomright)
        self.Legacy_text = Game_Font.render("Legacy", True, "White")
        self.Legacy_text_rect = self.Legacy_text.get_rect(center = self.Legacy_rect.center)

        #LegacyScreen
        self.LegacyScreen = pygame.Surface((640,520))
        self.LegacyScreen.fill("chocolate4")

        #LegacyInfo
        self.AscendCost_text = Game_Font.render(f"${OC["AscendCost"] * (1.5**OC["AscendNum"])} to ascend", True, "White")
        self.AscendCost_rect = self.AscendCost_text.get_rect(topleft = (678,195))
        self.Ascend = pygame.Surface((100,44))
        self.Ascend.fill("chocolate4")
        self.Ascend_rect = self.Ascend.get_rect(topleft = (524,197))
        self.Ascend_text = Game_Font.render("Ascend", True, "White")
        self.Ascend_text_rect = self.Ascend_text.get_rect(center = self.Ascend_rect.center)

        self.pressed = False

    def Draw(self):
        SCREEN.blit(self.bar, self.bar_rect)
        self.CC_Display = self.NumberShrink(OC['Clicks'],self.CC_Display)
        SCREEN.blit(self.options, self.options_rect)
        SCREEN.blit(self.options_text, self.options_text_rect)
        SCREEN.blit(self.Stats, self.Stats_rect)
        SCREEN.blit(self.Stats_text, self.Stats_text_rect)
        SCREEN.blit(self.Info, self.Info_rect)
        SCREEN.blit(self.Info_text, self.Info_text_rect)
        SCREEN.blit(self.Legacy, self.Legacy_rect)
        SCREEN.blit(self.Legacy_text, self.Legacy_text_rect)
        self.Check_click_Options()
        self.OptionsInfo()
        self.Check_click_Stats()
        self.StatsInfo()
        self.Check_click_Info()
        self.InfoInfo()
        self.Check_click_Legacy()
        self.LegacyInfo()
        Ascend()
    
    def Check_click_Options(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.options_rect.collidepoint(mouse_pos) and not self.Stat and not self.info and not self.legacy:
            self.options.fill("Red")
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.option:
                        self.option = False
                    else: self.option = True; self.options.fill("Red")
                    self.pressed = False
        else:
            if not self.option: self.options.fill((165, 84, 42))
            else: self.options.fill("Red")
    
    def Time(self, Time):
        Time += 1
        OC['Time'] += 1
        self.mins, self.secs = divmod(Time, 60)
        self.Hours, self.mins = divmod(self.mins, 60)
        self.CountUp = '{:02d}:{:02d}:{:02d}'.format(self.Hours,self.mins, self.secs) 
        self.TotalTime = Game_Font.render(f"PlayTime:{self.CountUp}", True, "White")

    def Check_click_Stats(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Stats_rect.collidepoint(mouse_pos) and not self.option and not self.info and not self.legacy:
            self.Stats.fill("Red")
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.Stat:
                        self.Stat = False
                    else: self.Stat = True; self.Stats.fill("Red")
                    self.pressed = False
        else:
            if not self.Stat: self.Stats.fill((165, 84, 42))
            else: self.options.fill("Red")
    
    def Check_click_Info(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Info_rect.collidepoint(mouse_pos) and not self.option and not self.Stat and not self.legacy:
            self.Info.fill("Red")
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.info: self.info = False
                    else: self.info = True
                    self.pressed = False
        else:
            if not self.info: self.Info.fill((165, 84, 42))
            else: self.Info.fill("Red")
    
    def Check_click_Legacy(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Legacy_rect.collidepoint(mouse_pos) and not self.Stat and not self.info and not self.option:
            self.Legacy.fill("Red")
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.legacy:
                        self.legacy = False
                    else: self.legacy = True
                    self.pressed = False
        else:
            if not self.legacy: self.Legacy.fill((165,84,42))
            else: self.Legacy.fill("Red")

    def OptionsInfo(self):
        if self.option:
            SCREEN.blit(self.bar, self.bar_rect)
            SCREEN.blit(self.options, self.options_rect)
            SCREEN.blit(self.options_text, self.options_text_rect)
            SCREEN.blit(self.OptionButton1, self.OptionButton1_rect)
            SCREEN.blit(self.OptionButton1_text,self.OptionButton1_text_rect)
            SCREEN.blit(self.OptionButton2, self.OptionButton2_rect)
            SCREEN.blit(self.OptionButton2_text,self.OptionButton2_text_rect)
            mouse_pos = pygame.mouse.get_pos()
            if self.OptionButton1_rect.collidepoint(mouse_pos):
                self.OptionButton1.fill("Green")
                if pygame.mouse.get_pressed()[0]: self.pressed = True
                else:
                    if self.pressed:
                        with open('Cookie.txt', 'w') as score_file:
                            json.dump(OC,score_file) #First is the data we want to store, second is the file we want to store it 
                            self.OptionButton1.fill((0,255,83))
                            self.pressed = False
            else:
                self.OptionButton1.fill((165, 84, 42))
            
            if self.OptionButton2_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]: self.pressed = True
                else:
                    if self.pressed:
                        try:os.remove("Cookie.txt")
                        except: pass
                        self.pressed = False

    def StatsInfo(self):
        if self.Stat:
            SCREEN.blit(self.bar, self.bar_rect)
            SCREEN.blit(self.Stats, self.Stats_rect)
            SCREEN.blit(self.Stats_text, self.Stats_text_rect)
            SCREEN.blit(self.StatsScreen, (404,101))
            self.OC_Display = self.NumberShrink(OC['AllClicks'],self.OC_Display)
            self.CC_Display = self.NumberShrink(OC['Clicks'],self.CC_Display)
            self.HM_Display = self.NumberShrink(OC['HandMade'], self.HM_Display)
            self.AC_Display = self.NumberShrink(OC['ShopClicks'], self.AC_Display)
            self.CurrentClicks = Game_Font.render(f"Oreos in Bank:{self.CC_Display}", True, "White")
            self.OverallClicks = Game_Font.render(f"Oreos made (all time): {self.OC_Display}", True, "White")
            self.TotalTime = Game_Font.render(f"PlayTime:{self.CountUp}", True, "White")
            self.Handmade = Game_Font.render(f"Hand-made Oreos:{self.HM_Display}", True, "White")
            self.AutoClicks = Game_Font.render(f"Auto Clicks: {self.AC_Display}", True, "White")
            self.ItemAmount = Game_Font.render(f"Items Purchased: {OC['ItemAmount']}", True, "White")
            self.UpgradeAmount = Game_Font.render(f'Upgrade Purchase: {OC["UpgradeAmount"]}', True, "White")
            self.PC_OPS_Display = self.NumberShrink((1_100_000_000_000*OC['PCX'])*OC['PCAmount'],self.PC_OPS_Display)
            self.PC_OPS = Game_Font.render(f"Overall Python Terminal OPS:{self.PC_OPS_Display}", True, "White")
            if OC["AMADD"]: self.Cursor_OPS_Display = self.NumberShrink(round((0.1*float(OC['AMX']) + (OC['AMADDER']*OC['AMADDERX']))*OC['AMAmount'], 1), self.Cursor_OPS_Display)
            elif not OC["AMADD"]:self.Cursor_OPS_Display = self.NumberShrink(round((0.1*float(OC['AMX']))*OC['AMAmount'], 1), self.Cursor_OPS_Display)
            self.Cursor_OPS = Game_Font.render(f"Overall Mouse/Cursor OPS:{self.Cursor_OPS_Display}", True, "White")
            self.Grandma_OPS_Display = self.NumberShrink((1*OC['GrandX']) * OC['GrandAmount'],self.Grandma_OPS_Display)
            self.Grandma_OPS = Game_Font.render(f"Overall Grandma OPS:{self.Grandma_OPS_Display}", True, "White")
            self.Mine_OPS_Display = self.NumberShrink((47*OC['MineX'])* OC['MineAmount'], self.Mine_OPS_Display)
            self.CM_OPS_Display = self.NumberShrink((21_000_000_000*OC['ChanceMakerX'])*OC['ChanceMakerAmount'],self.CM_OPS_Display)
            self.CM_OPS = Game_Font.render(f"Overall ChanceMaker OPS:{self.CM_OPS_Display}", True, "White")
            self.AL_OPS_Display = self.NumberShrink((1_600_000*float(OC['ALX']))*OC['ALAmount'],self.AL_OPS_Display)
            self.AL_OPS = Game_Font.render(f"Overall Alchemy Lab OPS:{self.AL_OPS_Display}", True, "White")
            self.Prism_OPS_Display = self.NumberShrink((2_900_000_000* OC['PrismX'])*OC['PrismAmount'],self.Prism_OPS_Display)
            self.Prism_OPS = Game_Font.render(f"Overall Prism OPS:{self.Prism_OPS_Display}", True, "White")
            self.FE_OPS_Display = self.NumberShrink((150_000_000_000* OC['FEX'])*OC['FEAmount'],self.FE_OPS_Display)
            self.FE_OPS = Game_Font.render(f"Overall Fractal Engine OPS:{self.FE_OPS_Display}", True, "White")
            self.IV_OPS_Display = self.NumberShrink((8_300_000_000_000*OC['IVX'])*OC['IVAmount'],self.IV_OPS_Display)
            self.IV_OPS = Game_Font.render(f"Overall Idleverse OPS:{self.IV_OPS_Display}", True, "White")
            self.Farm_OPS_Display = self.NumberShrink((8*OC['FarmX'])* OC['FarmAmount'],self.Farm_OPS_Display)
            self.Farm_OPS = Game_Font.render(f"Overall Farm OPS:{self.Farm_OPS_Display}", True, "White")
            self.Portal_OPS_display = self.NumberShrink((10_000_000*OC['PortalX'])*OC['PortalAmount'],self.Portal_OPS_display)
            self.Portal_OPS = Game_Font.render(f"Overall Portal OPS:{self.Portal_OPS_display}", True, "White")
            self.Mine_OPS = Game_Font.render(f"Overall Mine OPS:{self.Mine_OPS_Display}", True, "White")
            self.Factory_OPS_Display = self.NumberShrink((260*OC['FactoryX'])*OC['FactoryAmount'],self.Factory_OPS_Display)
            self.Factory_OPS = Game_Font.render(f"Overall Factory OPS:{self.Factory_OPS_Display}",True,"White")
            self.Bank_OPS_Diplay = self.NumberShrink((1400*OC['BankX']) * OC['BankAmount'],self.Bank_OPS_Diplay)
            self.Bank_OPS = Game_Font.render(f"Overall Bank OPS:{self.Bank_OPS_Diplay}", True, "White")
            self.Temple_OPS_Display = self.NumberShrink((7800*OC['TempleX']) *OC['TempleAmount'],self.Temple_OPS_Display)
            self.Temple_OPS = Game_Font.render(f"Overall Temple OPS:{self.Temple_OPS_Display}", True, "White")
            self.WT_OPS_Dipsplay = self.NumberShrink((44_000*OC['WizardTowerX'])*OC['WizardTowerAmount'],self.WT_OPS_Dipsplay)
            self.WT_OPS = Game_Font.render(f"Overall Wizard Tower OPS:{self.WT_OPS_Dipsplay}", True, "White")
            self.SM_OPS_Display = self.NumberShrink((260_000*OC['ShipmentX'])*OC['ShipmentAmount'],self.SM_OPS_Display)
            self.SM_OPS = Game_Font.render(f"Overall Shipment OPS:{self.SM_OPS_Display}", True, "White")
            self.TM_OPS_Display = self.NumberShrink((65_000_000*OC['TMX'])*OC['TMAmount'],self.TM_OPS_Display)
            self.TM_OPS = Game_Font.render(f"Overall Time Machine OPS:{self.TM_OPS_Display}", True, "White")
            self.AC_OPS_Display = self.NumberShrink((430_000_000*OC['ACX'])*OC['ACAmount'],self.AC_OPS_Display)
            self.AC_OPS = Game_Font.render(f"Overall Antimatter OPS:{self.AC_OPS_Display}", True, "White")
            self.CB_OPS_Display = self.NumberShrink((64_000_000_000_000*OC['CBX'])*OC['CBAmount'],self.CB_OPS_Display)
            self.CB_OPS = Game_Font.render(f"Overall Cortex Baker OPS:{self.CB_OPS_Display}", True, "White")
            SCREEN.blit(self.CurrentClicks, (400,101))
            SCREEN.blit(self.OverallClicks,(400,130) )
            SCREEN.blit(self.TotalTime, (400,160))
            SCREEN.blit(self.Handmade, (400, 190))
            SCREEN.blit(self.AutoClicks, (400,220))
            SCREEN.blit(self.ItemAmount, (400, 250))
            SCREEN.blit(self.UpgradeAmount, (400, 280))
            if OC["AMAmount"]:SCREEN.blit(self.Cursor_OPS, (400, 310))
            if OC["GrandAmount"]: SCREEN.blit(self.Grandma_OPS, (400, 340))
            if OC["FarmAmount"]: SCREEN.blit(self.Farm_OPS, (400,370))
            if OC['MineAmount']: SCREEN.blit(self.Mine_OPS, (400,400))
            if OC["FactoryAmount"]: SCREEN.blit(self.Factory_OPS, (400,430))
            if OC["BankAmount"]: SCREEN.blit(self.Bank_OPS, (400,460))
            if OC["TempleAmount"]: SCREEN.blit(self.Temple_OPS, (400,490))
            if OC['WizardTowerAmount']: SCREEN.blit(self.WT_OPS, (400,520))
            if OC['ShipmentAmount']:SCREEN.blit(self.SM_OPS , (400,550))
            if OC['ALAmount']: SCREEN.blit(self.AL_OPS,(400,580))
            if OC["PortalAmount"]: SCREEN.blit(self.Portal_OPS, (630,101))
            if OC["TMAmount"]: SCREEN.blit(self.TM_OPS,(670,130))
            if OC['ACAmount']: SCREEN.blit(self.AC_OPS, (620,160))
            if OC['PrismAmount']: SCREEN.blit(self.Prism_OPS, (630,190))
            if OC['ChanceMakerAmount']:SCREEN.blit(self.CM_OPS, (630,220))
            if OC['FEAmount']: SCREEN.blit(self.FE_OPS, (630,250))
            if OC['PCAmount']: SCREEN.blit(self.PC_OPS,(650,280))
            if OC['IVAmount']: SCREEN.blit(self.IV_OPS,(680,340))
            if OC["CBAmount"]: SCREEN.blit(self.CB_OPS,(680,370))
    
    def InfoInfo(self):
        if self.info:
            SCREEN.blit(self.bar, self.bar_rect)
            SCREEN.blit(self.Info, self.Info_rect)
            SCREEN.blit(self.Info_text, self.Info_text_rect)
            SCREEN.blit(self.InfoScreen, (404,101))
            SCREEN.blit(self.Language, (450,101))
            SCREEN.blit(self.Made, (450, 140))
            SCREEN.blit(self.Credits, (450,180))
            SCREEN.blit(self.Button, (450,220))
            SCREEN.blit(self.Buy, (450,250))
    
    def LegacyInfo(self):
        global OC
        if self.legacy:
            SCREEN.blit(self.bar, self.bar_rect)
            SCREEN.blit(self.Legacy, self.Legacy_rect)
            SCREEN.blit(self.Legacy_text, self.Legacy_text_rect)
            SCREEN.blit(self.LegacyScreen, (404,101))
            SCREEN.blit(self.Ascend, self.Ascend_rect)
            SCREEN.blit(self.Ascend_text, self.Ascend_text_rect)
            SCREEN.blit(self.AscendCost_text, self.AscendCost_rect)
            mouse_pos = pygame.mouse.get_pos()
            if self.Ascend_rect.collidepoint(mouse_pos):
                self.Ascend.fill("Green")
                if pygame.mouse.get_pressed()[0]: self.pressed = True
                else:
                    if self.pressed:
                        if (OC["AscendCost"] * (1.5**OC["AscendNum"])) <= OC["Clicks"]:
                            OC["AscendNum"] += 1
                            x = OC["AscendNum"]
                            Ascend()
                            OC["AscendNum"] = x
                            try:os.remove("Cookie.txt")
                            except: pass
                            self.Ascend.fill((0,255,83))
                        self.pressed = False
            else:
                self.Ascend.fill((165, 84, 42))
    
    def NumberShrink(self,Number,Display):
        Number = str(Number)
        Zeros = len(Number)
        if Zeros < 4:return Number
        if Zeros >= 4 and (Zeros - 4) <= 2:
            Display = str(Number[0:1 + (Zeros - 4)]) + "K"
        if Zeros >= 7 and (Zeros - 7) <= 2:
            Display = str(Number[0:1 + (Zeros - 7)]) + "M"
        if Zeros >= 10 and (Zeros - 10) <= 2:
            Display = str(Number[0:1 + (Zeros - 10)]) + "B"
        if Zeros >= 13 and (Zeros - 13) <= 2:
            Display = str(Number[0:1 + (Zeros - 13)]) + "T"
        if Zeros >= 16 and (Zeros - 16) <= 2:
            Display = str(Number[0:1 + (Zeros - 16)]) + "Q"
        if Zeros >= 19 and (Zeros - 19) <= 2:
            Display = str(Number[0:1 + (Zeros - 19)]) + "QT"
        if Zeros >= 22 and (Zeros - 22) <= 2:
            Display = str(Number[0:1 + (Zeros - 22)]) + "S"
        if Zeros >= 25 and (Zeros - 25) <= 2:
            Display = str(Number[0:1 + (Zeros - 25)]) + "SepT"
        if Zeros >= 28 and (Zeros - 28) <= 2:
            Display = str(Number[0:1 + (Zeros - 28)]) + "O"
        if Zeros >= 31 and (Zeros - 31) <= 2:
            Display = str(Number[0:1 + (Zeros - 31)]) + "N"
        if Zeros >= 34 and (Zeros - 34) <= 2:
            Display = str(Number[0:1 + (Zeros - 34)]) + "D"
        if Zeros >= 37 and (Zeros - 37) <= 2:
            Display = str(Number[0:1 + (Zeros - 37)]) + "UND"
        if Zeros >= 40 and (Zeros - 40) <= 2:
            Display = str(Number[0:1 + (Zeros - 40)]) + "DuoD"
        if Zeros >= 43 and (Zeros - 43) <= 2:
            Display = str(Number[0:1 + (Zeros - 43)]) + "TreD"
        if Zeros >= 46 and (Zeros - 46) <= 2:
            Display = str(Number[0:1 + (Zeros - 46)]) + "QuattD"
        if Zeros >= 49 and (Zeros - 49) <= 2:
            Display = str(Number[0:1 + (Zeros - 49)]) + "QuinD"
        if Zeros >= 52 and (Zeros - 52) <= 2:
            Display = str(Number[0:1 + (Zeros - 52)]) + "SexD"
        if Zeros >= 55 and (Zeros - 55) <= 2:
            Display = str(Number[0:1 + (Zeros - 55)]) + "SepD"
        if Zeros >= 58 and (Zeros - 58) <= 2:
            Display = str(Number[0:1 + (Zeros - 58)]) + "OctD"
        if Zeros >= 61 and (Zeros - 61) <= 2:
            Display = str(Number[0:1 + (Zeros - 61)]) + "NoveD"
        if Zeros >= 64 and (Zeros - 64) <= 2:
            Display = str(Number[0:1 + (Zeros - 64)]) + "ViginT"
        if Zeros >= 67 and (Zeros - 67) <= 2:
            Display = str(Number[0:1 +(Zeros - 67)]) + "?????"
        if Zeros >= 70 and (Zeros - 70) <= 2:
            Display = str(Number[0:1 +(Zeros - 70)]) + "STOP"
        if Zeros >= 73 and (Zeros - 73) <= 2:
            Display = str(Number[0:1 +(Zeros - 73)]) + "Touch Grass!"
        for i in Number[1::]:
            if i != "0":
                Display += "+"
                break
        return Display