import ROOT,os,sys
import myPlotFunc

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

r = {
	'MuonPt' 	: [20, "P_{T} (GeV)", 500],
	'Muon1Pt' 	: [20, "P_{T} (GeV)", 500],
	'Muon2Pt' 	: [20, "P_{T} (GeV)", 500],
	'ElectronPt': [20, "P_{T} (GeV)", 500],
	'TauPt'	 	: [20, "P_{T} (GeV)", 250],
	'TauPt0'	 	: [20, "P_{T} (GeV)", 250],
	'TauPt1'	 	: [20, "P_{T} (GeV)", 250],
	'TauPt10'	 	: [20, "P_{T} (GeV)", 250],
	'JetPt'	 	: [100, "P_{T} (GeV)", 2000],
	'MetPt'	 	: [20, "P_{T} (GeV)", 500],
	'dRl'	 	: [5, "dR", 5],
	'dRj'	 	: [5, "dR", 5],
	'dPhil'	 	: [5, "dPhi", 3.5],
	'dPhij'	 	: [5, "dphi", 3.5],
	'Mt'	 	: [20, "M_{T} (GeV)", 500],
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
	'Trigger'	: [1, "Triggers", 8]
}

#MuTauDebug - v11
#FullyLeptonic - v2
#JetHT - v2
#HTTrig - v2
#Inclusive - v3
#Nominal - v5
#Altered - v3

if "-al" in opts:
	ver = "v6"
	dataver = "v6"
	iteration = "AlteredID"

if "-nm" in opts:
	ver = "v6"
	dataver = "v6"
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
	histToPlot = ['hMuTau_highMt_dRcut_highMET', 'hMuTau_highMt_dRcut_highMET_TauPt', 'hMuTau_highMt_dRcut_highMET_JetPt', 'hMuTau_highMt_dRcut_highMET_Nj', 'hMuTau_highMt_highMET', 'hMuTau_highMt_highMET_TauPt', 'hMuTau_highMt_highMET_JetPt', 'hMuTau_highMt_highMET_Nj', 'hMuTau_highMt_highMET_dRl', 'hMuTau_highMt_highMET_dRj']
if "-dr2" in opts:
	collection = "DR2"	
	histToPlot = ['hMuTau_lowMET_dRcut_lowMt_TauPt','hMuTau_lowMET_lowMt_TauPt']
	# histToPlot = ['hMuTau_lowMET_dRcut_lowMt', 'hMuTau_lowMET_dRcut_lowMt_TauPt','hMuTau_lowMET_dRcut_lowMt_TauPt0','hMuTau_lowMET_dRcut_lowMt_TauPt1','hMuTau_lowMET_dRcut_lowMt_TauPt10', 'hMuTau_lowMET_dRcut_lowMt_MuonPt','hMuTau_lowMET_dRcut_lowMt_JetPt', 'hMuTau_lowMET_dRcut_lowMt_Nj', 'hMuTau_lowMET_lowMt', 'hMuTau_lowMET_lowMt_TauPt', 'hMuTau_lowMET_lowMt_JetPt', 'hMuTau_lowMET_lowMt_Nj', 'hMuTau_lowMET_lowMt_dRl', 'hMuTau_lowMET_lowMt_dRj']
if "-dr3" in opts:
	collection = "DR3"
	histToPlot = ['hMuTau_SS_dRcut_highMET_lowMt', 'hMuTau_SS_dRcut_highMET_lowMt_TauPt','hMuTau_SS_dRcut_highMET_lowMt_TauPt0','hMuTau_SS_dRcut_highMET_lowMt_TauPt1','hMuTau_SS_dRcut_highMET_lowMt_TauPt10', 'hMuTau_SS_dRcut_highMET_lowMt_MuonPt','hMuTau_SS_dRcut_highMET_lowMt_JetPt', 'hMuTau_SS_dRcut_highMET_lowMt_Nj', 'hMuTau_SS_dRcut_MetPt', 'hMuTau_SS_dRcut_highMET_Mt']
