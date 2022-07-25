import ROOT, sys, os
import myPlotFunc

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

def plot2D(toPlot,htotal,title):

    var = toPlot.split("_")[-1]
    nrebin = myPlotFunc.variableName(var)
    htotal.Rebin2D(nrebin[0], nrebin[1])

    projx = htotal.ProjectionX()
    projy = htotal.ProjectionY()

    c1.SetLogz()
    c1.SetRightMargin(0.15)
    htotal.SetStats(0)
    htotal.SetTitle(toPlot+"_"+title)
    htotal.Draw("colz")
    if (toPlot.split("_")[-2] == "dRcut" or toPlot.split("_")[-2] == "dRcutl") and ( toPlot.split("_")[-1] == "TauPtdRl" or toPlot.split("_")[-1] == "MuonPtdRl" or toPlot.split("_")[-1] == "MuonPtdRgenMu" or toPlot.split("_")[-1] == "TauPtdRgenMu" or toPlot.split("_")[-1] == "TauPtdRj2tau"):
        htotal.GetYaxis().SetRangeUser(0,0.5)
    if len(nrebin) > 2:
        htotal.GetXaxis().SetRangeUser(0,nrebin[2])

    c1.SaveAs(path+"/"+DR+toPlot+iteration+"_"+title+"_2DPlot.png")
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

    c1.SaveAs(path+"/"+DR+toPlot+iteration+"_"+title+"_ProjX.png")
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

    c1.SaveAs(path+"/"+DR+toPlot+iteration+"_"+title+"_ProjY.png")
    c1.Print(path+"/"+DR+"_2DPlots_"+iteration+".pdf")
    c1.Clear()

r = {
	'MuonPt' 	: [10, "Pt(GeV)", 250],
	'Muon1Pt' 	: [20, "Pt(GeV)", 500],
	'Muon2Pt' 	: [20, "Pt(GeV)", 500],
	'ElectronPt': [20, "Pt(GeV)", 500],
	'TauPt'	 	: [10, "Pt(GeV)", 250],
	'TauPt0'	 	: [20, "Pt(GeV)", 500],
	'TauPt1'	 	: [20, "Pt(GeV)", 500],
	'TauPt10'	 	: [20, "Pt(GeV)", 500],
	'JetPt'	 	: [50, "Pt(GeV)", 2000],
	'MetPt'	 	: [20, "Pt(GeV)", 500],
	'dRl'	 	: [1, "dR", 5],
	'dRj'	 	: [1, "dR", 5],
	'dPhil'	 	: [5, "dPhi", 3.5],
	'dPhij'	 	: [5, "dphi", 3.5],
	'Mt'	 	: [20, "Mt(GeV)", 500],
	'Nj'     	: [1, "N_{jet}", 10],
	'Mass'		: [5, "M_{vis}(GeV)", 100],
	'lowMET' 	: [5, "M_{vis}(GeV)", 100],
	'dRcut'	 	: [5, "M_{vis}(GeV)", 100],
	'lowMt'	 	: [5, "M_{vis}(GeV)", 100],
	'mTcut'	 	: [5, "M_{vis}(GeV)", 100],
	'highMET' 	: [5, "M_{vis}(GeV)", 100],
	'Metcut' 	: [5, "M_{vis}(GeV)", 100],
	'highMt'	: [5, "M_{vis}(GeV)", 100],
	'dPhicut'	: [5, "M_{vis}(GeV)", 100],
	'Trigger'	: [1, "Triggers", 8]
}

def addTCP(massTCP):

	s1 = f.Get("TCP_Ntuple_"+massTCP+"_HT-100to400_"+toPlot)
	s2 = f.Get("TCP_Ntuple_"+massTCP+"_HT-400toInf_"+toPlot)

	sig = s1.Clone("TCP")
	sig.Sumw2()
	sig.Add(s2)

	return sig


if "-al" in opts:
	iteration = '2DAltered'
	ver = 'v5'

if "-nm" in opts:
	iteration = '2DNominal'
	ver = 'v5'

path = '/Users/muti/Documents/Analysis/studyCleanedTaus/Taus2DPlots_'+ver
isExist = os.path.exists(path)

if not isExist:
	os.makedirs(path)
	print("Folder created, outputs in", path)

if isExist:
	print("Outputs in", path)

if "-ss" in opts:
	DR = "SS"
	histlist = ['hMuTau_SS_TauPtJetPt', 'hMuTau_SS_TauPtJet2Pt', 'hMuTau_SS_TauPtMuonPt']

