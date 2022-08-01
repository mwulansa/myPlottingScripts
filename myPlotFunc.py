import ROOT
import math

r = {
    'MuonPt'    : [10, "Pt(GeV)", 250],
    'Muon1Pt'   : [20, "Pt(GeV)", 500],
    'Muon2Pt'   : [20, "Pt(GeV)", 500],
    'ElectronPt': [20, "Pt(GeV)", 500],
    'TauPt'     : [10, "Pt(GeV)", 250],
    'TauPt0'        : [20, "Pt(GeV)", 500],
    'TauPt1'        : [20, "Pt(GeV)", 500],
    'TauPt10'       : [20, "Pt(GeV)", 500],
    'JetPt'     : [50, "Pt(GeV)", 2000],
    'MetPt'     : [20, "Pt(GeV)", 500],
    'dRl'       : [1, "dR", 5],
    'dRj'       : [1, "dR", 5],
    'dPhil'     : [5, "dPhi", 3.5],
    'dPhij'     : [5, "dphi", 3.5],
    'Mt'        : [20, "Mt(GeV)", 500],
    'Nj'        : [1, "N_{jet}", 10],
    'Mass'      : [5, "M_{vis}(GeV)", 100],
    'lowMET'    : [5, "M_{vis}(GeV)", 100],
    'dRcut'     : [5, "M_{vis}(GeV)", 100],
    'lowMt'     : [5, "M_{vis}(GeV)", 100],
    'mTcut'     : [5, "M_{vis}(GeV)", 100],
    'highMET'   : [5, "M_{vis}(GeV)", 100],
    'Metcut'    : [5, "M_{vis}(GeV)", 100],
    'highMt'    : [5, "M_{vis}(GeV)", 100],
    'dPhicut'   : [5, "M_{vis}(GeV)", 100],
    'Trigger'   : [1, "Triggers", 8]
}

def variableName(argument):
    match argument:
        case "TauPtJetPt":
            return r['TauPt'][0],r['JetPt'][0]
        case "TauPtJet2Pt":
            return r['TauPt'][0],r['JetPt'][0]
        case "TauPtMuonPt":
            return r['TauPt'][0],r['MuonPt'][0],r['MuonPt'][2]
        case "TauPtMetPt":
            return r['TauPt'][0],r['MetPt'][0]
        case "TauPtMuMuMass":
            return r['TauPt'][0],r['Mass'][0]
        case "TauPtdRjtau":
            return r['TauPt'][0],r['dRj'][0]
        case "TauPtdRj2tau":
            return r['TauPt'][0],r['dRj'][0]
        case "TauPtdRjmu":
            return r['TauPt'][0],r['dRj'][0]
        case "TauPtdRl":
            return r['TauPt'][0],r['dRl'][0]
        case "TauPtdRl2":
            return r['TauPt'][0],r['dRl'][0]
        case "MuonPtdRl":
            return r['MuonPt'][0],r['dRl'][0],r['MuonPt'][2]
        case "TauPtdRgenMu":
            return r['TauPt'][0],r['dRl'][0]
        case "MuonPtdRgenMu":
            return r['MuonPt'][0],r['dRl'][0]
        case "MuonPtMuon2Pt":
            return r['MuonPt'][0],r['MuonPt'][0],r['MuonPt'][2]
        case "DimuonMass":
            return r['TauPt'][0],r['Mass'][0]

def plotStyle(histogram, EvBin = 1, lineColour = 1, fillColour = 0, width = 3, xtitle = "hist", fillStyle = 1001, draw = "hist"):

    htemp = histogram.Clone("htemp")

    if draw == "point":
        htemp.SetMarkerStyle(8)
        htemp.SetMarkerSize(1)

    htemp.SetStats(0)   
    htemp.SetLineWidth(width)

    if htemp.GetMaximum() >= 10000:
        htemp.GetYaxis().SetMaxDigits(4)
    else: htemp.GetYaxis().SetMaxDigits(3)

    htemp.SetLineColor(lineColour)
    htemp.SetFillColor(fillColour)
    htemp.SetFillStyle(fillStyle)

    htemp.GetXaxis().SetTitle(xtitle)
    htemp.GetYaxis().SetTitle("Events / "+str(EvBin)+" GeV")
    htemp.GetYaxis().SetTitleSize(0.025)
    htemp.GetYaxis().SetLabelFont(43)
    htemp.GetYaxis().SetLabelSize(25)

    return htemp

