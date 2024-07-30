import pygame, json
pygame.init()
OC = {"Clicks": 0, "HandMade":0,"AllClicks": 0,"ItemAmount":0, "Time":0,"UpgradeAmount":0, "AMcost": 15,"Grandcost":100,"FarmAmount":0,"FarmCost":1100, "GrandAmount":0,"AMADD":False,"GrandmaUpgradecost":1000,"FarmX":1, "GrandX":1,"AMAmount":0,"AMADDER":0,"AMADDERX":1, "OPS":0, "ShopClicks":0, "AMX":1, "Autoupgrade":100,
"grandmaupgrade1cost":False,"grandmaupgrade2cost":False,"grandmaupgrade3cost":False,"grandmaupgrade4cost":False,"grandmaupgrade5cost":False,"grandmaupgrade6cost":False,"grandmaupgrade7cost":False,"grandmaupgrade8cost":False,"grandmaupgrade9cost":False,"grandmaupgrade10cost":False,"grandmaupgrade11cost":False,"grandmaupgrade12cost":False,
"grandmaupgrade13cost":False,"amupgrade1cost":False,"amupgrade2cost":False,"amupgrade3cost":False,"amupgrade4cost":False,"amupgrade5cost":False,"amupgrade6cost":False,"amupgrade7cost":False,"amupgrade8cost":False,"amupgrade9cost":False,"amupgrade10cost":False,"amupgrade11cost":False,"amupgrade12cost":False,"farmupgrade1cost":False,"farmupgrade2cost":False,
"farmupgrade3cost":False,"farmupgrade4cost":False,"farmupgrade5cost":False,"farmupgrade6cost":False,"farmupgrade7cost":False,"farmupgrade8cost":False,"farmupgrade9cost":False,"farmupgrade10cost":False,"farmupgrade11cost":False,"farmupgrade12cost":False,"farmupgrade13cost":False,"Farmupgradecost":11000, "MineCost":12_000, "MineAmount":0,"MineX":1,
"MineUpgradecost":120_000, "Mineupgrade1cost":False,"Mineupgrade2cost":False,"Mineupgrade3cost":False,"Mineupgrade4cost":False,"Mineupgrade5cost":False,"Mineupgrade6cost":False,"Mineupgrade7cost":False,"Mineupgrade8cost":False,"Mineupgrade9cost":False,"Mineupgrade10cost":False,"Mineupgrade11cost":False,"Mineupgrade12cost":False,"Mineupgrade13cost":False,
"FactoryCost":130_000,"FactoryAmount":0,"FactoryX":1,"FactoryupgradeCost":1_300_000,"factoryupgrade1Cost":False,"factoryupgrade2Cost":False,"factoryupgrade3Cost":False,"factoryupgrade4Cost":False,"factoryupgrade5Cost":False,"factoryupgrade6Cost":False,"factoryupgrade7Cost":False,"factoryupgrade8Cost":False,"factoryupgrade9Cost":False,"factoryupgrade10Cost":False,"factoryupgrade11Cost":False,
"factoryupgrade12Cost":False,"factoryupgrade13Cost":False, "BankCost":1_400_000, "BankAmount":0, "BankX":1,"BankUpgradeCost":14_000_000,"bankupgrade1cost":False,"bankupgrade2cost":False,"bankupgrade3cost":False,"bankupgrade4cost":False,"bankupgrade5cost":False,"bankupgrade6cost":False,"bankupgrade7cost":False,"bankupgrade8cost":False,"bankupgrade9cost":False,"bankupgrade10cost":False,"bankupgrade11cost":False,"bankupgrade12cost":False,"bankupgrade13cost":False,
"TempleAmount":0,"TempleX":1, "TempleCost":20_000_000, "TempleUpgradeCost":200_000_000, 'templeupgrade1cost':False,'templeupgrade2cost':False,'templeupgrade3cost':False,'templeupgrade4cost':False,'templeupgrade5cost':False,'templeupgrade6cost':False,'templeupgrade7cost':False,'templeupgrade8cost':False,'templeupgrade9cost':False,'templeupgrade10cost':False,'templeupgrade11cost':False,'templeupgrade12cost':False,'templeupgrade13cost':False, "WizardTowerCost":330_000_000,
"WizardTowerAmount":0,"WizardTowerX":1, "WizardTowerUpgradeCost":3_300_000_000, "WTUpgrade1Cost":False,"WTUpgrade2Cost":False,"WTUpgrade3Cost":False,"WTUpgrade4Cost":False,"WTUpgrade5Cost":False,"WTUpgrade6Cost":False,"WTUpgrade7Cost":False,"WTUpgrade8Cost":False,"WTUpgrade9Cost":False,"WTUpgrade10Cost":False,"WTUpgrade11Cost":False,"WTUpgrade12Cost":False,"WTUpgrade13Cost":False,"ShipmentCost":5_100_000_000, "ShipmentAmount":0, "ShipmentX":1,"ShipmentUpgradecost":51_000_000_000,
"Shipmentupgrade1cost":False,"Shipmentupgrade2cost":False,"Shipmentupgrade3cost":False,"Shipmentupgrade4cost":False,"Shipmentupgrade5cost":False,"Shipmentupgrade6cost":False,"Shipmentupgrade7cost":False,"Shipmentupgrade8cost":False,"Shipmentupgrade9cost":False,"Shipmentupgrade10cost":False,"Shipmentupgrade11cost":False,"Shipmentupgrade12cost":False,"Shipmentupgrade13cost":False, "ALCost":75_000_000_000, "ALAmount":0,"ALX":1, "ALUpgradeCost":750_000_000_000,"ALupgrade1cost":False,
"ALupgrade2cost":False,"ALupgrade3cost":False,"ALupgrade4cost":False,"ALupgrade5cost":False,"ALupgrade6cost":False,"ALupgrade7cost":False,"ALupgrade8cost":False,"ALupgrade9cost":False,"ALupgrade10cost":False,"ALupgrade11cost":False,"ALupgrade12cost":False,"ALupgrade13cost":False, "PortalCost":1_000_000_000_000, "PortalAmount":0, "PortalX":1,"PortalUpgradeCost":10_000_000_000_000,"portalupgrade1cost":False,"portalupgrade2cost":False,"portalupgrade3cost":False,
"portalupgrade4cost":False,"portalupgrade5cost":False,"portalupgrade6cost":False,"portalupgrade7cost":False,"portalupgrade8cost":False,"portalupgrade9cost":False,"portalupgrade10cost":False,"portalupgrade11cost":False,"portalupgrade12cost":False,"portalupgrade13cost":False,"TMCost":14_000_000_000_000, "TMAmount":0,"TMX":1,"TMUpgradecost":140_000_000_000_000,"TMupgrade1cost":False,"TMupgrade2cost":False,"TMupgrade3cost":False,"TMupgrade4cost":False,"TMupgrade5cost":False,"TMupgrade6cost":False,"TMupgrade7cost":False,"TMupgrade8cost":False,
"TMupgrade9cost":False,"TMupgrade10cost":False,"TMupgrade11cost":False,"TMupgrade12cost":False,"TMupgrade13cost":False,"ACAmount":0, "ACCost":170_000_000_000_000, "ACX":1, "ACUpgradecost":1_700_000_000_000_000, "ACUpgrade1cost":False,"ACUpgrade2cost":False,"ACUpgrade3cost":False,"ACUpgrade4cost":False,"ACUpgrade5cost":False,"ACUpgrade6cost":False,"ACUpgrade7cost":False,"ACUpgrade8cost":False,"ACUpgrade9cost":False,"ACUpgrade10cost":False,"ACUpgrade11cost":False,"ACUpgrade12cost":False,"ACUpgrade13cost":False, "PrismCost":2_100_000_000_000_000, "PrismX":1,"PrismAmount":0, "PrismUpgradecost":21_000_000_000_000_000_000,
"PrismUpgrade1cost":False,"PrismUpgrade2cost":False,"PrismUpgrade3cost":False,"PrismUpgrade4cost":False,"PrismUpgrade5cost":False,"PrismUpgrade6cost":False,"PrismUpgrade7cost":False,"PrismUpgrade8cost":False,"PrismUpgrade9cost":False,"PrismUpgrade10cost":False,"PrismUpgrade11cost":False,"PrismUpgrade12cost":False,"PrismUpgrade13cost":False,"ChanceMakerX":1,"ChanceMakerCost":26_000_000_000_000_000, "ChanceMakerAmount":0, "ChanceMakerUpgradeCost":260_000_000_000_000_000_000,"ChanceMakerUpgrade1Cost":False,"ChanceMakerUpgrade2Cost":False,"ChanceMakerUpgrade3Cost":False,"ChanceMakerUpgrade4Cost":False,"ChanceMakerUpgrade5Cost":False,"ChanceMakerUpgrade6Cost":False,"ChanceMakerUpgrade7Cost":False,"ChanceMakerUpgrade8Cost":False,"ChanceMakerUpgrade9Cost":False,
"ChanceMakerUpgrade10Cost":False,"ChanceMakerUpgrade11Cost":False,"ChanceMakerUpgrade12Cost":False,"ChanceMakerUpgrade13Cost":False,"FECost":310_000_000_000_000_000,"FEAmount":0,"FEX":1,"FEUpgradeCost":3_100_000_000_000_000_000, "FEUpgrade1Cost":False,"FEUpgrade2Cost":False,"FEUpgrade3Cost":False,"FEUpgrade4Cost":False,"FEUpgrade5Cost":False,"FEUpgrade6Cost":False,"FEUpgrade7Cost":False,"FEUpgrade8Cost":False,"FEUpgrade9Cost":False,"FEUpgrade10Cost":False,"FEUpgrade11Cost":False,"FEUpgrade12Cost":False,"FEUpgrade13Cost":False,"PCCost":71_000_000_000_000_000_000,"PCAmount":0,"PCX":1,"PCUpgradecost":710_000_000_000_000_000_000,"PCUpgrade1cost":False,"PCUpgrade2cost":False,"PCUpgrade3cost":False,"PCUpgrade4cost":False,"PCUpgrade5cost":False,"PCUpgrade6cost":False,
"PCUpgrade7cost":False,"PCUpgrade8cost":False,"PCUpgrade9cost":False,"PCUpgrade10cost":False,"PCUpgrade11cost":False,"PCUpgrade12cost":False,"PCUpgrade13cost":False,"IVCost":12_000_000_000_000_000_000_000,"IVAmount":0,"IVX":1,"IVUpgradeCost":120_000_000_000_000_000_000_000,"IVUpgrade1Cost":False,"IVUpgrade2Cost":False,"IVUpgrade3Cost":False,"IVUpgrade4Cost":False,"IVUpgrade5Cost":False,"IVUpgrade6Cost":False,"IVUpgrade7Cost":False,"IVUpgrade8Cost":False,"IVUpgrade9Cost":False,"IVUpgrade10Cost":False,"IVUpgrade11Cost":False,"IVUpgrade12Cost":False,"IVUpgrade13Cost":False,"CBCost":1_900_000_000_000_000_000_000_000, "CBX":1,"CBAmount":0,"CBUpgradeCost":19_000_000_000_000_000_000_000_000,"CBUpgrade1Cost":False,"CBUpgrade2Cost":False,"CBUpgrade3Cost":False,"CBUpgrade4Cost":False,"CBUpgrade5Cost":False,"CBUpgrade6Cost":False,
"CBUpgrade7Cost":False,"CBUpgrade8Cost":False,"CBUpgrade9Cost":False,"CBUpgrade10Cost":False,"CBUpgrade11Cost":False,"CBUpgrade12Cost":False,"CBUpgrade13Cost":False,"AscendCost":1_000_000,"AscendNum":0}
Width,Height = 1362, 615
SCREEN = pygame.display.set_mode((Width,Height))
Game_Font = pygame.font.SysFont('arial', 30, False, False)
BG1 = pygame.Surface((405,615))
BG1.fill((165, 42, 42))
BG1_Rect = BG1.get_rect(topleft = (0,0))
try:
    with open('Cookie.txt') as score_file: OC = json.load(score_file)
