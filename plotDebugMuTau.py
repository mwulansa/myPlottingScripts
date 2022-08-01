import ROOT,os,sys
import myPlotFunc
import numpy as np

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

r = {
	'MuonPt' 	: [20, "P_{T} (GeV)", 500],
	'Muon1Pt' 	: [20, "P_{T} (GeV)", 500],
	'Muon2Pt' 	: [20, "P_{T} (GeV)", 500],
	'ElectronPt': [20, "P_{T} (GeV)", 500],
	'TauPt'	 	: [20, "P_{T} (GeV)", 260],
	'TauPt0'	 	: [20, "P_{T} (GeV)", 260],
	'TauPt1'	 	: [20, "P_{T} (GeV)", 260],
	'TauPt10'	 	: [20, "P_{T} (GeV)", 260],
	'JetPt'	 	: [100, "P_{T} (GeV)", 2000],
	'MetPt'	 	: [20, "P_{T} (GeV)", 500],
	'dRl'	 	: [5, "dR", 5],
	'dRj'	 	: [5, "dR", 5],
	'dPhil'	 	: [5, "dPhi", 3.5],
	'dPhij'	 	: [5, "dphi", 3.5],
	'Mt'	 	: [5, "M_{T} (GeV)", 150],
	'Nj'     	: [1, "N_{jet}", 10],
	'lowMET' 	: [5, "M_{vis} (GeV)", 100],
	'dRcut'	 	: [5, "M_{vis} (GeV)", 100],
	'lowMt'	 	: [5, "M_{vis} (GeV)", 100],
	'mTcut'	 	: [5, "M_{vis} (GeV)", 100],
	'highMET' 	: [5, "M_{vis} (GeV)", 100],
	'Metcut' 	: [5, "M_{vis} (GeV)", 100],
	'highMt'	: [5, "M_{vis} (GeV)", 100],
	'dPhicut'	: [5, "M_{vis} (GeV)", 100],
	'SS'	: [5, "M_{vis} (GeV)", 100],
	'Trigger'	: [1, "Triggers", 8],
	'Mass'		: [5, "M_{vis} (GeV)", 100]
}

#MuTauDebug - v11
#FullyLeptonic - v2
#JetHT - v2
#HTTrig - v2
#Inclusive - v3
#Nominal - v5
#Altered - v3

if "-al" in opts:
	ver = "v12"
	dataver = "v12"
	iteration = "AlteredID"

if "-nm" in opts:
	ver = "v12"
	dataver = "v12"
	iteration = "Nominal"

dataset = "SingleMuon"
oneData = False

if "-od" in opts:
	oneData = True

path = '/Users/muti/Documents/Analysis/studyCleanedTaus/'+iteration+"_"+ver
isExist = os.path.exists(path)

if not isExist:
	os.makedirs(path)
	print("Folder created, outputs in", path)

if isExist:
	print("Outputs in", path)


if iteration == "FullyLeptonic":
	d = ROOT.TFile("h_debugMuTau_HighHT_FullyLeptonic_"+dataset+"_"+ver+".root");
	print("h_debugMuTau_HighHT_FullyLeptonic_"+dataset+"_"+ver+".root")
elif iteration == "JetHT":
	d = ROOT.TFile("h_debugMuTau_HighHT_FullyLeptonic_JetHT_"+dataset+"_"+ver+".root");
	print("h_debugMuTau_HighHT_FullyLeptonic_JetHT_"+dataset+"_"+ver+".root")
elif iteration == "HTTrig":
	d = ROOT.TFile("h_debugMuTau_HighHT_FullyLeptonic_HTTrig_"+dataset+"_"+ver+".root");
	print("h_debugMuTau_HighHT_FullyLeptonic_HTTrig_"+dataset+"_"+ver+".root")
elif iteration == "Nominal":
	d1 = ROOT.TFile("h_debugMuTau_HighHT_Data_SingleMuon_"+dataver+".root");
	d2 = ROOT.TFile("h_debugMuTau_HighHT_Data_JetHT_"+dataver+".root");
elif iteration == "AlteredID":
	d1 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_SingleMuon_"+dataver+".root");
	d2 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_JetHT_"+dataver+".root");
else: 
	d = ROOT.TFile("h_debugMuTau_HighHT_"+dataset+"_"+ver+".root");
	print("h_debugMuTau_HighHT_"+dataset+"_"+ver+".root")


SAMPLES = ['Diboson','WJetsToLNu','DYJetsToLL','DYJetsToLL_M-4to50','TTJets','QCD']
massTCP = 'm30'