def drawRatio(bkgh,data,var):

  nbin = data.GetNbinsX();

  ratio = data.Clone("ratio");
  ratio.Sumw2();

  ratio_band = bkgh.Clone("ratio_band")
  ratio_band.Sumw2()

  ratio_one = bkgh.Clone("ratio_one")
  ratio_one.Sumw2(0)

  ratio_band.Divide(ratio_one)
  ratio_band.SetFillColor(12);
  ratio_band.SetFillStyle(3244);

  ratio.Divide(bkgh);

  ratio.SetStats(0)
  ratio.SetTitle("")

  ratio.GetXaxis().SetTitle(var[1])
  ratio.GetXaxis().SetTitleSize(0.135)
  ratio.GetXaxis().SetLabelFont(43);
  ratio.GetXaxis().SetLabelSize(30);

  ratio.GetYaxis().SetTitle("Data/MC")
  ratio.GetYaxis().SetTitleSize(0.125)
  ratio.GetYaxis().SetTitleOffset(0.3)
  ratio.GetYaxis().SetLabelFont(43);
  ratio.GetYaxis().SetLabelSize(25);
  ratio.GetYaxis().SetNdivisions(6)  

  ratio.SetMarkerStyle(21);
  ratio.SetMaximum(2.5);
  ratio.SetMinimum(0);

  ratio.GetYaxis().ChangeLabel(1, -1, 0)
  ratio.GetYaxis().ChangeLabel(2, -1, 0)
  ratio.GetYaxis().ChangeLabel(4, -1, 0)
  ratio.GetYaxis().ChangeLabel(6, -1, 0)

  return ratio, ratio_band


def drawPad1(var, logy = False):
  pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
  # if var[1] == "M_{vis} (GeV)":
    # pad1.SetLogy();
  if logy == True:
      pad1.SetLogy();
  pad1.SetGridx();
  pad1.SetBottomMargin(0);
  pad1.Draw();
  pad1.cd();

def drawPad2():
  pad12 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
  pad12.SetTopMargin(0.1);
  # pad12.SetTopMargin(0);
  pad12.SetBottomMargin(0.3);
  pad12.SetGridx();
  pad12.Draw();
  pad12.cd();  

def drawCMS(cmsTextSize = 0.055):

    cmsText     = "CMS";
    cmsTextFont   = 61  

    writeExtraText = True
    extraText   = "Work In Progress"
    extraTextFont = 52 

    # cmsTextSize = 0.3

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)
    latex.SetTextFont(cmsTextFont)
    latex.SetTextSize(cmsTextSize)
    latex.DrawLatex(0.15, 0.85, cmsText)
    latex.SetTextFont(extraTextFont)
    latex.DrawLatex(0.15, 0.8, extraText)


