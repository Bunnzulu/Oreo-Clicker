import pygame, math
from Oreo import *
from Menu_Screen import *
pygame.init()
BG3 = pygame.Surface((318,615))
BG3.fill((205, 127, 50))
BG3_rect = BG3.get_rect(topleft = (1042,0))
Store_font = pygame.font.SysFont('arial', 15, False, False)
Test_Font = pygame.font.SysFont("arial", 20, True, False)
class Upgrades:
    def __init__(self):
        self.Title = Game_Font.render("Store", True, "White")
        self.Storeops = pygame.Surface((320, 100))
        self.Storeops.fill((165, 84, 42))
        self.Storeops_rect = self.Storeops.get_rect(center = (1201,100))
        self.pressed = False
        
        #Store settings
        self.Buy = pygame.Surface((84,44))
        self.Buy_color = "White"
        self.Buy.fill((165, 84, 42))
        self.Buy_rect = self.Buy.get_rect(topleft = self.Storeops_rect.topleft)
        self.Buy_Text = Game_Font.render("Buy", True, self.Buy_color)
        self.Buy_text_rect = self.Buy_Text.get_rect(center = self.Buy_rect.center)
        self.buy = True

        self.Sell = pygame.Surface((84,44))
        self.Sell.fill((165, 84, 42))
        self.Sell_color = "Black"
        self.Sell_rect = self.Sell.get_rect(bottomleft = self.Storeops_rect.bottomleft)
        self.Sell_Text = Game_Font.render("Sell", True, self.Sell_color)
        self.Sell_Text_rect = self.Sell_Text.get_rect(center = self.Sell_rect.center)
        self.sell = False

        self.X1 = pygame.Surface((84,44))
        self.X1.fill((165,84,42))
        self.Amountcolor1 = "Black"
        self.X1_rect = self.X1.get_rect(center = (1150,72))
        self.X1_Text = Game_Font.render("1", True, self.Amountcolor1)
        self.X1_Text_Rect = self.X1_Text.get_rect(center = self.X1_rect.center)
        self.x1 = True

        self.X10 = pygame.Surface((84,44))
        self.X10.fill((165,84,42))
        self.Amountcolor10 = "Black"
        self.X10_rect = self.X10.get_rect(center = (1200,72))
        self.X10_text = Game_Font.render("10", True, self.Amountcolor10)
        self.X10_text_rect = self.X10_text.get_rect(center = self.X10_rect.center)
        self.x10 = False

        self.X100 = pygame.Surface((84,44))
        self.X100.fill((165,84,42))
        self.Amountcolor100 = "Black"
        self.X100_rect = self.X100.get_rect(center = (1270,72))
        self.X100_text = Game_Font.render("100", True, self.Amountcolor100)
        self.X100_text_rect = self.X100_text.get_rect(center = self.X100_rect.center)
        self.x100 = False
        self.Upgrades = False

        self.AutoMousecost,self.AMDisplayCost = OC["AMcost"], ""
        self.AMColor = self.NumberCheck(OC["Clicks"],self.AutoMousecost)
        self.AMDisplayCost = self.NumberShrink(self.AutoMousecost, self.AMDisplayCost)
        self.AutoCount = 0
        self.AutoMousecostx10, self.AutoMousecostx100 ="",""
        self.AutoMouse_surf = pygame.Surface((64,44))
        self.AutoMouse_surf.fill((205, 127, 100))
        self.AutoMouse_rect = self.AutoMouse_surf.get_rect(topleft = self.Storeops_rect.bottomleft)
        self.AutoMouse_amount_text = Store_font.render(str(OC["AMAmount"]), True, "Black")
        self.AutoMouse_amount_rect = self.AutoMouse_amount_text.get_rect(topleft = self.AutoMouse_rect.topleft)
        self.AutoMouse_Cost_text = Test_Font.render(str(self.AMDisplayCost), True, self.AMColor)
        self.AutoMouse_Cost_text_rect = self.AutoMouse_Cost_text.get_rect(bottomleft = self.AutoMouse_rect.bottomleft)
        self.AutoMouse_image = pygame.image.load("Images/AutoMouse.png").convert_alpha()
        self.AutoMouse_image = pygame.transform.rotozoom(self.AutoMouse_image, 360, 1/7)
        self.AutoMouse_image_rect = self.AutoMouse_image.get_rect(topright = self.AutoMouse_rect.topright)
        self.AMSell = round(self.AutoMousecost/4)
        self.AMDisplay_Text = OC["Autoupgrade"]
        self.AMUpgrade1cost_text = Test_Font.render(str(self.AMDisplay_Text), True, "Blue")
        self.AMName = Store_font.render("Automouse", True, "Black")

        self.GrandmaCost,self.GrandCostDisplay = OC["Grandcost"],""
        self.GrandCostDisplay = self.NumberShrink(self.GrandmaCost, self.GrandCostDisplay)
        self.GrandColor = self.NumberCheck(OC["Clicks"],self.GrandmaCost)
        self.Grandcount = 0
        self.GrandmaCostx10,self.GrandmaCostx100 = "",""
        self.Grandma_surf = pygame.Surface((64,44))
        self.Grandma_surf.fill((205, 127, 100))
        self.Grandma_rect = self.Grandma_surf.get_rect(center = (1177,172))
        self.Grandma_amount_text = Store_font.render(str(OC["GrandAmount"]), True, "Black")
        self.Grandma_amount_rect = self.Grandma_amount_text.get_rect(topleft = self.Grandma_rect.topleft)
        self.Grandma_Cost_text = Test_Font.render(str(self.GrandCostDisplay), True, self.GrandColor)
        self.Grandma_Cost_rect = self.Grandma_Cost_text.get_rect(bottomleft = self.Grandma_rect.bottomleft)
        self.Grandma_image = pygame.image.load("Images/Grandma.png").convert_alpha()
        self.Grandma_image = pygame.transform.rotozoom(self.Grandma_image, 360, 1/20)
        self.Grandma_image_rect = self.Grandma_image.get_rect(topright = self.Grandma_rect.topright)
        self.GrandSell = round(self.GrandmaCost/4)
        self.GranddisplayText = OC["GrandmaUpgradecost"]
        self.GrandmaUpgrade_text = Test_Font.render(str(self.GranddisplayText), True, "Blue")
        self.GrandName = Store_font.render("Grandma", True, "Black")

        self.Farm_surf = pygame.Surface((64,44))
        self.Farm_surf.fill((205,127,100))
        self.Farm_rect = self.Farm_surf.get_rect(center = (1273,172))
        self.FarmCount = 0
        self.FarmCost,self.FarmCostDisplay = OC["FarmCost"],""
        self.FarmColor = self.NumberCheck(OC["Clicks"], self.FarmCost)
        self.FarmCostx10,self.FarmCostx100 = "",""
        self.FarmSellx10,self.FarmSellx100 = "",""
        self.FarmSell = round(OC["FarmCost"]/4)
        self.FarmAmount_text = Store_font.render(str(OC["FarmAmount"]), True, "Black")
        self.FarmAmount_rect = self.FarmAmount_text.get_rect(topleft = self.Farm_rect.topleft)
        self.FarmCostDisplay = self.NumberShrink(self.FarmCost, self.FarmCostDisplay)
        self.Farm_Cost_text = Test_Font.render(str(self.FarmCostDisplay), True, self.FarmColor)
        self.Farm_Cost_rect = self.Farm_Cost_text.get_rect(bottomleft = self.Farm_rect.bottomleft)
        self.Farm_image = pygame.image.load("Images/Farm.png").convert_alpha()
        self.Farm_image = pygame.transform.rotozoom(self.Farm_image,360,1/3)
        self.Farm_image_rect = self.Farm_image.get_rect(topright = self.Farm_rect.topright)
        self.FarmDisplaycost = OC["Farmupgradecost"]
        self.FarmUpgrade_text = Test_Font.render(str(self.FarmDisplaycost), True, "Blue")
        self.FarmName = Store_font.render("Farm", True, "Black")

        self.Mine_surf = pygame.Surface((64,44))
        self.Mine_surf.fill((205,127,100))
        self.Mine_image = pygame.image.load("Images/Mine.png").convert_alpha()
        self.Mine_image = pygame.transform.rotozoom(self.Mine_image, 360, 1/2)
        self.Mine_rect = self.Mine_surf.get_rect(topleft = (1041,214))
        self.Mine_image_rect = self.Mine_image.get_rect(topright = (1120,210))
        self.MineCost,self.MineCostDisplay  = OC["MineCost"],""
        self.MineColor = self.NumberCheck(OC["Clicks"], self.MineCost)
        self.MineCostDisplay = self.NumberShrink(self.MineCost,self.MineCostDisplay)
        self.MineCost_text = Test_Font.render(str(self.MineCostDisplay), True, self.MineColor)
        self.MineCost_rect = self.MineCost_text.get_rect(bottomleft = self.Mine_rect.bottomleft)
        self.MineAmount_Text = Store_font.render(str(OC["MineAmount"]), True, "Black")
        self.MineAmount_rect = self.MineAmount_Text.get_rect(topleft = self.Mine_rect.topleft)
        self.MineCostx10,self.MineCostx100 = "",""
        self.MineSell = round(OC["MineCost"]/4)
        self.MineCount = 0
        self.MineSellx10,self.MineSellx100 = "",""
        self.MineUpgradecost = OC["MineUpgradecost"]
        self.MineUpgrade_tect = Test_Font.render(str(self.MineUpgradecost),True,"Blue")
        self.MineName = Store_font.render("Mine", True, "Black")

        self.Factory_surf = pygame.Surface((64,44))
        self.Factory_surf.fill((205,127,100))
        self.FactoryCount = 0
        self.Factory_image = pygame.image.load("Images/Factory.png").convert_alpha()
        self.Factory_image = pygame.transform.rotozoom(self.Factory_image, 360, 1/2)
        self.Factory_rect = self.Factory_surf.get_rect(center = (1177,235))
        self.Factory_image_rect = self.Factory_image.get_rect(topright = (1230,200))
        self.FactoryCost,self.FactoryCostDisplay = OC["FactoryCost"],""
        self.FactoryColor = self.NumberCheck(OC["Clicks"],self.FactoryCost)
        self.FactoryCostx10,self.FactoryCostx100 = "",""
        self.FactorySellx10,self.FactorySellx100 = "",""
        self.FactoryCostDisplay = self.NumberShrink(self.FactoryCost,self.FactoryCostDisplay)
        self.FactoryCost_text = Test_Font.render(str(self.FactoryCostDisplay), True, self.FactoryColor)
        self.FactoryCost_rect = self.FactoryCost_text.get_rect(bottomleft = self.Factory_rect.bottomleft)
        self.FactoryAmount_Text = Store_font.render(str(OC["FactoryAmount"]), True, "Black")
        self.FactoryAmount_rect = self.FactoryAmount_Text.get_rect(topleft = self.Factory_rect.topleft)
        self.FactorySell = round(OC["FactoryCost"]/4)
        self.FactoryUpgradeCost = OC["FactoryupgradeCost"]
        self.FactoryUpgrade_text = Test_Font.render(str(self.FactoryUpgradeCost), True, "Blue")
        self.FactName = Store_font.render("Factory", True, "Black")

        self.Bank_surf = pygame.Surface((64,44))
        self.Bank_surf.fill((205,127,100))
        self.BankCount = 0
        self.Bank_rect = self.Bank_surf.get_rect(center = (1271,235))
        self.Bank_image = pygame.image.load("Images/Bank.png").convert_alpha()
        self.Bank_image = pygame.transform.rotozoom(self.Bank_image, 360, 1/2)
        self.Bank_image_rect = self.Bank_image.get_rect(topright = (1323,203))
        self.BankCost, self.BankCostDisplay = OC["BankCost"],""
        self.BankColor = self.NumberCheck(OC["Clicks"],self.BankCost)
        self.BankCostx10,self.BankCostx100 = "",""
        self.BankSellx10,self.BankSellx100 = "",""
        self.BankCostDisplay = self.NumberShrink(self.BankCost,self.BankCostDisplay)
        self.BankCost_text = Test_Font.render(str(self.BankCostDisplay), True, self.BankColor)
        self.BankCost_rect = self.BankCost_text.get_rect(bottomleft = self.Bank_rect.bottomleft)
        self.BankAmount_text = Store_font.render(str(OC["BankAmount"]), True, "Black")
        self.BankAmount_rect = self.BankAmount_text.get_rect(topleft = self.Bank_rect.topleft)
        self.BankSell = round(OC["BankAmount"]/4)
        self.BankUpgradeCost = OC["BankUpgradeCost"]
        self.BankUpgrade_text = Test_Font.render(str(self.BankUpgradeCost), True, "Blue")
        self.BankName = Store_font.render("Bank", True, "Black")

        self.Temple_surf = pygame.Surface((64,44))
        self.Temple_surf.fill((205,127,100))
        self.TempleCount = 0
        self.Temple_rect = self.Temple_surf.get_rect(center = (1073,300))
        self.Temple_image = pygame.image.load("Images/Temple.png").convert_alpha()
        self.Temple_image = pygame.transform.rotozoom(self.Temple_image, 360, 1/2)
        self.Temple_image_rect = self.Temple_image.get_rect(topright = (1105,270))
        self.TempleCost,self.TempleCostDisplay = OC["TempleCost"],""
        self.TempleColor = self.NumberCheck(OC["Clicks"], self.TempleCost)
        self.TempleCostDisplay = self.NumberShrink(self.TempleCost, self.TempleCostDisplay)
        self.TempleCost_text = Test_Font.render(str(self.TempleCostDisplay), True, self.TempleColor)
        self.TempleCost_rect = self.TempleCost_text.get_rect(bottomleft = self.Temple_rect.bottomleft)
        self.TempleAmount_Text = Store_font.render(str(OC["TempleAmount"]), True, "Black")
        self.TempleAmount_rect = self.TempleAmount_Text.get_rect(topleft = self.Temple_rect.topleft)
        self.TempleSell = round(self.TempleCost/4)
        self.TempleCostx10, self.TempleCostx100 = "",''
        self.TempleSellx10,self.TempleSellx100 = "",''
        self.TempleUpgradeCost = OC["TempleUpgradeCost"]
        self.TempleUpgrade_text = Test_Font.render(str(self.TempleUpgradeCost), True, "Blue")
        self.TempleName = Store_font.render("Temple", True, "Black")

        self.Wizard_Tower_surf = pygame.Surface((64,44))
        self.Wizard_Tower_surf.fill((205,127,100))
        self.Wizard_Tower_rect = self.Wizard_Tower_surf.get_rect(center = (1177,300))
        self.WT_image = pygame.image.load("Images/Wizard_Tower.png").convert_alpha()
        self.WT_image = pygame.transform.rotozoom(self.WT_image,360,1/2)
        self.WT_image_rect = self.WT_image.get_rect(topright = (1218,270))
        self.WTCount = 0
        self.WTCost, self.WTCostDisplay = OC["WizardTowerCost"],""
        self.WTColor = self.NumberCheck(OC["Clicks"],self.WTCost)
        self.WTCostDisplay = self.NumberShrink(self.WTCost, self.WTCostDisplay)
        self.WTCost_text = Test_Font.render(str(self.WTCostDisplay), True, self.WTColor)
        self.WTCost_rect = self.WTCost_text.get_rect(bottomleft = self.Wizard_Tower_rect.bottomleft)
        self.WTAmount_Text = Store_font.render(str(OC["WizardTowerAmount"]), True, "Black")
        self.WTAmount_rect = self.WTAmount_Text.get_rect(topleft = self.Wizard_Tower_rect.topleft)
        self.WTSell = round(OC["WizardTowerCost"]/4)
        self.WTCostx10,self.WTCostx100 = "",""
        self.WTSellx10,self.WTSellx100 = "",""
        self.WTUpgradeCost = "3.3B"
        self.WTUpgrade_Text = Test_Font.render(str(self.WTUpgradeCost),True,"Blue")
        self.WTName = Store_font.render("Wizard Tower", True, "Black")

        self.Shipment_surf = pygame.Surface((64,44))
        self.Shipment_surf.fill((205,127,100))
        self.Shipment_rect = self.Shipment_surf.get_rect(center = (1271,300))
        self.Shipment_image = pygame.image.load("Images/Shipment.png").convert_alpha()
        self.Shipment_image = pygame.transform.rotozoom(self.Shipment_image, 360, 1/2)
        self.Shipment_image_rect = self.Shipment_image.get_rect(topright = self.Shipment_rect.topright)
        self.ShipmentCount = 0
        self.ShipmentCost, self.ShipmentCostDisplay = OC["ShipmentCost"],""
        self.ShipmentColor = self.NumberCheck(OC["Clicks"],self.ShipmentCost)
        self.ShipmentCostDisplay = self.NumberShrink(self.ShipmentCost,self.ShipmentCostDisplay)
        self.ShipmentCost_Text = Test_Font.render(str(self.ShipmentCostDisplay), True, self.ShipmentColor)
        self.ShipmentCost_rect = self.ShipmentCost_Text.get_rect(bottomleft = self.Shipment_rect.bottomleft)
        self.ShipmentAmount_text = Store_font.render(str(OC["ShipmentAmount"]), True, "Black")
        self.ShipmentAmount_rect = self.ShipmentAmount_text.get_rect(topleft = self.Shipment_rect.topleft)
        self.ShipmentSell = round(OC["ShipmentCost"]/4)
        self.ShipmentCostx10,self.ShipmentCostx100 = "",""
        self.ShipmentSellx10,self.ShipmentSellx100 = "",""
        self.ShipmentUpgradeCost = "51B"
        self.ShipmentUpgradeCost_Text = Test_Font.render(str(self.ShipmentUpgradeCost),True,"Blue")
        self.ShipName = Store_font.render("Shipment", True, "Black")

        self.AL_surf = pygame.Surface((64,44))
        self.AL_surf.fill((205,127,100))
        self.AL_rect = self.AL_surf.get_rect(center = (1074,360))
        self.AL_image = pygame.image.load(r"Images/Alchemy_Lab.png").convert_alpha()
        self.AL_image = pygame.transform.rotozoom(self.AL_image, 360, 1/2)
        self.AL_image_rect = self.AL_image.get_rect(topright = (1106,330))
        self.ALCount = 0
        self.ALCost, self.ALCostDisplay = OC["ALCost"],""
        self.ALColor = self.NumberCheck(OC["Clicks"], self.ALCost)
        self.ALCostDisplay = self.NumberShrink(self.ALCost, self.ALCostDisplay)
        self.ALCost_text = Test_Font.render(str(self.ALCostDisplay), True, self.ALColor)
        self.ALCost_rect = self.ALCost_text.get_rect(bottomleft = self.AL_rect.bottomleft)
        self.ALAmount_text = Store_font.render(str(OC["ALAmount"]), True, "Black")
        self.ALAmount_rect = self.ALAmount_text.get_rect(topleft = self.AL_rect.topleft)
        self.ALSell = round(OC["ALCost"]/4)
        self.ALCostx10, self.ALCostx100 = "",""
        self.ALSellx10,self.ALSellx100 = "",""
        self.ALUpgradeCost = "750B"
        self.ALUpgradeCost_text = Test_Font.render(str(self.ALUpgradeCost), True, "Blue")
        self.ALName = Store_font.render("Alchemy Lab", True, "Black")

        self.Portal_Surf = pygame.Surface((64,44))
        self.Portal_Surf.fill((205,127,100))
        self.Portal_rect = self.Portal_Surf.get_rect(center = (1178,360))
        self.Portal_image = pygame.image.load(r"Images/Portal.png").convert_alpha()
        self.Portal_image = pygame.transform.rotozoom(self.Portal_image,360,1/2)
        self.Portal_image_rect = self.Portal_image.get_rect(topright = (1210,338))
        self.PortalCount = 0
        self.PortalCost,self.PortalCostDisplay = OC["PortalCost"],""
        self.PortalColor = self.NumberCheck(OC["Clicks"],self.PortalCost)
        self.PortalCostDisplay = self.NumberShrink(self.PortalCost, self.PortalCostDisplay)
        self.PortalCost_text = Test_Font.render(str(self.PortalCostDisplay), True, self.PortalColor)
        self.PortalCost_rect = self.PortalCost_text.get_rect(bottomleft = self.Portal_rect.bottomleft)
        self.PortalAmount_Text = Store_font.render(str(OC["PortalAmount"]), True, "Black")
        self.PortalAmount_rect = self.PortalAmount_Text.get_rect(topleft = self.Portal_rect.topleft)
        self.PortalSell = round(OC["PortalCost"]/4)
        self.PortalCostx10,self.PortalCostx100 = "",""
        self.PortalSellx10,self.PortalSellx100 = "",""
        self.PortalUpgradeCost = "10T"
        self.PortalUpgradeCost_text = Test_Font.render(str(self.PortalUpgradeCost), True, "Blue")
        self.PortalName = Store_font.render("Portal", True, "Black")

        self.TM_Surf = pygame.Surface((64,44))
        self.TM_Surf.fill((205,127,100))
        self.TM_rect = self.TM_Surf.get_rect(center = (1271,360))
        self.TM_image = pygame.image.load("Images/Time_Machine.png").convert_alpha()
        self.TM_image = pygame.transform.rotozoom(self.TM_image,360,1/2)
        self.TM_image_rect = self.TM_image.get_rect(topright = self.TM_rect.topright)
        self.TMCount = 0
        self.TMCost,self.TMCostDisplay = OC["TMCost"],""
        self.TMColor = self.NumberCheck(OC["Clicks"],self.TMCost)
        self.TMCostDisplay = self.NumberShrink(self.TMCost, self.TMCostDisplay)
        self.TMCost_text = Test_Font.render(str(self.TMCostDisplay), True, self.PortalColor)
        self.TMCost_rect = self.TMCost_text.get_rect(bottomleft = self.TM_rect.bottomleft)
        self.TMAmount_Text = Store_font.render(str(OC["TMAmount"]), True, "Black")
        self.TMAmount_rect = self.TMAmount_Text.get_rect(topleft = self.TM_rect.topleft)
        self.TMSell = round(OC["TMCost"]/4)
        self.TMCostx10,self.TMCostx100 = "",""
        self.TMSellx10,self.TMSellx100 = "",""
        self.TMUpgradeCost = "140T"
        self.TMUpgradeCost_text = Test_Font.render(str(self.TMUpgradeCost), True, "Blue")
        self.TMName = Store_font.render("Time Machine", True, "Black")

        self.AC_Surf = pygame.Surface((64,44))
        self.AC_Surf.fill((205,127,100))
        self.AC_rect = self.AC_Surf.get_rect(center = (1074,420))
        self.AC_image = pygame.image.load("Images/Antimatter_Condenser.png").convert_alpha()
        self.AC_image = pygame.transform.rotozoom(self.AC_image,360,1/4)
        self.AC_image_rect = self.AC_image.get_rect(topright = self.AC_rect.topright)
        self.ACCount = 0
        self.ACCost,self.ACCostDisplay = OC["ACCost"],""
        self.ACColor = self.NumberCheck(OC["Clicks"],self.ACCost)
        self.ACCostDisplay = self.NumberShrink(self.ACCost, self.ACCostDisplay)
        self.ACCost_text = Test_Font.render(str(self.ACCostDisplay), True, self.ACColor)
        self.ACCost_rect = self.ACCost_text.get_rect(bottomleft = self.AC_rect.bottomleft)
        self.ACAmount_Text = Store_font.render(str(OC["ACAmount"]), True, "Black")
        self.ACAmount_rect = self.ACAmount_Text.get_rect(topleft = self.AC_rect.topleft)
        self.ACSell = round(OC["ACCost"]/4)
        self.ACCostx10,self.ACCostx100 = "",""
        self.ACSellx10,self.ACSellx100 = "",""
        self.ACUpgradeCost = "1.7Q"
        self.ACUpgradeCost_text = Test_Font.render(str(self.ACUpgradeCost), True, "Blue")
        self.ACName = Store_font.render("Antimatter", True, "Black")

        self.Prism_Surf = pygame.Surface((64,44))
        self.Prism_Surf.fill((205,127,100))
        self.Prism_rect = self.Prism_Surf.get_rect(center = (1178,420))
        self.Prism_image = pygame.image.load("Images/Prism.png").convert_alpha()
        self.Prism_image = pygame.transform.rotozoom(self.Prism_image,360,1/2)
        self.Prism_image_rect = self.Prism_image.get_rect(topright = self.Prism_rect.topright)
        self.PrismCount = 0
        self.PrismCost,self.PrismCostDisplay = OC["PrismCost"],""
        self.PrismColor = self.NumberCheck(OC["Clicks"],self.PrismCost)
        self.PrismCostDisplay = self.NumberShrink(self.PrismCost, self.PrismCostDisplay)
        self.PrismCost_text = Test_Font.render(str(self.PrismCostDisplay), True, self.PrismColor)
        self.PrismCost_rect = self.PrismCost_text.get_rect(bottomleft = self.Prism_rect.bottomleft)
        self.PrismAmount_Text = Store_font.render(str(OC["PrismAmount"]), True, "Black")
        self.PrismAmount_rect = self.PrismAmount_Text.get_rect(topleft = self.Prism_rect.topleft)
        self.PrismSell = round(OC["PrismCost"]/4)
        self.PrismCostx10,self.PrismCostx100 = "",""
        self.PrismSellx10,self.PrismSellx100 = "",""
        self.PrismUpgradeCost = "21Q"
        self.PrismUpgradeCost_text = Test_Font.render(str(self.PrismUpgradeCost), True, "Blue")
        self.PrismName = Store_font.render("Prism", True, "Black")

        self.ChanceMaker_Surf = pygame.Surface((64,44))
        self.ChanceMaker_Surf.fill((205,127,100))
        self.ChanceMaker_rect = self.ChanceMaker_Surf.get_rect(center = (1271,420))
        self.ChanceMaker_image = pygame.image.load("Images/Chancemaker.png").convert_alpha()
        self.ChanceMaker_image = pygame.transform.rotozoom(self.ChanceMaker_image,360,1/2)
        self.ChanceMaker_image_rect = self.ChanceMaker_image.get_rect(topright = self.ChanceMaker_rect.topright)
        self.ChanceMakerCount = 0
        self.ChanceMakerCost,self.ChanceMakerCostDisplay = OC["ChanceMakerCost"],""
        self.ChanceMakerColor = self.NumberCheck(OC["Clicks"],self.ChanceMakerCost)
        self.ChanceMakerCostDisplay = self.NumberShrink(self.ChanceMakerCost, self.ChanceMakerCostDisplay)
        self.ChanceMakerCost_text = Test_Font.render(str(self.ChanceMakerCostDisplay), True, self.ChanceMakerColor)
        self.ChanceMakerCost_rect = self.ChanceMakerCost_text.get_rect(bottomleft = self.ChanceMaker_rect.bottomleft)
        self.ChanceMakerAmount_Text = Store_font.render(str(OC["ChanceMakerAmount"]), True, "Black")
        self.ChanceMakerAmount_rect = self.ChanceMakerAmount_Text.get_rect(topleft = self.ChanceMaker_rect.topleft)
        self.ChanceMakerSell = round(OC["ChanceMakerCost"]/4)
        self.ChanceMakerCostx10,self.ChanceMakerCostx100 = "",""
        self.ChanceMakerSellx10,self.ChanceMakerSellx100 = "",""
        self.ChanceMakerUpgradeCost = "260Q"
        self.ChanceMakerUpgradeCost_text = Test_Font.render(str(self.ChanceMakerUpgradeCost), True, "Blue")
        self.CMName = Store_font.render("ChanceMaker", True, "Black")

        self.FE_Surf = pygame.Surface((64,44))
        self.FE_Surf.fill((205,127,100))
        self.FE_rect = self.FE_Surf.get_rect(center = (1074,480))
        self.FE_image = pygame.image.load(r"Images/Fractal_Engine.png").convert_alpha()
        self.FE_image = pygame.transform.rotozoom(self.FE_image,360,1/2)
        self.FE_image_rect = self.FE_image.get_rect(topright = self.FE_rect.topright)
        self.FECount = 0
        self.FECost,self.FECostDisplay = OC["FECost"],""
        self.FEColor = self.NumberCheck(OC["Clicks"],self.FECost)
        self.FECostDisplay = self.NumberShrink(self.FECost, self.FECostDisplay)
        self.FECost_text = Test_Font.render(str(self.FECostDisplay), True, self.FEColor)
        self.FECost_rect = self.FECost_text.get_rect(bottomleft = self.FE_rect.bottomleft)
        self.FEAmount_Text = Store_font.render(str(OC["FEAmount"]), True, "Black")
        self.FEAmount_rect = self.FEAmount_Text.get_rect(topleft = self.FE_rect.topleft)
        self.FESell = round(OC["FECost"]/4)
        self.FECostx10,self.FECostx100 = "",""
        self.FESellx10,self.FESellx100 = "",""
        self.FEUpgradeCost = "3.1QT"
        self.FEUpgradeCost_text = Test_Font.render(str(self.FEUpgradeCost), True, "Blue")
        self.FEName = Store_font.render("Fractal Engine", True, "Black")
        
        self.PC_Surf = pygame.Surface((64,44))
        self.PC_Surf.fill((205,127,100))
        self.PC_rect = self.PC_Surf.get_rect(center = (1178,480))
        self.PC_image = pygame.image.load("Images/Python.png").convert_alpha()
        self.PC_image = pygame.transform.rotozoom(self.PC_image,360,1/24)
        self.PC_image_rect = self.PC_image.get_rect(topright = self.PC_rect.topright)
        self.PCCount = 0
        self.PCCost,self.PCCostDisplay = OC["PCCost"],""
        self.PCColor = self.NumberCheck(OC["Clicks"],self.PCCost)
        self.PCCostDisplay = self.NumberShrink(self.PCCost, self.PCCostDisplay)
        self.PCCost_text = Test_Font.render(str(self.PCCostDisplay), True, self.PCColor)
        self.PCCost_rect = self.PCCost_text.get_rect(bottomleft = self.PC_rect.bottomleft)
        self.PCAmount_Text = Store_font.render(str(OC["PCAmount"]), True, "Black")
        self.PCAmount_rect = self.PCAmount_Text.get_rect(topleft = self.PC_rect.topleft)
        self.PCSell = round(OC["PCCost"]/4)
        self.PCCostx10,self.PCCostx100 = "",""
        self.PCSellx10,self.PCSellx100 = "",""
        self.PCUpgradeCost = "710QT"
        self.PCUpgradeCost_text = Test_Font.render(str(self.PCUpgradeCost), True, "Blue")
        self.PCName = Store_font.render("Python Terminal", True, "Black")

        self.IV_Surf = pygame.Surface((64,44))
        self.IV_Surf.fill((205,127,100))
        self.IV_rect = self.IV_Surf.get_rect(center = (1271,480))
        self.IV_image = pygame.image.load("Images/IdeVerse.png").convert_alpha()
        self.IV_image = pygame.transform.rotozoom(self.IV_image,360,1/2)
        self.IV_image_rect = self.IV_image.get_rect(topright = self.IV_rect.topright)
        self.IVCount = 0
        self.IVCost,self.IVCostDisplay = OC["IVCost"],""
        self.IVColor = self.NumberCheck(OC["Clicks"],self.IVCost)
        self.IVCostDisplay = self.NumberShrink(self.IVCost, self.IVCostDisplay)
        self.IVCost_text = Test_Font.render(str(self.IVCostDisplay), True, self.IVColor)
        self.IVCost_rect = self.IVCost_text.get_rect(bottomleft = self.IV_rect.bottomleft)
        self.IVAmount_Text = Store_font.render(str(OC["IVAmount"]), True, "Black")
        self.IVAmount_rect = self.IVAmount_Text.get_rect(topleft = self.IV_rect.topleft)
        self.IVSell = round(OC["IVCost"]/4)
        self.IVCostx10,self.IVCostx100 = "",""
        self.IVSellx10,self.IVSellx100 = "",""
        self.IVUpgradeCost = "120S"
        self.IVUpgradeCost_text = Test_Font.render(str(self.IVUpgradeCost), True, "Blue")
        self.IVName = Store_font.render("Idleverse", True, "Black")

        self.CB_Surf = pygame.Surface((64,44))
        self.CB_Surf.fill((205,127,100))
        self.CB_rect = self.CB_Surf.get_rect(center = (1178,540))
        self.CB_image = pygame.image.load("Images/Cortex.png").convert_alpha()
        self.CB_image = pygame.transform.rotozoom(self.CB_image,360,1/2)
        self.CB_image_rect = self.CB_image.get_rect(topright = self.CB_rect.topright)
        self.CBCount = 0
        self.CBCost,self.CBCostDisplay = OC["CBCost"],""
        self.CBColor = self.NumberCheck(OC["Clicks"],self.CBCost)
        self.CBCostDisplay = self.NumberShrink(self.CBCost, self.CBCostDisplay)
        self.CBCost_text = Test_Font.render(str(self.CBCostDisplay), True, self.CBColor)
        self.CBCost_rect = self.CBCost_text.get_rect(bottomleft = self.CB_rect.bottomleft)
        self.CBAmount_Text = Store_font.render(str(OC["CBAmount"]), True, "Black")
        self.CBAmount_rect = self.CBAmount_Text.get_rect(topleft = self.CB_rect.topleft)
        self.CBSell = round(OC["CBCost"]/4)
        self.CBCostx10,self.CBCostx100 = "",""
        self.CBSellx10,self.CBSellx100 = "",""
        self.CBUpgradeCost = "19SepT"
        self.CBUpgradeCost_text = Test_Font.render(str(self.CBUpgradeCost), True, "Blue")
        self.CBName = Store_font.render("Cortaex Baker", True, "Black")

    def Draw(self):
        SCREEN.blit(self.Title, (1180,0))
        SCREEN.blit(self.Storeops, self.Storeops_rect)
        SCREEN.blit(self.Buy, self.Buy_rect)
        SCREEN.blit(self.Buy_Text, self.Buy_text_rect)
        SCREEN.blit(self.Sell, self.Sell_rect)
        SCREEN.blit(self.Sell_Text, self.Sell_Text_rect)
        SCREEN.blit(self.X1, self.X1_rect)
        SCREEN.blit(self.X1_Text, self.X1_Text_Rect)
        SCREEN.blit(self.X10, self.X10_rect)
        SCREEN.blit(self.X10_text, self.X10_text_rect)
        SCREEN.blit(self.X100, self.X100_rect)
        SCREEN.blit(self.X100_text, self.X100_text_rect)
        self.AutoMouse_surf.fill((205, 127, 100)); self.Grandma_surf.fill((205, 127, 100)); self.Farm_surf.fill((205, 127, 100))
        self.Mine_surf.fill((205, 127, 100)); self.Factory_surf.fill((205, 127, 100)); self.Bank_surf.fill((205, 127, 100))
        self.Temple_surf.fill((205,127,100)); self.Wizard_Tower_surf.fill((205,127,100));self.Shipment_surf.fill((205,127,100))
        self.AL_surf.fill((205,127,100));self.Portal_Surf.fill((205,127,100)); self.TM_Surf.fill((205,127,100))
        self.AC_Surf.fill((205,127,100));self.Prism_Surf.fill((205,127,100));self.ChanceMaker_Surf.fill((205,127,100))
        self.FE_Surf.fill((205,127,100));self.PC_Surf.fill((205,127,100));self.IV_Surf.fill((205,127,100))
        self.CB_Surf.fill((205,127,100))
        SCREEN.blit(self.AutoMouse_surf, self.AutoMouse_rect)
        SCREEN.blit(self.AutoMouse_amount_text,self.AutoMouse_amount_rect)
        SCREEN.blit(self.AutoMouse_Cost_text, self.AutoMouse_Cost_text_rect)
        SCREEN.blit(self.AutoMouse_image, self.AutoMouse_image_rect)
        SCREEN.blit(self.Grandma_surf, self.Grandma_rect)
        SCREEN.blit(self.Grandma_amount_text, self.Grandma_amount_rect)
        SCREEN.blit(self.Grandma_Cost_text, self.Grandma_Cost_rect)
        SCREEN.blit(self.Grandma_image, self.Grandma_image_rect)
        SCREEN.blit(self.Farm_surf, self.Farm_rect)
        SCREEN.blit(self.Farm_image, self.Farm_image_rect)
        SCREEN.blit(self.FarmAmount_text,self.FarmAmount_rect)
        SCREEN.blit(self.Farm_Cost_text,self.Farm_Cost_rect)
        SCREEN.blit(self.Mine_surf, self.Mine_rect)
        SCREEN.blit(self.Mine_image, self.Mine_image_rect)
        SCREEN.blit(self.MineCost_text, self.MineCost_rect)
        SCREEN.blit(self.MineAmount_Text, self.MineAmount_rect)
        SCREEN.blit(self.Factory_surf, self.Factory_rect)
        SCREEN.blit(self.Factory_image, self.Factory_image_rect)
        SCREEN.blit(self.FactoryCost_text, self.FactoryCost_rect)
        SCREEN.blit(self.FactoryAmount_Text,self.FactoryAmount_rect)
        SCREEN.blit(self.Bank_surf, self.Bank_rect)
        SCREEN.blit(self.Bank_image, self.Bank_image_rect)
        SCREEN.blit(self.BankCost_text, self.BankCost_rect)
        SCREEN.blit(self.BankAmount_text, self.BankAmount_rect)
        SCREEN.blit(self.Temple_surf, self.Temple_rect)
        SCREEN.blit(self.Temple_image, self.Temple_image_rect)
        SCREEN.blit(self.TempleCost_text, self.TempleCost_rect)
        SCREEN.blit(self.TempleAmount_Text, self.TempleAmount_rect)
        SCREEN.blit(self.Wizard_Tower_surf, self.Wizard_Tower_rect)
        SCREEN.blit(self.WT_image,self.WT_image_rect)
        SCREEN.blit(self.WTCost_text,self.WTCost_rect)
        SCREEN.blit(self.WTAmount_Text,self.WTAmount_rect)
        SCREEN.blit(self.Shipment_surf,self.Shipment_rect)
        SCREEN.blit(self.ShipmentCost_Text, self.ShipmentCost_rect)
        SCREEN.blit(self.Shipment_image,self.Shipment_image_rect)
        SCREEN.blit(self.ShipmentAmount_text,self.ShipmentAmount_rect)
        SCREEN.blit(self.AL_surf,self.AL_rect)
        SCREEN.blit(self.AL_image,self.AL_image_rect)
        SCREEN.blit(self.ALCost_text,self.ALCost_rect)
        SCREEN.blit(self.ALAmount_text,self.ALAmount_rect)
        SCREEN.blit(self.Portal_Surf, self.Portal_rect)
        SCREEN.blit(self.Portal_image, self.Portal_image_rect)
        SCREEN.blit(self.PortalCost_text,self.PortalCost_rect)
        SCREEN.blit(self.PortalAmount_Text, self.PortalAmount_rect)
        SCREEN.blit(self.TM_Surf, self.TM_rect)
        SCREEN.blit(self.TM_image, self.TM_image_rect)
        SCREEN.blit(self.TMCost_text,self.TMCost_rect)
        SCREEN.blit(self.TMAmount_Text, self.TMAmount_rect)
        SCREEN.blit(self.AC_Surf, self.AC_rect)
        SCREEN.blit(self.AC_image, self.AC_image_rect)
        SCREEN.blit(self.ACCost_text,self.ACCost_rect)
        SCREEN.blit(self.ACAmount_Text,self.ACAmount_rect)
        SCREEN.blit(self.Prism_Surf, self.Prism_rect)
        SCREEN.blit(self.Prism_image, self.Prism_image_rect)
        SCREEN.blit(self.PrismCost_text, self.PrismCost_rect)
        SCREEN.blit(self.PrismAmount_Text, self.PrismAmount_rect)
        SCREEN.blit(self.ChanceMaker_Surf, self.ChanceMaker_rect)
        SCREEN.blit(self.ChanceMaker_image, self.ChanceMaker_image_rect)
        SCREEN.blit(self.ChanceMakerCost_text,self.ChanceMakerCost_rect)
        SCREEN.blit(self.ChanceMakerAmount_Text,self.ChanceMakerAmount_rect)
        SCREEN.blit(self.FE_Surf,self.FE_rect)
        SCREEN.blit(self.FE_image,self.FE_image_rect)
        SCREEN.blit(self.FECost_text,self.FECost_rect)
        SCREEN.blit(self.FEAmount_Text,self.FEAmount_rect)
        SCREEN.blit(self.PC_Surf,self.PC_rect)
        SCREEN.blit(self.PC_image,self.PC_image_rect)
        SCREEN.blit(self.PCCost_text,self.PCCost_rect)
        SCREEN.blit(self.PCAmount_Text,self.PCAmount_rect)
        SCREEN.blit(self.IV_Surf,self.IV_rect)
        SCREEN.blit(self.IV_image,self.IV_image_rect)
        SCREEN.blit(self.IVCost_text,self.IVCost_rect)
        SCREEN.blit(self.IVAmount_Text,self.IVAmount_rect)
        SCREEN.blit(self.CB_Surf,self.CB_rect)
        SCREEN.blit(self.CB_image,self.CB_image_rect)
        SCREEN.blit(self.CBCost_text,self.CBCost_rect)
        SCREEN.blit(self.CBAmount_Text,self.CBAmount_rect)
        self.IVAmount_Text = Store_font.render(str(OC["IVAmount"]), True, "Black")
        self.IVUpgradeCost_text = Test_Font.render(str(self.IVUpgradeCost), True, "Blue")
        self.PCUpgradeCost_text = Test_Font.render(str(self.PCUpgradeCost), True, "Blue")
        self.PCAmount_Text = Store_font.render(str(OC["PCAmount"]), True, "Black")
        self.CBColor = self.NumberCheck(OC["Clicks"],self.CBCost)
        self.CBCostDisplay = self.NumberShrink(self.CBCost, self.CBCostDisplay)
        self.CBCost_text = Test_Font.render(str(self.CBCostDisplay), True, self.CBColor)
        self.FEColor = self.NumberCheck(OC["Clicks"],self.FECost)
        self.FECostDisplay = self.NumberShrink(self.FECost, self.FECostDisplay)
        self.FECost_text = Test_Font.render(str(self.FECostDisplay), True, self.FEColor)
        self.PrismColor = self.NumberCheck(OC["Clicks"],self.PrismCost)
        self.PrismCostDisplay = self.NumberShrink(self.PrismCost, self.PrismCostDisplay)
        self.CBAmount_Text = Store_font.render(str(OC["CBAmount"]), True, "Black")
        self.PrismCost_text = Test_Font.render(str(self.PrismCostDisplay), True, self.PrismColor)
        self.PrismAmount_Text = Store_font.render(str(OC["PrismAmount"]), True, "Black")
        self.PrismUpgradeCost_text = Test_Font.render(str(self.PrismUpgradeCost), True, "Blue")
        self.TMColor = self.NumberCheck(OC["Clicks"],self.TMCost)
        self.TMCostDisplay = self.NumberShrink(self.TMCost, self.TMCostDisplay)
        self.PCColor = self.NumberCheck(OC["Clicks"],self.PCCost)
        self.PCCostDisplay = self.NumberShrink(self.PCCost, self.PCCostDisplay)
        self.PCCost_text = Test_Font.render(str(self.PCCostDisplay), True, self.PCColor)
        self.TMCost_text = Test_Font.render(str(self.TMCostDisplay), True, self.PortalColor)
        self.ChanceMakerUpgradeCost_text = Test_Font.render(str(self.ChanceMakerUpgradeCost), True, "Blue")
        self.AMColor = self.NumberCheck(OC["Clicks"],self.AutoMousecost)
        self.WTUpgrade_Text = Test_Font.render(str(self.WTUpgradeCost),True,"Blue")
        self.IVColor = self.NumberCheck(OC["Clicks"],self.IVCost)
        self.IVCostDisplay = self.NumberShrink(self.IVCost, self.IVCostDisplay)
        self.CBUpgradeCost_text = Test_Font.render(str(self.CBUpgradeCost), True, "Blue")
        self.IVCost_text = Test_Font.render(str(self.IVCostDisplay), True, self.IVColor)
        self.ACAmount_Text = Store_font.render(str(OC["ACAmount"]), True, "Black")
        self.GrandColor = self.NumberCheck(OC["Clicks"],self.GrandmaCost)
        self.FarmColor = self.NumberCheck(OC["Clicks"], self.FarmCost)
        self.ACUpgradeCost_text = Test_Font.render(str(self.ACUpgradeCost), True, "Blue")
        self.MineColor = self.NumberCheck(OC["Clicks"], self.MineCost)
        self.FactoryColor = self.NumberCheck(OC["Clicks"],self.FactoryCost)
        self.BankColor = self.NumberCheck(OC["Clicks"],self.BankCost)
        self.WTColor = self.NumberCheck(OC["Clicks"],self.WTCost)
        self.ALColor = self.NumberCheck(OC["Clicks"], self.ALCost)
        self.FEUpgradeCost_text = Test_Font.render(str(self.FEUpgradeCost), True, "Blue")
        self.ChanceMakerAmount_Text = Store_font.render(str(OC["ChanceMakerAmount"]), True, "Black")
        self.ALCostDisplay = self.NumberShrink(self.ALCost, self.ALCostDisplay)
        self.TMAmount_Text = Store_font.render(str(OC["TMAmount"]), True, "Black")
        self.ALCost_text = Test_Font.render(str(self.ALCostDisplay), True, self.ALColor)
        self.ChanceMakerColor = self.NumberCheck(OC["Clicks"],self.ChanceMakerCost)
        self.ChanceMakerCostDisplay = self.NumberShrink(self.ChanceMakerCost, self.ChanceMakerCostDisplay)
        self.ChanceMakerCost_text = Test_Font.render(str(self.ChanceMakerCostDisplay), True, self.ChanceMakerColor)
        self.ALAmount_text = Store_font.render(str(OC["ALAmount"]), True, "Black")
        self.FEAmount_Text = Store_font.render(str(OC["FEAmount"]), True, "Black")
        self.ShipmentColor = self.NumberCheck(OC["Clicks"],self.ShipmentCost)
        self.ShipmentCostDisplay = self.NumberShrink(self.ShipmentCost,self.ShipmentCostDisplay)
        self.ShipmentCost_Text = Test_Font.render(str(self.ShipmentCostDisplay), True, self.ShipmentColor)
        self.WTCostDisplay = self.NumberShrink(self.WTCost, self.WTCostDisplay)
        self.WTCost_text = Test_Font.render(str(self.WTCostDisplay), True, self.WTColor)
        self.AutoMouse_amount_text = Store_font.render(str(OC["AMAmount"]), True, "Black")
        self.TMUpgradeCost_text = Test_Font.render(str(self.TMUpgradeCost), True, "Blue")
        self.AMDisplayCost = self.NumberShrink(self.AutoMousecost, self.AMDisplayCost)
        self.GrandCostDisplay = self.NumberShrink(self.GrandmaCost, self.GrandCostDisplay)
        self.ShipmentAmount_text = Store_font.render(str(OC["ShipmentAmount"]), True, "Black")
        self.ACColor = self.NumberCheck(OC["Clicks"],self.ACCost)
        self.ACCostDisplay = self.NumberShrink(self.ACCost, self.ACCostDisplay)
        self.ACCost_text = Test_Font.render(str(self.ACCostDisplay), True, self.ACColor)
        self.FarmCostDisplay = self.NumberShrink(self.FarmCost, self.FarmCostDisplay)
        self.PortalUpgradeCost_text = Test_Font.render(str(self.PortalUpgradeCost), True, "Blue")
        self.PortalColor = self.NumberCheck(OC["Clicks"],self.PortalCost)
        self.PortalCostDisplay = self.NumberShrink(self.PortalCost, self.PortalCostDisplay)
        self.PortalCost_text = Test_Font.render(str(self.PortalCostDisplay), True, self.PortalColor)
        self.PortalAmount_Text = Store_font.render(str(OC["PortalAmount"]), True, "Black")
        self.AutoMouse_Cost_text = Test_Font.render(str(self.AMDisplayCost), True, self.AMColor)
        self.MineAmount_Text = Store_font.render(str(OC["MineAmount"]), True, "Black")
        self.MineCost_text = Test_Font.render(str(self.MineCostDisplay), True, self.MineColor)
        self.WTAmount_Text = Store_font.render(str(OC["WizardTowerAmount"]), True, "Black")
        self.BankAmount_text = Store_font.render(str(OC["BankAmount"]), True, "Black")
        self.FactoryCostDisplay = self.NumberShrink(self.FactoryCost,self.FactoryCostDisplay)
        self.FactoryCost_text = Test_Font.render(str(self.FactoryCostDisplay), True, self.FactoryColor)
        self.MineUpgrade_tect = Test_Font.render(str(self.MineUpgradecost),True,"Blue")
        self.FarmUpgrade_text = Test_Font.render(str(self.FarmDisplaycost), True, "Blue")
        self.MineCostDisplay = self.NumberShrink(self.MineCost,self.MineCostDisplay)
        self.TempleColor = self.NumberCheck(OC["Clicks"], self.TempleCost)
        self.TempleCostDisplay = self.NumberShrink(self.TempleCost, self.TempleCostDisplay)
        self.TempleCost_text = Test_Font.render(str(self.TempleCostDisplay), True, self.TempleColor)
        self.TempleAmount_Text = Store_font.render(str(OC["TempleAmount"]), True, "Black")
        self.AMUpgrade1cost_text = Test_Font.render(str(self.AMDisplay_Text), True, "Blue")
        self.Grandma_amount_text = Store_font.render(str(OC["GrandAmount"]), True, "Black")
        self.Grandma_Cost_text = Test_Font.render(str(self.GrandCostDisplay), True, self.GrandColor)
        self.GrandmaUpgrade_text = Test_Font.render(str(self.GranddisplayText), True, "Blue")
        self.ShipmentUpgradeCost_Text = Test_Font.render(str(self.ShipmentUpgradeCost),True,"Blue")
        self.FactoryAmount_Text = Store_font.render(str(OC["FactoryAmount"]), True, "Black")
        self.FarmAmount_text = Store_font.render(str(OC["FarmAmount"]), True, "Black")
        self.Farm_Cost_text = Test_Font.render(str(self.FarmCostDisplay), True, self.FarmColor)
        self.FactoryUpgrade_text = Test_Font.render(str(self.FactoryUpgradeCost), True, "Blue")
        self.BankCostDisplay = self.NumberShrink(self.BankCost,self.BankCostDisplay)
        self.BankCost_text = Test_Font.render(str(self.BankCostDisplay), True, self.BankColor)
        self.TempleUpgrade_text = Test_Font.render(str(self.TempleUpgradeCost), True, "Blue")
        self.BankUpgrade_text = Test_Font.render(str(self.BankUpgradeCost), True, "Blue")
        self.ALUpgradeCost_text = Test_Font.render(str(self.ALUpgradeCost), True, "Blue")
        self.Check_click_Buy()
        self.Check_click_Sell()
        self.Check_click_X1()
        self.Check_click_X10()
        self.Check_click_X100()
        self.CC_AutoMouse()
        self.CC_Grandma()
        self.CC_Farm()
        self.CC_Mine()
        self.CC_Factory()
        self.CC_Bank()
        self.CC_Temple()
        self.CC_WT()
        self.CC_AL()
        self.CC_Shipment()
        self.CC_Portal()
        self.CC_TM()
        self.CC_AC()
        self.CC_Prism()
        self.CC_ChanceMaker()
        self.CC_FE()
        self.CC_PC()
        self.CC_IV()
        self.CC_CB()
        self.Display()
        self.ShopUpgrades()
    
    def Check_click_Buy(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Buy_rect.collidepoint(mouse_pos):
            if not self.buy:
                self.Buy_color = "White"
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy: self.buy = False
                    else: self.buy = True; self.sell = False
                    self.pressed = False
        else:
            if not self.buy: self.Buy_color = "Black"
            else: self.Buy_color = "White"
        self.Buy_Text = Game_Font.render("Buy", True, self.Buy_color)

    def Check_click_Sell(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Sell_rect.collidepoint(mouse_pos):
            if not self.sell:
                self.Sell_color = "White"
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    self.sell = True; self.buy = False
                    self.pressed = False
        else:
            if not self.sell: self.Sell_color = "Black"
            else: self.Sell_color = "White"   
        self.Sell_Text = Game_Font.render("Sell", True, self.Sell_color)
    
    def Check_click_X1(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.X1_rect.collidepoint(mouse_pos):
            self.Amountcolor1 = "White"
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    self.x1 = True; self.x10 = False; self.x100 = False
                    self.pressed = False
        else:
            if not self.x1: self.Amountcolor1 = "Black"
            else: self.Amountcolor1 = "White"
        self.X1_Text = Game_Font.render("1", True, self.Amountcolor1)
    
    def Check_click_X10(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.X10_rect.collidepoint(mouse_pos):
            self.Amountcolor10 = "White"
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    self.x10 = True; self.x1 = False; self.x100 = False
                    self.pressed = False
        else:
            if not self.x10: self.Amountcolor10 = "Black"
            else: self.Amountcolor10 = "White"
        self.X10_text = Game_Font.render("10", True, self.Amountcolor10)
    
    def Check_click_X100(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.X100_rect.collidepoint(mouse_pos):
            self.Amountcolor100 = "White"
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    self.x100 = True; self.x10 = False; self.x1 = False
                    self.pressed = False
        else:
            if not self.x100: self.Amountcolor100 = "Black"
            else: self.Amountcolor100 = "White"
        self.X100_text = Game_Font.render("100", True, self.Amountcolor100)
    
    def Display(self):
        if self.buy:
            self.AutoMousecostx10, self.AutoMousecostx100 = self.CostDisplay(15, OC["AMAmount"])
            self.GrandmaCostx10, self.GrandmaCostx100 = self.CostDisplay(100,OC["GrandAmount"])
            self.FarmCostx10,self.FarmCostx100 = self.CostDisplay(1100,OC["FarmAmount"])
            self.MineCostx10,self.MineCostx100 = self.CostDisplay(12_000,OC["MineAmount"])
            self.FactoryCostx10,self.FactoryCostx100 = self.CostDisplay(130_000,OC["FactoryAmount"])
            self.BankCostx10,self.BankCostx100 = self.CostDisplay(1_400_000, OC["BankAmount"])
            self.TempleCostx10, self.TempleCostx100 = self.CostDisplay(20_000_000, OC["TempleAmount"])
            self.WTCostx10,self.WTCostx100 = self.CostDisplay(330_000_000, OC["WizardTowerAmount"])
            self.ShipmentCostx10,self.ShipmentCostx100 = self.CostDisplay(5_100_000_000, OC["ShipmentAmount"])
            self.ALCostx10, self.ALCostx100 = self.CostDisplay(75_000_000_000,OC["ALAmount"])
            self.PortalCostx10,self.PortalCostx100 = self.CostDisplay(1_000_000_000_000,OC["PortalAmount"])
            self.TMCostx10,self.TMCostx100 = self.CostDisplay(14_000_000_000_000,OC["TMAmount"])
            self.ACCostx10,self.ACCostx100 = self.CostDisplay(170_000_000_000_000,OC["ACAmount"])
            self.PrismCostx10,self.PrismCostx100 = self.CostDisplay(2_100_000_000_000_000_000,OC["PrismAmount"])
            self.ChanceMakerCostx10,self.ChanceMakerCostx100 = self.CostDisplay(26_000_000_000_000_000_000,OC["ChanceMakerAmount"])
            self.FECostx10,self.FECostx100 = self.CostDisplay(310_000_000_000_000_000_000,OC["FEAmount"])
            self.PCCostx10,self.PCCostx100 = self.CostDisplay(71_000_000_000_000_000_000,OC["PCAmount"])
            self.IVCostx10,self.IVCostx100 = self.CostDisplay(12_000_000_000_000_000_000_000,OC["IVAmount"])
            self.CBCostx10,self.CBCostx100 = self.CostDisplay(1_900_000_000_000_000_000_000_000,OC['CBAmount'])
            if self.x10:
                self.AutoMousecost = self.AutoMousecostx10
                self.GrandmaCost = self.GrandmaCostx10
                self.FarmCost = self.FarmCostx10
                self.MineCost = self.MineCostx10
                self.FactoryCost = self.FactoryCostx10
                self.BankCost = self.BankCostx10
                self.TempleCost = self.TempleCostx10
                self.WTCost = self.WTCostx10
                self.ShipmentCost = self.ShipmentCostx10
                self.ALCost = self.ALCostx10
                self.PortalCost = self.PortalCostx10
                self.TMCost = self.TMCostx10
                self.ACCost = self.ACCostx10
                self.PrismCost = self.PrismCostx10
                self.ChanceMakerCost = self.ChanceMakerCostx10
                self.FECost = self.FECostx10
                self.PCCost = self.PCCostx10
                self.IVCost = self.IVCostx10
                self.CBCost = self.CBCostx10
            elif self.x100:
                self.AutoMousecost = self.AutoMousecostx100
                self.GrandmaCost = self.GrandmaCostx100
                self.FarmCost = self.FarmCostx100
                self.MineCost = self.MineCostx100
                self.FactoryCost = self.FactoryCostx100
                self.BankCost = self.BankCostx100
                self.TempleCost = self.TempleCostx100
                self.WTCost = self.WTCostx100
                self.ShipmentCost = self.ShipmentCostx100
                self.ALCost = self.ALCostx100
                self.PortalCost = self.PortalCostx100
                self.TMCost = self.TMCostx100
                self.ACCost = self.ACCostx100
                self.PrismCost = self.PrismCostx100
                self.ChanceMakerCost = self.ChanceMakerCostx100
                self.FECost = self.FECostx100
                self.PCCost = self.PCCostx100
                self.IVCost = self.IVCostx100
                self.CBCost = self.CBCostx100
            else:
                self.AutoMousecost = OC["AMcost"]
                self.GrandmaCost = OC["Grandcost"]
                self.FarmCost = OC["FarmCost"]
                self.MineCost = OC["MineCost"]
                self.FactoryCost = OC["FactoryCost"]
                self.BankCost = OC["BankCost"]
                self.TempleCost = OC["TempleCost"]
                self.WTCost = OC["WizardTowerCost"]
                self.ShipmentCost = OC["ShipmentCost"]
                self.ALCost = OC["ALCost"]
                self.PortalCost = OC["PortalCost"]
                self.TMCost = OC["TMCost"]
                self.ACCost = OC["ACCost"]
                self.PrismCost = OC["PrismCost"]
                self.ChanceMakerCost = OC["ChanceMakerCost"]
                self.FECost = OC["FECost"]
                self.PCCost = OC["PCCost"]
                self.IVCost = OC["IVCost"]
                self.CBCost = OC["CBCost"]
        elif self.sell:
            self.AMSellx10,self.AMSellx100 = self.SellDisplay(15, OC["AMAmount"]); self.AMSell = round(OC["AMcost"]/4)
            self.GrandSellx10, self.GrandSellx100 = self.SellDisplay(100,OC["GrandAmount"]);self.GrandSell = round(OC["Grandcost"]/4)
            self.FarmSellx10,self.FarmSellx100 = self.SellDisplay(1100, OC["FarmAmount"]);self.FarmSell = round(OC["FarmCost"]/4)
            self.MineSellx10,self.MineSellx100 = self.SellDisplay(12000, OC["MineAmount"]); self.MineSell = round(OC["MineCost"]/4)
            self.FactorySellx10,self.FactorySellx100 = self.SellDisplay(130_000,OC["FactoryAmount"]);self.FactorySell = round(OC["FactoryCost"]/4)
            self.BankSellx10,self.BankSellx100 = self.SellDisplay(1_400_000,OC["BankAmount"]);self.BankSell = round(OC["BankCost"]/4)
            self.TempleSellx10,self.TempleSellx100 = self.SellDisplay(20_000_000,OC["TempleAmount"]); self.TempleSell = round(OC["TempleCost"]/4)
            self.WTSellx10,self.WTSellx100 = self.SellDisplay(330_000_000,OC["WizardTowerAmount"]); self.WTSell = round(OC["WizardTowerCost"]/4)
            self.ShipmentSellx10,self.ShipmentSellx100 = self.SellDisplay(5_100_000_000, OC["ShipmentAmount"]); self.ShipmentSell = round(OC["ShipmentCost"]/4)
            self.ALSellx10,self.ALSellx100 = self.SellDisplay(75_000_000_000,OC["ALAmount"]);self.ALSell = round(OC["ALCost"]/4)
            self.PortalSellx10,self.PortalSellx100 = self.SellDisplay(1_000_000_000_000,OC["PortalAmount"]); self.PortalSell = round(OC["PortalCost"]/4)
            self.TMSellx10,self.TMSellx100 = self.SellDisplay(14_000_000_000_000,OC["TMAmount"]); self.TMSell = round(OC["TMCost"]/4)
            self.ACSellx10,self.ACSellx100 = self.SellDisplay(170_000_000_000_000,OC["ACAmount"]); self.ACSell = round(OC["ACCost"]/4)
            self.PrismSellx10,self.PrismSellx100 = self.SellDisplay(2_100_000_000_000_000_000,OC["PrismAmount"]);self.PrismSell = round(OC["PrismCost"]/4)
            self.ChanceMakerSellx10,self.ChanceMakerSellx100 = self.SellDisplay(26_000_000_000_000_000_000,OC["ChanceMakerAmount"]);self.ChanceMakerSell = round(OC["ChanceMakerCost"]/4)
            self.FESellx10,self.FESellx100 = self.SellDisplay(310_000_000_000_000_000_000,OC["FEAmount"]);self.FESell = round(OC["FECost"]/4)
            self.PCSellx10,self.PCSellx100 = self.SellDisplay(71_000_000_000_000_000_000,OC["PCAmount"]);self.PCSell = round(OC["PCCost"]/4)
            self.IVSellx10,self.IVSellx100 = self.SellDisplay(12_000_000_000_000_000_000_000,OC["IVAmount"]);self.IVSell = round(OC["IVCost"]/4) 
            self.CBSellx10, self.CBSellx100 = self.SellDisplay(1_900_000_000_000_000_000_000_000,OC['CBAmount']);self.CBSell = round(OC["CBCost"]/4)
            if self.x10:
                self.AutoMousecost = self.AMSellx10
                self.GrandmaCost = self.GrandSellx10
                self.FarmCost = self.FarmSellx10
                self.MineCost = self.MineSellx10
                self.FactoryCost = self.FactorySellx10
                self.BankCost = self.BankSellx10
                self.TempleCost = self.TempleSellx10
                self.WTCost = self.WTSellx10
                self.ShipmentCost = self.ShipmentSellx10
                self.ALCost = self.ALSellx10
                self.PortalCost = self.PortalSellx10
                self.TMCost = self.TMSellx10
                self.ACCost = self.ACSellx10
                self.PrismCost = self.PrismSellx10
                self.ChanceMakerCost = self.ChanceMakerSellx10
                self.FECost = self.FESellx10
                self.PCCost = self.PCSellx10
                self.IVCost = self.IVSellx10
                self.CBCost = self.CBSellx10
            elif self.x100:
                self.AutoMousecost = self.AMSellx100
                self.GrandmaCost = self.GrandSellx100
                self.FarmCost = self.FarmSellx100
                self.MineCost = self.MineSellx100
                self.FactoryCost = self.FactorySellx100
                self.BankCost = self.BankSellx100
                self.TempleCost = self.TempleSellx100
                self.WTCost = self.WTSellx100
                self.ShipmentCost = self.ShipmentSellx100
                self.ALCost = self.ALSellx100
                self.PortalCost = self.PortalSellx100
                self.TMCost = self.TMSellx100
                self.ACCost = self.ACSellx100
                self.PrismCost = self.PrismSellx100
                self.ChanceMakerCost = self.ChanceMakerSellx100
                self.FECost = self.FESellx100
                self.PCCost = self.PCSellx100
                self.IVCost = self.IVSellx100
                self.CBCost = self.CBSellx100
            else:
                self.AutoMousecost = self.AMSell
                self.GrandmaCost = self.GrandSell
                self.FarmCost = self.FarmSell
                self.MineCost = self.MineSell
                self.FactoryCost = self.FactorySell
                self.BankCost = self.BankSell
                self.TempleCost = self.TempleSell
                self.WTCost = self.WTSell
                self.ShipmentCost = self.ShipmentSell
                self.ALCost = self.ALSell
                self.PortalCost = self.PortalSell
                self.TMCost = self.TMSell
                self.ACCost = self.ACSell
                self.PrismCost = self.PrismSell
                self.ChanceMakerCost = self.ChanceMakerSell
                self.FECost = self.FESell
                self.PCCost = self.PCSell
                self.IVCost = self.IVSell
                self.CBCost = self.CBSell
    
    def ShopUpgrades(self):
        if self.Upgrades:
            SCREEN.blit(BG3, BG3_rect)
            SCREEN.blit(self.Title, (1180,0))
            SCREEN.blit(self.Storeops, self.Storeops_rect)
            SCREEN.blit(self.Buy, self.Buy_rect)
            SCREEN.blit(self.Buy_Text, self.Buy_text_rect)
            SCREEN.blit(self.Sell, self.Sell_rect)
            SCREEN.blit(self.Sell_Text, self.Sell_Text_rect)
            SCREEN.blit(self.X1, self.X1_rect)
            SCREEN.blit(self.X1_Text, self.X1_Text_Rect)
            SCREEN.blit(self.X10, self.X10_rect)
            SCREEN.blit(self.X10_text, self.X10_text_rect)
            SCREEN.blit(self.X100, self.X100_rect)
            SCREEN.blit(self.X100_text, self.X100_text_rect)
            self.AutoMouse_surf.fill((100, 127, 100)); self.Grandma_surf.fill((100, 127, 100));self.Farm_surf.fill((100, 127, 100))
            self.Mine_surf.fill((100, 127, 100));self.Factory_surf.fill((100, 127, 100)); self.Bank_surf.fill((100, 127, 100))
            self.Temple_surf.fill((100,127,100)); self.Wizard_Tower_surf.fill((100, 127, 100)); self.Shipment_surf.fill((100, 127, 100))
            self.AL_surf.fill((100,127,100)); self.Portal_Surf.fill((100,127,100));self.TM_Surf.fill((100,127,100))
            self.AC_Surf.fill((100,127,100)); self.Prism_Surf.fill((100,127,100)); self.ChanceMaker_Surf.fill((100,127,100))
            self.FE_Surf.fill((100,127,100));self.PC_Surf.fill((100,127,100)); self.IV_Surf.fill((100,127,100))
            self.CB_Surf.fill((100,127,100))
            SCREEN.blit(self.AutoMouse_surf, self.AutoMouse_rect)
            SCREEN.blit(self.AutoMouse_image, self.AutoMouse_image_rect)
            SCREEN.blit(self.AMUpgrade1cost_text, self.AutoMouse_Cost_text_rect)
            SCREEN.blit(self.AMName,self.AutoMouse_amount_rect)
            SCREEN.blit(self.Grandma_surf, self.Grandma_rect)
            SCREEN.blit(self.Grandma_image,self.Grandma_image_rect)
            SCREEN.blit(self.GrandmaUpgrade_text, self.Grandma_Cost_rect)
            SCREEN.blit(self.GrandName,self.Grandma_amount_rect)
            SCREEN.blit(self.Farm_surf, self.Farm_rect)
            SCREEN.blit(self.Farm_image, self.Farm_image_rect)
            SCREEN.blit(self.FarmUpgrade_text, self.Farm_Cost_rect)
            SCREEN.blit(self.FarmName,self.FarmAmount_rect)
            SCREEN.blit(self.Mine_surf, self.Mine_rect)
            SCREEN.blit(self.Mine_image,self.Mine_image_rect)
            SCREEN.blit(self.MineUpgrade_tect,self.MineCost_rect)
            SCREEN.blit(self.MineName,self.MineAmount_rect)
            SCREEN.blit(self.Factory_surf, self.Factory_rect)
            SCREEN.blit(self.Factory_image, self.Factory_image_rect)
            SCREEN.blit(self.FactoryUpgrade_text, self.FactoryCost_rect)
            SCREEN.blit(self.FactName,self.FactoryAmount_rect)
            SCREEN.blit(self.Bank_surf, self.Bank_rect)
            SCREEN.blit(self.Bank_image, self.Bank_image_rect)
            SCREEN.blit(self.BankUpgrade_text, self.BankCost_rect)
            SCREEN.blit(self.BankName,self.BankAmount_rect)
            SCREEN.blit(self.Temple_surf, self.Temple_rect)
            SCREEN.blit(self.Temple_image, self.Temple_image_rect)
            SCREEN.blit(self.TempleUpgrade_text, self.TempleCost_rect)
            SCREEN.blit(self.TempleName,self.TempleAmount_rect)
            SCREEN.blit(self.Wizard_Tower_surf, self.Wizard_Tower_rect)
            SCREEN.blit(self.WT_image,self.WT_image_rect)
            SCREEN.blit(self.WTUpgrade_Text,self.WTCost_rect)
            SCREEN.blit(self.WTName,self.WTAmount_rect)
            SCREEN.blit(self.Shipment_surf,self.Shipment_rect)
            SCREEN.blit(self.ShipmentUpgradeCost_Text, self.ShipmentCost_rect)
            SCREEN.blit(self.Shipment_image,self.Shipment_image_rect)
            SCREEN.blit(self.ShipName,self.ShipmentAmount_rect)
            SCREEN.blit(self.AL_surf,self.AL_rect)
            SCREEN.blit(self.AL_image,self.AL_image_rect)
            SCREEN.blit(self.ALUpgradeCost_text,self.ALCost_rect)
            SCREEN.blit(self.ALName, self.ALAmount_rect)
            SCREEN.blit(self.Portal_Surf, self.Portal_rect)
            SCREEN.blit(self.Portal_image, self.Portal_image_rect)
            SCREEN.blit(self.PortalUpgradeCost_text,self.PortalCost_rect)
            SCREEN.blit(self.PortalName,self.PortalAmount_rect)
            SCREEN.blit(self.TM_Surf, self.TM_rect)
            SCREEN.blit(self.TM_image, self.TM_image_rect)
            SCREEN.blit(self.TMUpgradeCost_text,self.TMCost_rect)
            SCREEN.blit(self.TMName,self.TMAmount_rect)
            SCREEN.blit(self.AC_Surf, self.AC_rect)
            SCREEN.blit(self.AC_image, self.AC_image_rect)
            SCREEN.blit(self.ACUpgradeCost_text,self.ACCost_rect)
            SCREEN.blit(self.ACName,self.ACAmount_rect)
            SCREEN.blit(self.Prism_Surf, self.Prism_rect)
            SCREEN.blit(self.Prism_image, self.Prism_image_rect)
            SCREEN.blit(self.PrismUpgradeCost_text, self.PrismCost_rect)
            SCREEN.blit(self.PrismName,self.PrismAmount_rect)
            SCREEN.blit(self.ChanceMaker_Surf, self.ChanceMaker_rect)
            SCREEN.blit(self.ChanceMaker_image, self.ChanceMaker_image_rect)
            SCREEN.blit(self.ChanceMakerUpgradeCost_text,self.ChanceMakerCost_rect)
            SCREEN.blit(self.CMName,self.ChanceMakerAmount_rect)
            SCREEN.blit(self.FE_Surf,self.FE_rect)
            SCREEN.blit(self.FE_image,self.FE_image_rect)
            SCREEN.blit(self.FEUpgradeCost_text,self.FECost_rect)
            SCREEN.blit(self.FEName,self.FEAmount_rect)
            SCREEN.blit(self.PC_Surf,self.PC_rect)
            SCREEN.blit(self.PC_image,self.PC_image_rect)
            SCREEN.blit(self.PCUpgradeCost_text,self.PCCost_rect)
            SCREEN.blit(self.PCName,self.PCAmount_rect)
            SCREEN.blit(self.IV_Surf,self.IV_rect)
            SCREEN.blit(self.IV_image,self.IV_image_rect)
            SCREEN.blit(self.IVUpgradeCost_text,self.IVCost_rect)
            SCREEN.blit(self.IVName,self.IVAmount_rect)
            SCREEN.blit(self.CB_Surf,self.CB_rect)
            SCREEN.blit(self.CB_image,self.CB_image_rect)
            SCREEN.blit(self.CBUpgradeCost_text,self.CBCost_rect)
            SCREEN.blit(self.CBName,self.CBAmount_rect)
            self.AMUpgrade1()
            self.AMCost_req()
            self.GrandmaUpgrade()
            self.GrandmaCost_req()
            self.FarmUpgrade()
            self.Farmcost_req()
            self.MineUpgrade()
            self.Minecost_req()
            self.FactoryUpgrade()
            self.FactoryUpgrade_req()
            self.BankUpgrade()
            self.BankUpgrade_req()
            self.TempleUpgrade()
            self.TempleUpgrade_req()
            self.WTUpgrade()
            self.WTUpgrade_req()
            self.ShipmentUpgrades()
            self.ShipmentUpgrade_req()
            self.ALUpgrades()
            self.ALupgrade_req()
            self.PortalUpgrades()
            self.PortalUpgrade_req()
            self.TMUpgrades()
            self.TMUpgrades_req()
            self.PrismUpgrades()
            self.PrismUpgrade_req()
            self.ChanceMakerUpgrades()
            self.ChanceMakerupgrade_req()
            self.FEUpgrades()
            self.FEUpgrades_req()
            self.PCUpgrades()
            self.PCUpgrades_req()
            self.IVUpgrade()
            self.IVUpgrade_req()
            self.CBUpgrade()
            self.CBUpgrade_req()

    def AMUpgrade1(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.AutoMouse_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed and OC["AMAmount"] > 0:
                    if OC["Autoupgrade"] == 100 and OC["Clicks"] >= OC["Autoupgrade"] and OC["Autoupgrade"] != "Done":
                            OC["Clicks"] -= OC["Autoupgrade"]
                            OC["AMX"] *= 2
                            OC["UpgradeAmount"] += 1
                           
                            OC["Autoupgrade"] = 500
                            self.AMDisplay_Text = 500
                    elif OC["Autoupgrade"] == 500 and OC["Clicks"] >= OC["Autoupgrade"]:
                            OC["Clicks"] -= OC["Autoupgrade"]
                            OC["AMX"] *= 2
                            OC["UpgradeAmount"] += 1
                            OC["amupgrade1cost"] = True
                    elif OC["Autoupgrade"] == 10000 and OC["Clicks"] >= OC["Autoupgrade"]:
                            OC["Clicks"] -= OC["Autoupgrade"]
                            OC["AMX"] *= 2
                            OC["UpgradeAmount"] += 1
                            OC["amupgrade1cost"] = False
                            OC["amupgrade2cost"] = True
                    elif OC["Autoupgrade"] == 100_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADD"] = True
                        OC["amupgrade3cost"] = True
                        OC["amupgrade2cost"] = False
                        print("Done")
                    elif OC["Autoupgrade"] == 10_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 5
                        OC["amupgrade3cost"], OC["amupgrade4cost"] = False, True
                    elif OC["Autoupgrade"] == 100_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 10
                        OC["amupgrade4cost"], OC["amupgrade5cost"] = False, True
                    elif OC["Autoupgrade"] == 1_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["amupgrade5cost"], OC["amupgrade6cost"] = False, True
                    elif OC["Autoupgrade"] == 10_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["amupgrade6cost"], OC["amupgrade7cost"] = False, True
                    elif OC["Autoupgrade"] == 10_000_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["amupgrade7cost"], OC["amupgrade8cost"] = False, True
                    elif OC["Autoupgrade"] == 10_000_000_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["amupgrade8cost"], OC["amupgrade9cost"] = False, True
                    elif OC["Autoupgrade"] == 10_000_000_000_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["amupgrade9cost"], OC["amupgrade10cost"] = False, True
                    elif OC["Autoupgrade"] == 10_000_000_000_000_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["amupgrade10cost"], OC["amupgrade11cost"] = False, True
                    elif OC["Autoupgrade"] == 10_000_000_000_000_000_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["amupgrade11cost"], OC["amupgrade12cost"] = False, True
                    elif OC["Autoupgrade"] == 10_000_000_000_000_000_000_000_000_000 and OC["Clicks"] >= OC["Autoupgrade"]:
                        OC["Clicks"] -= OC["Autoupgrade"]
                        OC["UpgradeAmount"] += 1
                        OC["AMADDERX"] *= 20
                        OC["Autoupgrade"] = "Done"
                        OC["amupgrade12cost"] = False
                self.pressed = False

    def Costs_calc(self, Base_price, Amount_owned):
        New_price = float(Base_price) * (1.15**Amount_owned)
        New_price = math.ceil(New_price)
        return New_price

    def AMCost_req(self):
        if OC["amupgrade1cost"]:
            if OC["AMAmount"] < 10: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 10:OC["Autoupgrade"] = 10_000; self.AMDisplay_Text = "10K"
        elif OC["amupgrade2cost"]:
            if OC["AMAmount"] < 25: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 25:OC["Autoupgrade"] = 100_000; self.AMDisplay_Text = "100K"
        elif OC["amupgrade3cost"]:
            if OC["AMAmount"] < 50: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 50: OC["Autoupgrade"] = 10_000_000; self.AMDisplay_Text = "10m"
        elif OC["amupgrade4cost"]:
            if OC["AMAmount"] < 100: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 100: OC["Autoupgrade"] = 100_000_000; self.AMDisplay_Text = "100m"
        elif OC["amupgrade5cost"]:
            if OC["AMAmount"] < 150: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 150: OC["Autoupgrade"] = 1_000_000_000; self.AMDisplay_Text = "1B"
        elif OC["amupgrade6cost"]:
            if OC["AMAmount"] < 200: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 200: OC["Autoupgrade"] = 10_000_000_000; self.AMDisplay_Text = "10B"
        elif OC["amupgrade7cost"]:
            if OC["AMAmount"] < 250: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 250: OC["Autoupgrade"] = 10_000_000_000_000; self.AMDisplay_Text = "10T"
        elif OC["amupgrade8cost"]:
            if OC["AMAmount"] < 300: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 300: OC["Autoupgrade"] = 10_000_000_000_000_000; self.AMDisplay_Text = "10Q"
        elif OC["amupgrade9cost"]:
            if OC["AMAmount"] < 350: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 350: OC["Autoupgrade"] = 10_000_000_000_000_000_000; self.AMDisplay_Text = "10 QT"
        elif OC["amupgrade10cost"]:
            if OC["AMAmount"] < 400: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 400: OC["Autoupgrade"] = 10_000_000_000_000_000_000_000; self.AMDisplay_Text = "10 ST"
        elif OC["amupgrade11cost"]:
            if OC["AMAmount"] < 450: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 450: OC["Autoupgrade"] = 10_000_000_000_000_000_000_000_000; self.AMDisplay_Text = "10 SEPT"
        elif OC["amupgrade12cost"]:
            if OC["AMAmount"] < 500: OC["Autoupgrade"] = "TBC"; self.AMDisplay_Text = "TBC"
            elif OC["AMAmount"] >= 500: OC["Autoupgrade"] = 10_000_000_000_000_000_000_000_000_000; self.AMDisplay_Text = "10OCT"

    def CC_AutoMouse(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.AutoMouse_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.AutoMousecost:
                            OC["Clicks"] -= self.AutoMousecost
                            if self.x10:
                                OC["AMAmount"] += 10
                                OC['ItemAmount'] += 10
                            elif self.x100:
                                OC["AMAmount"] += 100
                                OC['ItemAmount'] += 100
                            else: 
                                OC["AMAmount"] += 1
                                OC['ItemAmount'] += 1
                            OC["AMcost"] = self.Costs_calc(15, OC["AMAmount"])
                            self.AutoMousecost = OC["AMcost"]
                    elif self.sell:
                        if self.x1 and OC["AMAmount"] > 0:
                                OC["AMAmount"] -= 1
                                OC["Clicks"] += self.AutoMousecost
                        elif self.x10 and OC["AMAmount"] >= 10:
                                OC["AMAmount"] -= 10
                                OC["Clicks"] += self.AutoMousecost
                        elif self.x100 and  OC["AMAmount"] >= 100: 
                                OC["AMAmount"] -= 100; OC["Clicks"] += self.AutoMousecost
                        OC["AMcost"] = self.Costs_calc(15, OC["AMAmount"])
                        self.AutoMousecost = OC["AMcost"]
                    self.pressed = False

    def AMFunc(self):
        if OC["AMAmount"]:
            for _ in range(OC["AMAmount"]):
                if OC["AMADD"]: self.AutoCount += (1*OC["AMX"]) + (OC["AMADDER"]*OC["AMADDERX"])
                elif not OC["AMADD"]: self.AutoCount += (1*OC["AMX"])
                if self.AutoCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.AutoCount -= 10
        self.Toptext = Game_Font.render(f"{OC['Clicks']} Oreos", True, "White")

    def CC_Grandma(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Grandma_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.GrandmaCost:
                            OC["Clicks"] -= self.GrandmaCost
                            if self.x10:
                                OC["GrandAmount"] += 10
                              
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            
                            elif self.x100:
                                OC["GrandAmount"] += 100
                               
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                               
                            else: 
                                OC["GrandAmount"] += 1
                             
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                               
                            OC["Grandcost"] = self.Costs_calc(100,OC["GrandAmount"])
                            self.GrandmaCost = OC["Grandcost"]
                    elif self.sell:
                        if self.x1 and OC["GrandAmount"] > 0:
                            OC["GrandAmount"] -= 1
                            
                            OC["Clicks"] += self.GrandmaCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                            
                        elif self.x10 and OC["GrandAmount"] >= 10:
                            OC["GrandAmount"] -= 10
                            OC['ItemAmount'] -= 10
                         
                            OC["Clicks"] += self.GrandmaCost
                            OC["AMADDER"] -= 1
                     
                        elif self.x100 and OC["GrandAmount"] >= 100:
                            OC["GrandAmount"] -= 100
                            
                            OC["Clicks"] += self.GrandmaCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["Grandcost"] = self.Costs_calc(100,OC["GrandAmount"])
                        self.GrandmaCost = OC["Grandcost"]
                    self.pressed = False
    
    def GrandmaFunc(self):
        if OC["GrandAmount"]:
            for _ in range(OC["GrandAmount"]):
                self.Grandcount += (10*OC["GrandX"])
                if self.Grandcount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.Grandcount -= 10

    def FarmFunc(self):
        if OC["FarmAmount"]:
            for _ in range(OC["FarmAmount"]):
                self.FarmCount += (80*OC["FarmX"])
                for i in range(0,self.FarmCount + 1, 10):
                    if self.FarmCount >= 10:
                        OC["Clicks"] += 1
                        OC["AllClicks"] += 1
                        OC['ShopClicks'] += 1
                        self.FarmCount -= 10
                    
    def GrandmaUpgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Grandma_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed and OC["GrandAmount"] > 0 and OC["GrandmaUpgradecost"] != "TBC" and OC["GrandmaUpgradecost"] != "Done":
                    if OC["Clicks"] >= OC["GrandmaUpgradecost"]:
                        OC["Clicks"] -= OC["GrandmaUpgradecost"]
                        OC["GrandX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["GrandmaUpgradecost"] == 1000:
                            OC["grandmaupgrade1cost"] = True
                        elif OC["GrandmaUpgradecost"] == 5000 :
                            OC["grandmaupgrade1cost"],OC["grandmaupgrade2cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50000 :
                            OC["grandmaupgrade2cost"],OC["grandmaupgrade3cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 5_000_000 :
                            OC["grandmaupgrade3cost"],OC["grandmaupgrade4cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 500_000_000:
                           OC["grandmaupgrade4cost"],OC["grandmaupgrade5cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50_000_000_000: 
                            OC["grandmaupgrade5cost"],OC["grandmaupgrade6cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50_000_000_000_000:
                            OC["grandmaupgrade6cost"],OC["grandmaupgrade7cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50_000_000_000_000_000:
                            OC["grandmaupgrade7cost"],OC["grandmaupgrade8cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50_000_000_000_000_000_000:
                            OC["grandmaupgrade8cost"],OC["grandmaupgrade9cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50_000_000_000_000_000_000_000:
                            OC["grandmaupgrade9cost"],OC["grandmaupgrade10cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50_000_000_000_000_000_000_000_000:
                            OC["grandmaupgrade10cost"],OC["grandmaupgrade11cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 5_000_000_000_000_000_000_000_000_000_000:
                            OC["grandmaupgrade11cost"],OC["grandmaupgrade12cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 50_000_000_000_000_000_000_000_000_000_000_000:
                            OC["grandmaupgrade12cost"],OC["grandmaupgrade13cost"] = False,True
                        elif OC["GrandmaUpgradecost"] == 500_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["grandmaupgrade13cost"] = False
                            OC["GrandmaUpgradecost"] = "Done"
                self.pressed = False

    def GrandmaCost_req(self):
        if OC["grandmaupgrade1cost"]:
            if OC["GrandAmount"] < 5: OC["GrandmaUpgradecost"] = "TBC";self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 5: OC["GrandmaUpgradecost"] = 5_000; self.GranddisplayText = "5K"
        elif OC["grandmaupgrade2cost"]:
            if OC["GrandAmount"] < 25: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 25: OC["GrandmaUpgradecost"] = 50_000; self.GranddisplayText = "50K"
        elif OC["grandmaupgrade3cost"]:
            if OC["GrandAmount"] < 50: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 50: OC["GrandmaUpgradecost"] = 5_000_000; self.GranddisplayText = "5m"
        elif OC["grandmaupgrade4cost"]:
            if OC["GrandAmount"] < 100: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 100: OC["GrandmaUpgradecost"] = 500_000_000; self.GranddisplayText = "500m"
        elif OC["grandmaupgrade5cost"]:
            if OC["GrandAmount"] < 150: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 150: OC["GrandmaUpgradecost"] = 50_000_000_000; self.GranddisplayText = "50B"
        elif OC["grandmaupgrade6cost"]:
            if OC["GrandAmount"] < 200: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 200: OC["GrandmaUpgradecost"] = 50_000_000_000_000; self.GranddisplayText = "50T"
        elif OC["grandmaupgrade7cost"]:
            if OC["GrandAmount"] < 250: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 250: OC["GrandmaUpgradecost"] = 50_000_000_000_000_000; self.GranddisplayText = "50Q"
        elif OC["grandmaupgrade8cost"]:
            if OC["GrandAmount"] < 300: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 300: OC["GrandmaUpgradecost"] = 50_000_000_000_000_000_000; self.GranddisplayText = "50 QT"
        elif OC["grandmaupgrade9cost"]:
            if OC["GrandAmount"] < 350: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 350: OC["GrandmaUpgradecost"] = 50_000_000_000_000_000_000_000; self.GranddisplayText = "50 ST"
        elif OC["grandmaupgrade10cost"]:
            if OC["GrandAmount"] < 400: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 400: OC["GrandmaUpgradecost"] = 50_000_000_000_000_000_000_000_000; self.GranddisplayText = "50 sept"
        elif OC["grandmaupgrade11cost"]:
            if OC["GrandAmount"] < 450: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 450: OC["GrandmaUpgradecost"] = 5_000_000_000_000_000_000_000_000_000_000; self.GranddisplayText = "50 non"
        elif OC["grandmaupgrade12cost"]:
            if OC["GrandAmount"] < 500: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 500: OC["GrandmaUpgradecost"] = 50_000_000_000_000_000_000_000_000_000_000_000; self.GranddisplayText = "50 Dec"
        elif OC["grandmaupgrade13cost"]:
            if OC["GrandAmount"] < 550: OC["GrandmaUpgradecost"] = "TBC"; self.GranddisplayText = "TBC"
            elif OC["GrandAmount"] >= 550: OC["GrandmaUpgradecost"] = 500_000_000_000_000_000_000_000_000_000_000_000_000; self.GranddisplayText = "50 UNDec"
    
    def CC_Farm(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Farm_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.FarmCost:
                            OC["Clicks"] -= self.FarmCost
                            if self.x10:
                                OC["FarmAmount"] += 10
                                
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                         
                            elif self.x100:
                                OC["FarmAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["FarmAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC["FarmCost"] = self.Costs_calc(1100,OC["FarmAmount"])
                            self.FarmCost = OC["FarmCost"]
                    elif self.sell:
                        if self.x1 and OC["FarmAmount"] > 0:
                            OC["FarmAmount"] -= 1
                            OC["Clicks"] += self.FarmCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC["FarmAmount"] >= 10:
                            OC["FarmAmount"] -= 10
                            OC["Clicks"] += self.FarmCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC["FarmAmount"] >= 100:
                            OC["FarmAmount"] -= 10
                            OC["Clicks"] += self.FarmCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["FarmCost"] = self.Costs_calc(1100,OC["FarmAmount"])
                        self.FarmCost = OC["FarmCost"]
                    self.pressed = False

    def FarmUpgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Farm_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed and OC["FarmAmount"] > 0 and OC["Farmupgradecost"] != "TBC" and OC["Farmupgradecost"] != "Done":
                    if OC["Clicks"] >= OC["Farmupgradecost"]:
                        OC["Clicks"] -= OC["Farmupgradecost"]
                        OC["FarmX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["Farmupgradecost"] == 11000:
                            OC["farmupgrade1cost"] = True
                        elif OC["Farmupgradecost"] == 55000:
                            OC["farmupgrade1cost"],OC["farmupgrade2cost"] = False,True
                        elif OC["Farmupgradecost"] == 550_000:
                            OC["farmupgrade2cost"],OC["farmupgrade3cost"] = False,True
                        elif OC["Farmupgradecost"] == 55_000_000:
                            OC["farmupgrade3cost"],OC["farmupgrade4cost"] = False,True
                        elif OC["Farmupgradecost"] == 5_500_000_000:
                            OC["farmupgrade4cost"],OC["farmupgrade5cost"] = False,True
                        elif OC["Farmupgradecost"] == 550_000_000_000:
                            OC["farmupgrade5cost"],OC["farmupgrade6cost"] = False,True
                        elif OC["Farmupgradecost"] == 550_000_000_000_000:
                            OC["farmupgrade6cost"],OC["farmupgrade7cost"] = False,True
                        elif OC["Farmupgradecost"] == 550_000_000_000_000_000:
                            OC["farmupgrade7cost"],OC["farmupgrade8cost"] = False,True
                        elif OC["Farmupgradecost"] == 550_000_000_000_000_000_000:
                            OC["farmupgrade8cost"],OC["farmupgrade9cost"] = False,True
                        elif OC["Farmupgradecost"] == 550_000_000_000_000_000_000_000:
                            OC["farmupgrade9cost"],OC["farmupgrade10cost"] = False,True
                        elif OC["Farmupgradecost"] == 5_500_000_000_000_000_000_000_000_000:
                            OC["farmupgrade10cost"],OC["farmupgrade11cost"] = False,True
                        elif OC["Farmupgradecost"] == 55_000_000_000_000_000_000_000_000_000_000:
                            OC["farmupgrade11cost"],OC["farmupgrade12cost"] = False,True
                        elif OC["Farmupgradecost"] == 550_000_000_000_000_000_000_000_000_000_000_000:
                            OC["farmupgrade12cost"],OC["farmupgrade13cost"] = False,True
                        elif OC["Farmupgradecost"] == 5500000000000000000000000000000000000000:
                            OC["farmupgrade13cost"], self.FarmDisplaycost,OC["Farmupgradecost"]  = False,"Done","Done"
                self.pressed = False
    
    def Farmcost_req(self):
        if OC["farmupgrade1cost"]:
            if OC["FarmAmount"] < 5: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 5: OC["Farmupgradecost"] = 55_000;self.FarmDisplaycost = "55K"
        elif OC["farmupgrade2cost"]:
            if OC["FarmAmount"] < 25: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 25: OC["Farmupgradecost"] = 550_000;self.FarmDisplaycost = "550K"
        elif OC["farmupgrade3cost"]:
            if OC["FarmAmount"] < 50: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 50: OC["Farmupgradecost"] = 55_000_000;self.FarmDisplaycost = "55m"
        elif OC["farmupgrade4cost"]:
            if OC["FarmAmount"] < 100: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 100: OC["Farmupgradecost"] = 5_500_000_000;self.FarmDisplaycost = "5.5B"
        elif OC["farmupgrade5cost"]:
            if OC["FarmAmount"] < 150: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 150: OC["Farmupgradecost"] = 550_000_000_000;self.FarmDisplaycost = "550B"
        elif OC["farmupgrade6cost"]:
            if OC["FarmAmount"] < 200: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 200: OC["Farmupgradecost"] = 550_000_000_000_000;self.FarmDisplaycost = "550T"
        elif OC["farmupgrade7cost"]:
            if OC["FarmAmount"] < 250: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 250: OC["Farmupgradecost"] = 550_000_000_000_000_000;self.FarmDisplaycost = "550Q"
        elif OC["farmupgrade8cost"]:
            if OC["FarmAmount"] < 300: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 300: OC["Farmupgradecost"] = 550_000_000_000_000_000_000;self.FarmDisplaycost = "550QT"
        elif OC["farmupgrade9cost"]:
            if OC["FarmAmount"] < 350: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 350: OC["Farmupgradecost"] = 550_000_000_000_000_000_000_000;self.FarmDisplaycost = "550S"
        elif OC["farmupgrade10cost"]:
            if OC["FarmAmount"] < 400: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 400: OC["Farmupgradecost"] = 5_500_000_000_000_000_000_000_000_000;self.FarmDisplaycost = "5.5O"
        elif OC["farmupgrade11cost"]:
            if OC["FarmAmount"] < 450: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 450: OC["Farmupgradecost"] = 55_000_000_000_000_000_000_000_000_000_000;self.FarmDisplaycost = "55N"
        elif OC["farmupgrade12cost"]:
            if OC["FarmAmount"] < 500: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 500: OC["Farmupgradecost"] = 550_000_000_000_000_000_000_000_000_000_000_000;self.FarmDisplaycost = "550D"
        elif OC["farmupgrade13cost"]:
            if OC["FarmAmount"] < 550: OC["Farmupgradecost"] = "TBC";self.FarmDisplaycost = "TBC"
            elif OC["FarmAmount"] >= 550: OC["Farmupgradecost"] = 5_500_000_000_000_000_000_000_000_000_000_000_000_000;self.FarmDisplaycost = "5.5DuoD"
    
    def CC_Mine(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Mine_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.MineCost:
                            OC["Clicks"] -= self.MineCost
                            if self.x10:
                                OC["MineAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["MineAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["MineAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                        OC["MineCost"] = self.Costs_calc(12000,OC["MineAmount"])
                        self.MineCost = OC["MineCost"]
                    elif self.sell:
                        if self.x1 and OC["MineAmount"] > 0:
                            OC["MineAmount"] -= 1
                            OC["Clicks"] += self.MineCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC["MineAmount"] >= 10:
                            OC["MineAmount"] -= 10
                            OC["Clicks"] += self.MineCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC["MineAmount"] > 100:
                            OC["MineAmount"] -= 100
                            OC["Clicks"] += self.MineCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["MineCost"] = self.Costs_calc(12000,OC["MineAmount"])
                        self.MineCost = OC["MineCost"]
                self.pressed = False

    def MineFunc(self):
        if OC["MineAmount"]:
            for _ in range(OC["MineAmount"]):
                self.MineCount += (470*OC["FarmX"])
                for i in range(0,self.MineCount + 1, 10):
                    if self.MineCount >= 10:
                        OC["Clicks"] += 1
                        OC["AllClicks"] += 1
                        OC['ShopClicks'] += 1
                        self.MineCount -= 10

    def MineUpgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Mine_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed and OC["MineAmount"] > 0 and OC["MineUpgradecost"] != "TBC" and OC["MineUpgradecost"] != "Done":
                    if OC["Clicks"] >= OC["MineUpgradecost"]:
                        OC["Clicks"] -= OC["MineUpgradecost"]
                        OC["MineX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["MineUpgradecost"] == 120_000:
                            OC["Mineupgrade1cost"] = True
                        elif OC["MineUpgradecost"] == 600_000:
                            OC["Mineupgrade1cost"],OC["Mineupgrade2cost"] = False,True
                        elif OC["MineUpgradecost"] == 6_000_000:
                            OC["Mineupgrade2cost"],OC["Mineupgrade3cost"] = False,True
                        elif OC["MineUpgradecost"] == 600_000_000:
                            OC["Mineupgrade3cost"],OC["Mineupgrade4cost"] = False,True
                        elif OC["MineUpgradecost"] == 60_000_000_000:
                            OC["Mineupgrade4cost"],OC["Mineupgrade5cost"] = False,True
                        elif OC["MineUpgradecost"] == 6_000_000_000_000:
                            OC["Mineupgrade5cost"],OC["Mineupgrade6cost"] = False,True
                        elif OC["MineUpgradecost"] == 6_000_000_000_000_000:
                            OC["Mineupgrade6cost"],OC["Mineupgrade7cost"] = False,True
                        elif OC["MineUpgradecost"] == 6_000_000_000_000_000_000:
                            OC["Mineupgrade7cost"],OC["Mineupgrade8cost"] = False,True
                        elif OC["MineUpgradecost"] == 6_000_000_000_000_000_000_000:
                            OC["Mineupgrade8cost"],OC["Mineupgrade9cost"] = False,True
                        elif OC["MineUpgradecost"] == 6_000_000_000_000_000_000_000_000:
                            OC["Mineupgrade9cost"],OC["Mineupgrade10cost"] = False,True
                        elif OC["MineUpgradecost"] == 60_000_000_000_000_000_000_000_000_000:
                            OC["Mineupgrade10cost"],OC["Mineupgrade11cost"] = False,True
                        elif OC["MineUpgradecost"] == 600_000_000_000_000_000_000_000_000_000_000:
                            OC["Mineupgrade11cost"],OC["Mineupgrade12cost"] = False,True
                        elif OC["MineUpgradecost"] == 6_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["Mineupgrade12cost"],OC["Mineupgrade13cost"] = False,True
                        elif OC["MineUpgradecost"] == 60_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["Mineupgrade13cost"] = False;OC["MineUpgradecost"],self.MineUpgradecost = "Done","Done"
                self.pressed = False
    
    def Minecost_req(self):
        if OC["Mineupgrade1cost"]:
            if OC["MineAmount"] < 5: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 5: OC["MineUpgradecost"] = 600_000; self.MineUpgradecost = "600K"
        elif OC["Mineupgrade2cost"]:
            if OC["MineAmount"] < 25: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 25: OC["MineUpgradecost"] = 6_000_000; self.MineUpgradecost = "6m"
        elif OC["Mineupgrade3cost"]:
            if OC["MineAmount"] < 50: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 50: OC["MineUpgradecost"] = 600_000_000; self.MineUpgradecost = "600m"
        elif OC["Mineupgrade4cost"]:
            if OC["MineAmount"] < 100: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 100: OC["MineUpgradecost"] = 60_000_000_000; self.MineUpgradecost = "60B"
        elif OC["Mineupgrade5cost"]:
            if OC["MineAmount"] < 150: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 150: OC["MineUpgradecost"] = 6_000_000_000_000; self.MineUpgradecost = "6T"
        elif OC["Mineupgrade6cost"]:
            if OC["MineAmount"] < 200: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 200: OC["MineUpgradecost"] = 6_000_000_000_000_000; self.MineUpgradecost = "6Q"
        elif OC["Mineupgrade7cost"]:
            if OC["MineAmount"] < 250: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 250: OC["MineUpgradecost"] = 6_000_000_000_000_000_000; self.MineUpgradecost = "6QT"
        elif OC["Mineupgrade8cost"]:
            if OC["MineAmount"] < 300: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 300: OC["MineUpgradecost"] = 6_000_000_000_000_000_000_000; self.MineUpgradecost = "6S"
        elif OC["Mineupgrade9cost"]:
            if OC["MineAmount"] < 350: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 350: OC["MineUpgradecost"] = 6_000_000_000_000_000_000_000_000; self.MineUpgradecost = "6Sept"
        elif OC["Mineupgrade10cost"]:
            if OC["MineAmount"] < 400: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 400: OC["MineUpgradecost"] = 60_000_000_000_000_000_000_000_000_000; self.MineUpgradecost = "60O"
        elif OC["Mineupgrade11cost"]:
            if OC["MineAmount"] < 450: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 450: OC["MineUpgradecost"] = 600_000_000_000_000_000_000_000_000_000_000; self.MineUpgradecost = "600N"
        elif OC["Mineupgrade12cost"]:
            if OC["MineAmount"] < 500: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 500: OC["MineUpgradecost"] = 6_000_000_000_000_000_000_000_000_000_000_000_000; self.MineUpgradecost = "6UND"
        elif OC["Mineupgrade13cost"]:
            if OC["MineAmount"] < 550: OC["MineUpgradecost"] = "TBC"; self.MineUpgradecost = "TBC"
            elif OC["MineAmount"] >= 550: OC["MineUpgradecost"] = 60_000_000_000_000_000_000_000_000_000_000_000_000_000; self.MineUpgradecost = "6DUOD"
    
    def CC_Factory(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Factory_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.FactoryCost:
                            OC["Clicks"] -= self.FactoryCost
                            if self.x10:
                                OC["FactoryAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["FactoryAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["FactoryAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                        OC["FactoryCost"] = self.Costs_calc(130_000, OC["FactoryAmount"])
                        self.FactoryCost = OC["FactoryCost"]
                    elif self.sell:
                        if self.x1 and OC["FactoryAmount"] > 0:
                            OC["FactoryAmount"] -= 1
                            OC["Clicks"] += self.FactoryCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC["FactoryAmount"] >= 10:
                            OC["FactoryAmount"] -= 10
                            OC["Clicks"] += self.FactoryCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC["FactoryAmount"] >= 100:
                            OC["FactoryAmount"] -= 100
                            OC["Clicks"] += self.FactoryCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["FactoryCost"] = self.Costs_calc(130_000, OC["FactoryAmount"])
                        self.FactoryCost = OC["FactoryCost"]
                self.pressed = False

    def FactoryFunc(self):
        if OC["FactoryAmount"]:
            for _ in range(OC["FactoryAmount"]):
                self.FactoryCount += (2600*OC["FactoryX"])
                for i in range(0,self.FactoryCount + 1, 10):
                    if self.FactoryCount >= 10:
                        OC["Clicks"] += 1
                        OC["AllClicks"] += 1
                        OC['ShopClicks'] += 1
                        self.FactoryCount -= 10

    def FactoryUpgrade(self):
      mouse_pos = pygame.mouse.get_pos()
      if self.Factory_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:self.pressed = True
        else:
            if self.pressed and OC["FactoryAmount"] > 0 and OC["FactoryupgradeCost"] != "TBC" and OC["FactoryupgradeCost"] != "Done":
                if OC["Clicks"] >= OC["FactoryupgradeCost"]:
                    OC["Clicks"] -= OC["FactoryupgradeCost"]
                    OC["FactoryX"] *= 2
                    OC["UpgradeAmount"] += 1
                    if OC["FactoryupgradeCost"] == 1_300_000:
                            OC["factoryupgrade1Cost"] = True
                    elif OC["FactoryupgradeCost"] == 6_500_000:
                            OC["factoryupgrade1Cost"],OC["factoryupgrade2Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 65_000_000:
                            OC["factoryupgrade2Cost"],OC["factoryupgrade3Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 6_500_000_000:
                            OC["factoryupgrade3Cost"],OC["factoryupgrade4Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 650_000_000_000:
                            OC["factoryupgrade4Cost"],OC["factoryupgrade5Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 65_000_000_000_000:
                            OC["factoryupgrade5Cost"],OC["factoryupgrade6Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 65_000_000_000_000_000:
                            OC["factoryupgrade6Cost"],OC["factoryupgrade7Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 65_000_000_000_000_000_000:
                            OC["factoryupgrade7Cost"],OC["factoryupgrade8Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 65_000_000_000_000_000_000_000:
                            OC["factoryupgrade8Cost"],OC["factoryupgrade9Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 65_000_000_000_000_000_000_000_000:
                            OC["factoryupgrade9Cost"],OC["factoryupgrade10Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 650_000_000_000_000_000_000_000_000_000:
                            OC["factoryupgrade10Cost"],OC["factoryupgrade11Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 6_500_000_000_000_000_000_000_000_000_000_000:
                            OC["factoryupgrade11Cost"],OC["factoryupgrade12Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 65_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["factoryupgrade12Cost"],OC["factoryupgrade13Cost"] = False,True
                    elif OC["FactoryupgradeCost"] == 650_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["factoryupgrade13Cost"] = False; OC["FactoryupgradeCost"] = "Done";self.FactoryUpgradeCost = "Done"
            self.pressed = False

    def FactoryUpgrade_req(self):
        if OC["factoryupgrade1Cost"]:
            if OC["FactoryAmount"] < 5: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 5: OC["FactoryupgradeCost"] = 6_500_000;self.FactoryUpgradeCost = "6.5m"
        elif OC["factoryupgrade2Cost"]:
            if OC["FactoryAmount"] < 25: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 25: OC["FactoryupgradeCost"] = 65_000_000;self.FactoryUpgradeCost = "65m"
        elif OC["factoryupgrade3Cost"]:
            if OC["FactoryAmount"] < 50: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 50: OC["FactoryupgradeCost"] = 6_500_000_000;self.FactoryUpgradeCost = "6.5B"
        elif OC["factoryupgrade4Cost"]:
            if OC["FactoryAmount"] < 100: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 100: OC["FactoryupgradeCost"] = 650_000_000_000;self.FactoryUpgradeCost = "650B"
        elif OC["factoryupgrade5Cost"]:
            if OC["FactoryAmount"] < 150: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 150: OC["FactoryupgradeCost"] = 65_000_000_000_000;self.FactoryUpgradeCost = "65T"
        elif OC["factoryupgrade6Cost"]:
            if OC["FactoryAmount"] < 200: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 200: OC["FactoryupgradeCost"] = 65_000_000_000_000_000;self.FactoryUpgradeCost = "65Q"
        elif OC["factoryupgrade7Cost"]:
            if OC["FactoryAmount"] < 250: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 250: OC["FactoryupgradeCost"] = 65_000_000_000_000_000_000;self.FactoryUpgradeCost = "65QT"
        elif OC["factoryupgrade8Cost"]:
            if OC["FactoryAmount"] < 300: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 300: OC["FactoryupgradeCost"] = 65_000_000_000_000_000_000_000;self.FactoryUpgradeCost = "65S"
        elif OC["factoryupgrade9Cost"]:
            if OC["FactoryAmount"] < 350: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 350: OC["FactoryupgradeCost"] = 65_000_000_000_000_000_000_000_000;self.FactoryUpgradeCost = "65SepT"
        elif OC["factoryupgrade10Cost"]:
            if OC["FactoryAmount"] < 400: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 400: OC["FactoryupgradeCost"] = 650_000_000_000_000_000_000_000_000_000;self.FactoryUpgradeCost = "650O"
        elif OC["factoryupgrade11Cost"]:
            if OC["FactoryAmount"] < 450: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 450: OC["FactoryupgradeCost"] = 6_500_000_000_000_000_000_000_000_000_000_000;self.FactoryUpgradeCost = "6.5D"
        elif OC["factoryupgrade12Cost"]:
            if OC["FactoryAmount"] < 500: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 500: OC["FactoryupgradeCost"] = 65_000_000_000_000_000_000_000_000_000_000_000_000;self.FactoryUpgradeCost = "65UnD"
        elif OC["factoryupgrade13Cost"]:
            if OC["FactoryAmount"] < 550: OC["FactoryupgradeCost"] = "TBC";self.FactoryUpgradeCost = "TBC"
            elif OC["FactoryAmount"] >= 550: OC["FactoryupgradeCost"] = 650_000_000_000_000_000_000_000_000_000_000_000_000_000;self.FactoryUpgradeCost = "650DuoD"

    def CC_Bank(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Bank_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.BankCost:
                            OC["Clicks"] -= self.BankCost
                            if self.x10:
                                OC["BankAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["BankAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["BankAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                        OC["BankCost"] = self.Costs_calc(1_400_000, OC["BankAmount"])
                        self.FactoryCost = OC["BankCost"]
                    elif self.sell:
                        if self.x1 and OC["BankAmount"] > 0:
                            OC["BankAmount"] -= 1
                            OC["Clicks"] += self.BankCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC["BankAmount"] >= 10:
                            OC["BankAmount"] -= 10
                            OC["Clicks"] += self.BankCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC["BankAmount"] >= 100:
                            OC["BankAmount"] -= 100
                            OC["Clicks"] += self.BankCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["BankCost"] = self.Costs_calc(1_400_000, OC["BankAmount"])
                        self.FactoryCost = OC["BankCost"]
                self.pressed = False

    def BankFunc(self):
        if OC["BankAmount"]:
            for _ in range(OC["BankAmount"]):
                self.BankCount += (1_4000*OC["BankX"])
                for i in range(0,self.BankCount + 1, 10):
                    if self.BankCount >= 10:
                        OC["Clicks"] += 1
                        OC["AllClicks"] += 1
                        OC['ShopClicks'] += 1
                        self.BankCount -= 10

    def BankUpgrade(self): 
        mouse_pos = pygame.mouse.get_pos()
        if self.Bank_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed and OC["BankAmount"] > 0 and OC["BankUpgradeCost"] != "TBC" and OC["BankUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["BankUpgradeCost"]:
                        OC["Clicks"] -= OC["BankUpgradeCost"]
                        OC["BankX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["BankUpgradeCost"] == 14_000_000:
                            OC["bankupgrade1cost"] = True
                        elif OC["BankUpgradeCost"] == 70_000_000:
                            OC["bankupgrade1cost"],OC["bankupgrade2cost"] = False,True
                        elif OC["BankUpgradeCost"] == 700_000_000:
                            OC["bankupgrade2cost"],OC["bankupgrade3cost"] = False,True
                        elif OC["BankUpgradeCost"] == 70_000_000_000:
                            OC["bankupgrade3cost"],OC["bankupgrade4cost"] = False,True
                        elif OC["BankUpgradeCost"] == 7_000_000_000_000:
                            OC["bankupgrade4cost"],OC["bankupgrade5cost"] = False,True
                        elif OC["BankUpgradeCost"] == 700_000_000_000_000:
                            OC["bankupgrade5cost"],OC["bankupgrade6cost"] = False,True
                        elif OC["BankUpgradeCost"] == 700_000_000_000_000_000:
                            OC["bankupgrade6cost"],OC["bankupgrade7cost"] = False,True
                        elif OC["BankUpgradeCost"] == 700_000_000_000_000_000_000:
                            OC["bankupgrade7cost"],OC["bankupgrade8cost"] = False,True
                        elif OC["BankUpgradeCost"] == 700_000_000_000_000_000_000_000:
                            OC["bankupgrade8cost"],OC["bankupgrade9cost"] = False,True
                        elif OC["BankUpgradeCost"] == 700_000_000_000_000_000_000_000_000:
                            OC["bankupgrade9cost"],OC["bankupgrade10cost"] = False,True
                        elif OC["BankUpgradeCost"] == 7_000_000_000_000_000_000_000_000_000_000:
                            OC["bankupgrade10cost"],OC["bankupgrade11cost"] = False,True
                        elif OC["BankUpgradeCost"] == 70_000_000_000_000_000_000_000_000_000_000_000:
                            OC["bankupgrade11cost"],OC["bankupgrade12cost"] = False,True
                        elif OC["BankUpgradeCost"] == 700_000_000_000_000_000_000_000_000_000_000_000:
                            OC["bankupgrade12cost"],OC["bankupgrade13cost"] = False,True
                        elif OC["BankUpgradeCost"] == 7_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["bankupgrade13cost"] = False; self.BankUpgradeCost = "Done"; OC["BankUpgradeCost"] = "Done"
                self.pressed = False

    def BankUpgrade_req(self):
        if OC["bankupgrade1cost"]:
            if OC["BankAmount"] < 5: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 5: OC["BankUpgradeCost"] = 70_000_000; self.BankUpgradeCost = "70m"
        elif OC["bankupgrade2cost"]:
            if OC["BankAmount"] < 25: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 25: OC["BankUpgradeCost"] = 700_000_000; self.BankUpgradeCost = "700m"
        elif OC["bankupgrade3cost"]:
            if OC["BankAmount"] < 50: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 50: OC["BankUpgradeCost"] = 70_000_000_000; self.BankUpgradeCost = "70B"
        elif OC["bankupgrade4cost"]:
            if OC["BankAmount"] < 100: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 100: OC["BankUpgradeCost"] = 7_000_000_000_000; self.BankUpgradeCost = "7T"
        elif OC["bankupgrade5cost"]:
            if OC["BankAmount"] < 150: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 150: OC["BankUpgradeCost"] = 700_000_000_000_000; self.BankUpgradeCost = "700T"
        elif OC["bankupgrade6cost"]:
            if OC["BankAmount"] < 200: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 200: OC["BankUpgradeCost"] = 700_000_000_000_000_000; self.BankUpgradeCost = "700Q"
        elif OC["bankupgrade7cost"]:
            if OC["BankAmount"] < 250: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 250: OC["BankUpgradeCost"] = 700_000_000_000_000_000_000; self.BankUpgradeCost = "700QT"
        elif OC["bankupgrade8cost"]:
            if OC["BankAmount"] < 300: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 300: OC["BankUpgradeCost"] = 700_000_000_000_000_000_000_000; self.BankUpgradeCost = "700S"
        elif OC["bankupgrade9cost"]:
            if OC["BankAmount"] < 350: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 350: OC["BankUpgradeCost"] = 700_000_000_000_000_000_000_000_000; self.BankUpgradeCost = "700SepT"
        elif OC["bankupgrade10cost"]:
            if OC["BankAmount"] < 400: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 400: OC["BankUpgradeCost"] = 7_000_000_000_000_000_000_000_000_000_000; self.BankUpgradeCost = "7N"
        elif OC["bankupgrade11cost"]:
            if OC["BankAmount"] < 450: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 450: OC["BankUpgradeCost"] = 70_000_000_000_000_000_000_000_000_000_000_000; self.BankUpgradeCost = "70D"
        elif OC["bankupgrade12cost"]:
            if OC["BankAmount"] < 500: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 500: OC["BankUpgradeCost"] = 700_000_000_000_000_000_000_000_000_000_000_000; self.BankUpgradeCost = "700UND"
        elif OC["bankupgrade13cost"]:
            if OC["BankAmount"] < 550: OC["BankUpgradeCost"] = "TBC"; self.BankUpgradeCost = "TBC"
            elif OC["BankAmount"] >= 550: OC["BankUpgradeCost"] = 7_000_000_000_000_000_000_000_000_000_000_000_000_000; self.BankUpgradeCost = "7TreD"

    def CC_Temple(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Temple_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.TempleCost:
                            OC["Clicks"] -= self.TempleCost
                            if self.x10:
                                OC["TempleAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["TempleAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else: 
                                OC["TempleAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                        OC["TempleCost"] = self.Costs_calc(20_000_000, OC["TempleAmount"])
                        self.TempleCost = OC["TempleCost"]
                    elif self.sell:
                        if self.x1 and OC["TempleAmount"] > 0:
                            OC["TempleAmount"] -= 1
                            OC["Clicks"] += self.TempleCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1

                        elif self.x10 and OC["TempleAmount"] >= 10:
                            OC["TempleAmount"] -= 10
                            OC["Clicks"] += self.TempleCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                            
                        if self.x100 and OC["TempleAmount"] >= 100:
                            OC["TempleAmount"] -= 100
                            OC["Clicks"] += self.TempleCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["TempleCost"] = self.Costs_calc(20_000_000, OC["TempleAmount"])
                        self.TempleCost = OC["TempleCost"]
                self.pressed = False

    def TempleFunc(self):
        if OC["TempleAmount"]:
            for _ in range(OC["TempleAmount"]):
                self.TempleCount += (78000 * OC["TempleX"])
            for i in range(0,self.TempleCount + 1, 10):
                if self.TempleCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.TempleCount -= 10

    def TempleUpgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Temple_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["TempleAmount"] > 0 and OC["TempleUpgradeCost"] != "TBC" and OC["TempleUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["TempleUpgradeCost"]:
                        OC["Clicks"] -= OC["TempleUpgradeCost"]
                        OC["TempleX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["TempleUpgradeCost"] == 200_000_000:
                            OC['templeupgrade1cost'] = True
                        elif OC["TempleUpgradeCost"] == 1_000_000_000:
                            OC['templeupgrade1cost'],OC['templeupgrade2cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000:
                            OC['templeupgrade2cost'],OC['templeupgrade3cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 1_000_000_000_000:
                            OC['templeupgrade3cost'],OC['templeupgrade4cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 100_000_000_000_000:
                            OC['templeupgrade4cost'],OC['templeupgrade5cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000_000_000:
                            OC['templeupgrade5cost'],OC['templeupgrade6cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000_000_000_000:
                            OC['templeupgrade6cost'],OC['templeupgrade7cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000_000_000_000_000:
                            OC['templeupgrade7cost'],OC['templeupgrade8cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000_000_000_000_000_000:
                            OC['templeupgrade8cost'],OC['templeupgrade9cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000_000_000_000_000_000_000:
                            OC['templeupgrade9cost'],OC['templeupgrade10cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 100_000_000_000_000_000_000_000_000_000_000:
                            OC['templeupgrade10cost'],OC['templeupgrade11cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 1_000_000_000_000_000_000_000_000_000_000_000_0000:
                            OC['templeupgrade11cost'],OC['templeupgrade12cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC['templeupgrade12cost'],OC['templeupgrade13cost'] = False,True
                        elif OC["TempleUpgradeCost"] == 10_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC['templeupgrade13cost'],OC["TempleUpgradeCost"] = False,"Done";self.TempleUpgradeCost = "Done"
                self.pressed = False
    
    def TempleUpgrade_req(self):
        if OC['templeupgrade1cost']:
            if OC["TempleAmount"] < 5: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 5: OC["TempleUpgradeCost"] = 1_000_000_000; self.TempleUpgradeCost = "1B"
        elif OC['templeupgrade2cost']:
            if OC["TempleAmount"] < 25: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 25: OC["TempleUpgradeCost"] = 10_000_000_000; self.TempleUpgradeCost = "10B"
        elif OC['templeupgrade3cost']:
            if OC["TempleAmount"] < 50: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 50: OC["TempleUpgradeCost"] = 1_000_000_000_000; self.TempleUpgradeCost = "1T"
        elif OC['templeupgrade4cost']:
            if OC["TempleAmount"] < 100: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 100: OC["TempleUpgradeCost"] = 100_000_000_000_000; self.TempleUpgradeCost = "100T"
        elif OC['templeupgrade5cost']:
            if OC["TempleAmount"] < 150: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 150: OC["TempleUpgradeCost"] = 10_000_000_000_000_000; self.TempleUpgradeCost = "10Q"
        elif OC['templeupgrade6cost']:
            if OC["TempleAmount"] < 200: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 200: OC["TempleUpgradeCost"] = 10_000_000_000_000_000_000; self.TempleUpgradeCost = "10QT"
        elif OC['templeupgrade7cost']:
            if OC["TempleAmount"] < 250: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 250: OC["TempleUpgradeCost"] = 10_000_000_000_000_000_000_000; self.TempleUpgradeCost = "10S"
        elif OC['templeupgrade8cost']:
            if OC["TempleAmount"] < 300: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 300: OC["TempleUpgradeCost"] = 10_000_000_000_000_000_000_000_000; self.TempleUpgradeCost = "10SepT"
        elif OC['templeupgrade9cost']:
            if OC["TempleAmount"] < 350: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 350: OC["TempleUpgradeCost"] = 10_000_000_000_000_000_000_000_000_000; self.TempleUpgradeCost = "10O"
        elif OC['templeupgrade10cost']:
            if OC["TempleAmount"] < 400: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 400: OC["TempleUpgradeCost"] = 100_000_000_000_000_000_000_000_000_000_000; self.TempleUpgradeCost = "100N"
        elif OC['templeupgrade11cost']:
            if OC["TempleAmount"] < 450: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 450: OC["TempleUpgradeCost"] = 1_000_000_000_000_000_000_000_000_000_000_000_000; self.TempleUpgradeCost = "1UnD"
        elif OC['templeupgrade12cost']:
            if OC["TempleAmount"] < 500: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 500: OC["TempleUpgradeCost"] = 10_000_000_000_000_000_000_000_000_000_000_000_000_000; self.TempleUpgradeCost = "10DuoD"
        elif OC['templeupgrade13cost']:
            if OC["TempleAmount"] < 550: OC["TempleUpgradeCost"] = "TBC"; self.TempleUpgradeCost = "TBC"
            elif OC["TempleAmount"] >= 550: OC["TempleUpgradeCost"] = 100_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.TempleUpgradeCost = "10TreD"

    def CC_WT(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Wizard_Tower_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.WTCost:
                            OC["Clicks"] -= self.WTCost
                            if self.x10:
                                OC["WizardTowerAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["WizardTowerAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["WizardTowerAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC["WizardTowerCost"] = self.Costs_calc(330_000_000, OC["WizardTowerAmount"])
                            self.WTCost = OC["WizardTowerCost"]
                    elif self.sell:
                        if self.x1 and OC["WizardTowerAmount"] > 0:
                            OC["WizardTowerAmount"] -= 1
                            OC["Clicks"] += self.WTCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC["WizardTowerAmount"] >= 10:
                            OC["WizardTowerAmount"] -= 10
                            OC["Clicks"] += self.WTCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC["WizardTowerAmount"] >= 100:
                            OC["WizardTowerAmount"] -= 100
                            OC["Clicks"] += self.WTCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["WizardTowerCost"] = self.Costs_calc(330_000_000, OC["WizardTowerAmount"])
                        self.WTCost = OC["WizardTowerCost"]
                self.pressed = False
                    
    def WTFunc(self):
        if OC["WizardTowerAmount"]:
            for _ in range(OC["WizardTowerAmount"]):
                self.WTCount += (44_0000 * OC["WizardTowerX"])
            for i in range(0,self.WTCount + 1, 10):
                if self.WTCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.WTCount -= 10

    def WTUpgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Wizard_Tower_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["WizardTowerAmount"] > 0 and OC["WizardTowerUpgradeCost"] != "TBC" and OC["WizardTowerUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["WizardTowerUpgradeCost"]:
                        OC["Clicks"] -= OC["WizardTowerUpgradeCost"]
                        OC["WizardTowerX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["WizardTowerUpgradeCost"] == 3_300_000_000:
                            OC["WTUpgrade1Cost"] = True
                        elif OC["WizardTowerUpgradeCost"] == 16_500_000_000:
                            OC["WTUpgrade1Cost"],OC["WTUpgrade2Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000:
                            OC["WTUpgrade2Cost"],OC["WTUpgrade3Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 16_500_000_000_000:
                            OC["WTUpgrade3Cost"],OC["WTUpgrade4Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 1_650_000_000_000_000:
                            OC["WTUpgrade4Cost"],OC["WTUpgrade5Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000_000_000:
                            OC["WTUpgrade5Cost"],OC["WTUpgrade6Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000_000_000_000:
                            OC["WTUpgrade6Cost"],OC["WTUpgrade7Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000_000_000_000_000:
                            OC["WTUpgrade7Cost"],OC["WTUpgrade8Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000_000_000_000_000_000:
                            OC["WTUpgrade8Cost"],OC["WTUpgrade9Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000_000_000_000_000_000_000:
                            OC["WTUpgrade9Cost"],OC["WTUpgrade10Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 1_650_000_000_000_000_000_000_000_000_000_000:
                            OC["WTUpgrade10Cost"],OC["WTUpgrade11Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 16_500_000_000_000_000_000_000_000_000_000_000_000:
                            OC["WTUpgrade11Cost"],OC["WTUpgrade12Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["WTUpgrade12Cost"],OC["WTUpgrade13Cost"] = False,True
                        elif OC["WizardTowerUpgradeCost"] == 165_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["WTUpgrade13Cost"],OC["WizardTowerUpgradeCost"] = False,"Done";self.WTUpgradeCost = "Done"
                self.pressed = False
    
    def WTUpgrade_req(self):
        if OC["WTUpgrade1Cost"]:
            if OC["WizardTowerAmount"] < 5:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 5:OC["WizardTowerUpgradeCost"] = 16_500_000_000; self.WTUpgradeCost = "16.5B"
        elif OC["WTUpgrade2Cost"]:
            if OC["WizardTowerAmount"] < 25:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 25:OC["WizardTowerUpgradeCost"] = 165_000_000_000; self.WTUpgradeCost = "165B"
        elif OC["WTUpgrade3Cost"]:
            if OC["WizardTowerAmount"] < 50:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 50:OC["WizardTowerUpgradeCost"] = 16_500_000_000_000; self.WTUpgradeCost = "16.5T"
        elif OC["WTUpgrade4Cost"]:
            if OC["WizardTowerAmount"] < 100:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 100:OC["WizardTowerUpgradeCost"] = 1_650_000_000_000_000; self.WTUpgradeCost = "1.65Q"
        elif OC["WTUpgrade5Cost"]:
            if OC["WizardTowerAmount"] < 150:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 150:OC["WizardTowerUpgradeCost"] = 165_000_000_000_000_000; self.WTUpgradeCost = "165Q"
        elif OC["WTUpgrade6Cost"]:
            if OC["WizardTowerAmount"] < 200:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 200:OC["WizardTowerUpgradeCost"] = 165_000_000_000_000_000_000; self.WTUpgradeCost = "165QT"
        elif OC["WTUpgrade7Cost"]:
            if OC["WizardTowerAmount"] < 250:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 250:OC["WizardTowerUpgradeCost"] = 165_000_000_000_000_000_000_000; self.WTUpgradeCost = "165S"
        elif OC["WTUpgrade8Cost"]:
            if OC["WizardTowerAmount"] < 300:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 300:OC["WizardTowerUpgradeCost"] = 165_000_000_000_000_000_000_000_000; self.WTUpgradeCost = "165SepT"
        elif OC["WTUpgrade9Cost"]:
            if OC["WizardTowerAmount"] < 350:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 350:OC["WizardTowerUpgradeCost"] = 165_000_000_000_000_000_000_000_000_000; self.WTUpgradeCost = "165O"
        elif OC["WTUpgrade10Cost"]:
            if OC["WizardTowerAmount"] < 400:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 400:OC["WizardTowerUpgradeCost"] = 1_650_000_000_000_000_000_000_000_000_000_000; self.WTUpgradeCost = "1.65D"
        elif OC["WTUpgrade11Cost"]:
            if OC["WizardTowerAmount"] < 450:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 450:OC["WizardTowerUpgradeCost"] = 16_500_000_000_000_000_000_000_000_000_000_000_000; self.WTUpgradeCost = "16.5UnD"
        elif OC["WTUpgrade12Cost"]:
            if OC["WizardTowerAmount"] < 500:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 500:OC["WizardTowerUpgradeCost"] = 165_000_000_000_000_000_000_000_000_000_000_000_000_000; self.WTUpgradeCost = "165DuoD"
        elif OC["WTUpgrade13Cost"]:
            if OC["WizardTowerAmount"] < 550:OC["WizardTowerUpgradeCost"] = "TBC"; self.WTUpgradeCost = "TBC"
            elif OC["WizardTowerAmount"] >= 550:OC["WizardTowerUpgradeCost"] = 165_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.WTUpgradeCost = "165QuattD"

    def CC_Shipment(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Shipment_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.ShipmentCost:
                            OC["Clicks"] -= self.ShipmentCost
                            if self.x10:
                                OC["ShipmentAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["ShipmentAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["ShipmentAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC["ShipmentCost"] = self.Costs_calc(5_100_000_000, OC["ShipmentAmount"])
                            self.ShipmentCost = OC["ShipmentCost"]
                    elif self.sell:
                        if self.x1 and OC["ShipmentAmount"] > 0:
                            OC["ShipmentAmount"] -= 1
                            OC["Clicks"] += self.ShipmentCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC["ShipmentAmount"] >= 10:
                            OC["ShipmentAmount"] -= 10
                            OC["Clicks"] += self.ShipmentCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC["ShipmentAmount"] >= 100:
                            OC["ShipmentAmount"] -= 100
                            OC["Clicks"] += self.ShipmentCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["ShipmentCost"] = self.Costs_calc(5_100_000_000, OC["ShipmentAmount"])
                        self.ShipmentCost = OC["ShipmentCost"]
                self.pressed = False

    def ShipmentFunc(self):
        if OC["ShipmentAmount"]:
            for _ in range(OC["ShipmentAmount"]):
                self.ShipmentCount += (260_0000 * OC["ShipmentX"])
            for i in range(0,self.ShipmentCount + 1, 10):
                if self.ShipmentCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.ShipmentCount -= 10

    def ShipmentUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Shipment_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC['ShipmentAmount'] > 0 and OC["ShipmentUpgradecost"] != "TBC" and OC["ShipmentUpgradecost"] != "Done":
                    if OC["Clicks"] >= OC["ShipmentUpgradecost"]:
                        OC["Clicks"] -= OC["ShipmentUpgradecost"]
                        OC["ShipmentX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["ShipmentUpgradecost"] == 51_000_000_000:
                            OC["Shipmentupgrade1cost"] = True
                        elif OC["ShipmentUpgradecost"] == 255_000_000_000:
                            OC["Shipmentupgrade1cost"],OC["Shipmentupgrade2cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 2_550_000_000_000:
                            OC["Shipmentupgrade2cost"],OC["Shipmentupgrade3cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 255_000_000_000_000:
                            OC["Shipmentupgrade3cost"],OC["Shipmentupgrade4cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 25_500_000_000_000_000:
                            OC["Shipmentupgrade4cost"],OC["Shipmentupgrade5cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 2_550_000_000_000_000_000:
                            OC["Shipmentupgrade5cost"],OC["Shipmentupgrade6cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 2_550_000_000_000_000_000_000:
                            OC["Shipmentupgrade6cost"],OC["Shipmentupgrade7cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 2_550_000_000_000_000_000_000_000:
                            OC["Shipmentupgrade7cost"],OC["Shipmentupgrade8cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 2_550_000_000_000_000_000_000_000_000:
                            OC["Shipmentupgrade8cost"],OC["Shipmentupgrade9cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 2_550_000_000_000_000_000_000_000_000_000:
                            OC["Shipmentupgrade9cost"],OC["Shipmentupgrade10cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 25_500_000_000_000_000_000_000_000_000_000_000:
                            OC["Shipmentupgrade10cost"],OC["Shipmentupgrade11cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 255_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["Shipmentupgrade11cost"],OC["Shipmentupgrade12cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 2_550_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["Shipmentupgrade12cost"],OC["Shipmentupgrade13cost"] = False,True
                        elif OC["ShipmentUpgradecost"] == 25_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["Shipmentupgrade13cost"],OC["ShipmentUpgradecost"] = False,"Done"; self.ShipmentUpgradeCost = "Done"
                self.pressed = False

    def ShipmentUpgrade_req(self):
        if OC["Shipmentupgrade1cost"]:
            if OC['ShipmentAmount'] < 5: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 5: OC["ShipmentUpgradecost"] = 255_000_000_000; self.ShipmentUpgradeCost = '255B'
        elif OC["Shipmentupgrade2cost"]:
            if OC['ShipmentAmount'] < 25: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 25: OC["ShipmentUpgradecost"] = 2_550_000_000_000; self.ShipmentUpgradeCost = '2.55T'
        elif OC["Shipmentupgrade3cost"]:
            if OC['ShipmentAmount'] < 50: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 50: OC["ShipmentUpgradecost"] = 255_000_000_000_000; self.ShipmentUpgradeCost = '255T'
        elif OC["Shipmentupgrade4cost"]:
            if OC['ShipmentAmount'] < 100: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 100: OC["ShipmentUpgradecost"] = 25_500_000_000_000_000; self.ShipmentUpgradeCost = '25.5Q'
        elif OC["Shipmentupgrade5cost"]:
            if OC['ShipmentAmount'] < 150: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 150: OC["ShipmentUpgradecost"] = 2_550_000_000_000_000_000; self.ShipmentUpgradeCost = '2.55QT'
        elif OC["Shipmentupgrade6cost"]:
            if OC['ShipmentAmount'] < 200: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 200: OC["ShipmentUpgradecost"] = 2_550_000_000_000_000_000_000; self.ShipmentUpgradeCost = '2.55S'
        elif OC["Shipmentupgrade7cost"]:
            if OC['ShipmentAmount'] < 250: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 250: OC["ShipmentUpgradecost"] = 2_550_000_000_000_000_000_000_000; self.ShipmentUpgradeCost = '2.55SepT'
        elif OC["Shipmentupgrade8cost"]:
            if OC['ShipmentAmount'] < 300: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 300: OC["ShipmentUpgradecost"] = 2_550_000_000_000_000_000_000_000_000; self.ShipmentUpgradeCost = '2.55O'
        elif OC["Shipmentupgrade9cost"]:
            if OC['ShipmentAmount'] < 350: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 350: OC["ShipmentUpgradecost"] = 2_550_000_000_000_000_000_000_000_000_000; self.ShipmentUpgradeCost = '2.55N'
        elif OC["Shipmentupgrade10cost"]:
            if OC['ShipmentAmount'] < 400: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 400: OC["ShipmentUpgradecost"] = 25_500_000_000_000_000_000_000_000_000_000_000; self.ShipmentUpgradeCost = '25.5D'
        elif OC["Shipmentupgrade11cost"]:
            if OC['ShipmentAmount'] < 450: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 450: OC["ShipmentUpgradecost"] = 255_000_000_000_000_000_000_000_000_000_000_000_000; self.ShipmentUpgradeCost = '255UnD'
        elif OC["Shipmentupgrade12cost"]:
            if OC['ShipmentAmount'] < 500: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 500: OC["ShipmentUpgradecost"] = 2_550_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ShipmentUpgradeCost = '2.55TreD'
        elif OC["Shipmentupgrade13cost"]:
            if OC['ShipmentAmount'] < 550: OC["ShipmentUpgradecost"] = "TBC"; self.ShipmentUpgradeCost = 'TBC'
            elif OC['ShipmentAmount'] >= 550: OC["ShipmentUpgradecost"] =25_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ShipmentUpgradeCost = '25.5QuattD'

    def CC_AL(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.AL_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.ALCost:
                            OC["Clicks"] -= self.ALCost
                            if self.x10:
                                OC["ALAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["ALAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["ALAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC["ALCost"] = self.Costs_calc(75_000_000_000, OC["ALAmount"])
                            self.ALCost = OC["ALCost"]
                    elif self.sell:
                        if self.x1 and OC["ALAmount"] > 0:
                            OC["ALAmount"] -= 1
                            OC["Clicks"] += self.ALCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC["ALAmount"] >= 10:
                            OC["ALAmount"] -= 10
                            OC["Clicks"] += self.ALCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        if self.x100 and OC["ALAmount"] >= 100:
                            OC["ALAmount"] -= 100
                            OC["Clicks"] += self.ALCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 100
                        OC["ALCost"] = self.Costs_calc(75_000_000_000, OC["ALAmount"])
                        self.ALCost = OC["ALCost"]
                self.pressed = False

    def ALFunc(self):
        if OC["ALAmount"]:
            for _ in range(OC["ALAmount"]):
                self.ALCount += (1_600_0000 * OC["ALX"])
            for i in range(0,self.ALCount + 1, 10):
                if self.ALCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.ALCount -= 10

    def ALUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.AL_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC['ALAmount'] > 0 and OC["ALUpgradeCost"] != "TBC" and OC["ALUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["ALUpgradeCost"]:
                        OC["Clicks"] -= OC["ALUpgradeCost"]
                        OC["ALX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["ALUpgradeCost"] == 750_000_000_000:
                            OC["ALupgrade1cost"] = True
                        elif OC["ALUpgradeCost"] == 3_750_000_000_000:
                            OC["ALupgrade1cost"],OC["ALupgrade2cost"] = False,True
                        elif OC["ALUpgradeCost"] == 37_500_000_000_000:
                            OC["ALupgrade2cost"],OC["ALupgrade3cost"] = False,True
                        elif OC["ALUpgradeCost"] == 3_750_000_000_000_000:
                            OC["ALupgrade3cost"],OC["ALupgrade4cost"] = False,True
                        elif OC["ALUpgradeCost"] == 375_000_000_000_000_000:
                            OC["ALupgrade4cost"],OC["ALupgrade5cost"] = False,True
                        elif OC["ALUpgradeCost"] == 37_500_000_000_000_000_000:
                            OC["ALupgrade5cost"],OC["ALupgrade6cost"] = False,True
                        elif OC["ALUpgradeCost"] == 37_500_000_000_000_000_000_000:
                            OC["ALupgrade6cost"],OC["ALupgrade7cost"] = False,True
                        elif OC["ALUpgradeCost"] == 37_500_000_000_000_000_000_000_000:
                            OC["ALupgrade7cost"],OC["ALupgrade8cost"] = False,True
                        elif OC["ALUpgradeCost"] == 37_500_000_000_000_000_000_000_000_000:
                            OC["ALupgrade8cost"],OC["ALupgrade9cost"] = False,True
                        elif OC["ALUpgradeCost"] == 37_500_000_000_000_000_000_000_000_000_000:
                            OC["ALupgrade9cost"],OC["ALupgrade10cost"] = False,True
                        elif OC["ALUpgradeCost"] == 375_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ALupgrade10cost"],OC["ALupgrade11cost"] = False,True
                        elif OC["ALUpgradeCost"] == 3_750_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ALupgrade11cost"],OC["ALupgrade12cost"] = False,True
                        elif OC["ALUpgradeCost"] == 37_500_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ALupgrade12cost"],OC["ALupgrade13cost"] = False,True
                        elif OC["ALUpgradeCost"] == 375_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ALupgrade13cost"],OC["ALUpgradeCost"] = False,"Done"; self.ALUpgradeCost = "Done"
    
    def ALupgrade_req(self):
        if OC["ALupgrade1cost"]:
            if OC['ALAmount'] < 5: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 5: OC["ALUpgradeCost"] = 3_750_000_000_000; self.ALUpgradeCost = "3.75T"
        elif OC["ALupgrade2cost"]:
            if OC['ALAmount'] < 25: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 25: OC["ALUpgradeCost"] = 37_500_000_000_000; self.ALUpgradeCost = "37.5T"
        elif OC["ALupgrade3cost"]:
            if OC['ALAmount'] < 50: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 50: OC["ALUpgradeCost"] = 3_750_000_000_000_000; self.ALUpgradeCost = "3.75Q"
        elif OC["ALupgrade4cost"]:
            if OC['ALAmount'] < 100: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 100: OC["ALUpgradeCost"] = 375_000_000_000_000_000; self.ALUpgradeCost = "375Q"
        elif OC["ALupgrade5cost"]:
            if OC['ALAmount'] < 150: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 150: OC["ALUpgradeCost"] = 37_500_000_000_000_000_000; self.ALUpgradeCost = "37.5QT"
        elif OC["ALupgrade6cost"]:
            if OC['ALAmount'] < 200: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 200: OC["ALUpgradeCost"] = 37_500_000_000_000_000_000_000; self.ALUpgradeCost = "37.5S"
        elif OC["ALupgrade7cost"]:
            if OC['ALAmount'] < 250: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 250: OC["ALUpgradeCost"] = 37_500_000_000_000_000_000_000_000; self.ALUpgradeCost = "37.5SepT"
        elif OC["ALupgrade8cost"]:
            if OC['ALAmount'] < 300: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 300: OC["ALUpgradeCost"] = 37_500_000_000_000_000_000_000_000_000; self.ALUpgradeCost = "37.5O"
        elif OC["ALupgrade9cost"]:
            if OC['ALAmount'] < 350: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 350: OC["ALUpgradeCost"] = 37_500_000_000_000_000_000_000_000_000_000; self.ALUpgradeCost = "37.5N"
        elif OC["ALupgrade10cost"]:
            if OC['ALAmount'] < 400: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 400: OC["ALUpgradeCost"] = 375_000_000_000_000_000_000_000_000_000_000_000; self.ALUpgradeCost = "375D"
        elif OC["ALupgrade11cost"]:
            if OC['ALAmount'] < 450: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 450: OC["ALUpgradeCost"] = 3_750_000_000_000_000_000_000_000_000_000_000_000_000; self.ALUpgradeCost = "3.75DuoD"
        elif OC["ALupgrade12cost"]:
            if OC['ALAmount'] < 500: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 500: OC["ALUpgradeCost"] = 37_500_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ALUpgradeCost = "37.5TreD"
        elif OC["ALupgrade13cost"]:
            if OC['ALAmount'] < 550: OC["ALUpgradeCost"] = "TBC"; self.ALUpgradeCost = "TBC"
            elif OC['ALAmount'] >= 550: OC["ALUpgradeCost"] = 375_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ALUpgradeCost = "375QuattD"

    def CC_Portal(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Portal_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.PortalCost:
                            OC["Clicks"] -= self.PortalCost
                            if self.x10:
                                OC["PortalAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["PortalAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["PortalAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC["PortalCost"] = self.Costs_calc(1_000_000_000_000, OC["PortalAmount"])
                            self.PortalCost = OC["PortalCost"]
                    elif self.sell:
                        if self.x1 and OC["PortalAmount"] > 0:
                            OC["PortalAmount"] -= 1
                            OC["Clicks"] += self.PortalCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        if self.x10 and OC["PortalAmount"] >= 10:
                            OC["PortalAmount"] -= 10
                            OC["Clicks"] += self.PortalCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        if self.x100 and OC["PortalAmount"] >= 100:
                            OC["PortalAmount"] -= 100
                            OC["Clicks"] += self.PortalCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["PortalCost"] = self.Costs_calc(1_000_000_000_000, OC["PortalAmount"])
                        self.PortalCost = OC["PortalCost"]
                self.pressed = False

    def PortalFunc(self):
        if OC["PortalAmount"]:
            for _ in range(OC["PortalAmount"]):
                self.PortalCount += (10_000_0000 * OC["PortalX"])
            for i in range(0,self.PortalCount + 1, 10):
                if self.PortalCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.PortalCount -= 10

    def PortalUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Portal_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC['PortalAmount'] > 0 and OC["PortalUpgradeCost"] != "TBC" and OC["PortalUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["PortalUpgradeCost"]:
                        OC["Clicks"] -= OC["PortalUpgradeCost"]
                        OC["PortalX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["PortalUpgradeCost"] == 10_000_000_000_000:
                            OC["portalupgrade1cost"] = True
                        elif OC["PortalUpgradeCost"] == 50_000_000_000_000:
                            OC["portalupgrade1cost"],OC["portalupgrade2cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 500_000_000_000_000:
                            OC["portalupgrade2cost"],OC["portalupgrade3cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 50_000_000_000_000_000:
                            OC["portalupgrade3cost"],OC["portalupgrade4cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 5_000_000_000_000_000_000:
                            OC["portalupgrade4cost"],OC["portalupgrade5cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 500_000_000_000_000_000_000:
                            OC["portalupgrade5cost"],OC["portalupgrade6cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 500_000_000_000_000_000_000_000:
                            OC["portalupgrade6cost"],OC["portalupgrade7cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 500_000_000_000_000_000_000_000_000:
                            OC["portalupgrade7cost"],OC["portalupgrade8cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 500_000_000_000_000_000_000_000_000_000:
                            OC["portalupgrade8cost"],OC["portalupgrade9cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 500_000_000_000_000_000_000_000_000_000_000:
                            OC["portalupgrade9cost"],OC["portalupgrade10cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 5_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["portalupgrade10cost"],OC["portalupgrade11cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 50_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["portalupgrade11cost"],OC["portalupgrade12cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 500_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["portalupgrade12cost"],OC["portalupgrade13cost"] = False,True
                        elif OC["PortalUpgradeCost"] == 5_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["portalupgrade13cost"],OC["PortalUpgradeCost"] = False,"Done"; self.PortalUpgradeCost  = "Done"
                self.pressed = False
    
    def PortalUpgrade_req(self):
        if OC["portalupgrade1cost"]:
            if OC['PortalAmount'] < 5: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 5: OC["PortalUpgradeCost"] = 50_000_000_000_000; self.PortalUpgradeCost  = "50T"
        elif OC["portalupgrade2cost"]:
            if OC['PortalAmount'] < 25: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 25: OC["PortalUpgradeCost"] = 500_000_000_000_000; self.PortalUpgradeCost  = "500T"
        elif OC["portalupgrade3cost"]:
            if OC['PortalAmount'] < 50: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 50: OC["PortalUpgradeCost"] = 50_000_000_000_000_000; self.PortalUpgradeCost  = "50Q"
        elif OC["portalupgrade4cost"]:
            if OC['PortalAmount'] < 100: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 100: OC["PortalUpgradeCost"] = 5_000_000_000_000_000_000; self.PortalUpgradeCost  = "5QT"
        elif OC["portalupgrade5cost"]:
            if OC['PortalAmount'] < 150: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 150: OC["PortalUpgradeCost"] = 500_000_000_000_000_000_000; self.PortalUpgradeCost  = "500QT"
        elif OC["portalupgrade6cost"]:
            if OC['PortalAmount'] < 200: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 200: OC["PortalUpgradeCost"] = 500_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "500S"
        elif OC["portalupgrade7cost"]:
            if OC['PortalAmount'] < 250: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 250: OC["PortalUpgradeCost"] = 500_000_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "500SepT"
        elif OC["portalupgrade8cost"]:
            if OC['PortalAmount'] < 300: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 300: OC["PortalUpgradeCost"] = 500_000_000_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "500O"
        elif OC["portalupgrade9cost"]:
            if OC['PortalAmount'] < 350: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 350: OC["PortalUpgradeCost"] = 500_000_000_000_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "500N"
        elif OC["portalupgrade10cost"]:
            if OC['PortalAmount'] < 400: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 400: OC["PortalUpgradeCost"] = 5_000_000_000_000_000_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "5UnD"
        elif OC["portalupgrade11cost"]:
            if OC['PortalAmount'] < 450: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 450: OC["PortalUpgradeCost"] = 50_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "50DuoD"
        elif OC["portalupgrade12cost"]:
            if OC['PortalAmount'] < 500: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 500: OC["PortalUpgradeCost"] = 500_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "500TreD"
        elif OC["portalupgrade13cost"]:
            if OC['PortalAmount'] < 550: OC["PortalUpgradeCost"] = "TBC"; self.PortalUpgradeCost = "TBC"
            elif OC['PortalAmount'] >= 550: OC["PortalUpgradeCost"] = 5_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PortalUpgradeCost  = "5QuinD"

    def CC_TM(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.TM_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.TMCost:
                            OC["Clicks"] -= self.TMCost
                            if self.x10:
                                OC["TMAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["TMAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["TMAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC["TMCost"] = self.Costs_calc(14_000_000_000_000, OC["TMAmount"])
                            self.TMCost = OC["TMCost"]
                    elif self.sell:
                        if self.x1 and OC["TMAmount"] > 0:
                            OC["TMAmount"] -= 1
                            OC["Clicks"] += self.TMCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        if self.x10 and OC["TMAmount"] >= 10:
                            OC["TMAmount"] -= 10
                            OC["Clicks"] += self.TMCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        if self.x100 and OC["TMAmount"] >= 100:
                            OC["TMAmount"] -= 100
                            OC["Clicks"] += self.TMCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["TMCost"] = self.Costs_calc(14_000_000_000_000, OC["TMAmount"])
                        self.TMCost = OC["TMCost"]
                self.pressed = False

    def TMFunc(self):
        if OC["TMAmount"]:
            for _ in range(OC["TMAmount"]):
                self.TMCount += (65_000_0000 * OC["TMX"])
            for i in range(0,self.TMCount + 1, 10):
                if self.TMCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.TMCount -= 10

    def TMUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.TM_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC['TMAmount'] > 0 and OC["TMUpgradecost"] != "TBC" and OC["TMUpgradecost"] != "Done":
                    if OC["Clicks"] >= OC["TMUpgradecost"]:
                        OC["Clicks"] -= OC["TMUpgradecost"]
                        OC["TMX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["TMUpgradecost"] == 140_000_000_000_000:
                            OC["TMupgrade1cost"] = True
                        elif OC["TMUpgradecost"] == 700_000_000_000_000:
                            OC["TMupgrade1cost"],OC["TMupgrade2cost"] = False,True
                        elif OC["TMUpgradecost"] == 7_000_000_000_000_000:
                            OC["TMupgrade2cost"],OC["TMupgrade3cost"] = False,True
                        elif OC["TMUpgradecost"] == 700_000_000_000_000_000:
                            OC["TMupgrade3cost"],OC["TMupgrade4cost"] = False,True
                        elif OC["TMUpgradecost"] == 70_000_000_000_000_000_000:
                            OC["TMupgrade4cost"],OC["TMupgrade5cost"] = False,True
                        elif OC["TMUpgradecost"] == 7_000_000_000_000_000_000_000:
                            OC["TMupgrade5cost"],OC["TMupgrade6cost"] = False,True
                        elif OC["TMUpgradecost"] == 7_000_000_000_000_000_000_000_000: 
                            OC["TMupgrade6cost"],OC["TMupgrade7cost"] = False,True
                        elif OC["TMUpgradecost"] == 7_000_000_000_000_000_000_000_000_000: 
                            OC["TMupgrade7cost"],OC["TMupgrade8cost"] = False,True
                        elif OC["TMUpgradecost"] == 7_000_000_000_000_000_000_000_000_000_000:
                            OC["TMupgrade8cost"],OC["TMupgrade9cost"] = False,True
                        elif OC["TMUpgradecost"] == 7_000_000_000_000_000_000_000_000_000_000_000:
                            OC["TMupgrade9cost"],OC["TMupgrade10cost"] = False,True
                        elif OC["TMUpgradecost"] == 70_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["TMupgrade10cost"],OC["TMupgrade11cost"] = False,True
                        elif OC["TMUpgradecost"] == 700_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["TMupgrade11cost"],OC["TMupgrade12cost"] = False,True
                        elif OC["TMUpgradecost"] == 7_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["TMupgrade12cost"],OC["TMupgrade13cost"] = False,True
                        elif OC["TMUpgradecost"] == 70_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["TMupgrade13cost"],OC["TMUpgradecost"] = False,"Done"; self.TMUpgradeCost  = "Done"
                self.pressed = False
    
    def TMUpgrades_req(self):
        if OC["TMupgrade1cost"]:
            if OC['TMAmount'] < 5:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 5:  OC["TMUpgradecost"] = 700_000_000_000_000; self.TMUpgradeCost = "700T"
        elif OC["TMupgrade2cost"]:
            if OC['TMAmount'] < 25:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 25:  OC["TMUpgradecost"] = 7_000_000_000_000_000; self.TMUpgradeCost = "7Q"
        elif OC["TMupgrade3cost"]:
            if OC['TMAmount'] < 50:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 50:  OC["TMUpgradecost"] = 700_000_000_000_000_000; self.TMUpgradeCost = "700Q"
        elif OC["TMupgrade4cost"]:
            if OC['TMAmount'] < 100:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 100:  OC["TMUpgradecost"] = 70_000_000_000_000_000_000; self.TMUpgradeCost = "70QT"
        elif OC["TMupgrade5cost"]:
            if OC['TMAmount'] < 150:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 150:  OC["TMUpgradecost"] = 7_000_000_000_000_000_000_000; self.TMUpgradeCost = "7S"
        elif OC["TMupgrade6cost"]:
            if OC['TMAmount'] < 200:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 200:  OC["TMUpgradecost"] = 7_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "7Sept"
        elif OC["TMupgrade7cost"]:
            if OC['TMAmount'] < 250:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 250:  OC["TMUpgradecost"] = 7_000_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "7O"
        elif OC["TMupgrade8cost"]:
            if OC['TMAmount'] < 300:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 300:  OC["TMUpgradecost"] = 7_000_000_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "7N"
        elif OC["TMupgrade9cost"]:
            if OC['TMAmount'] < 350:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 350:  OC["TMUpgradecost"] = 7_000_000_000_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "7D"
        elif OC["TMupgrade10cost"]:
            if OC['TMAmount'] < 400:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 400:  OC["TMUpgradecost"] = 70_000_000_000_000_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "70UnD"
        elif OC["TMupgrade11cost"]:
            if OC['TMAmount'] < 450:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 450:  OC["TMUpgradecost"] = 700_000_000_000_000_000_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "700DuoD"
        elif OC["TMupgrade11cost"]:
            if OC['TMAmount'] < 500:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 500:  OC["TMUpgradecost"] = 7_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "7QuattD"
        elif OC["TMupgrade11cost"]:
            if OC['TMAmount'] < 550:  OC["TMUpgradecost"] = "TBC"; self.TMUpgradeCost = "TBC"
            elif OC['TMAmount'] >= 550:  OC["TMUpgradecost"] = 70_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.TMUpgradeCost = "70QuinD"

    def CC_AC(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.AC_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.ACCost:
                            OC["Clicks"] -= self.ACCost
                            if self.x10:
                                OC["ACAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["ACAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["ACAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC["ACCost"] = self.Costs_calc(14_000_000_000_000, OC["ACAmount"])
                            self.ACCost = OC["ACCost"]
                    elif self.sell:
                        if self.x1 and OC["ACAmount"] > 0:
                            OC["ACAmount"] -= 1
                            OC["Clicks"] += self.ACCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        if self.x10 and OC["ACAmount"] >= 10:
                            OC["ACAmount"] -= 10
                            OC["Clicks"] += self.ACCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        if self.x100 and OC["ACAmount"] >= 100:
                            OC["ACAmount"] -= 100
                            OC["Clicks"] += self.ACCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC["ACCost"] = self.Costs_calc(14_000_000_000_000, OC["ACAmount"])
                        self.ACCost = OC["ACCost"]
                self.pressed = False

    def ACFunc(self):
        if OC["ACAmount"]:
            for _ in range(OC["ACAmount"]):
                self.ACCount += (430_000_0000 * OC["ACX"])
            for i in range(0,self.ACCount + 1, 10):
                if self.ACCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.ACCount -= 10

    def ACUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.AC_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["ACAmount"] > 0 and OC["ACUpgradecost"] != "TBC" and OC["ACUpgradecost"] != "Done":
                    if OC["Clicks"] >= OC["ACUpgradecost"]:
                        OC["Clicks"] -= OC["ACUpgradecost"]
                        OC["ACX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["ACUpgradecost"] == 1_700_000_000_000_000:
                            OC["ACUpgrade1cost"] = True
                        elif OC["ACUpgradecost"] == 8_500_000_000_000_000:
                            OC["ACUpgrade1cost"],OC["ACUpgrade2cost"] = False,True
                        elif OC["ACUpgradecost"] == 85_000_000_000_000_000:
                            OC["ACUpgrade2cost"],OC["ACUpgrade3cost"] = False,True
                        elif OC["ACUpgradecost"] == 8_500_000_000_000_000_000:
                            OC["ACUpgrade3cost"],OC["ACUpgrade4cost"] = False,True
                        elif OC["ACUpgradecost"] == 850_000_000_000_000_000_000:
                            OC["ACUpgrade4cost"],OC["ACUpgrade5cost"] = False,True
                        elif OC["ACUpgradecost"] == 85_000_000_000_000_000_000_000:
                            OC["ACUpgrade5cost"],OC["ACUpgrade6cost"] = False,True
                        elif OC["ACUpgradecost"] == 85_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade6cost"],OC["ACUpgrade7cost"] = False,True
                        elif OC["ACUpgradecost"] == 85_000_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade7cost"],OC["ACUpgrade8cost"] = False,True
                        elif OC["ACUpgradecost"] == 85_000_000_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade8cost"],OC["ACUpgrade9cost"] = False,True
                        elif OC["ACUpgradecost"] == 85_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade9cost"],OC["ACUpgrade10cost"] = False,True
                        elif OC["ACUpgradecost"] == 850_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade10cost"],OC["ACUpgrade11cost"] = False,True
                        elif OC["ACUpgradecost"] == 8_500_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade11cost"],OC["ACUpgrade12cost"] = False,True
                        elif OC["ACUpgradecost"] == 85_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade12cost"],OC["ACUpgrade13cost"] = False,True
                        elif OC["ACUpgradecost"] == 850_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ACUpgrade13cost"],OC["ACUpgradecost"] = False,"Done"; self.ACUpgradeCost = "Done"
    
    def ACUpgrade_req(self):
        if OC["ACUpgrade1cost"]:
            if OC["ACAmount"] < 5: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 5: OC["ACUpgradecost"] = 8_500_000_000_000_000; self.ACUpgradeCost = "8.5Q"
        elif OC["ACUpgrade2cost"]:
            if OC["ACAmount"] < 25: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 25: OC["ACUpgradecost"] = 85_000_000_000_000_000; self.ACUpgradeCost = "85Q"
        elif OC["ACUpgrade3cost"]:
            if OC["ACAmount"] < 50: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 50: OC["ACUpgradecost"] = 8_500_000_000_000_000_000; self.ACUpgradeCost = "8.5QT"
        elif OC["ACUpgrade4cost"]:
            if OC["ACAmount"] < 100: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 100: OC["ACUpgradecost"] = 850_000_000_000_000_000_000; self.ACUpgradeCost = "850QT"
        elif OC["ACUpgrade5cost"]:
            if OC["ACAmount"] < 150: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 150: OC["ACUpgradecost"] = 85_000_000_000_000_000_000_000; self.ACUpgradeCost = "85S"
        elif OC["ACUpgrade6cost"]:
            if OC["ACAmount"] < 200: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 200: OC["ACUpgradecost"] = 85_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "85SepT"
        elif OC["ACUpgrade7cost"]:
            if OC["ACAmount"] < 250: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 250: OC["ACUpgradecost"] = 85_000_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "85O"
        elif OC["ACUpgrade8cost"]:
            if OC["ACAmount"] < 300: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 300: OC["ACUpgradecost"] = 85_000_000_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "85N"
        elif OC["ACUpgrade9cost"]:
            if OC["ACAmount"] < 350: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 350: OC["ACUpgradecost"] = 85_000_000_000_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "85D"
        elif OC["ACUpgrade10cost"]:
            if OC["ACAmount"] < 400: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 400: OC["ACUpgradecost"] = 850_000_000_000_000_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "850UnD"
        elif OC["ACUpgrade11cost"]:
            if OC["ACAmount"] < 450: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 450: OC["ACUpgradecost"] = 8_500_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "8.5TreD"
        elif OC["ACUpgrade12cost"]:
            if OC["ACAmount"] < 500: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 500: OC["ACUpgradecost"] = 85_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "85QuattD"
        elif OC["ACUpgrade13cost"]:
            if OC["ACAmount"] < 550: OC["ACUpgradecost"] = "TBC"; self.ACUpgradeCost = "TBC"
            elif OC["ACAmount"] >= 550: OC["ACUpgradecost"] = 850_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ACUpgradeCost = "850QuinD"

    def CC_Prism(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Prism_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.PrismCost:
                            OC["Clicks"] -= self.PrismCost
                            if self.x10:
                                OC["PrismAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["PrismAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["PrismAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC['PrismCost'] = self.Costs_calc(2_100_000_000_000_000_000,OC['PrismAmount'])
                            self.PrismCost = OC['PrismCost']
                    elif self.sell:
                        if self.x1 and OC['PrismAmount'] > 0:
                            OC['PrismAmount'] -= 1
                            OC["Clicks"] += self.PrismCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        if self.x10 and OC['PrismAmount'] >= 10:
                            OC['PrismAmount'] -= 10
                            OC["Clicks"] +=  self.PrismCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        if self.x100 and OC['PrismAmount'] >= 100:
                            OC['PrismAmount'] -= 100
                            OC["Clicks"] +=  self.PrismCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC['PrismCost'] = self.Costs_calc(14_000_000_000_000, OC['PrismAmount'])
                        self.PrismCost = OC['PrismCost']
                    self.pressed = False

    def PrismFunc(self):
        if OC['PrismAmount']:
            for _ in range(OC['PrismAmount']):
                self.PrismCount += (2_900_000_0000 * OC["PrismX"])
            for i in range(0,self.PrismCount + 1, 10):
                if self.PrismCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.PrismCount -= 10

    def PrismUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Prism_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["PrismAmount"] > 0 and OC["PrismUpgradecost"] != "TBC" and OC["PrismUpgradecost"] != "Done":
                    if OC["Clicks"] >= OC["PrismUpgradecost"]:
                        OC["Clicks"] -= OC["PrismUpgradecost"]
                        OC["PrismX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["PrismUpgradecost"] == 21_000_000_000_000_000_000:
                            OC["PrismUpgrade1cost"] = True
                        elif OC["PrismUpgradecost"] == 105_000_000_000_000_000_000:
                            OC["PrismUpgrade1cost"],OC["PrismUpgrade2cost"] = False,True
                        elif OC["PrismUpgradecost"] == 1_050_000_000_000_000_000_000:
                            OC["PrismUpgrade2cost"],OC["PrismUpgrade3cost"] = False,True
                        elif OC["PrismUpgradecost"] == 105_000_000_000_000_000_000_000:
                            OC["PrismUpgrade3cost"],OC["PrismUpgrade4cost"] = False,True
                        elif OC["PrismUpgradecost"] == 10_500_000_000_000_000_000_000_000:
                            OC["PrismUpgrade4cost"],OC["PrismUpgrade5cost"] = False,True
                        elif OC["PrismUpgradecost"] == 1_050_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade5cost"],OC["PrismUpgrade6cost"] = False,True
                        elif OC["PrismUpgradecost"] == 1_050_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade6cost"],OC["PrismUpgrade7cost"] = False,True
                        elif OC["PrismUpgradecost"] == 1_050_000_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade7cost"],OC["PrismUpgrade8cost"] = False,True
                        elif OC["PrismUpgradecost"] == 1_050_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade8cost"],OC["PrismUpgrade9cost"] = False,True
                        elif OC["PrismUpgradecost"] == 1_050_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade9cost"],OC["PrismUpgrade10cost"] = False,True
                        elif OC["PrismUpgradecost"] == 10_500_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade10cost"],OC["PrismUpgrade11cost"] = False,True
                        elif OC["PrismUpgradecost"] == 105_000_00_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade11cost"],OC["PrismUpgrade12cost"] = False,True
                        elif OC["PrismUpgradecost"] == 1_050_000_000_00_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade12cost"],OC["PrismUpgrade13cost"] = False,True
                        elif OC["PrismUpgradecost"] == 10_050_000_000_000_00_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PrismUpgrade13cost"],OC["PrismUpgradecost"] = False,"DOne"; self.PrismUpgradeCost = "Done"
                        
    def PrismUpgrade_req(self):
        if OC["PrismUpgrade1cost"]:
            if OC["PrismAmount"] < 5: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 5: OC["PrismUpgradecost"] = 105_000_000_000_000_000_000; self.PrismUpgradeCost = "105Q"
        elif OC["PrismUpgrade2cost"]:
            if OC["PrismAmount"] < 25: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 25: OC["PrismUpgradecost"] = 1_050_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05QT"
        elif OC["PrismUpgrade3cost"]:
            if OC["PrismAmount"] < 50: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 50: OC["PrismUpgradecost"] = 105_000_000_000_000_000_000_000; self.PrismUpgradeCost = "105QT"
        elif OC["PrismUpgrade4cost"]:
            if OC["PrismAmount"] < 100: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 100: OC["PrismUpgradecost"] = 10_500_000_000_000_000_000_000_000; self.PrismUpgradeCost = "10.5S"
        elif OC["PrismUpgrade5cost"]:
            if OC["PrismAmount"] < 150: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 150: OC["PrismUpgradecost"] = 1_050_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05SepT"
        elif OC["PrismUpgrade6cost"]:
            if OC["PrismAmount"] < 200: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 200: OC["PrismUpgradecost"] = 1_050_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05O"
        elif OC["PrismUpgrade7cost"]:
            if OC["PrismAmount"] < 250: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 250: OC["PrismUpgradecost"] = 1_050_000_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05N"
        elif OC["PrismUpgrade8cost"]:
            if OC["PrismAmount"] < 300: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 300: OC["PrismUpgradecost"] = 1_050_000_000_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05D"
        elif OC["PrismUpgrade9cost"]:
            if OC["PrismAmount"] < 350: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 350: OC["PrismUpgradecost"] = 1_050_000_000_000_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05UnD"
        elif OC["PrismUpgrade10cost"]:
            if OC["PrismAmount"] < 400: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 400: OC["PrismUpgradecost"] = 10_500_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "10.5DuoD"
        elif OC["PrismUpgrade11cost"]:
            if OC["PrismAmount"] < 450: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 450: OC["PrismUpgradecost"] = 105_000_00_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "105TreD"
        elif OC["PrismUpgrade12cost"]:
            if OC["PrismAmount"] < 500: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 500: OC["PrismUpgradecost"] = 1_050_000_000_00_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05QuinD"
        elif OC["PrismUpgrade13cost"]:
            if OC["PrismAmount"] < 550: OC["PrismUpgradecost"] = "TBC"; self.PrismUpgradeCost = "TBC"
            elif OC["PrismAmount"] >= 550: OC["PrismUpgradecost"] = 10_050_000_000_000_00_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PrismUpgradeCost = "1.05SexD"

    def CC_ChanceMaker(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.ChanceMaker_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.ChanceMakerCost:
                            OC["Clicks"] -= self.ChanceMakerCost
                            if self.x10:
                                OC["ChanceMakerAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["ChanceMakerAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["ChanceMakerAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC['ChanceMakerCost'] = self.Costs_calc(26_000_000_000_000_000_000,OC['ChanceMakerAmount'])
                            self.ChanceMakerCost = OC['ChanceMakerCost']
                    elif self.sell:
                        if self.x1 and OC['ChanceMakerAmount'] > 0:
                            OC['ChanceMakerAmount'] -= 1
                            OC["Clicks"] += self.ChanceMakerCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        if self.x10 and OC['ChanceMakerAmount'] >= 10:
                            OC['ChanceMakerAmount'] -= 10
                            OC["Clicks"] +=  self.ChanceMakerCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        if self.x100 and OC['ChanceMakerAmount'] >= 100:
                            OC['ChanceMakerAmount'] -= 100
                            OC["Clicks"] +=  self.ChanceMakerCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC['ChanceMakerCost'] = self.Costs_calc(26_000_000_000_000_000_000, OC['ChanceMakerAmount'])
                        self.ChanceMakerCost = OC['ChanceMakerCost']
                    self.pressed = False

    def ChanceMakerFunc(self):
        if OC['ChanceMakerAmount']:
            for _ in range(OC['ChanceMakerAmount']):
                self.ChanceMakerCount += (21_000_000_0000 * OC["ChanceMakerX"])
            for i in range(0,self.ChanceMakerCount + 1, 10):
                if self.ChanceMakerCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.ChanceMakerCount -= 10

    def ChanceMakerUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.ChanceMaker_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["ChanceMakerAmount"] > 0 and OC["ChanceMakerUpgradecost"] != "TBC" and OC["ChanceMakerUpgradecost"] != "Done":
                    if OC["Clicks"] >= OC["ChanceMakerUpgradecost"]:
                        OC["Clicks"] -= OC["ChanceMakerUpgradecost"]
                        OC["ChanceMakerX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["ChanceMakerUpgradecost"] == 260_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade1Cost"] = True
                        elif OC["ChanceMakerUpgradecost"] == 1_300_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade1Cost"],OC["ChanceMakerUpgrade2Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 13_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade2Cost"],OC["ChanceMakerUpgrade3Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 1_300_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade3Cost"],OC["ChanceMakerUpgrade4Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 130_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade4Cost"],OC["ChanceMakerUpgrade5Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 13_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade5Cost"],OC["ChanceMakerUpgrade6Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 13_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade6Cost"],OC["ChanceMakerUpgrade7Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 13_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade7Cost"],OC["ChanceMakerUpgrade8Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 13_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade8Cost"],OC["ChanceMakerUpgrade9Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 13_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade9Cost"],OC["ChanceMakerUpgrade10Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 130_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade10Cost"],OC["ChanceMakerUpgrade11Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 1_300_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade11Cost"],OC["ChanceMakerUpgrade12Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 13_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade12Cost"],OC["ChanceMakerUpgrade13Cost"] = False,True
                        elif OC["ChanceMakerUpgradecost"] == 130_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["ChanceMakerUpgrade13Cost"],OC["ChanceMakerUpgradecost"] = False,"Done";self.ChanceMakerUpgradeCost = "Done"
                    self.pressed = False

    def ChanceMakerupgrade_req(self):
        if OC["ChanceMakerUpgrade1Cost"]:
            if OC["ChanceMakerAmount"] < 5: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 5: OC["ChanceMakerUpgradecost"] = 1_300_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "1.3QT"
        elif OC["ChanceMakerUpgrade2Cost"]:
            if OC["ChanceMakerAmount"] < 25: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 25: OC["ChanceMakerUpgradecost"] = 13_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "13QT"
        elif OC["ChanceMakerUpgrade3Cost"]:
            if OC["ChanceMakerAmount"] < 50: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 50: OC["ChanceMakerUpgradecost"] = 1_300_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "1.3S"
        elif OC["ChanceMakerUpgrade4Cost"]:
            if OC["ChanceMakerAmount"] < 100: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 100: OC["ChanceMakerUpgradecost"] = 130_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "130S"
        elif OC["ChanceMakerUpgrade5Cost"]:
            if OC["ChanceMakerAmount"] < 150: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 150: OC["ChanceMakerUpgradecost"] = 13_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "13SepT"
        elif OC["ChanceMakerUpgrade6Cost"]:
            if OC["ChanceMakerAmount"] < 200: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 200: OC["ChanceMakerUpgradecost"] = 13_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "13O"
        elif OC["ChanceMakerUpgrade7Cost"]:
            if OC["ChanceMakerAmount"] < 250: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 250: OC["ChanceMakerUpgradecost"] = 13_000_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "13N"
        elif OC["ChanceMakerUpgrade8Cost"]:
            if OC["ChanceMakerAmount"] < 300: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 300: OC["ChanceMakerUpgradecost"] = 13_000_000_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "13D"
        elif OC["ChanceMakerUpgrade9Cost"]:
            if OC["ChanceMakerAmount"] < 350: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 350: OC["ChanceMakerUpgradecost"] = 13_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "13UnD"
        elif OC["ChanceMakerUpgrade10Cost"]:
            if OC["ChanceMakerAmount"] < 400: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 400: OC["ChanceMakerUpgradecost"] = 130_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "130DuoD"
        elif OC["ChanceMakerUpgrade11Cost"]:
            if OC["ChanceMakerAmount"] < 450: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 450: OC["ChanceMakerUpgradecost"] = 1_300_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "1.3QuattD"
        elif OC["ChanceMakerUpgrade12Cost"]:
            if OC["ChanceMakerAmount"] < 500: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 500: OC["ChanceMakerUpgradecost"] = 13_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "13QuinD"
        elif OC["ChanceMakerUpgrade13Cost"]:
            if OC["ChanceMakerAmount"] < 550: OC["ChanceMakerUpgradecost"] = "TBC"; self.ChanceMakerUpgradeCost = "TBC"
            elif OC["ChanceMakerAmount"] >= 550: OC["ChanceMakerUpgradecost"] = 130_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.ChanceMakerUpgradeCost = "130SexD"

    def CC_FE(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.FE_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.FECost:
                            OC["Clicks"] -= self.FECost
                            if self.x10:
                                OC["FEAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["FEAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["FEAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC['FECost'] = self.Costs_calc(310_000_000_000_000_000_000,OC['FEAmount'])
                            self.FECost = OC['FECost']
                    elif self.sell:
                        if self.x1 and OC['FEAmount'] > 0:
                            OC['FEAmount'] -= 1
                            OC["Clicks"] += self.FECost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC['FEAmount'] >= 10:
                            OC['FEAmount'] -= 10
                            OC["Clicks"] += self.FECost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x1 and OC['FEAmount'] >= 100:
                            OC['FEAmount'] -= 100
                            OC["Clicks"] += self.FECost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC['FECost'] = self.Costs_calc(310_000_000_000_000_000_000,OC['FEAmount'])
                        self.FECost = OC['FECost']
                    self.pressed = False

    def FEFunc(self):
        if OC['FEAmount']:
            for _ in range(OC['FEAmount']):
                self.FECount += (150_000_000_0000 * OC["FEX"])
            for i in range(0,self.FECount + 1, 10):
                if self.FECount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.FECount -= 10

    def FEUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.FE_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["FEAmount"] > 0 and OC["FEUpgradeCost"] != "TBC" and OC["FEUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["FEUpgradeCost"]:
                        OC["Clicks"] -= OC["FEUpgradeCost"]
                        OC["FEX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["FEUpgradeCost"] == 3_100_000_000_000_000_000:
                            OC["FEUpgrade1Cost"] = True
                        elif OC["FEUpgradeCost"] == 15_500_000_000_000_000_000:
                            OC["FEUpgrade1Cost"],OC["FEUpgrade2Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 155_000_000_000_000_000_000_000:
                            OC["FEUpgrade2Cost"],OC["FEUpgrade3Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 15_500_000_000_000_000_000_000:
                            OC["FEUpgrade3Cost"],OC["FEUpgrade4Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 1_550_000_000_000_000_000_000_000:
                            OC["FEUpgrade4Cost"],OC["FEUpgrade5Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 155_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade5Cost"],OC["FEUpgrade6Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 155_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade6Cost"],OC["FEUpgrade7Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 155_000_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade7Cost"],OC["FEUpgrade8Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 155_000_000_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade8Cost"],OC["FEUpgrade9Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 155_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade9Cost"],OC["FEUpgrade10Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 1_550_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade10Cost"],OC["FEUpgrade11Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 15_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade11Cost"],OC["FEUpgrade12Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 155_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade12Cost"],OC["FEUpgrade13Cost"] = False,True
                        elif OC["FEUpgradeCost"] == 1_550_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["FEUpgrade13Cost"],OC["FEUpgradeCost"] = False,"Done"; self.FEUpgradeCost = "Done"
                self.pressed = False
    
    def FEUpgrades_req(self):
        if OC["FEUpgrade1Cost"]:
            if OC["FEAmount"] < 5:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 5:OC["FEUpgradeCost"] = 15_500_000_000_000_000_000;self.FEUpgradeCost = "15.5QT"
        elif OC["FEUpgrade2Cost"]:
            if OC["FEAmount"] < 25:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 25:OC["FEUpgradeCost"] = 155_000_000_000_000_000_000;self.FEUpgradeCost = "155QT"
        elif OC["FEUpgrade3Cost"]:
            if OC["FEAmount"] < 50:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 50:OC["FEUpgradeCost"] = 15_500_000_000_000_000_000_000;self.FEUpgradeCost = "15.5S"
        elif OC["FEUpgrade4Cost"]:
            if OC["FEAmount"] < 100:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 100:OC["FEUpgradeCost"] = 1_550_000_000_000_000_000_000_000;self.FEUpgradeCost = "1.55SepT"
        elif OC["FEUpgrade5Cost"]:
            if OC["FEAmount"] < 150:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 150:OC["FEUpgradeCost"] = 155_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "155SepT"
        elif OC["FEUpgrade6Cost"]:
            if OC["FEAmount"] < 200:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 200:OC["FEUpgradeCost"] = 155_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "155O"
        elif OC["FEUpgrade7Cost"]:
            if OC["FEAmount"] < 250:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 250:OC["FEUpgradeCost"] = 155_000_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "155N"  
        elif OC["FEUpgrade8Cost"]:
            if OC["FEAmount"] < 300:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 300:OC["FEUpgradeCost"] = 155_000_000_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "155D"
        elif OC["FEUpgrade9Cost"]:
            if OC["FEAmount"] < 350:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 350:OC["FEUpgradeCost"] = 155_000_000_000_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "155UnD"
        elif OC["FEUpgrade10Cost"]:
            if OC["FEAmount"] < 400:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 400:OC["FEUpgradeCost"] = 1_550_000_000_000_000_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "1.55TreD"
        elif OC["FEUpgrade11Cost"]:
            if OC["FEAmount"] < 450:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 450:OC["FEUpgradeCost"] = 15_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "15QuattD"
        elif OC["FEUpgrade12Cost"]:
            if OC["FEAmount"] < 500:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 500:OC["FEUpgradeCost"] = 155_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "155QuinD"
        elif OC["FEUpgrade13Cost"]:
            if OC["FEAmount"] < 550:OC["FEUpgradeCost"] = "TBC";self.FEUpgradeCost = "TBC"
            elif OC["FEAmount"] >= 550:OC["FEUpgradeCost"] = 1_550_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000;self.FEUpgradeCost = "1.55SepTD"

    def CC_PC(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.PC_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.PCCost:
                            OC["Clicks"] -= self.PCCost
                            if self.x10:
                                OC["PCAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["PCAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["PCAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC['PCCost'] = self.Costs_calc(71_000_000_000_000_000_000,OC['PCAmount'])
                            self.PCCost = OC['PCCost']
                    elif self.sell:
                        if self.x1 and OC['PCAmount'] > 0:
                            OC['PCAmount'] -= 1
                            OC["Clicks"] += self.PCCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC['PCAmount'] >= 10:
                            OC['PCAmount'] -= 10
                            OC["Clicks"] += self.PCCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC['PCAmount'] >= 100:
                            OC['PCAmount'] -= 100
                            OC["Clicks"] += self.PCCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC['PCCost'] = self.Costs_calc(71_000_000_000_000_000_000,OC['PCAmount'])
                        self.PCCost = OC['PCCost']
                self.pressed = False

    def PCFunc(self):
        if OC['PCAmount']:
            for _ in range(OC['PCAmount']):
                self.PCCount += (1_100_000_000_0000 * OC["PCX"])
            for i in range(0,self.PCCount + 1, 10):
                if self.PCCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.PCCount -= 10

    def PCUpgrades(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.PC_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["PCAmount"] > 0 and OC["PCUpgradeCost"] != "TBC" and OC["PCUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["PCUpgradeCost"]:
                        OC["Clicks"] -= OC["PCUpgradeCost"]
                        OC["PCX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["PCUpgradeCost"] == 710_000_000_000_000_000_000:
                            OC["PCUpgrade1cost"] = True
                        elif OC["PCUpgradeCost"] == 3_550_000_000_000_000_000_000:
                            OC["PCUpgrade1cost"],OC["PCUpgrade2cost"] = False,True
                        elif OC["PCUpgradeCost"] == 35_500_000_000_000_000_000_000:
                            OC["PCUpgrade2cost"],OC["PCUpgrade3cost"] = False,True
                        elif OC["PCUpgradeCost"] == 3_550_000_000_000_000_000_000_000:
                            OC["PCUpgrade3cost"],OC["PCUpgrade4cost"] = False,True
                        elif OC["PCUpgradeCost"] == 355_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade4cost"],OC["PCUpgrade5cost"] = False,True
                        elif OC["PCUpgradeCost"] == 35_500_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade5cost"],OC["PCUpgrade6cost"] = False,True
                        elif OC["PCUpgradeCost"] == 35_500_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade6cost"],OC["PCUpgrade7cost"] = False,True
                        elif OC["PCUpgradeCost"] == 35_500_000_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade7cost"],OC["PCUpgrade8cost"] = False,True
                        elif OC["PCUpgradeCost"] == 35_500_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade8cost"],OC["PCUpgrade9cost"] = False,True
                        elif OC["PCUpgradeCost"] == 35_500_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade9cost"],OC["PCUpgrade10cost"] = False,True
                        elif OC["PCUpgradeCost"] == 355_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade10cost"],OC["PCUpgrade11cost"] = False,True
                        elif OC["PCUpgradeCost"] == 3_550_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade11cost"],OC["PCUpgrade12cost"] = False,True
                        elif OC["PCUpgradeCost"] == 35_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade12cost"],OC["PCUpgrade13cost"] = False,True
                        elif OC["PCUpgradeCost"] == 355_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["PCUpgrade13cost"],OC["PCUpgradeCost"] = False,"Done";self.PCUpgradeCost = "Done"
                    self.pressed = False
    
    def PCUpgrades_req(self):
        if OC["PCUpgrade1cost"]:
            if OC["PCAmount"] < 5: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 5: OC["PCUpgradeCost"] = 3_550_000_000_000_000_000_000; self.PCUpgradeCost = "3.55S"
        elif OC["PCUpgrade2cost"]:
            if OC["PCAmount"] < 25: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 25: OC["PCUpgradeCost"] = 35_500_000_000_000_000_000_000; self.PCUpgradeCost = "35.5S"
        elif OC["PCUpgrade3cost"]:
            if OC["PCAmount"] < 50: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 50: OC["PCUpgradeCost"] = 3_550_000_000_000_000_000_000_000; self.PCUpgradeCost = "3.55SepT"
        elif OC["PCUpgrade4cost"]:
            if OC["PCAmount"] < 100: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 100: OC["PCUpgradeCost"] = 355_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "355SepT"
        elif OC["PCUpgrade5cost"]:
            if OC["PCAmount"] < 150: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 150: OC["PCUpgradeCost"] = 35_500_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "35.5O"
        elif OC["PCUpgrade6cost"]:
            if OC["PCAmount"] < 200: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 200: OC["PCUpgradeCost"] = 35_500_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "35.5N"
        elif OC["PCUpgrade7cost"]:
            if OC["PCAmount"] < 250: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 250: OC["PCUpgradeCost"] = 35_500_000_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "35.5D"
        elif OC["PCUpgrade8cost"]:
            if OC["PCAmount"] < 300: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 300: OC["PCUpgradeCost"] = 35_500_000_000_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "35.5UnD"
        elif OC["PCUpgrade9cost"]:
            if OC["PCAmount"] < 350: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 350: OC["PCUpgradeCost"] = 35_500_000_000_000_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "35.5DuoD"
        elif OC["PCUpgrade10cost"]:
            if OC["PCAmount"] < 400: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 400: OC["PCUpgradeCost"] = 355_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "35.5TreD"
        elif OC["PCUpgrade11cost"]:
            if OC["PCAmount"] < 450: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 450: OC["PCUpgradeCost"] = 3_550_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "3.55QuinD"
        elif OC["PCUpgrade12cost"]:
            if OC["PCAmount"] < 500: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 500: OC["PCUpgradeCost"] = 35_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "35.5SexD"
        elif OC["PCUpgrade13cost"]:
            if OC["PCAmount"] < 550: OC["PCUpgradeCost"] = "TBC"; self.PCUpgradeCost = "TBC"
            elif OC["PCAmount"] >= 550: OC["PCUpgradeCost"] = 355_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.PCUpgradeCost = "355SeptxD"

    def CC_IV(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.IV_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.IVCost:
                            OC["Clicks"] -= self.IVCost
                            if self.x10:
                                OC["IVAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["IVAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["IVAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC['IVCost'] = self.Costs_calc(12_000_000_000_000_000_000_000,OC['IVAmount'])
                            self.IVCost = OC['IVCost']
                    elif self.sell:
                        if self.x1 and OC['IVAmount'] > 0:
                            OC["IVAmount"] -= 1
                            OC["Clicks"] += self.IVCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC['IVAmount'] >= 10:
                            OC["IVAmount"] -= 10
                            OC["Clicks"] += self.IVCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC['IVAmount'] >= 100:
                            OC["IVAmount"] -= 100
                            OC["Clicks"] += self.IVCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC['IVCost'] = self.Costs_calc(12_000_000_000_000_000_000_000,OC['IVAmount'])
                        self.IVCost = OC['IVCost']
                self.pressed = False

    def IVFunc(self):
        if OC['IVAmount']:
            for _ in range(OC['IVAmount']):
                self.IVCount += (8_300_000_000_0000 * OC["IVX"])
            for i in range(0,self.IVCount + 1, 10):
                if self.IVCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.IVCount -= 10

    def IVUpgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.PC_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["IVAmount"] > 0 and OC["IVUpgradeCost"] != "TBC" and OC["IVUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["IVUpgradeCost"]:
                        OC["Clicks"] -= OC["IVUpgradeCost"]
                        OC["IVX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["IVUpgradeCost"] == 120_000_000_000_000_000_000_000:
                            OC["IVUpgrade1Cost"] = True
                        elif OC["IVUpgradeCost"] == 600_000_000_000_000_000_000_000:
                            OC["IVUpgrade1Cost"],OC["IVUpgrade2Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 6_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade2Cost"],OC["IVUpgrade3Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 600_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade3Cost"],OC["IVUpgrade4Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 60_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade4Cost"],OC["IVUpgrade5Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 6_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade5Cost"],OC["IVUpgrade6Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 6_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade6Cost"],OC["IVUpgrade7Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 6_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade7Cost"],OC["IVUpgrade8Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 6_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade8Cost"],OC["IVUpgrade9Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 6_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade9Cost"],OC["IVUpgrade10Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 60_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade10Cost"],OC["IVUpgrade11Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 600_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade11Cost"],OC["IVUpgrade12Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 6_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade12Cost"],OC["IVUpgrade13Cost"] = False,True
                        elif OC["IVUpgradeCost"] == 60_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["IVUpgrade13Cost"],OC["IVUpgradeCost"] = False,"Done";self.IVUpgradeCost = "Done"
    
    def IVUpgrade_req(self):
        if OC["IVUpgrade1Cost"]: 
            if OC["IVAmount"] < 5: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 5: OC["IVUpgradeCost"] = 600_000_000_000_000_000_000_000; self.IVUpgradeCost = "600S"
        elif OC["IVUpgrade2Cost"]: 
            if OC["IVAmount"] < 25: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 25: OC["IVUpgradeCost"] = 6_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "6SepT"
        elif OC["IVUpgrade3Cost"]: 
            if OC["IVAmount"] < 50: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 50: OC["IVUpgradeCost"] = 600_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "600SepT"
        elif OC["IVUpgrade4Cost"]: 
            if OC["IVAmount"] < 100: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 100: OC["IVUpgradeCost"] = 60_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "60O"
        elif OC["IVUpgrade5Cost"]: 
            if OC["IVAmount"] < 150: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 150: OC["IVUpgradeCost"] = 6_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "6N"
        elif OC["IVUpgrade6Cost"]: 
            if OC["IVAmount"] < 200: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 200: OC["IVUpgradeCost"] = 6_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "6D"
        elif OC["IVUpgrade7Cost"]: 
            if OC["IVAmount"] < 250: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 250: OC["IVUpgradeCost"] = 6_000_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "6UnD"
        elif OC["IVUpgrade8Cost"]: 
            if OC["IVAmount"] < 300: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 300: OC["IVUpgradeCost"] = 6_000_000_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "6DuoD"
        elif OC["IVUpgrade9Cost"]: 
            if OC["IVAmount"] < 350: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 350: OC["IVUpgradeCost"] = 6_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "6TreD"
        elif OC["IVUpgrade10Cost"]: 
            if OC["IVAmount"] < 400: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 400: OC["IVUpgradeCost"] = 60_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "60QuattD"
        elif OC["IVUpgrade11Cost"]: 
            if OC["IVAmount"] < 450: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 450: OC["IVUpgradeCost"] = 600_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "600QuinnD"
        elif OC["IVUpgrade12Cost"]: 
            if OC["IVAmount"] < 500: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 500: OC["IVUpgradeCost"] = 6_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "6SeptD"
        elif OC["IVUpgrade13Cost"]: 
            if OC["IVAmount"] < 550: OC["IVUpgradeCost"] = "TBC"; self.IVUpgradeCost = "TBC"
            elif OC["IVAmount"] >= 550: OC["IVUpgradeCost"] = 60_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.IVUpgradeCost = "60OD"

    def CC_CB(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.CB_rect.collidepoint(mouse_pos) and not self.Upgrades:
            if pygame.mouse.get_pressed()[0]: self.pressed = True
            else:
                if self.pressed:
                    if self.buy:
                        if OC["Clicks"] >= self.CBCost:
                            OC["Clicks"] -= self.CBCost
                            if self.x10:
                                OC["CBAmount"] += 10
                                OC['ItemAmount'] += 10
                                OC["AMADDER"] += 1
                            elif self.x100:
                                OC["CBAmount"] += 100
                                OC['ItemAmount'] += 100
                                OC["AMADDER"] += 10
                            else:
                                OC["CBAmount"] += 1
                                OC['ItemAmount'] += 1
                                OC["AMADDER"] += 0.1
                            OC['CBCost'] = self.Costs_calc(1_900_000_000_000_000_000_000_000,OC['CBAmount'])
                            self.CBCost = OC['CBCost']
                    elif self.sell:
                        if self.x1 and OC['CBAmount'] > 0:
                            OC["CBAmount"] -= 1
                            OC["Clicks"] += self.CBCost
                            OC['ItemAmount'] -= 1
                            OC["AMADDER"] -= 0.1
                        elif self.x10 and OC['CBAmount'] >= 10:
                            OC["CBAmount"] -= 10
                            OC["Clicks"] += self.CBCost
                            OC['ItemAmount'] -= 10
                            OC["AMADDER"] -= 1
                        elif self.x100 and OC['CBAmount'] >= 100:
                            OC["CBAmount"] -= 100
                            OC["Clicks"] += self.CBCost
                            OC['ItemAmount'] -= 100
                            OC["AMADDER"] -= 10
                        OC['CBCost'] = self.Costs_calc(1_900_000_000_000_000_000_000_000,OC['CBAmount'])
                        self.CBCost = OC['CBCost']
                    self.pressed = False

    def CBFunc(self):
        if OC['CBAmount']:
            for _ in range(OC['CBAmount']):
                self.CBCount += (64_000_000_000_0000 * OC["CBX"])
            for i in range(0,self.CBCount + 1, 10):
                if self.CBCount >= 10:
                    OC["Clicks"] += 1
                    OC["AllClicks"] += 1
                    OC['ShopClicks'] += 1
                    self.CBCount -= 10

    def CBUpgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.CB_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:self.pressed = True
            else:
                if self.pressed and OC["CBAmount"] > 0 and OC["CBUpgradeCost"] != "TBC" and OC["CBUpgradeCost"] != "Done":
                    if OC["Clicks"] >= OC["CBUpgradeCost"]:
                        OC["Clicks"] -= OC["CBUpgradeCost"]
                        OC["CBX"] *= 2
                        OC["UpgradeAmount"] += 1
                        if OC["CBUpgradeCost"] == 19_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade1Cost"] = True
                        elif OC["CBUpgradeCost"] == 95_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade1Cost"],OC["CBUpgrade2Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 950_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade2Cost"],OC["CBUpgrade3Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 95_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade3Cost"],OC["CBUpgrade4Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 9_500_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade4Cost"],OC["CBUpgrade5Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 950_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade5Cost"],OC["CBUpgrade6Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 950_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade6Cost"],OC["CBUpgrade7Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 950_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade7Cost"],OC["CBUpgrade8Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 950_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade8Cost"],OC["CBUpgrade9Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 950_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade9Cost"],OC["CBUpgrade10Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 9_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade10Cost"],OC["CBUpgrade11Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 95_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade11Cost"],OC["CBUpgrade12Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 950_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade12Cost"],OC["CBUpgrade13Cost"] = False,True
                        elif OC["CBUpgradeCost"] == 9_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000:
                            OC["CBUpgrade12Cost"],OC["CBUpgradeCost"] = False,"Done";self.CBUpgradeCost = "Done"
                    self.pressed = False
    
    
    def CBUpgrade_req(self):
        if OC["CBUpgrade1Cost"]:
            if OC["CBAmount"] < 5: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 5: OC["CBUpgradeCost"] = 95_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "95SepT"
        elif OC["CBUpgrade2Cost"]:
            if OC["CBAmount"] < 25: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 25: OC["CBUpgradeCost"] = 950_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "950SepT"
        elif OC["CBUpgrade3Cost"]:
            if OC["CBAmount"] < 50: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 50: OC["CBUpgradeCost"] = 95_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "95O"
        elif OC["CBUpgrade4Cost"]:
            if OC["CBAmount"] < 100: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 100: OC["CBUpgradeCost"] = 9_500_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "9.5N"
        elif OC["CBUpgrade5Cost"]:
            if OC["CBAmount"] < 150: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 150: OC["CBUpgradeCost"] = 950_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "950N"
        elif OC["CBUpgrade6Cost"]:
            if OC["CBAmount"] < 200: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 200: OC["CBUpgradeCost"] = 950_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "950D"
        elif OC["CBUpgrade7Cost"]:
            if OC["CBAmount"] < 250: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 250: OC["CBUpgradeCost"] = 950_000_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "950UnD"
        elif OC["CBUpgrade8Cost"]:
            if OC["CBAmount"] < 300: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 300: OC["CBUpgradeCost"] = 950_000_000_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "950DuoD"
        elif OC["CBUpgrade9Cost"]:
            if OC["CBAmount"] < 350: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 350: OC["CBUpgradeCost"] = 950_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "950TreD"
        elif OC["CBUpgrade10Cost"]:
            if OC["CBAmount"] < 400: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 400: OC["CBUpgradeCost"] = 9_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "9.5QuinD"
        elif OC["CBUpgrade11Cost"]:
            if OC["CBAmount"] < 450: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 450: OC["CBUpgradeCost"] = 95_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "95SexD"
        elif OC["CBUpgrade12Cost"]:
            if OC["CBAmount"] < 500: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 500: OC["CBUpgradeCost"] = 950_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "950SeptD"
        elif OC["CBUpgrade13Cost"]:
            if OC["CBAmount"] < 550: OC["CBUpgradeCost"] = "TBC"; self.CBUpgradeCost = "TBC"
            elif OC["CBAmount"] >= 550: OC["CBUpgradeCost"] = 9_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000; self.CBUpgradeCost = "9.5NoveD"

    def CostDisplay(self, Base_Price, Amount_Owned):
        Price = float(Base_Price) * (1.15**Amount_Owned)
        Price = math.ceil(Price)
        Newprice_x10 = Price * 20.303718238
        Newprice_x100 = Price * 7828749.671335256
        return round(Newprice_x10), round(Newprice_x100)
    
    def SellDisplay(self, Base_Price, Amount_Owned):
        Price = float(Base_Price) * (1.15**Amount_Owned)
        Price = math.ceil(Price)
        Sell_x10 = (Price * 20.303718238)/4
        Sell_x100 = (Price * 7828749.671335256)/4
        return round(Sell_x10), round(Sell_x100)
    
    def NumberShrink(self, Number, Display):
        Number = str(Number)
        Zeros = len(Number)
        if Zeros <= 5:return Number
        if Zeros >= 6:
           Display = str(Number[0:3]) + "K"
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
    
    def NumberCheck(self, GivenNumber, Threshold):
        if self.buy:
            if GivenNumber >= Threshold:
                return "Green"
            else:
                return "Red"
        else:
                return "Red"