if "-dr2" in opts:
	DR = "dr2"
	REGION = ['hMuTau_OS_lowMET_lowMt','hMuTau_OS_lowMET_lowMt_dRcut']
	if "-dRl" in opts:
		DR = "dr2_dRl"
		REGION = ['hMuTau_OS_lowMET_lowMt_dRcutl']
	if "-dRjt" in opts:
		DR = "dr2_dRjt"
		REGION = ['hMuTau_OS_lowMET_lowMt_dRcutjt']
	if "-dRjm" in opts:
		DR = "dr2_dRjm"
		REGION = ['hMuTau_OS_lowMET_lowMt_dRcutjm']

if "-dr3" in opts:
	DR = "DR3"
	REGION = ['hMuTau_SS_highMET_lowMt','hMuTau_SS_highMET_lowMt_dRcut']
	if "-dRl" in opts:
		DR = "DR3_dRl"
		REGION = ['hMuTau_SS_highMET_lowMt_dRcutl']
	if "-dRjt" in opts:
		DR = "DR3_dRjt"
		REGION = ['hMuTau_SS_highMET_lowMt_dRcutjt']
	if "-dRjm" in opts:
		DR = "DR3_dRjm"
		REGION = ['hMuTau_SS_highMET_lowMt_dRcutjm']

if "-dr4" in opts:
	DR = "dr4"
	REGION = ['hMuTau_OS_lowMET_highMt','hMuTau_OS_lowMET_highMt_dRcut']
	if "-dRl" in opts:
		DR = "dr4_dRl"
		REGION = ['hMuTau_OS_lowMET_highMt_dRcutl']
	if "-dRjt" in opts:
		DR = "dr4_dRjt"
		REGION = ['hMuTau_OS_lowMET_highMt_dRcutjt']
	if "-dRjm" in opts:
		DR = "dr4_dRjm"
		REGION = ['hMuTau_OS_lowMET_highMt_dRcutjm']

if "-dr6" in opts:
	DR = "DR6"
	REGION = ['hMuTau_SS_lowMET_lowMt','hMuTau_SS_lowMET_lowMt_dRcut']
	if "-dRl" in opts:
		DR = "DR6_dRl"
		REGION = ['hMuTau_SS_lowMET_lowMt_dRcutl']
	if "-dRjt" in opts:
		DR = "DR6_dRjt"
		REGION = ['hMuTau_SS_lowMET_lowMt_dRcutjt']
	if "-dRjm" in opts:
		DR = "DR6_dRjm"
		REGION = ['hMuTau_SS_lowMET_lowMt_dRcutjm']

if "-sr" in opts:
	DR = "SR"
	REGION = ['hMuTau_SR_highMET_lowMt','hMuTau_SR_highMET_lowMt_dRcut']

# VARIABLE = ['TauPtdRjmu']
VARIABLE = ['TauPtdRjmu','TauPtdRjtau','TauPtdRl','MuonPtdRl','TauPtMuonPt','TauPtJetPt','TauPtJet2Pt','TauPtdRj2tau','DimuonMass','MuonPtMuon2Pt','TauPtdRl2','TauPtdRgenMu','MuonPtdRgenMu']
# VARIABLE = ['TauPtJetPt', 'TauPtJet2Pt', 'TauPtMuonPt', 'TauPtdRl', 'TauPtdRj2tau', 'TauPtdRjtau', 'TauPtdRjmu', 'MuonPtdRl', 'TauPtdRgenMu', 'MuonPtdRgenMu']

histlist = []

for variable in VARIABLE:
	for region in REGION:
		histlist.append(region+"_"+variable)

print(histlist)

SAMPLES = ['Diboson','WJetsToLNu','DYJetsToLL','DYJetsToLL_M-4to50','TTJets']
massTCP = 'm30'

ROOT.gStyle.SetOptStat(111010)

c1 = ROOT.TCanvas("c1","c1",1000, 1200)
c1.cd()	
c1.Print(path+"/"+DR+"_2DPlots_"+iteration+".pdf[")

hists = {}

for toPlot in histlist:
	f = ROOT.TFile("h_"+toPlot+"_"+iteration+"_"+ver+".root")

	sig30 = addTCP('m30')
	sig50 = addTCP('m50')

	# d1 = ROOT.TFile("h_"+toPlot+"_")

	for sample in SAMPLES:
		h = f.Get(sample+"_"+toPlot)
		hists[sample] = h

	htotal = hists['Diboson'].Clone("htotal")
	for sample in SAMPLES:
		if sample != 'Diboson':
			htotal.Add(hists[sample])

	plot2D(toPlot, htotal, "MC_{Bkg.}")
	plot2D(toPlot, sig30, "MC_{TCP_m30}")
	plot2D(toPlot, sig50, "MC_{TCP_m50}")

c1.Print(path+"/"+DR+"_2DPlots_"+iteration+".pdf]")
