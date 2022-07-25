import ROOT,os, sys
import CMS_lumi, tdrstyle
import myPlotFunc

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

r = {
	'MuonPt' 	: [20, "P_{T} (GeV)", 500],
	'Muon1Pt' 	: [20, "P_{T} (GeV)", 500],
	'Muon2Pt' 	: [20, "P_{T} (GeV)", 500],
	'ElectronPt': [20, "P_{T} (GeV)", 500],
	'TauPt'	 	: [20, "P_{T} (GeV)", 500],
	'TauPt0'	 	: [20, "P_{T} (GeV)", 500],
	'TauPt1'	 	: [20, "P_{T} (GeV)", 500],
	'TauPt10'	 	: [20, "P_{T} (GeV)", 500],
	'JetPt'	 	: [100, "P_{T} (GeV)", 2000],
	'MetPt'	 	: [20, "P_{T} (GeV)", 500],
	'dRl'	 	: [5, "dR", 5],
	'dRj'	 	: [5, "dR", 5],
	'dPhil'	 	: [5, "dPhi", 3.5],
	'dPhij'	 	: [5, "dphi", 3.5],
	'Mt'	 	: [20, "Mt", 500],
	'Nj'     	: [1, "N_{jet}", 10],
	'lowMET' 	: [5, "M_{vis} (GeV)", 100],
	'dRcut'	 	: [5, "M_{vis} (GeV)", 100],
	'lowMt'	 	: [5, "M_{vis} (GeV)", 100],
	'mTcut'	 	: [5, "M_{vis} (GeV)", 100],
	'highMET' 	: [5, "M_{vis} (GeV)", 100],
	'Metcut' 	: [5, "M_{vis} (GeV)", 100],
	'highMt'	: [5, "M_{vis} (GeV)", 100],
	'dPhicut'	: [5, "M_{vis} (GeV)", 100],
	'Trigger'	: [1, "Triggers", 8]
}

inVer = "v6"
altVer = "v6"
inDataVer = "v6" 
altDataVer = "v8" 

iteration = "Ff"
ver = "v4"

if "-dr1" in opts:
	DRReg = "DR1_Ff"
	histList = ['hMuTau_highMt_dRcut_highMET', 'hMuTau_highMt_dRcut_highMET_TauPt','hMuTau_highMt_dRcut_highMET_TauPt0','hMuTau_highMt_dRcut_highMET_TauPt10','hMuTau_highMt_dRcut_highMET_TauPt1', 'hMuTau_highMt_dRcut_highMET_Nj']
if "-dr2" in opts:
	DRReg = "DR2_Ff"
	histList = ['hMuTau_lowMET_dRcut_lowMt', 'hMuTau_lowMET_dRcut_lowMt_TauPt', 'hMuTau_lowMET_dRcut_lowMt_TauPt0','hMuTau_lowMET_dRcut_lowMt_TauPt10','hMuTau_lowMET_dRcut_lowMt_TauPt1','hMuTau_lowMET_dRcut_lowMt_Nj']
if "-dr3" in opts:
	DRReg = "DR3_Ff"
	histList = ['hMuTau_SS_dRcut_highMET_lowMt', 'hMuTau_SS_dRcut_highMET_lowMt_TauPt','hMuTau_SS_dRcut_highMET_lowMt_TauPt0','hMuTau_SS_dRcut_highMET_lowMt_TauPt10','hMuTau_SS_dRcut_highMET_lowMt_TauPt1', 'hMuTau_SS_dRcut_highMET_lowMt_Nj','hMuTau_SS_dRcut_highMET_lowMt_MetPt']
if "-dr4" in opts:
	DRReg = "DR4_Ff"
	histList = ['hMuTau_lowMET_dRcut_highMt', 'hMuTau_lowMET_dRcut_highMt_TauPt', 'hMuTau_lowMET_dRcut_highMt_TauPt0','hMuTau_lowMET_dRcut_highMt_TauPt10','hMuTau_lowMET_dRcut_highMt_TauPt1','hMuTau_lowMET_dRcut_highMt_Nj']
if "-dr5" in opts:
	DRReg = "DR5_Ff"
	histList = ['hMuTau_SS_dRcut_highMET_highMt', 'hMuTau_SS_dRcut_highMET_highMt_TauPt','hMuTau_SS_dRcut_highMET_highMt_TauPt0','hMuTau_SS_dRcut_highMET_highMt_TauPt10','hMuTau_SS_dRcut_highMET_highMt_TauPt1','hMuTau_SS_dRcut_highMET_highMt_Nj']