def plot2D(toPlot,htotal):

    var = toPlot.split("_")[-1]
    nrebin = variableName(var)
    htotal.Rebin2D(nrebin[0], nrebin[1])

    projx = htotal.ProjectionX()
    projy = htotal.ProjectionY()

    c1.SetLogz()
    c1.SetRightMargin(0.15)
    htotal.SetStats(0)
    htotal.SetTitle(toPlot)
    htotal.Draw("colz")
    if (toPlot.split("_")[-2] == "dRcut" or toPlot.split("_")[-2] == "dRcutl") and ( toPlot.split("_")[-1] == "TauPtdRl" or toPlot.split("_")[-1] == "MuonPtdRl" or toPlot.split("_")[-1] == "MuonPtdRgenMu" or toPlot.split("_")[-1] == "TauPtdRgenMu" or toPlot.split("_")[-1] == "TauPtdRj2tau"):
        htotal.GetYaxis().SetRangeUser(0,0.5)
    if len(nrebin) > 2:
        htotal.GetXaxis().SetRangeUser(0,nrebin[2])

    c1.SaveAs(path+"/"+DR+toPlot+iteration+"_2DPlot.png")
    c1.Print(path+"/"+DR+"_2DPlots_"+iteration+".pdf")
    c1.Clear()

    # projx.SetOptStat(111100)
    projx.Draw("E hist")
    projx.GetYaxis().SetTitle("Events / "+str(nrebin[0])+" GeV")
    if projx.GetMaximum() >= 10000:
        projx.GetYaxis().SetMaxDigits(4)
    else: projx.GetYaxis().SetMaxDigits(3)
    projx.SetFillColor(0)
    projx.SetLineWidth(3)

    c1.SaveAs(path+"/"+DR+toPlot+iteration+"_ProjX.png")
    c1.Print(path+"/"+DR+"_2DPlots_"+iteration+".pdf")
    c1.Clear()

    # projy.SetOptStat(111100)
    projy.Draw("E hist")
    projy.GetYaxis().SetTitle("Events / "+str(nrebin[1])+" GeV")
    if projy.GetMaximum() >= 10000:
        projy.GetYaxis().SetMaxDigits(4)
    else: projy.GetYaxis().SetMaxDigits(3)
    if (toPlot.split("_")[-2] == "dRcut" or toPlot.split("_")[-2] == "dRcutl") and ( toPlot.split("_")[-1] == "TauPtdRl" or toPlot.split("_")[-1] == "MuonPtdRl" or toPlot.split("_")[-1] == "MuonPtdRgenMu" or toPlot.split("_")[-1] == "TauPtdRgenMu" or toPlot.split("_")[-1] == "TauPtdRj2tau"):
        projy.GetXaxis().SetRangeUser(0,0.5)
    if len(nrebin) > 2:
        projy.GetXaxis().SetRangeUser(0,nrebin[2])

    projy.SetFillColor(0)
    projy.SetLineWidth(3)

    c1.SaveAs(path+"/"+DR+toPlot+iteration+"_ProjY.png")
    c1.Print(path+"/"+DR+"_2DPlots_"+iteration+".pdf")
    c1.Clear()

def drawSOverB(background,signal,var):

  nbin = signal.GetNbinsX();

  h_sqrt = ROOT.TH1D("h_sqrt", "", nbin, 0 ,100);
  h_sqrt.Sumw2(); 

  ratio = signal.Clone("ratio");
  ratio.Sumw2();

  for i in range(nbin):
    s = ratio.GetBinContent(i+1)
    b = background.GetBinContent(i+1)
    if b > 0 :
      b_sqrt = math.sqrt(b)
      h_sqrt.SetBinContent(i+1, b_sqrt)

  ratio.Divide(h_sqrt)

  ratio.SetStats(0)
  ratio.SetTitle("")

  ratio.GetXaxis().SetTitle(var[1])
  ratio.GetXaxis().SetTitleSize(0.135)
  ratio.GetXaxis().SetLabelFont(43);
  ratio.GetXaxis().SetLabelSize(30);

  ratio.GetYaxis().SetTitle("S/#sqrt{B}")
  ratio.GetYaxis().SetTitleSize(0.125)
  ratio.GetYaxis().SetTitleOffset(0.3)
  ratio.GetYaxis().SetLabelFont(43);
  ratio.GetYaxis().SetLabelSize(25);
  ratio.GetYaxis().SetNdivisions(6)  

  ratio.SetMarkerStyle(21);
  # ratio.SetMaximum(2.5);
  ratio.SetMinimum(0);

  ratio.GetYaxis().ChangeLabel(1, -1, 0)

  return ratio

def makeBkg(rootFile, SAMPLE, histo, xtitle = "x", ytitle = "y", rebin = 1):

    f = ROOT.TFile(rootFile)

    htot = f.Get(SAMPLE[0]+"_"+histo)
    htot.Rebin(rebin)

    for sample in SAMPLE[1:]:
        h = f.Get(sample+"_"+histo)
        h.Rebin(rebin)
        htot.Add(h)

    htot.Draw()

    return htot