if "-ar" in opts:	
	if iteration == "Nominal": collection = "SR"
	if iteration == "AlteredID": collection = "AR"
	histToPlot = ['hMuTau_SR_dRcut_highMET_lowMt', 'hMuTau_SR_dRcut_highMET_lowMt_TauPt', 'hMuTau_SR_dRcut_highMET_lowMt_JetPt', 'hMuTau_SR_dRcut_highMET_lowMt_Nj', 'hMuTau_SR_dRcut_highMET_lowMt_MuonPt', 'hMuTau_SR_dRcut_highMET_lowMt_MetPt', 'hMuTau_SR_dRcut_highMET_lowMt_Mt','hMuTau_SR_dRcut_highMET_lowMt_TauPt0','hMuTau_SR_dRcut_highMET_lowMt_TauPt1','hMuTau_SR_dRcut_highMET_lowMt_TauPt10']
if "-dr4" in opts:
	collection = "DR4"
	histToPlot = ['hMuTau_lowMET_dRcut_highMt', 'hMuTau_lowMET_dRcut_highMt_TauPt', 'hMuTau_lowMET_dRcut_highMt_JetPt', 'hMuTau_lowMET_dRcut_highMt_Nj', 'hMuTau_lowMET_highMt', 'hMuTau_lowMET_highMt_TauPt', 'hMuTau_lowMET_highMt_JetPt', 'hMuTau_lowMET_highMt_Nj', 'hMuTau_lowMET_highMt_dRl', 'hMuTau_lowMET_highMt_dRj']
if "-dr5" in opts:
	collection = "DR5"
	histToPlot = ['hMuTau_SS_dRcut_highMET_highMt', 'hMuTau_SS_dRcut_highMET_highMt_TauPt', 'hMuTau_SS_dRcut_highMET_highMt_TauPt0','hMuTau_SS_dRcut_highMET_highMt_TauPt1','hMuTau_SS_dRcut_highMET_highMt_TauPt10','hMuTau_SS_dRcut_highMET_highMt_JetPt', 'hMuTau_SS_dRcut_highMET_highMt_Nj']
if "-dr6" in opts:
	collection = "DR6"
	histToPlot = ['hMuTau_SS_lowMET_dRcut_lowMt_TauPt','hMuTau_SS_lowMET_lowMt_TauPt']
	# histToPlot = ['hMuTau_SS_lowMET_dRcut_lowMt', 'hMuTau_SS_lowMET_dRcut_lowMt_TauPt', 'hMuTau_SS_lowMET_dRcut_lowMt_MuonPt','hMuTau_SS_lowMET_dRcut_lowMt_JetPt', 'hMuTau_SS_lowMET_dRcut_lowMt_Nj', 'hMuTau_SS_lowMET_lowMt', 'hMuTau_SS_lowMET_lowMt_TauPt', 'hMuTau_SS_lowMET_lowMt_JetPt', 'hMuTau_SS_lowMET_lowMt_Nj', 'hMuTau_SS_lowMET_lowMt_dRj', 'hMuTau_SS_lowMET_lowMt_dRl','hMuTau_SS_lowMET_lowMt_MuonPt']

if "-dr7" in opts:
	collection = "DR7"
	histToPlot = ['hMuTau_SS_lowMET_dRcut_highMt', 'hMuTau_SS_lowMET_dRcut_highMt_TauPt','hMuTau_SS_lowMET_dRcut_highMt_MuonPt', 'hMuTau_SS_lowMET_dRcut_highMt_JetPt', 'hMuTau_SS_lowMET_dRcut_highMt_Nj', 'hMuTau_SS_lowMET_highMt', 'hMuTau_SS_lowMET_highMt_TauPt', 'hMuTau_SS_lowMET_highMt_JetPt', 'hMuTau_SS_lowMET_highMt_Nj', 'hMuTau_SS_lowMET_highMt_dRl', 'hMuTau_SS_lowMET_highMt_dRj','hMuTau_SS_lowMET_highMt_MuonPt']

ROOT.gStyle.SetOptStat(111010)