if "-dr6" in opts:
	DRReg = "DR6_Ff"
	histList = ['hMuTau_SS_lowMET_dRcut_lowMt', 'hMuTau_SS_lowMET_dRcut_lowMt_TauPt', 'hMuTau_SS_lowMET_dRcut_lowMt_TauPt0','hMuTau_SS_lowMET_dRcut_lowMt_TauPt10','hMuTau_SS_lowMET_dRcut_lowMt_TauPt1','hMuTau_SS_lowMET_dRcut_lowMt_Nj','hMuTau_SS_lowMET_dRcut_lowMt_MetPt']
if "-dr7" in opts:
	DRReg = "DR7_Ff"
	histList = ['hMuTau_SS_lowMET_dRcut_highMt', 'hMuTau_SS_lowMET_dRcut_highMt_TauPt', 'hMuTau_SS_lowMET_dRcut_highMt_Nj']

AR = ['hMuTau_SR_dRcut_highMET_lowMt','hMuTau_SR_dRcut_highMET_lowMt_TauPt','hMuTau_SR_dRcut_highMET_lowMt_TauPt0','hMuTau_SR_dRcut_highMET_lowMt_TauPt10','hMuTau_SR_dRcut_highMET_lowMt_TauPt1','hMuTau_SR_dRcut_highMET_lowMt_Nj','hMuTau_SR_dRcut_highMET_lowMt_MetPt']

path = '/Users/muti/Documents/Analysis/studyCleanedTaus/'+iteration+"_"+ver
isExist = os.path.exists(path)

if not isExist:
	os.makedirs(path)
	print("Folder created, outputs in", path)

if isExist:
	print("Outputs in", path)

histToPlot = []
for h in histList:
	histToPlot.append(h+"_Nominal")
	histToPlot.append(h+"_AlteredID")

print(histToPlot)

SAMPLES = ['Diboson','WJetsToLNu','DYJetsToLL','DYJetsToLL_M-4to50','TTJets','QCD']
DRbkg = 'QCD'

# DR = {}
testHist = {}

out = ROOT.TFile(path+"/"+DRReg+".root",'recreate')

c1 = ROOT.TCanvas("c1","c1",850, 850)
c1.cd()	
c1.SetGridx()
c1.Print(path+"/"+DRReg+".pdf[")