collection = "TauPt"
# histToPlot = ['hMuMu_lowMET', 'hMuMu_lowMET_Muon1Pt', 'hMuMu_lowMET_Muon2Pt', 'hMuMu_lowMET_JetPt', 'hMuMu_lowMET_MetPt', 'hMuMu_lowMET_Nj', 'hMuTau_lowMET', 'hMuTau_lowMET_TauPt', 'hMuTau_lowMET_JetPt', 'hMuTau_lowMET_Nj', 'hMuTau_lowMET_MuonPt']
histToPlot = ['hMuTau_SS_TauPt', 'hMuTau_SS_dRcut_TauPt','hMuTau_SS_lowMET_TauPt', 'hMuTau_SS_lowMET_dRcut_TauPt','hMuTau_SS_lowMET_highMt_TauPt','hMuTau_SS_lowMET_dRcut_highMt_TauPt', 'hMuTau_SS_lowMET_lowMt_TauPt', 'hMuTau_SS_lowMET_dRcut_lowMt_TauPt' , 'hMuTau_SS_dRcut_highMET_TauPt', 'hMuTau_SS_dRcut_highMET_highMt_TauPt', 'hMuTau_SS_dRcut_highMET_lowMt_TauPt','hMuTau_lowMET_lowMt_TauPt','hMuTau_lowMET_dRcut_lowMt_TauPt','hMuTau_highMt_highMET_TauPt','hMuTau_highMt_dRcut_highMET_TauPt']

if "-dr1" in opts:
	collection = "DR1"
	# REGION = ['hMuTau_highMt_dRcut','hMuTau_highMt_dRcut_highMET']
	REGION = ['hMuTau_highMt_dRcut_highMET','hMuTau_highMt_dRcut','hMuTau_highMt_dRcut_highMET_110','hMuTau_highMt_dRcut_highMET_120','hMuTau_highMt_dRcut_highMET_140','hMuTau_highMt_dRcut_highMET_150','hMuTau_highMt_dRcut_highMET_160']
if "-dr2" in opts:
	collection = "DR2"	
	REGION = ['hMuTau_lowMET_dRcut_lowMt', 'hMuTau_lowMET_lowMt']
if "-dr3" in opts:
	collection = "DR3"
	REGION = ['hMuTau_SS_dRcut_highMET_lowMt']
if "-ar" in opts:	
	if iteration == "Nominal": collection = "SR"
	if iteration == "AlteredID": collection = "AR"
	REGION = ['hMuTau_SR_dRcut_highMET_lowMt']
if "-dr4" in opts:
	collection = "DR4"
	REGION = ['hMuTau_lowMET_dRcut_highMt','hMuTau_lowMET_highMt']
if "-dr5" in opts:
	collection = "DR5"
	REGION = ['hMuTau_SS_dRcut_highMET_highMt']
if "-dr6" in opts:
	collection = "DR6"
	REGION = ['hMuTau_SS_lowMET_dRcut_lowMt','hMuTau_SS_lowMET_lowMt']
if "-dr7" in opts:
	collection = "DR7"
	REGION = ['hMuTau_SS_lowMET_dRcut_highMt','hMuTau_SS_lowMET_highMt']

if "-custom" in opts:
	collection = "Custom"
	REGION = ['hMuTau_SS', 'hMuTau_SR', 'hMuTau_SS_dRcut', 'hMuTau_SR_dRcut', 'hMuTau_lowMET', 'hMuTau_lowMET_dRcut', 'hMuTau_SS_dRcut_highMET', 'hMuTau_SR_dRcut_highMET']

VARIABLE = ['TauPt', 'Nj', 'JetPt', 'MuonPt', 'MetPt', 'Mass']
# VARIABLE = ['MetPt']
# VARIABLE = ['Mt']

histToPlot = []

for region in REGION:
    # histToPlot.append(region)
    for variable in VARIABLE:
        histToPlot.append(region+"_"+variable)


ROOT.gStyle.SetOptStat(111010)