c1 = ROOT.TCanvas("c1","c1",850, 850)
c1.cd()
# c1.SetLogy()
if oneData == True:
	c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf[")
else:
	c1.Print(path+"/"+collection+"_"+iteration+".pdf[")

histToNorm = []
ROOT.TH1.AddDirectory(0)

for toPlot in histToPlot:
	f = ROOT.TFile("h_"+toPlot+"_"+iteration+"_"+ver+".root")
	print("h_"+toPlot)

	toRebin = toPlot.split("_")
	hists = {}
	bkg = ROOT.THStack("Bkg",toPlot+";M_{#tau#tau};Events/"+str(r[toRebin[-1]][0])+" GeV")
	bkg_nQCD = ROOT.THStack("Bkg_nQCD",toPlot+"_MC_{non-QCD};"+str(r[toRebin[-1]][1])+";Events/"+str(r[toRebin[-1]][0])+" GeV")

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

	# data = d2.Get(toPlot);
	data.Rebin(r[toRebin[-1]][0])

	data = myPlotFunc.plotStyle(data, r[toRebin[-1]][0], 1, xtitle = r[toRebin[-1]][1])

	hbkg = myPlotFunc.plotStyle(hbkg, r[toRebin[-1]][0], 12, 12, r[toRebin[-1]][1], 3244, draw = "E20P")
	hbkg_nQCD = myPlotFunc.plotStyle(hbkg_nQCD, r[toRebin[-1]][0], 12, 12, r[toRebin[-1]][1], 3244, draw = "E20P")

	data_norm = data.Clone("data_norm")
	data_norm.Sumw2()
	data_norm.Scale(1/data.Integral())

	hbkg_norm = hbkg_nQCD.Clone("hbkg_norm")
	hbkg_norm.Sumw2()
	hbkg_norm.Scale(1/hbkg_nQCD.Integral())

	histToNorm.append(data_norm)
	histToNorm.append(hbkg_norm)

	nbindata = data.GetNbinsX()

	ld = ROOT.TLegend(0.4,0.5,0.83,0.88)
	ld.SetLineWidth(0)
	if oneData == True:
		ld.AddEntry(data, dataset+" - "+str(int(data.Integral(1,nbindata+1))), "l");
	elif iteration == "Inclusive" or iteration == "AlteredID" or iteration == "Nominal":
		ld.AddEntry(data, "SingleMuon + JetHT - "+str(int(data.Integral(1,nbindata+1))), "l");
	else: ld.AddEntry(data, dataset+" - "+str(int(data.Integral(1,nbindata+1))), "l");

	c1.cd()

	data.SetTitle(toPlot+"_DataOnly")
	data.Draw("E0P");	
	if data.GetMaximum() >= 10000:
		data.GetYaxis().SetMaxDigits(4)
	else: data.GetYaxis().SetMaxDigits(3)
	if toRebin[-1] == "TauPt":
		data.GetXaxis().SetRangeUser(0,260)
	ld.Draw("same")

	if oneData == True:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+dataset+"Only_"+ver+"_DataOnly.png")
		c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf")
		c1.Clear()
	else:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_DataOnly.png")
		c1.Print(path+"/"+collection+"_"+iteration+".pdf")
		c1.Clear()

	lmc = ROOT.TLegend(0.5,0.55,0.9,0.88)
	lmc.SetLineWidth(0)
	lmc.AddEntry(hists['TTJets'], "TTJets - "+str(int(integral['TTJets'])), "f");
	lmc.AddEntry(hists['DYJetsToLL'], "DYJetsToLL - "+str(int(integral['DYJetsToLL']+integral['DYJetsToLL_M-4to50'])), "f");
	lmc.AddEntry(hists['WJetsToLNu'], "WJetsToLNu - "+str(int(integral['WJetsToLNu'])), "f");
	lmc.AddEntry(hists['Diboson'], "Diboson - "+str(int(integral['Diboson'])), "f");

	c1.cd()
	bkg_nQCD.Draw("hist")
	bkg_nQCD.GetXaxis().SetTitleSize(0.04)
	hbkg_nQCD.Draw("same E20P");

	if bkg_nQCD.GetMaximum() >= 10000:
		bkg_nQCD.GetYaxis().SetMaxDigits(4)
	else: bkg_nQCD.GetYaxis().SetMaxDigits(3)

	if toRebin[-1] == "TauPt":
		bkg_nQCD.GetXaxis().SetRangeUser(0,260)
		hbkg_nQCD.GetXaxis().SetRangeUser(0,260)

	lmc.Draw("same")

	c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_MCOnly.png")
	c1.Print(path+"/"+collection+"_"+iteration+".pdf")
	c1.Clear()

	#lg = ROOT.TLegend(0.28,0.35,0.53,0.67)
	lg = ROOT.TLegend(0.3,0.7,0.83,0.88)
	lg.SetLineWidth(0)
	lg.SetNColumns(2)
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
	lg.AddEntry(sig, "TCP_"+massTCP+" - "+str(int(sig.Integral(1,nbindata+1))), "f");
	lg.AddEntry(hbkg, "Bkg. Uncert.", "f");

	l = ROOT.TLine(0,1,(r[toRebin[-1]][2]),1)
	l.SetLineColor(ROOT.kRed)
	l.SetLineStyle(10)

	myPlotFunc.drawPad1(r[toRebin[-1]]);
	bkg.SetMinimum(1)
	bkg.SetMaximum(1E7)
	# if bkg.GetMaximum() < data.GetMaximum():
	# 	bkg.SetMaximum(data.GetMaximum()*1.2)
	bkg.Draw("hist")
	hbkg.Draw("same E20P");
	data.Draw("same E0P");
	sig.Draw("same hist")
	bkg.GetYaxis().SetTitle()
	if toRebin[-1] == "TauPt":
		bkg.GetXaxis().SetRangeUser(0,260)
		hbkg.GetXaxis().SetRangeUser(0,260)
		data.GetXaxis().SetRangeUser(0,260)
		sig.GetXaxis().SetRangeUser(0,260)
	if toRebin[-1] != "Trigger" :
		lg.Draw("same")
	c1.cd();
	myPlotFunc.drawPad2();	
	rhist = myPlotFunc.drawRatio(hbkg,data,r[toRebin[-1]])

	rhist[0].Draw()
	rhist[1].Draw("same E20P")

	if oneData == True:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+dataset+"Only_"+ver+".png")
		c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf")
		c1.Clear()
	else:
		c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+".png")
		c1.Print(path+"/"+collection+"_"+iteration+".pdf")
		c1.Clear()

	# print(hists)