for n,hname in enumerate(histList):
	histToPlot = []
	histToPlot.append(hname+"_Nominal")
	histToPlot.append(hname+"_AlteredID")

	DR = {}
	ROOT.TH1.AddDirectory(0)

	for toPlot in histToPlot:
		print("h_"+toPlot)
	# print(toPlot.split("_"))
		if toPlot.split("_")[-1] == "Nominal":
			# print(toPlot.split("_")[-1])
			f = ROOT.TFile("h_"+toPlot+"_"+inVer+".root")
			d1 = ROOT.TFile("h_debugMuTau_HighHT_Data_SingleMuon_"+inDataVer+".root");
			d2 = ROOT.TFile("h_debugMuTau_HighHT_Data_JetHT_"+inDataVer+".root");
		if toPlot.split("_")[-1] == "AlteredID":
			# print(toPlot.split("_")[-1])
			f = ROOT.TFile("h_"+toPlot+"_"+altVer+".root")
			d1 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_SingleMuon_"+altDataVer+".root");
			d2 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_JetHT_"+altDataVer+".root");
		
		hists = {}
		integral = {}

		bkgStack = ROOT.THStack("Bkg",toPlot+";"+r[toPlot.split("_")[-2]][1]+";Events / "+str(r[toPlot.split("_")[-2]][0])+" GeV")

		for sample in SAMPLES:
			if toPlot.split("_")[-1] == "Nominal":
				# print(sample+"_"+toPlot.strip("_")[:-8])
				h = f.Get(sample+"_"+toPlot.strip("_")[:-8])
			if toPlot.split("_")[-1] == "AlteredID":
				# print(sample+"_"+toPlot.strip("_")[:-10])
				h = f.Get(sample+"_"+toPlot.strip("_")[:-10])
			nbinx = h.GetNbinsX()
			toRebin = toPlot.split("_")
			h.Rebin(r[toRebin[-2]][0])
			if toRebin == "TauPt" or toRebin == "TauPt0" or toRebin == "TauPt1" or toRebin == "TauPt10":
				h.GetXaxis().SetRangeUser(0,250)
			integral[sample] = h.Integral(1,nbinx+1)
			# if sample != DRbkg:
			bkgStack.Add(h)
			hists[sample] = h


		if toPlot.split("_")[-1] == "Nominal":
			data1 = d1.Get(toPlot.strip("_")[:-8])
			data2 = d2.Get(toPlot.strip("_")[:-8])
		if toPlot.split("_")[-1] == "AlteredID":
			data1 = d1.Get(toPlot.strip("_")[:-10])
			data2 = d2.Get(toPlot.strip("_")[:-10])
		data = data1.Clone("data")
		data.Add(data2)

		data.Rebin(r[toRebin[-2]][0])
		data.SetLineWidth(3);
		data.SetMarkerStyle(8);
		data.SetMarkerSize(1);
		data.SetLineColor(ROOT.kBlack);
		if toPlot.split("_")[-2] == "TauPt" or toPlot.split("_")[-2] == "TauPt0" or toPlot.split("_")[-2] == "TauPt1" or toPlot.split("_")[-2] == "TauPt10":
			data.GetXaxis().SetRangeUser(0,250)

		bkgHist = hists['DYJetsToLL'].Clone("bkgHist")
		bkgHist.Sumw2()

		bkgHistTot = hists['DYJetsToLL'].Clone("bkgHistTot")
		bkgHistTot.Sumw2()

		for sample in SAMPLES:
			if sample != 'DYJetsToLL' :
				bkgHistTot.Add(hists[sample])
				integral['total'] = bkgHistTot.Integral(1,nbinx+1)
				if sample != DRbkg:
					bkgHist.Add(hists[sample])
					integral['totalNonQCD'] = bkgHist.Integral(1,nbinx+1)

		bkgHist.SetFillColor(12);
		bkgHist.SetFillStyle(3244);
		bkgHistTot.SetFillColor(12);
		bkgHistTot.SetFillStyle(3244);

		diff = data.Clone("difference")
		diff.Sumw2()

		# diff.Add(bkgHist,-1)

		for k in range(diff.GetNbinsX()): #Force negative bins to be 0
			if diff.GetBinContent(k+1) < bkgHist.GetBinContent(k+1):
				diff.SetBinContent(k+1, 0)
			else:
				delta = diff.GetBinContent(k+1) - bkgHist.GetBinContent(k+1)
				diff.SetBinContent(k+1, delta)
			# if diff.GetBinContent(k+1) < 0:
			# 	diff.SetBinContent(k+1, 0)

		diff.SetStats(0)
		diff.SetTitle(toPlot+" Data - MC_{Non-QCD}")
		if toPlot.split("_")[-2] == "TauPt" or toPlot.split("_")[-2] == "TauPt0" or toPlot.split("_")[-2] == "TauPt1" or toPlot.split("_")[-2] == "TauPt10":
			diff.GetXaxis().SetRangeUser(0,250)

		print("DR =", toPlot)
		DR[toPlot] = diff
		print(DR)

		l = ROOT.TLine(0,1,(r[toRebin[-2]][2]),1)
		l.SetLineColor(ROOT.kRed)
		l.SetLineStyle(10)

		lg = ROOT.TLegend(0.45,0.4,0.83,0.83)
		lg.SetLineWidth(0)
		
		lg.AddEntry(data, "SingleMuon + JetHT - "+str(int(data.Integral(1,nbinx))), "l")
		lg.AddEntry(hists['QCD'], "QCD - "+str(int(integral['QCD'])), "f");
		lg.AddEntry(hists['TTJets'], "TTJets - "+str(int(integral['TTJets'])), "f");
		lg.AddEntry(hists['DYJetsToLL'], "DYJetsToLL - "+str(int(integral['DYJetsToLL']+integral['DYJetsToLL_M-4to50'])), "f");
		lg.AddEntry(hists['WJetsToLNu'], "WJetsToLNu - "+str(int(integral['WJetsToLNu'])), "f");
		lg.AddEntry(hists['Diboson'], "Diboson - "+str(int(integral['Diboson'])), "f");
		lg.AddEntry(hists['Diboson'],"Total non-QCD - "+str(int(integral['totalNonQCD'])),"f")
		lg.AddEntry(bkgHistTot, "Bkg. Uncert.", "f")

		ls = ROOT.TLegend(0.45,0.55,0.83,0.83)
		ls.SetLineWidth(0)
		ls.AddEntry(data, "SingleMuon + JetHT - "+str(int(data.Integral(1,nbinx))), "l")
		ls.AddEntry(data,"Total non-QCD - "+str(int(integral['totalNonQCD'])),"l")
		ls.AddEntry(data, "Data - MC_{Non-QCD} = "+str(int(data.Integral(1,nbinx)-integral['totalNonQCD'])), "l")

		print(r[toPlot.split("_")[-2]][1])

		#Page 1-2, 3-4
		myPlotFunc.drawPad1(r[toRebin[-2]]);

		if bkgStack.GetMaximum() < data.GetMaximum() :
			bkgStack.SetMaximum( data.GetMaximum()*1.2 + bkgStack.GetMaximum()*0.2)
		else: bkgStack.SetMaximum(bkgStack.GetMaximum() + bkgStack.GetMaximum()*0.35)
		bkgStack.Draw("hist")

		bkgStack.GetXaxis().SetTitle(r[toPlot.split("_")[-2]][1])

		bkgStack.GetYaxis().SetTitleOffset(0.9)
		bkgStack.GetYaxis().SetTitleSize(0.05)
		bkgStack.GetYaxis().SetLabelFont(43);
		bkgStack.GetYaxis().SetLabelSize(25);

		if bkgStack.GetMaximum() >= 10000:
			bkgStack.GetYaxis().SetMaxDigits(4)
		elif bkgStack.GetMaximum() >= 1000: 
			bkgStack.GetYaxis().SetMaxDigits(3)
		else: bkgStack.GetYaxis().SetMaxDigits(2)

		if toPlot.split("_")[-2] == "TauPt" or toPlot.split("_")[-2] == "TauPt0" or toPlot.split("_")[-2] == "TauPt1" or toPlot.split("_")[-2] == "TauPt10":
			bkgStack.GetXaxis().SetRangeUser(0,250)

		bkgHistTot.Draw("same E20P")
		data.Draw("same E0P")
		lg.Draw("same")

		myPlotFunc.drawCMS()

		c1.cd()

		myPlotFunc.drawPad2();

		# rhist = myPlotFunc.drawRatio(bkgHist,data,r[toRebin[-2]])
		rhist = myPlotFunc.drawRatio(bkgHistTot,data,r[toRebin[-2]])

		rhist[0].Draw()
		rhist[1].Draw("same E20P")
		
		c1.SaveAs(path+"/"+toPlot+"_DataMC.png")
		c1.Print(path+"/"+DRReg+".pdf")
		c1.Clear()

		diff.SetMaximum(diff.GetMaximum()*1.5)

		diff.Draw()
		diff.GetXaxis().SetTitle(r[toPlot.split("_")[-2]][1])

		diff.GetYaxis().SetTitle("Events / "+str(r[toPlot.split("_")[-2]][0])+" GeV")
		diff.GetYaxis().SetTitleSize(0.04)
		diff.GetYaxis().SetTitleOffset(1)
		diff.GetYaxis().SetLabelFont(43);
		diff.GetYaxis().SetLabelSize(25);

		if diff.GetMaximum() >= 10000:
			diff.GetYaxis().SetMaxDigits(4)
		elif diff.GetMaximum() >= 1000: 
			diff.GetYaxis().SetMaxDigits(3)
		else: diff.GetYaxis().SetMaxDigits(2)

		ls.Draw("same")
		myPlotFunc.drawCMS(0.04)

		c1.SaveAs(path+"/"+toPlot+"_Diff.png")
		c1.Print(path+"/"+DRReg+".pdf")
		c1.Clear()

		ldiff = ROOT.TLegend(0.15,0.15,0.85,0.85)
		for j in range(diff.GetNbinsX()):
			ldiff.AddEntry(diff, "Bin"+str(j+1)+" = "+str(diff.GetBinContent(j+1))+"#pm"+str(diff.GetBinError(j+1)))

		ldiff.Draw()
		c1.Print(path+"/"+DRReg+".pdf")
		c1.Clear()


	DR[hname+'_AlteredID'].SetLineColor(ROOT.kBlue)

	lratio = ROOT.TLegend(0.58,0.6,0.8,0.83)
	lratio.AddEntry(DR[hname+'_Nominal'],"Nominal","l")
	lratio.AddEntry(DR[hname+'_AlteredID'],"AlteredID","l")

	DR[hname+'_AlteredID'].SetTitle(hname+"_Data-MC_{non-QCD}")

	DR[hname+'_AlteredID'].Draw()
	DR[hname+'_Nominal'].Draw("same")

	myPlotFunc.drawCMS(0.04)

	lratio.Draw("same")

	c1.SaveAs(path+"/"+hname+"_Data-MC.png")
	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	Ff = DR[hname+'_Nominal'].Clone("numerator")
	Ff.Sumw2()
	Ff.Divide(DR[hname+'_AlteredID'])
	Ff.SetTitle(hname+"_F_{F}^{"+DRbkg+"}")

	Ff.GetYaxis().SetTitle("F_{F}")
	Ff.GetYaxis().SetTitleSize(0.045)
	Ff.GetYaxis().SetLabelFont(43);
	Ff.GetYaxis().SetLabelSize(25)

	lname = ROOT.TLegend(0.58,0.6,0.8,0.83)
	lname.SetLineWidth(0)
	lname.AddEntry(Ff, DRReg.split("_")[0])

	nbinFf = Ff.GetNbinsX()

	txtFf = open("F_F_"+DRReg+"_"+AR[n].split("_")[-1]+".txt", "w+")
	for l in range(Ff.GetNbinsX()):
		txtFf.write(str((l*20)+20)+"\t"+str(Ff.GetBinContent(l+1))+"\n")
	txtFf.close()

	Ff.Draw()
	Ff.SetMaximum(1)
	Ff.SetMinimum(0)
	lname.Draw("same")

	myPlotFunc.drawCMS(0.04)

	out.cd()
	Ff.Write(hname)

	c1.SaveAs(path+"/"+hname+"_Ff.png")
	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	lFf = ROOT.TLegend(0.15,0.15,0.85,0.85)
	for j in range(Ff.GetNbinsX()):
		lFf.AddEntry(Ff, "Bin"+str(j+1)+" = "+str(Ff.GetBinContent(j+1))+"#pm"+str(Ff.GetBinError(j+1)))

	lFf.Draw()
	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	fAR = ROOT.TFile("h_"+AR[n]+"_AlteredID_"+altVer+".root")
	fSR = ROOT.TFile("h_"+AR[n]+"_Nominal_"+inVer+".root")

	integralAR = {}
	integralSR = {}

	histsAR = {}
	histsSR = {}

	bkgStackSR = ROOT.THStack("BkgStackSR",AR[n]+"_SR;"+r[AR[n].split("_")[-1]][1]+";Events / "+str(r[toPlot.split("_")[-2]][0])+" GeV")
	bkgStackAR = ROOT.THStack("BkgStackAR",AR[n]+"_AR;"+r[AR[n].split("_")[-1]][1]+";Events / "+str(r[toPlot.split("_")[-2]][0])+" GeV")

	for sample in SAMPLES:
		hAR = fAR.Get(sample+"_"+AR[n])
		hSR = fSR.Get(sample+"_"+AR[n])
		if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
			hSR.GetXaxis().SetRangeUser(0,250)
			hAR.GetXaxis().SetRangeUser(0,250)
		nbinx = h.GetNbinsX()
		toRebin = AR[n].split("_")
		hAR.Rebin(r[toRebin[-1]][0])
		hSR.Rebin(r[toRebin[-1]][0])
		# integralAR[sample] = hAR.Integral(1,nbinx+1)
		# integralSR[sample] = hSR.Integral(1,nbinx+1)
		integralAR[sample] = hAR.Integral()
		integralSR[sample] = hSR.Integral()
		bkgStackSR.Add(hSR)
		bkgStackAR.Add(hAR)
		histsSR[sample] = hSR
		histsAR[sample] = hAR


	bkgHistAR = histsAR['DYJetsToLL'].Clone("hbkgHistAR")
	bkgHistAR.Sumw2()

	bkgHistSR = histsSR['DYJetsToLL'].Clone("hbkgHistSR")
	bkgHistSR.Sumw2()

	bkgHistTotAR = histsAR['DYJetsToLL'].Clone("hbkgHistTotAR")
	bkgHistTotAR.Sumw2()

	bkgHistTotSR = histsSR['DYJetsToLL'].Clone("hbkgHistTotSR")
	bkgHistTotSR.Sumw2()


	for sample in SAMPLES:
		if sample != 'DYJetsToLL': 
			bkgHistTotAR.Add(histsAR[sample])
			integralAR['total'] = bkgHistTotAR.Integral()
			bkgHistTotSR.Add(histsSR[sample])
			integralSR['total'] = bkgHistTotSR.Integral()
			if sample != DRbkg:
				bkgHistAR.Add(histsAR[sample])
				integralAR['totalNonQCD'] = bkgHistAR.Integral()
				bkgHistSR.Add(histsSR[sample])
				integralSR['totalNonQCD'] = bkgHistSR.Integral()

		# if sample != 'DYJetsToLL':	
		# 	bkgHistTotSR.Add(histsSR[sample])
		# 	integralSR['total'] = bkgHistTotSR.Integral()
			# integralSR['total'] = hbkgSR.Integral(1,nbinx+1)


	dataFileAR1 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_SingleMuon_"+altDataVer+".root");
	dataFileAR2 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_JetHT_"+altDataVer+".root");

	dataAR1 = dataFileAR1.Get(AR[n])
	dataAR2 = dataFileAR2.Get(AR[n])

	dataAR = dataAR1.Clone("dataAR1")
	dataAR.Add(dataAR2)

	dataAR.Rebin(r[toRebin[-1]][0])
	dataAR.SetLineWidth(3);
	dataAR.SetMarkerStyle(8);
	dataAR.SetMarkerSize(1);
	dataAR.SetLineColor(ROOT.kBlack);

	diffAR = dataAR.Clone("differenceAR")
	diffAR.Sumw2()
	diffAR.Add(bkgHistAR,-1)
	diffAR.SetStats(0)
	diffAR.SetTitle(AR[n]+"_AR_Difference")

	for k in range(diffAR.GetNbinsX()): #Force negative bins to be 0
			if diffAR.GetBinContent(k+1) < 0:
				diffAR.SetBinContent(k+1, 0)

	bkgHistTotAR.SetFillColor(12);
	bkgHistTotAR.SetFillStyle(3244);

	bkgStackAR.SetMaximum(dataAR.GetMaximum()*1.2)
	bkgStackAR.Draw("hist")

	if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
		bkgStackAR.GetXaxis().SetRangeUser(0,250)
	bkgStackAR.GetXaxis().SetTitle(r[AR[n].split("_")[-1]][1])

	bkgStackAR.GetYaxis().SetTitleOffset(0.9)
	bkgStackAR.GetYaxis().SetTitleSize(0.045)
	bkgStackAR.GetYaxis().SetLabelFont(43);
	bkgStackAR.GetYaxis().SetLabelSize(25);

	if bkgStackAR.GetMaximum() >= 10000:
		bkgStackAR.GetYaxis().SetMaxDigits(4)
	elif bkgStackAR.GetMaximum() >= 1000:
		bkgStackAR.GetYaxis().SetMaxDigits(3)
	else: bkgStackAR.GetYaxis().SetMaxDigits(2)

	bkgHistTotAR.Draw("same E20P")
	dataAR.Draw("same E0P");
	if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
		dataAR.GetXaxis().SetRangeUser(0,250)

	lAR = ROOT.TLegend(0.45,0.5,0.83,0.83)		
	lAR.SetLineWidth(0)
	lAR.AddEntry(data, "SingleMuon + JetHT - "+str(int(dataAR.Integral())), "l")
	lAR.AddEntry(hists['QCD'], "QCD - "+str(int(integralAR['QCD'])), "f");
	lAR.AddEntry(hists['TTJets'], "TTJets - "+str(int(integralAR['TTJets'])), "f");
	lAR.AddEntry(hists['DYJetsToLL'], "DYJetsToLL - "+str(int(integralAR['DYJetsToLL']+integral['DYJetsToLL_M-4to50'])), "f");
	lAR.AddEntry(hists['WJetsToLNu'], "WJetsToLNu - "+str(int(integralAR['WJetsToLNu'])), "f");
	lAR.AddEntry(hists['Diboson'], "Diboson - "+str(int(integralAR['Diboson'])), "f");
	lAR.AddEntry(hists['Diboson'],"Total non-QCD - "+str(int(integralAR['totalNonQCD'])),"f")
	lAR.AddEntry(bkgHistTot, "Bkg. Uncert.", "f")
		
	lAR.Draw("same")
	bkgStackAR.GetXaxis().SetTitle(r[AR[n].split("_")[-1]][1])
	bkgHistTotAR.GetXaxis().SetTitle(r[AR[n].split("_")[-1]][1])

	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	tothbkgAR = bkgHistAR.Clone("totalAR")
	tothbkgAR.Add(diffAR)

	wQCD = diffAR.Integral()/tothbkgAR.Integral()