c1 = ROOT.TCanvas("c1","c1",850, 850)
c1.cd()
c1.SetLogy()
if oneData == True:
	c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf[")
else:
	c1.Print(path+"/"+collection+"_"+iteration+"_"+ver+".pdf[")

histToNorm = []
ROOT.TH1.AddDirectory(0)

for toPlot in histToPlot:
	f = ROOT.TFile("h_"+toPlot+"_"+iteration+"_"+ver+".root")
	print("h_"+toPlot)

	toRebin = toPlot.split("_")
	hists = {}
	bkg = ROOT.THStack("Bkg",toPlot+";M_{#tau#tau};Events / "+str(r[toRebin[-1]][0])+" GeV")
	bkg_nQCD = ROOT.THStack("Bkg_nQCD",toPlot+"_MC_{non-QCD};"+str(r[toRebin[-1]][1])+";Events / "+str(r[toRebin[-1]][0])+" GeV")

	integral = {}

	for sample in SAMPLES:
		h = f.Get(sample+"_"+toPlot)
		nbinx = h.GetNbinsX()
		# integral[sample] = h.Integral(1,nbinx+1)
		h.Rebin(r[toRebin[-1]][0])
		# integral[sample] = h.Integral(2,6)
		integral[sample] = h.Integral(1,nbinx+1)
		bkg.Add(h)
		if sample != 'QCD':
			bkg_nQCD.Add(h)
		hists[sample] = h

	hbkg = hists['DYJetsToLL'].Clone("hbkg")
	hbkg.Sumw2()
	hbkg_nQCD = hists['DYJetsToLL'].Clone("hbkg_nQCD")
	hbkg_nQCD.Sumw2()

	for sample in SAMPLES:
		if sample != 'DYJetsToLL':
			hbkg.Add(hists[sample])
			if sample != 'QCD':
				hbkg_nQCD.Add(hists[sample])

	s1 = f.Get("TCP_Ntuple_"+massTCP+"_HT-100to400_"+toPlot)
	s2 = f.Get("TCP_Ntuple_"+massTCP+"_HT-400toInf_"+toPlot)

	sig = s1.Clone("TCP")
	sig.Sumw2()
	sig.Add(s2)
	sig.Rebin(r[toRebin[-1]][0])

	sig = myPlotFunc.plotStyle(sig, r[toRebin[-1]][0], 4, 4, fillStyle = 3334)

	if collection != "SR":

		if oneData == True:
			if dataset == "SingleMuon":
				data = d1.Get(toPlot)
			if dataset == "JetHT":
				data = d2.Get(toPlot)
		else:
			data1 = d1.Get(toPlot)
			data2 = d2.Get(toPlot)
			data = data1.Clone("data")
			data.Add(data2)

		data.Rebin(r[toRebin[-1]][0])
		data = myPlotFunc.plotStyle(data, r[toRebin[-1]][0], 1, xtitle = r[toRebin[-1]][1])

	hbkg = myPlotFunc.plotStyle(hbkg, r[toRebin[-1]][0], 12, 12, 3, r[toRebin[-1]][1], 3244, draw = "E20P")
	hbkg_nQCD = myPlotFunc.plotStyle(hbkg_nQCD, r[toRebin[-1]][0], 12, 12, 3, r[toRebin[-1]][1], 3244, draw = "E20P")

	# if collection != "SR":	
	# 	data_norm = data.Clone("data_norm")
	# 	data_norm.Sumw2()
	# 	data_norm.Scale(1/data.Integral())
	# 	histToNorm.append(data_norm)

	# hbkg_norm = hbkg_nQCD.Clone("hbkg_norm")
	# hbkg_norm.Sumw2()
	# hbkg_norm.Scale(1/hbkg_nQCD.Integral())
	
	# histToNorm.append(hbkg_norm)


	ld = ROOT.TLegend(0.4,0.5,0.83,0.88)
	ld.SetLineWidth(0)
	ld.SetNColumns(2)

	if collection != "SR":
		nbindata = data.GetNbinsX()
		if oneData == True:
			ld.AddEntry(data, dataset+" - "+str(int(data.Integral(1,nbindata+1))), "l");
		elif iteration == "Inclusive" or iteration == "AlteredID" or iteration == "Nominal":
			ld.AddEntry(data, "SingleMuon + JetHT - "+str(int(data.Integral(1,nbindata+1))), "l");
		else: ld.AddEntry(data, dataset+" - "+str(int(data.Integral(1,nbindata+1))), "l");

	c1.cd()

	if collection != "SR":
		data.SetTitle(toPlot+"_DataOnly")
		data.Draw("E0P");	
		data.SetMaximum(data.GetMaximum()*10)
		data.SetMinimum(1)
		data.GetYaxis().SetTitleSize(0.04)
		if data.GetMaximum() >= 10000:
			data.GetYaxis().SetMaxDigits(4)
		else: data.GetYaxis().SetMaxDigits(3)

		if toRebin[-1] == "TauPt":
			data.GetXaxis().SetRangeUser(0,260)
	ld.Draw("same")

	# myPlotFunc.drawCMS()

	if oneData == True:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+dataset+"Only_"+ver+"_DataOnly.png")
		c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf")
		c1.Clear()
	else:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_DataOnly.png")
		c1.Print(path+"/"+collection+"_"+iteration+"_"+ver+".pdf")
		c1.Clear()

	lmc = ROOT.TLegend(0.3,0.65,0.83,0.88)
	lmc.SetLineWidth(0)
	lmc.SetNColumns(2)
	lmc.AddEntry(hists['TTJets'], "TTJets - "+str(int(integral['TTJets'])), "f");
	lmc.AddEntry(hists['DYJetsToLL'], "DYJetsToLL - "+str(int(integral['DYJetsToLL']+integral['DYJetsToLL_M-4to50'])), "f");
	lmc.AddEntry(hists['WJetsToLNu'], "WJetsToLNu - "+str(int(integral['WJetsToLNu'])), "f");
	lmc.AddEntry(hists['Diboson'], "Diboson - "+str(int(integral['Diboson'])), "f");

	c1.cd()
	bkg_nQCD.Draw("hist")
	bkg_nQCD.SetMaximum(bkg_nQCD.GetMaximum()*10)
	bkg_nQCD.SetMinimum(1)
	bkg_nQCD.GetXaxis().SetTitleSize(0.04)
	hbkg_nQCD.Draw("same E20P");

	if bkg_nQCD.GetMaximum() >= 10000:
		bkg_nQCD.GetYaxis().SetMaxDigits(4)
	else: bkg_nQCD.GetYaxis().SetMaxDigits(3)

	if toRebin[-1] == "TauPt":
		bkg_nQCD.GetXaxis().SetRangeUser(0,260)
		hbkg_nQCD.GetXaxis().SetRangeUser(0,260)

	lmc.Draw("same")

	# myPlotFunc.drawCMS()

	c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_MCOnly.png")
	c1.Print(path+"/"+collection+"_"+iteration+"_"+ver+".pdf")
	c1.Clear()

	#lg = ROOT.TLegend(0.28,0.35,0.53,0.67)
	lg = ROOT.TLegend(0.3,0.65,0.83,0.88)
	lg.SetLineWidth(0)
	lg.SetNColumns(2)
	if collection != "SR":
		if oneData == True:
			lg.AddEntry(data, dataset+" - "+str(int(data.Integral(1,nbindata+1))), "l");
		elif iteration == "Inclusive" or iteration == "AlteredID" or iteration == "Nominal":
			lg.AddEntry(data, "SingleMuon + JetHT - "+str(int(data.Integral(1,nbindata+1))), "l");
		else: lg.AddEntry(data, dataset+" - "+str(int(data.Integral(1,nbindata+1))), "l");
	lg.AddEntry(hists['QCD'], "QCD - "+str(int(integral['QCD'])), "f");
	lg.AddEntry(hists['TTJets'], "TTJets - "+str(int(integral['TTJets'])), "f");
	lg.AddEntry(hists['DYJetsToLL'], "DYJetsToLL - "+str(int(integral['DYJetsToLL']+integral['DYJetsToLL_M-4to50'])), "f");
	lg.AddEntry(hists['WJetsToLNu'], "WJetsToLNu - "+str(int(integral['WJetsToLNu'])), "f");
	lg.AddEntry(hists['Diboson'], "Diboson - "+str(int(integral['Diboson'])), "f");
	nbintcp = sig.GetNbinsX()
	lg.AddEntry(sig, "TCP_"+massTCP+" - "+str(int(sig.Integral(1,nbintcp+1))), "f");
	lg.AddEntry(hbkg, "Bkg. Uncert.", "f");

	l = ROOT.TLine(0,1,(r[toRebin[-1]][2]),1)
	l.SetLineColor(ROOT.kRed)
	l.SetLineStyle(10)

	# if collection != "SR":		

	# 	ratio = []	

	# 	for k in range(1,5):
	# 		nom = data.GetBinContent(k+1)
	# 		denom = hbkg.GetBinContent(k+1)
	# 		if denom > 0.0 :
	# 			ratioDataMC = (nom-denom)/denom
	# 			ratio.append(ratioDataMC)
	# 		if denom == 0 : 
	# 			ratioDataMC = 0
	# 			ratio.append(ratioDataMC)

	# 	ave = sum(ratio)/len(ratio)

	myPlotFunc.drawPad1(r[toRebin[-1]], logy = True);
	bkg.SetMinimum(1)
	# bkg.SetMaximum(1E7)
	if collection != "SR":
		if bkg.GetMaximum() < data.GetMaximum():
			bkg.SetMaximum(data.GetMaximum()*10)
	# bkg.SetMaximum(1E4)
	bkg.Draw("hist")
	bkg.GetYaxis().SetTitleSize(0.05)
	hbkg.Draw("same E20P");
	if collection != "SR":
		data.Draw("same E0P");
		if toRebin[-1] == "TauPt": data.GetXaxis().SetRangeUser(0,260)
	sig.Draw("same hist")
	bkg.GetYaxis().SetTitle()
	# myPlotFunc.drawCMS()
	if toRebin[-1] == "TauPt":
		bkg.GetXaxis().SetRangeUser(0,260)
		hbkg.GetXaxis().SetRangeUser(0,260)		
		sig.GetXaxis().SetRangeUser(0,260)
	if toRebin[-1] != "Trigger" :
		lg.Draw("same")
	c1.cd();

	if collection != "SR":	
		myPlotFunc.drawPad2();	
		rhist = myPlotFunc.drawRatio(hbkg,data,r[toRebin[-1]])
		rhist[0].Draw()
		rhist[1].Draw("same E20P")


		if r[toRebin[-1]] == 'Mass':
			ave = rhist[0].Integral(2,6)/5.0
		else:
			ave = rhist[0].Integral()/nbindata	

		print("Average Data/MC = ", ave)
		
		aveDataMC = ROOT.TLine(0, ave, r[toRebin[-1]][2], ave)
		aveDataMC.Draw("same Y+")

		axis8 = ROOT.TGaxis(r[toRebin[-1]][2],0,r[toRebin[-1]][2], 2.5 , 0 , 2.5 , 50010,"+L");
		axis8.SetName("axis8");
		axis8.Draw("same");
		axis8.SetTitle("Average Data/MC");

		axis8.ChangeLabel(1, -1, 0)
		axis8.ChangeLabel(2, -1, 0)
		axis8.ChangeLabel(4, -1, 0)
		axis8.ChangeLabel(6, -1, 0)

		axis8.SetTitleSize(0.075)
		axis8.SetTitleOffset(0.3)
		axis8.SetLabelSize(25)
		axis8.SetLabelFont(43)
		axis8.SetTitleColor(ROOT.kBlue)

		aveDataMC.SetLineWidth(3)
		aveDataMC.SetLineColor(ROOT.kBlue)
		aveDataMC.SetLineStyle(10)
		# myPlotFunc.drawCMS()

	else :
		myPlotFunc.drawPad2();
		sbhist = myPlotFunc.drawSOverB(hbkg, sig, r[toRebin[-1]])
		sbhist.Draw()
		# myPlotFunc.drawCMS()

	if oneData == True:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+dataset+"Only_"+ver+".png")
		c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf")
		c1.Clear()
	else:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+".png")
		c1.Print(path+"/"+collection+"_"+iteration+"_"+ver+".pdf")
		c1.Clear()

	# print(hists)