except:pass

class Cookie:
    def __init__(self):
        self.image = pygame.image.load("Images/Oreo.png").convert_alpha()
        self.rect = self.image.get_rect(center = BG1_Rect.center)
        self.x,self.y = self.rect.midtop
        self.pressed = False
        self.ClicksDisplay =""
        self.OPS_Display = ''
        self.ClicksDisplay = self.NumberShrink(OC['Clicks'], self.ClicksDisplay)
        self.Toptext = Game_Font.render(f"{self.ClicksDisplay} Oreos", True, "White")
        self.Toptext_rect = self.Toptext.get_rect(center = (self.x,self.y - 50))
        self.Bottomtext = Game_Font.render(f"{OC['OPS']} Oreos per second", True, "White")
        self.Bottomtext_rect = self.Bottomtext.get_rect(center = (self.x, self.y - 25))
    
    def Draw(self):
        BG1.blit(self.image,self.rect)
        self.ClicksDisplay = self.NumberShrink(OC['Clicks'], self.ClicksDisplay)
        SCREEN.blit(self.Toptext, self.Toptext_rect) #So the text wont be overlapping when clicked
        SCREEN.blit(self.Bottomtext, self.Bottomtext_rect)

        if OC["AMADD"]: OC['OPS'] = (0.1*float(OC['AMX']) + (OC['AMADDER']*OC['AMADDERX'])*OC['AMAmount']) + ((1*float(OC['GrandX'])) * OC['GrandAmount']) + (8*float(OC['FarmX'])* OC['FarmAmount']) + (47*float(OC['MineX'])* OC['MineAmount']) + (260*float(OC['FactoryX'])*OC['FactoryAmount']) + (1400*float(OC['BankX']) * OC['BankAmount']) + (7800*float(OC['TempleX']) *OC['TempleAmount']) + (44_000*float(OC['WizardTowerX'])*OC['WizardTowerAmount']) + (260_000*float(OC['ShipmentX'])*OC['ShipmentAmount']) + ((1_600_000*float(OC['ALX']))*OC['ALAmount']) + ((10_000_000*float(OC['PortalX']))*OC['PortalAmount']) + ((430_000_000*float(OC['ACX']))*OC['ACAmount']) + ((65_000_000*float(OC['TMX']))*OC['TMAmount']) + ((2_900_000_000* OC['PrismX'])*OC['PrismAmount']) + ((21_000_000_000*OC["ChanceMakerX"])*OC['ChanceMakerAmount']) + ((150_000_000_000* OC['FEX'])*OC['FEAmount']) + ((1_100_000_000_000*OC['PCX'])*OC['PCAmount']) + ((8_300_000_000_000*OC['IVX'])*OC['IVAmount']) + ((64_000_000_000_000*OC['CBX'])*OC['CBAmount'])
        elif not OC["AMADD"]: OC['OPS'] = (0.1*float(OC['AMX'])*OC['AMAmount']) + ((1*float(OC['GrandX'])) * OC['GrandAmount']) + (8*float(OC['FarmX'])* OC['FarmAmount']) + (47*float(OC['MineX'])* OC['MineAmount']) + (260*float(OC['FactoryX'])*OC['FactoryAmount']) + (1400*float(OC['BankX']) * OC['BankAmount']) + (7800*float(OC['TempleX']) *OC['TempleAmount']) + (44_000*float(OC['WizardTowerX'])*OC['WizardTowerAmount']) + (260_000*float(OC['ShipmentX'])*OC['ShipmentAmount']) + ((1_600_000*float(OC['ALX']))*OC['ALAmount']) + ((10_000_000*float(OC['PortalX']))*OC['PortalAmount']) + ((430_000_000*float(OC['ACX']))*OC['ACAmount']) + ((65_000_000*float(OC['TMX']))*OC['TMAmount']) + ((2_900_000_000* OC['PrismX'])*OC['PrismAmount']) + ((21_000_000_000*OC["ChanceMakerX"])*OC['ChanceMakerAmount']) + ((150_000_000_000* OC['FEX'])*OC['FEAmount']) + ((1_100_000_000_000*OC['PCX'])*OC['PCAmount']) + ((8_300_000_000_000*OC['IVX'])*OC['IVAmount']) + ((64_000_000_000_000*OC['CBX'])*OC['CBAmount'])
        OC['OPS'] = round(OC['OPS'],1)
        self.OPS_Display = self.NumberShrink(OC['OPS'],self.OPS_Display)
        self.Bottomtext = Game_Font.render(f"{self.OPS_Display} Oreos per second", True, "White")
        if OC['OPS'] < 0:
            OC['OPS'] = 0
        self.Toptext = Game_Font.render(f"{self.ClicksDisplay} Oreos", True, "White")
        self.Check_Clicks()
    
    def Check_Clicks(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if OC["AMADD"]:
                        OC['Clicks'] += (1*OC["AMX"]) + (OC["AMADDER"]*OC["AMADDERX"])
                        OC["AllClicks"] += (1*OC["AMX"]) + (OC["AMADDER"]*OC["AMADDERX"])
                        OC["HandMade"] += (1*OC["AMX"]) + (OC["AMADDER"]*OC["AMADDERX"])
                    elif not OC["AMADD"]:
                        OC['Clicks'] += (1*OC["AMX"])
                        OC["AllClicks"] +=(1*OC["AMX"])
                        OC["HandMade"] += (1*OC["AMX"])
                    self.ClicksDisplay = self.NumberShrink(OC['Clicks'], self.ClicksDisplay)
                    self.Toptext = Game_Font.render(f"{self.ClicksDisplay} Oreos", True, "White")
                    self.pressed = False
   
    def NumberShrink(self, Number, Display):
        Number = str(Number)
        Zeros = len(Number)
        if Zeros <= 6:return Number
        # if Zeros >= 4 and (Zeros - 4) <= 2:
        #     Display = str(Number[0:1 + (Zeros - 4)]) + "K"
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