histToNorm[2] = myPlotFunc.plotStyle(histToNorm[2], lineColour = 4, xtitle = r["TauPt"][1], EvBin = r["TauPt"][0])

ln = ROOT.TLegend(0.4,0.5,0.83,0.88)
ln.SetLineWidth(0)
ln.AddEntry(histToNorm[2], "Before dR cut", "l")
ln.AddEntry(histToNorm[0], "After dR cut", "l")

histToNorm[2].Draw()
histToNorm[0].Draw("same")
ln.Draw("same")

histToNorm[2].GetXaxis().SetRangeUser(0,260)
histToNorm[0].GetXaxis().SetRangeUser(0,260)

c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_DataOnly_Norm.png")
c1.Print(path+"/"+collection+"_"+iteration+".pdf")
c1.Clear()

histToNorm[1] = myPlotFunc.plotStyle(histToNorm[1], lineColour = 1, xtitle = r["TauPt"][1], EvBin = r["TauPt"][0])
histToNorm[3] = myPlotFunc.plotStyle(histToNorm[3], lineColour = 4, xtitle = r["TauPt"][1], EvBin = r["TauPt"][0])

histToNorm[3].Draw()
histToNorm[1].Draw("same")
ln.Draw("same")

histToNorm[3].GetXaxis().SetRangeUser(0,260)
histToNorm[1].GetXaxis().SetRangeUser(0,260)

c1.SaveAs(path+"/"+toPlot+"_"+iteration+"_"+ver+"_MCOnly_Norm.png")
c1.Print(path+"/"+collection+"_"+iteration+".pdf")
c1.Clear()

print("Outputs in", path)
print(histToPlot)

if oneData == True:
	c1.Print(path+"/"+collection+"_"+iteration+"_"+dataset+"Only.pdf]")
else:
	c1.Print(path+"/"+collection+"_"+iteration+".pdf]")