# if collection != "SR":	

# 	histToNorm[2] = myPlotFunc.plotStyle(histToNorm[2], lineColour = 4, xtitle = r["TauPt"][1], EvBin = r["TauPt"][0])

# 	ln = ROOT.TLegend(0.4,0.5,0.83,0.88)
# 	ln.SetLineWidth(0)
# 	ln.SetNColumns(2)
# 	ln.AddEntry(histToNorm[2], "Before dR cut", "l")
# 	ln.AddEntry(histToNorm[0], "After dR cut", "l")

# 	histToNorm[2].Draw()
# 	histToNorm[0].Draw("same")
# 	ln.Draw("same")

# 	histToNorm[2].GetXaxis().SetRangeUser(0,260)
# 	histToNorm[0].GetXaxis().SetRangeUser(0,260)

# 	c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_DataOnly_Norm.png")
# 	c1.Print(path+"/"+collection+"_"+iteration+"_"+ver+".pdf")
# 	c1.Clear()

# 	histToNorm[1] = myPlotFunc.plotStyle(histToNorm[1], lineColour = 1, xtitle = r["TauPt"][1], EvBin = r["TauPt"][0])
# 	histToNorm[3] = myPlotFunc.plotStyle(histToNorm[3], lineColour = 4, xtitle = r["TauPt"][1], EvBin = r["TauPt"][0])

# 	histToNorm[3].Draw()
# 	histToNorm[1].Draw("same")
# 	ln.Draw("same")

# 	histToNorm[3].GetXaxis().SetRangeUser(0,260)
# 	histToNorm[1].GetXaxis().SetRangeUser(0,260)

# 	c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_MCOnly_Norm.png")
# 	c1.Print(path+"/"+collection+"_"+iteration+"_"+ver+".pdf")
# 	c1.Clear()

print("Outputs in", path)
print(histToPlot)

if oneData == True:
	c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf]")
else:
	c1.Print(path+"/"+collection+"_"+iteration+"_"+ver+".pdf]")