#	wWjets = bkgHistAR.Integral()/tothbkgAR.Integral()
	wWjets = 0.0

	hWQCD = ROOT.TH1F(AR[n]+"_wQCD",AR[n]+"_w_{QCD};"+r[AR[n].split("_")[-1]][1]+";w_{QCD}",r[AR[n].split("_")[-1]][2],0,r[AR[n].split("_")[-1]][2])
	hWQCD.Sumw2()

	hWQCD.SetLineWidth(3);
	hWQCD.SetMarkerStyle(8);
	hWQCD.SetMarkerSize(1);
	hWQCD.SetLineColor(ROOT.kBlack);
	hWQCD.SetStats(0)

	hWQCD.Rebin(r[AR[n].split("_")[-1]][0])

	lWQCD = ROOT.TLegend(0.15,0.15,0.85,0.85)

	for i in range(nbinFf):
		if tothbkgAR.GetBinContent(i+1) > 0:
			hWQCD.SetBinContent(i+1,diffAR.GetBinContent(i+1)/tothbkgAR.GetBinContent(i+1))
			lWQCD.AddEntry(hWQCD, str(hWQCD.GetBinContent(i+1)))

	hWQCD.Draw()
	hWQCD.SetMinimum(0)
	hWQCD.SetMaximum(1)
	if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
		hWQCD.GetXaxis().SetRangeUser(0,250)

	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	lWQCD.Draw()
	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	hFFQCD = ROOT.TH1F(AR[n]+"_F_{F}QCD",AR[n]+"_F_{F};"+r[AR[n].split("_")[-1]][1]+";F_{F}",r[AR[n].split("_")[-1]][2],0,r[AR[n].split("_")[-1]][2])
	hFFQCD.Sumw2()

	hFFQCD.SetLineWidth(3);
	hFFQCD.SetMarkerStyle(8);
	hFFQCD.SetMarkerSize(1);
	hFFQCD.SetLineColor(ROOT.kBlack);
	hFFQCD.SetStats(0)

	hFFQCD.Rebin(r[AR[n].split("_")[-1]][0])

	lFFQCD = ROOT.TLegend(0.15,0.15,0.85,0.85)

	for i in range(nbinFf):
		hFFQCD.SetBinContent(i+1,hWQCD.GetBinContent(i+1)*Ff.GetBinContent(1+i)+wWjets)
		lFFQCD.AddEntry(hFFQCD, str(hFFQCD.GetBinContent(i+1)))

	hFFQCD.Draw("hist")
	hFFQCD.SetMaximum(1)
	hFFQCD.SetMinimum(0)
	if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
		hFFQCD.GetXaxis().SetRangeUser(0,250)

	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	lFFQCD.Draw()

	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	print("wQCD, wWjets", wQCD, wWjets)
	
	lsAR = ROOT.TLegend(0.45,0.55,0.83,0.83)
	lsAR.SetLineWidth(0)	
	# lsAR.AddEntry(data, "SingleMuon + JetHT - "+str(int(dataAR.Integral(1,nbinx+1))), "l")
	lsAR.AddEntry(data, "SingleMuon + JetHT - "+str(int(dataAR.Integral())), "l")
	lsAR.AddEntry(data,"Total non-QCD - "+str(int(integralAR['totalNonQCD'])),"l")
	lsAR.AddEntry(data, "Data - MC_{Non-QCD} = "+str(int(dataAR.Integral()-integralAR['totalNonQCD'])), "l")
	# lsAR.AddEntry(data, "Difference - "+str(int(dataAR.Integral(1,nbinx+1)-integralAR['total'])), "l")

	# lg.Draw("same")
	
	diffAR.Draw()
	if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
		diffAR.GetXaxis().SetRangeUser(0,250)

	diffAR.GetYaxis().SetTitle("Events / "+str(r[toPlot.split("_")[-2]][0])+" GeV")
	diffAR.GetYaxis().SetTitleSize(0.04)
	diffAR.GetYaxis().SetTitleOffset(0.9)
	diffAR.GetYaxis().SetLabelFont(43);
	diffAR.GetYaxis().SetLabelSize(30);

	if diffAR.GetMaximum() >= 10000:
		diffAR.GetYaxis().SetMaxDigits(4)
	elif diffAR.GetMaximum() >= 1000:
		diffAR.GetYaxis().SetMaxDigits(3)
	else: diffAR.GetYaxis().SetMaxDigits(2)

	lsAR.Draw("same")
	diffAR.GetXaxis().SetTitle(r[AR[n].split("_")[-1]][1])
	# ls.Draw("same")
	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	SR_predicted = ROOT.TH1F(AR[n]+"_SR_Predicted",AR[n]+"_SR_Predicted;"+r[AR[n].split("_")[-1]][1]+";N_{events}",r[AR[n].split("_")[-1]][2],0,r[AR[n].split("_")[-1]][2])

	SR_predicted.SetLineWidth(3);
	SR_predicted.SetMarkerStyle(8);
	SR_predicted.SetMarkerSize(1);
	SR_predicted.SetLineColor(ROOT.kBlack);
	SR_predicted.SetStats(0)

	SR_predicted.Rebin(r[AR[n].split("_")[-1]][0])

	for j in range(nbinFf):
		# SR_predicted.SetBinContent(1+j,dataAR.GetBinContent(1+j)*((Ff.GetBinContent(1+j)*wQCD))+wWjets) #multiplied to AR
		# SR_predicted.SetBinContent(1+j,diffAR.GetBinContent(1+j)*((Ff.GetBinContent(1+j)*wQCD))+wWjets)	#multiplied to diffAR
		SR_predicted.SetBinContent(1+j,dataAR.GetBinContent(1+j)*((Ff.GetBinContent(1+j)*hWQCD.GetBinContent(1+j)))+wWjets)

	if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
		SR_predicted.GetXaxis().SetRangeUser(0,250)

	bkgHistTotSR.SetFillColor(12);
	bkgHistTotSR.SetFillStyle(3244);
	

	# bkgARtot.Draw("hist")
	# bkgARtot.GetXaxis().SetRangeUser(0,250)
	# lAR.Draw("same")
	# bkgARtot.SetMaximum(dataAR.GetMaximum()*1.2)
	# dataAR.Draw("same")
	# c1.Print(path+"/"+DRReg+".pdf")
	# c1.Clear()

	lSR_Predicted = ROOT.TLegend(0.58,0.5,0.83,0.83)	
	lSR_Predicted.SetLineWidth(0)	
	lSR_Predicted.AddEntry(dataAR, "Integral - "+str(int(SR_predicted.Integral())))

	SR_predicted.Draw()
	lSR_Predicted.Draw("same")

	SR_predicted.GetYaxis().SetTitle("Events / "+str(r[toPlot.split("_")[-2]][0])+" GeV")
	SR_predicted.GetYaxis().SetTitleSize(0.035)
	SR_predicted.GetYaxis().SetTitleOffset(0.9)
	SR_predicted.GetYaxis().SetLabelFont(43);
	SR_predicted.GetYaxis().SetLabelSize(25);

	if SR_predicted.GetMaximum() >= 10000:
		SR_predicted.GetYaxis().SetMaxDigits(4)
	elif SR_predicted.GetMaximum() >= 1000:
		SR_predicted.GetYaxis().SetMaxDigits(3)
	else: SR_predicted.GetYaxis().SetMaxDigits(2)

	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

	lSR = ROOT.TLegend(0.58,0.45,0.9,0.83)		
	lSR.SetLineWidth(0)
	lSR.AddEntry(hists['QCD'], "QCD - "+str(int(integralSR['QCD'])), "f");
	lSR.AddEntry(hists['TTJets'], "TTJets - "+str(int(integralSR['TTJets'])), "f");
	lSR.AddEntry(hists['DYJetsToLL'], "DYJetsToLL - "+str(int(integralSR['DYJetsToLL']+integralSR['DYJetsToLL_M-4to50'])), "f");
	lSR.AddEntry(hists['WJetsToLNu'], "WJetsToLNu - "+str(int(integralSR['WJetsToLNu'])), "f");
	lSR.AddEntry(hists['Diboson'], "Diboson - "+str(int(integralSR['Diboson'])), "f");
	lSR.AddEntry(bkgHistTot, "Bkg. Uncert.", "f")
	lSR.AddEntry(SR_predicted, "Predicted backgrounds - "+str(int(SR_predicted.Integral())), "l");

	myPlotFunc.drawPad1(r[AR[n].split("_")[-1]])
	bkgStackSR.Draw("hist")
	bkgStackSR.SetMaximum(SR_predicted.GetMaximum()*1.2)
	if AR[n].split("_")[-1] == "TauPt" or AR[n].split("_")[-1] == "TauPt0" or AR[n].split("_")[-1] == "TauPt10" or AR[n].split("_")[-1] == "TauPt1":
		bkgStackSR.GetXaxis().SetRangeUser(0,250)

	if bkgStackSR.GetMaximum() >= 10000:
		bkgStackSR.GetYaxis().SetMaxDigits(4)
	elif bkgStackSR.GetMaximum() >= 1000:
		bkgStackSR.GetYaxis().SetMaxDigits(3)	
	else: bkgStackSR.GetYaxis().SetMaxDigits(2)

	bkgStackSR.GetYaxis().SetTitleOffset(0.9)
	bkgStackSR.GetYaxis().SetTitleSize(0.05)
	bkgStackSR.GetYaxis().SetLabelFont(43);
	bkgStackSR.GetYaxis().SetLabelSize(25);

	bkgHistTotSR.Draw("same E20P")
	SR_predicted.Draw("same E0P")
	lSR.Draw("same")

	myPlotFunc.drawCMS()

	c1.cd()
	myPlotFunc.drawPad2()
	# rhistSR = myPlotFunc.drawRatio(histsSR['Diboson'],histsSR['WJetsToLNu'],histsSR['DYJetsToLL'],histsSR['DYJetsToLL_M-4to50'],histsSR['TTJets'],histsSR['QCD'],SR_predicted,r[AR[n].split("_")[-1]])

	# rhistSR = myPlotFunc.drawRatio(bkgHistTotSR,SR_predicted,r[AR[n].split("_")[-1]])
	rhistSR = myPlotFunc.drawRatio(bkgHistTotSR,SR_predicted,r[AR[n].split("_")[-1]])

	rhistSR[0].Draw();
	rhistSR[1].Draw("same E20P");

	# rhistSR.Draw();
	# l.Draw("same")
	c1.SaveAs(path+"/"+hname+"_SRPredicted.png")
	c1.Print(path+"/"+DRReg+".pdf")
	c1.Clear()

c1.Print(path+"/"+DRReg+".pdf]")
out.Close()
