import ROOT

def drawPad1(var):
  pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
  # if var[1] == "M_{vis}":
  # 	pad1.SetLogy();
  # pad1.SetLogy();
  pad1.SetGridx();
  pad1.SetBottomMargin(0);
  pad1.Draw();
  pad1.cd();

def drawPad2():
  pad12 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
  pad12.SetTopMargin(0);
  pad12.SetBottomMargin(0.3);
  pad12.SetGridx();
  pad12.Draw();
  pad12.cd();  

r = {
	'MuonPt' 	: [5, "Pt(GeV)", 250],
	'Muon1Pt' 	: [20, "Pt(GeV)", 500],
	'Muon2Pt' 	: [20, "Pt(GeV)", 500],
	'ElectronPt': [20, "Pt(GeV)", 500],
	'TauPt'	 	: [5, "Pt(GeV)", 500, "TauPt"],
	'TauPt0'	 	: [20, "Pt(GeV)", 500, "TauPt DM0"],
	'TauPt1'	 	: [20, "Pt(GeV)", 500, "TauPt DM1"],
	'TauPt10'	 	: [20, "Pt(GeV)", 500, "TauPt DM10"],
	'JetPt'	 	: [50, "Pt(GeV)", 2000],
	'MetPt'	 	: [20, "Pt(GeV)", 500, "MET"],
	'dRl'	 	: [1, "dR", 5],
	'dRj'	 	: [2, "dR", 5],
	'dPhil'	 	: [5, "dPhi", 3.5],
	'dPhij'	 	: [5, "dphi", 3.5],
	'Mt'	 	: [20, "Mt(GeV)", 500],
	'Nj'     	: [1, "N_{jet}", 10, "N-Jets"],
	'Mass'		: [5, "M_{vis}(GeV)", 100],
	'lowMET' 	: [5, "M_{vis}(GeV)", 100],
	'dRcut'	 	: [5, "M_{vis}(GeV)", 100],
	'lowMt'	 	: [5, "M_{vis}(GeV)", 100, "Visible Mass (#mu,#tau)"],
	'mTcut'	 	: [5, "M_{vis}(GeV)", 100],
	'highMET' 	: [5, "M_{vis}(GeV)", 100],
	'Metcut' 	: [5, "M_{vis}(GeV)", 100],
	'highMt'	: [5, "M_{vis}(GeV)", 100],
	'dPhicut'	: [5, "M_{vis}(GeV)", 100],
	'Trigger'	: [1, "Triggers", 8]
}

ver = 'vdRTight'

path ='/Users/muti/Documents/Analysis/studyCleanedTaus/Ff_'+ver+'/'

# DRs = ["DR3","DR6"]
DRs = ["DR1","DR4"]

# variables = ["lowMt_TauPt","lowMt_Nj","lowMt","lowMt_TauPt1","lowMt_TauPt10","lowMt_MetPt"]
# variables = ["TauPt","Nj","TauPt0","TauPt1","TauPt10"]

# variables = ["Mass"]


rFile1 = ROOT.TFile(path+DRs[0]+"_Ff.root")
rFile2 = ROOT.TFile(path+DRs[1]+"_Ff.root")

c1 = ROOT.TCanvas("c1","c1",850, 850)
c1.cd()	
c1.Print(path+"Ratio"+DRs[0]+DRs[1]+".pdf[")

for var in variables:
	print(var)
	# r1 = rFile1.Get("hMuTau_SS_dRcut_highMET_"+var)
	# r2 = rFile2.Get("hMuTau_SS_lowMET_dRcut_"+var)
	r1 = rFile1.Get("hMuTau_highMt_dRcut_highMET_"+var)
	r2 = rFile2.Get("hMuTau_lowMET_dRcut_highMt_"+var)

	ratio = r1.Clone("ratio")
	ratio.Sumw2()
	ratio.Divide(r2)

	r1.SetLineColor(ROOT.kBlack)
	r2.SetLineColor(ROOT.kBlue)

	l = ROOT.TLine(0,1,250,1)
	l.SetLineColor(ROOT.kRed)
	l.SetLineStyle(10)

	lg = ROOT.TLegend(0.58,0.5,0.83,0.83)
	lg.SetLineWidth(0)
	lg.AddEntry(r1, DRs[0])
	lg.AddEntry(r2, DRs[1])

	r1.SetTitle("F_{F}^{QCD} of "+DRs[0]+" and "+DRs[1]+" as a function of "+r[var.split("_")[-1]][3])
	drawPad1(var)
	r1.Draw()
	r2.Draw("same")
	lg.Draw("same")
	r1.GetYaxis().SetTitle("F_{F}")
	r1.GetYaxis().SetTitleSize(0.055)
	r1.GetYaxis().SetTitleOffset(0.7);
	r1.GetYaxis().SetLabelFont(43);
	r1.GetYaxis().SetLabelSize(25)
	c1.cd()
	drawPad2()
	ratio.Draw()
	l.Draw("same")

	ratio.SetStats(0)
	ratio.SetTitle("")

	ratio.GetYaxis().SetTitleSize(0.125)
	ratio.GetYaxis().SetTitle(DRs[0]+"/"+DRs[1])
	ratio.GetYaxis().SetTitleOffset(0.3);
	ratio.GetYaxis().SetLabelFont(43);
	ratio.GetYaxis().SetLabelSize(25);
	ratio.GetYaxis().SetNdivisions(4)

	ratio.GetXaxis().SetTitle(r[var.split("_")[-1]][1])
	ratio.GetXaxis().SetTitleSize(0.135)
	ratio.GetXaxis().SetLabelFont(43);
	ratio.GetXaxis().SetLabelSize(30);

	ratio.SetMarkerStyle(21);
	ratio.SetMaximum(2)

	c1.SaveAs(path+"Ratio"+DRs[0]+DRs[1]+"_"+var+".png")
	c1.Print(path+"Ratio"+DRs[0]+DRs[1]+".pdf")
	c1.Clear()

c1.Print(path+"Ratio"+DRs[0]+DRs[1]+".pdf]")
